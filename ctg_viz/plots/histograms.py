"""
Módulos de visualización para datos CTG (Histogramas)
"""

import altair as alt
import pandas as pd

def plot_histogram_lb_by_nsp(df: pd.DataFrame) -> alt.Chart:
    """
    Crea un histograma de Altair de 'LB' (Baseline Heart Rate) agrupado por 'NSP'

    Args:
        df (pd.DataFrame): El DataFrame de entrada

    Returns:
        alt.Chart: El objeto de gráfico de Altair
    """
    return alt.Chart(df).mark_bar(opacity=0.7).encode(
        x=alt.X('LB', bin=alt.Bin(maxbins=30), title='Latidos por minuto (LB)'),
        y=alt.Y('count()', title='Frecuencia'),
        color=alt.Color('NSP:N', legend=alt.Legend(title='Clase NSP'), scale=alt.Scale(scheme='category10')),
        tooltip=['LB', 'count()', 'NSP']
    ).properties(
        title='Distribución de LB (Baseline Heart Rate) por Clase NSP - Altair'
    ).interactive()
