import streamlit as st
import pandas as pd
from ctg_viz import load_data, process_data, check_data_completeness
from ctg_viz.plots import (
    plot_histogram_lb_by_nsp,
    plot_violin_with_swarm,
    plot_line_lb_evolution,
    plot_scatter_lb_astv,
    plot_correlation_heatmap,
    plot_bar_class_counts,
    plot_boxplot_astv_by_nsp,
    plot_violin_uc_by_nsp,
    plot_density_width_by_nsp
)

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Cardiotocografía (CTG)",
    page_icon="❤️",
    layout="wide"
)

def main():
    st.title("❤️ Análisis y Visualización de Datos CTG")
    st.markdown("""
    Esta aplicación permite explorar y visualizar datos de cardiotocografía para el análisis de la salud fetal.
    Utiliza la librería `ctg_viz` para el procesamiento y generación de gráficos.
    """)

    # Sidebar
    st.sidebar.header("Configuración")
    
    # Carga de datos
    data_file = st.sidebar.file_uploader("Cargar archivo CSV", type=['csv'])
    
    if data_file is not None:
        try:
            df = load_data(data_file)
            st.sidebar.success("Datos cargados exitosamente!")
        except Exception as e:
            st.sidebar.error(f"Error al cargar el archivo: {e}")
            return
    else:
        # Intentar cargar el archivo por defecto si existe
        try:
            df = load_data('data/CTG.csv')
            st.sidebar.info("Usando dataset por defecto (data/CTG.csv)")
        except FileNotFoundError:
            st.warning("Por favor, sube un archivo CSV para comenzar.")
            return

    # Preprocesamiento
    if st.sidebar.checkbox("Mostrar reporte de completitud", value=False):
        st.subheader("📋 Reporte de Completitud de Datos")
        completeness = check_data_completeness(df)
        st.dataframe(completeness)

    # Procesar datos para visualización
    df_clean = process_data(df)
    
    st.divider()

    # Visualizaciones
    st.header("📊 Visualizaciones Interactivas")

    tab1, tab2, tab3 = st.tabs(["Distribuciones", "Relaciones", "Series de Tiempo"])

    with tab1:
        st.subheader("Distribuciones de Variables")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Histograma LB por NSP")
            st.altair_chart(plot_histogram_lb_by_nsp(df_clean), use_container_width=True)
            
            st.markdown("### Densidad Width por NSP")
            st.pyplot(plot_density_width_by_nsp(df_clean), use_container_width=True)

        with col2:
            st.markdown("### Conteo de Clases (NSP)")
            st.plotly_chart(plot_bar_class_counts(df_clean), use_container_width=True)
            
            st.markdown("### Violín UC por NSP")
            st.pyplot(plot_violin_uc_by_nsp(df_clean), use_container_width=True)

    with tab2:
        st.subheader("Relaciones entre Variables")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Scatter LB vs ASTV")
            st.altair_chart(plot_scatter_lb_astv(df_clean), use_container_width=True)
            
            st.markdown("### Boxplot ASTV por NSP")
            st.plotly_chart(plot_boxplot_astv_by_nsp(df_clean), use_container_width=True)

        with col2:
            st.markdown("### Mapa de Calor de Correlación")
            # Selector de variables para correlación
            all_cols = df_clean.select_dtypes(include=['number']).columns.tolist()
            default_cols = ['LB', 'AC', 'FM', 'UC', 'ASTV', 'MSTV', 'ALTV', 'MLTV']
            # Filtrar default_cols para asegurar que existen en el df
            default_cols = [c for c in default_cols if c in all_cols]
            
            selected_cols = st.multiselect(
                "Selecciona variables para correlación", 
                all_cols, 
                default=default_cols
            )
            
            if selected_cols:
                st.altair_chart(plot_correlation_heatmap(df_clean, selected_cols), use_container_width=True)
            
            st.markdown("### Violín con Swarm (LB por NSP)")
            st.pyplot(plot_violin_with_swarm(df_clean), use_container_width=True)

    with tab3:
        st.subheader("Análisis Temporal")
        st.markdown("### Evolución de LB (Simulada)")
        st.pyplot(plot_line_lb_evolution(df_clean), use_container_width=True)

    # Footer
    st.markdown("---")
    st.markdown("Desarrollado con `ctg_viz` | Streamlit")

if __name__ == "__main__":
    main()
