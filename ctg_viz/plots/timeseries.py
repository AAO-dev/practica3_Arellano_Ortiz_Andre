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
    
    # Cambio de color a un esquema más vibrante: azul oscuro con relleno
    sns.lineplot(data=subset, x=subset.index, y='LB', linewidth=2.5, color='#1f77b4', ax=ax)
    ax.set_title('Serie Temporal: Evolución de Línea Base (LB) - Primeros 200 Registros', fontsize=16, fontweight='bold')
    ax.set_xlabel('Índice Temporal', fontsize=12)
    ax.set_ylabel('Línea Base (LB)', fontsize=12)
    ax.fill_between(subset.index, subset['LB'], alpha=0.3, color='#1f77b4')
    ax.grid(True, alpha=0.3, linestyle='--')
    
    plt.close(fig)
    return fig
