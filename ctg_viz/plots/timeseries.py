"""
Módulos de visualización para datos CTG (Timeseries)
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_line_lb_evolution(df: pd.DataFrame) -> plt.Figure:
    """
    Crea un gráfico de línea de Seaborn de 'LB' (serie temporal simulada)

    Args:
        df (pd.DataFrame): El DataFrame de entrada
    """
    fig, ax = plt.subplots(figsize=(14, 5))
    # Use a subset of 200 data points for clarity
    subset = df.iloc[:200]
    sns.lineplot(data=subset, x=subset.index, y='LB', linewidth=2, color='teal', ax=ax)
    ax.set_title('Serie Temporal Simulada: Evolución de LB (Primeros 200 registros)', fontsize=15)
    ax.set_xlabel('Índice de Tiempo (Simulado)')
    ax.set_ylabel('LB')
    ax.fill_between(subset.index, subset['LB'], alpha=0.2, color='teal')
    return fig
