import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_violin_with_swarm(df, x_col='NSP', y_col='UC', sample_size=500, 
                          violin_palette="Pastel1", swarm_color="k", 
                          swarm_alpha=0.6, swarm_size=3, figsize=(12, 7), 
                          title='Violin Plot con Swarm Overlay: Contracciones Uterinas (UC) por NSP'):
    fig, ax = plt.subplots(figsize=figsize)
    
    # Violin plot
    sns.violinplot(x=x_col, y=y_col, data=df, palette=violin_palette, inner=None, ax=ax)
    
    # Swarm plot overlay (usamos una muestra pequeña para no saturar)
    sns.swarmplot(x=x_col, y=y_col, data=df.sample(sample_size), 
                  color=swarm_color, alpha=swarm_alpha, size=swarm_size, ax=ax)
    
    ax.set_title(title, fontsize=15)
    return fig