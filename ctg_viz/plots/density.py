"""
Módulos de visualización para datos CTG (Density)
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_density_width_by_nsp(df: pd.DataFrame) -> plt.Figure:
    """
    Crea un gráfico de densidad de 'Width' por 'NSP' en Seaborn

    Args:
        df (pd.DataFrame): El DataFrame de entrada
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(data=df, x='Width', hue='NSP', fill=True, palette="crest", alpha=0.5, linewidth=2, ax=ax)
    ax.set_title('Gráfico de Densidad de Width por Clase NSP', fontsize=15)
    ax.set_xlabel('Width')
    return fig
