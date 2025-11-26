"""
Módulos de visualización para datos CTG (Barplots)
"""

import plotly.graph_objects as go
import pandas as pd

def plot_bar_class_counts(df: pd.DataFrame) -> go.Figure:
    """
    Crea un gráfico de barras horizontal de conteos de 'CLASS' en Plotly

    Args:
        df (pd.DataFrame): El DataFrame de entrada

    Returns:
        go.Figure: El objeto de figura de Plotly
    """
    class_counts = df['CLASS'].value_counts().sort_values(ascending=True)

    fig = go.Figure(go.Bar(
        x=class_counts.values,
        y=class_counts.index.astype(str),
        orientation='h',
        marker=dict(
            color=class_counts.values,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Frecuencia")
        ),
        text=class_counts.values,
        textposition='auto',
    ))

    fig.update_layout(
        title='Frecuencia de Registros por Clase Morfológica (CLASS) - Plotly',
        xaxis_title='Número de Registros',
        yaxis_title='Clase Morfológica (CLASS)',
        template='plotly_white',
        height=600,
        font=dict(size=12)
    )
    return fig
