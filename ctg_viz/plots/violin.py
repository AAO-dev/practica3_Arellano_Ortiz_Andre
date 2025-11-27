import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_violin_with_swarm(df, x_col='NSP', y_col='UC', sample_size=500, 
                          violin_palette="mako", swarm_color="#e74c3c", 
                          swarm_alpha=0.5, swarm_size=2.5, figsize=(12, 7), 
                          title='Distribución de Contracciones Uterinas (UC) por NSP'):
    fig, ax = plt.subplots(figsize=figsize)
    
    # Violin plot con nueva paleta de colores
    sns.violinplot(x=x_col, y=y_col, data=df, palette=violin_palette, inner=None, 
                   ax=ax, hue=x_col, legend=False)
        
    # Swarm plot overlay con color rojo
    sns.swarmplot(x=x_col, y=y_col, data=df.sample(sample_size), 
                  color=swarm_color, alpha=swarm_alpha, size=swarm_size, ax=ax)
    
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel('Clasificación NSP', fontsize=12)
    ax.set_ylabel('Contracciones Uterinas (UC)', fontsize=12)
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    plt.close(fig)
    return fig