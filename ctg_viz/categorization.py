import pandas as pd
import numpy as np

def check_data_completeness_Arellano_Ortiz_Andre(df):
    """
    Función general para verificar la completitud y calidad de los datos.
    Incluye:
    - Conteo de Nulos
    - Porcentaje de completitud
    - Tipo de Datos
    - Estadísticos de Dispersión (Std, Varianza) para numéricos
    - Clasificación automática (Continua/Discreta)
    """
    res = []
    for col in df.columns:
        null_count = df[col].isnull().sum()
        total_rows = len(df)
        null_pct = (null_count / total_rows) * 100
        completeness_pct = 100 - null_pct
        dtype = df[col].dtype
        unique_vals = df[col].nunique()
        
        # Una sentencia condicional para calcular estadisticos de dispersion y clasificacion
        if pd.api.types.is_numeric_dtype(df[col]):
            std_dev = df[col].std()
            variance = df[col].var()
            # Se realiza la clasificacion automatica
            if unique_vals > 10:
                col_type = 'Continua'
            else:
                col_type = 'Discreta'
        else:
            std_dev = np.nan
            variance = np.nan
            col_type = 'Categórica'
            if unique_vals < 10:
                 col_type = 'Discreta (Categórica)'

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

