"""
Módulos de visualización para datos CTG (Distribution)
"""

import altair as alt
import pandas as pd

def plot_boxplot_uc_by_nsp(df: pd.DataFrame) -> alt.Chart:
    """
    Crea un gráfico de caja (boxplot) interactivo de 'UC' por 'NSP' usando Altair

    Args:
        df (pd.DataFrame): El DataFrame de entrada
        
    Returns:
        alt.Chart: Gráfico de Altair con boxplot y puntos
    """
    # Preparar datos: convertir NSP a string para mejor visualización
    df_plot = df.copy()
    df_plot['NSP'] = df_plot['NSP'].astype(str)
    
    # Boxplot base con Altair
    boxplot = alt.Chart(df_plot).mark_boxplot(
        size=50,
        color='#3498db'
    ).encode(
        x=alt.X('NSP:N', title='Clasificación NSP', axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
        y=alt.Y('UC:Q', title='Contracciones Uterinas (UC)', axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
        color=alt.Color('NSP:N', 
                       scale=alt.Scale(scheme='tableau10'),
                       legend=alt.Legend(title='NSP'))
    ).properties(
        width=600,
        height=400,
        title=alt.Title(
            'Boxplot de Contracciones Uterinas (UC) por Clasificación NSP',
            fontSize=16,
            fontWeight='bold'
        )
    )
    
    # Puntos individuales para mostrar distribución
    points = alt.Chart(df_plot.sample(min(300, len(df_plot)))).mark_circle(
        size=30,
        opacity=0.3
    ).encode(
        x=alt.X('NSP:N', title='Clasificación NSP'),
        y=alt.Y('UC:Q', title='Contracciones Uterinas (UC)'),
        color=alt.Color('NSP:N', scale=alt.Scale(scheme='tableau10'), legend=None)
    )
    
    # Combinar boxplot con puntos
    chart = (boxplot + points).configure_axis(
        gridOpacity=0.3
    ).configure_view(
        strokeWidth=0
    )
    
    return chart
