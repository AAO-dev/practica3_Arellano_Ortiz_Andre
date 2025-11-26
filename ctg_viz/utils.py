"""
Funciones de utilidad para carga y análisis de datos
"""

import pandas as pd
import numpy as np

def load_data(filepath: str) -> pd.DataFrame:
    """
    Carga el dataset desde un archivo CSV

    Args:
        filepath (str): El path al archivo CSV

    Returns:
        pd.DataFrame: El dataset cargado
    """
    return pd.read_csv(filepath)

def check_data_completeness(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analiza la completitud y calidad de los datos

    Calcula conteos de valores nulos, porcentaje de completitud, tipos de datos,
    valores únicos y estadísticas básicas (std dev, varianza) para columnas numéricas.
    Clasifica columnas como 'Continua', 'Discreta' o 'Categórica'.

    Args:
        df (pd.DataFrame): El DataFrame de entrada

    Returns:
        pd.DataFrame: Un DataFrame resumen con métricas de calidad de datos para cada columna
    """
    res = []
    for col in df.columns:
        null_count = df[col].isnull().sum()
        total_rows = len(df)
        null_pct = (null_count / total_rows) * 100
        completeness_pct = 100 - null_pct
        dtype = df[col].dtype
        unique_vals = df[col].nunique()
        
        # Una sentencia condicional para conseguir estadisticas de 
        # dispersion y clasificación
        if pd.api.types.is_numeric_dtype(df[col]):
            std_dev = df[col].std()
            variance = df[col].var()
            # Clasificación automatica
            if unique_vals > 10:
                col_type = 'Continua'
            else:
                col_type = 'Discreta'
        else:
            std_dev = np.nan
            variance = np.nan
            col_type = 'Categórica'
            if unique_vals < 10:
                 col_type = 'Discreta (Cat)'

        res.append({
            'Columna': col,
            'Nulos': null_count,
            '% Completitud': round(completeness_pct, 2),
            'Tipo Dato': dtype,
            'Valores Únicos': unique_vals,
            'Std Dev': round(std_dev, 2) if not pd.isna(std_dev) else np.nan,
            'Varianza': round(variance, 2) if not pd.isna(variance) else np.nan,
            'Clasificación': col_type  
        })
    
    return pd.DataFrame(res)
