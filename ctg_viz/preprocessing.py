"""
Funciones de preprocesamiento para limpieza y imputación de datos
"""

import pandas as pd
import numpy as np

def process_data(df_input: pd.DataFrame) -> pd.DataFrame:
    """
    Procesa los datos eliminando columnas con más del 20% de valores nulos,
    imputando valores faltantes con la mediana para columnas numéricas
    y con la moda para columnas categóricas, y tratando valores atípicos
    en columnas numéricas (excluyendo 'NSP', 'CLASS', 'Tendency')
    utilizando el método IQR (clipping)

    Args:
        df_input (pd.DataFrame): El DataFrame de entrada

    Returns:
        pd.DataFrame: El procesado del DataFrame
    """
    df_proc = df_input.copy()
    
    # 1. Elimina columnas con >20% null values
    null_pct = df_proc.isnull().mean()
    cols_to_drop = null_pct[null_pct > 0.2].index
    if len(cols_to_drop) > 0:
        print(f"Columnas eliminadas (>20% nulos): {list(cols_to_drop)}")
        df_proc = df_proc.drop(columns=cols_to_drop)
    else:
        print("No hay columnas con >20% de nulos para eliminar.")
    
    # 2. Imputa valores faltantes
    numeric_cols = df_proc.select_dtypes(include=[np.number]).columns
    categorical_cols = df_proc.select_dtypes(exclude=[np.number]).columns
    
    # Imputacion numeric: Mediana (robusta a valores atipicos)
    for col in numeric_cols:
        if df_proc[col].isnull().sum() > 0:
            median_val = df_proc[col].median()
            df_proc[col] = df_proc[col].fillna(median_val)
            
    # Imputacion categórica: Moda
    for col in categorical_cols:
        if df_proc[col].isnull().sum() > 0:
            mode_val = df_proc[col].mode()[0]
            df_proc[col] = df_proc[col].fillna(mode_val)
            
    # 3. Detecta y trata valores atipicos con IQR
    # Excluye columnas objetivo o identificadores
    cols_exclude_outlier = ['NSP', 'CLASS', 'Tendency']
    cols_for_outliers = [c for c in numeric_cols if c not in cols_exclude_outlier]
    
    for col in cols_for_outliers:
        Q1 = df_proc[col].quantile(0.25)
        Q3 = df_proc[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Tratamiento: Clipping (valores límite al rango)
        # Preserva la distribución mejor que eliminar filas
        df_proc[col] = np.clip(df_proc[col], lower_bound, upper_bound)
        
    return df_proc
