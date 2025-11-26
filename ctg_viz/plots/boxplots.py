"""
Módulos de visualización para datos CTG (Boxplots)
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def plot_boxplot_astv_by_nsp(df: pd.DataFrame) -> go.Figure:
    """
    Crea un boxplot de 'ASTV' por 'NSP' en Plotly

    Args:
        df (pd.DataFrame): El DataFrame de entrada

    Returns:
        go.Figure: El objeto de figura de Plotly
    """
    fig = px.box(
        df,
        x='NSP',
        y='ASTV',
        color='NSP',
        title='Boxplot de ASTV (Abnormal Short Term Variability) por Clase NSP - Plotly',
        labels={'NSP': 'NSP (1=Normal, 2=Sospechoso, 3=Patológico)', 'ASTV': 'ASTV (%)'},
        color_discrete_sequence=px.colors.qualitative.Set2,
        points='outliers',
        notched=True
    )

    fig.update_layout(
        template='plotly_white',
        height=600,
        showlegend=True,
        font=dict(size=12)
    )
    return fig
