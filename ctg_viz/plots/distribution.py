"""
Módulos de visualización para datos CTG (Distribution)
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_violin_uc_by_nsp(df: pd.DataFrame) -> plt.Figure:
    """
    Crea un gráfico de violin de 'UC' por 'NSP' con overlay de swarm

    Args:
        df (pd.DataFrame): El DataFrame de entrada
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    # Violin plot
    sns.violinplot(x='NSP', y='UC', data=df, palette="Pastel1", inner=None, ax=ax)
    # Swarm plot overlay (using a small sample to avoid saturation)
    sns.swarmplot(x='NSP', y='UC', data=df.sample(min(500, len(df))), color="k", alpha=0.6, size=3, ax=ax)
    ax.set_title('Violin Plot con Swarm Overlay: Contracciones Uterinas (UC) por NSP', fontsize=15)
    return fig
