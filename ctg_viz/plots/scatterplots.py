"""
Módulos de visualización para datos CTG (Scatterplots)
"""

import altair as alt
import pandas as pd

def plot_scatter_lb_astv(df: pd.DataFrame) -> alt.Chart:
    """
    Crea un gráfico de dispersión de Altair de 'LB' vs 'ASTV'

    Args:
        df (pd.DataFrame): El DataFrame de entrada

    Returns:
        alt.Chart: El objeto de gráfico de Altair
    """
    base = alt.Chart(df).encode(
        x=alt.X('LB', title='Latidos por minuto (LB)'),
        y=alt.Y('ASTV', title='ASTV (%)'),
        tooltip=['LB', 'ASTV', 'NSP', 'CLASS']
    ).properties(
        title='Relación entre LB y ASTV por Clase NSP - Altair (Interactivo)'
    )

    brush = alt.selection_interval()
    
    points = base.mark_circle().encode(
        color=alt.Color('NSP:N', scale=alt.Scale(scheme='category10'), legend=alt.Legend(title='Clase NSP')),
        opacity=alt.value(0.7)
    ).add_params(
        brush
    )

    return points.interactive()
