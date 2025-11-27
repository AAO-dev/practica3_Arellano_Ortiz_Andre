import altair as alt
import pandas as pd

def plot_density_width_by_nsp(df: pd.DataFrame) -> alt.Chart:
    """
    Crea un gráfico de densidad interactivo de 'Width' por 'NSP' usando Altair

    Args:
        df (pd.DataFrame): El DataFrame de entrada
        
    Returns:
        alt.Chart: Gráfico de área de densidad interactivo
    """
    # Preparar datos: convertir NSP a string para mejor visualización
    df_plot = df.copy()
    df_plot['NSP'] = df_plot['NSP'].astype(str)
    
    chart = alt.Chart(df_plot).transform_density(
        density='Width',
        as_=['Width_density', 'density'],
        groupby=['NSP']
    ).mark_area(opacity=0.5).encode(
        x=alt.X('Width_density:Q', title='Ancho del Histograma (Width)'),
        y=alt.Y('density:Q', title='Densidad'),
        color=alt.Color('NSP:N', scale=alt.Scale(scheme='viridis'), title='NSP'),
        tooltip=['NSP:N', alt.Tooltip('Width_density:Q', title='Width', format='.2f'), alt.Tooltip('density:Q', format='.4f')]
    ).properties(
        title=alt.TitleParams(
            text='Densidad de Ancho de Histograma (Width) por Clasificación NSP',
            fontSize=16,
            fontWeight='bold'
        ),
        width=600,
        height=400
    ).interactive()
    
    return chart
