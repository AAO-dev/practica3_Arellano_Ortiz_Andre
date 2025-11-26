"""
Módulos de visualización para datos CTG (Heatmaps)
"""

import altair as alt
import pandas as pd

def plot_correlation_heatmap(df: pd.DataFrame, variables: list[str]) -> alt.Chart:
    """
    Crea un mapa de calor de correlaciones

    Args:
        df (pd.DataFrame): El DataFrame de entrada.
        variables (list[str]): Lista de variables para incluir en la matriz de correlación

    Returns:
        alt.Chart: El objeto de gráfico de Altair
    """
    correlation_matrix = df[variables].corr().reset_index().melt('index')
    correlation_matrix.columns = ['Variable1', 'Variable2', 'Correlation']

    return alt.Chart(correlation_matrix).mark_rect().encode(
        x=alt.X('Variable1:N', title=''),
        y=alt.Y('Variable2:N', title=''),
        color=alt.Color('Correlation:Q', 
                       scale=alt.Scale(scheme='redblue', domain=[-1, 1]),
                       legend=alt.Legend(title='Correlación')),
        tooltip=['Variable1:N', 'Variable2:N', alt.Tooltip('Correlation:Q', format='.2f')]
    ).properties(
        width=500,
        height=500,
        title='Mapa de Calor - Correlación entre Variables - Altair'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16
    )
