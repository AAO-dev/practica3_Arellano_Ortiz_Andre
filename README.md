# ctg_viz

Biblioteca en Python para el análisis y visualización de datos de Cardiotocografía (CTG).

## Información del Paquete

- **Nombre del Paquete**: `ctg-viz`
- **Versión**: 0.1.0
- **Autor**: Arellano Ortiz Andre
- **Correo Electrónico**: arellanoortizandre@gmail.com
- **Repositorio**: [https://github.com/AAO-dev/practica3_Arellano_Ortiz_Andre](https://github.com/AAO-dev/practica3_Arellano_Ortiz_Andre)

## Descripción

`ctg_viz` es una biblioteca especializada que proporciona herramientas para la carga, preprocesamiento, análisis y visualización de datos de cardiotocografía. Incorpora funciones optimizadas para el tratamiento de datos médicos y ofrece múltiples opciones de visualización utilizando las bibliotecas Altair y Plotly.

## Estructura del Proyecto

```
practica3_Arellano_Ortiz_Andre/
├── ctg_viz/              # Paquete principal
│   ├── __init__.py       # Inicialización del paquete
│   ├── utils.py          # Utilidades de carga de datos
│   ├── preprocessing.py  # Preprocesamiento de datos
│   ├── categorization.py # Análisis de completitud
│   └── plots/            # Módulo de visualizaciones
│       ├── __init__.py
│       ├── histograms.py
│       ├── boxplots.py
│       ├── barplots.py
│       ├── density.py
│       ├── heatmap.py
│       └── ...
├── tests/                # Pruebas unitarias
│   └── test_ctg_viz.py
├── data/                 # Datos de ejemplo
│   └── CTG.csv
├── app.py                # Aplicación Streamlit
├── demostracion.ipynb    # Notebook de demostración
├── setup.py              # Configuración del paquete
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

## Características Principales

- **Carga de Datos**: Funciones dedicadas para la importación de conjuntos de datos CTG desde archivos CSV.
- **Análisis de Completitud**: Herramientas para la evaluación de la calidad y completitud de los datos.
- **Preprocesamiento Robusto**:
  - Eliminación automática de columnas con una alta proporción de valores nulos.
  - Imputación inteligente de datos (mediana para variables numéricas, moda para variables categóricas).
  - Tratamiento de valores atípicos (outliers) mediante el método del Rango Intercuartílico (IQR).
- **Visualizaciones Interactivas**:
  - Histogramas.
  - Gráficos de violín.
  - Series temporales.
  - Diagramas de dispersión.
  - Mapas de calor de correlación.
  - Gráficos de barras.
  - Diagramas de caja (Boxplots).
  - Gráficos de densidad.

## Instalación


Siga estos pasos para ejecutar el proyecto completo:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/AAO-dev/practica3_Arellano_Ortiz_Andre.git
cd practica3_Arellano_Ortiz_Andre
```

### 2. Instalar Dependencias

**Opción A: Usando requirements.txt (Recomendado)**
```bash
python -m pip install -r requirements.txt
```

**Opción B: Instalación del paquete**

Para uso básico:
```bash
python -m pip install -e .
```

Para desarrollo (incluye pytest, jupyter, etc.):
```bash
python -m pip install -e ".[dev]"
```

### 3. Ejecutar la Aplicación Streamlit

```bash
python -m streamlit run app.py
```

Esto abrirá una interfaz web interactiva.

### 4. Ejecutar las Pruebas Unitarias

```bash
python -m pytest tests/
```

### 5. Explorar el Notebook de Demostración

```bash
jupyter notebook demostracion.ipynb
```

Este notebook contiene ejemplos de uso de todos los módulos y funciones disponibles.


## Visualización Web con Streamlit

Para iniciar la aplicación interactiva, ejecute el siguiente comando en su terminal:

```bash
python -m streamlit run app.py
```

Esta acción abrirá una interfaz web que le permitirá cargar sus datos y explorar las visualizaciones de manera dinámica.

## Uso Básico

### Carga y Preprocesamiento de Datos

A continuación se presenta un ejemplo de cómo cargar y procesar los datos:

```python
from ctg_viz import load_data, process_data, check_data_completeness

# Cargar datos
df = load_data('data/CTG.csv')

# Analizar completitud
report = check_data_completeness(df)
print(report)

# Preprocesar datos
df_clean = process_data(df)
```

### Creación de Visualizaciones

Ejemplos de generación de gráficos:

```python
from ctg_viz.plots import (
    plot_histogram_lb_by_nsp,
    plot_correlation_heatmap,
    plot_boxplot_astv_by_nsp
)

# Histograma interactivo
chart = plot_histogram_lb_by_nsp(df_clean)
chart.show()

# Mapa de calor de correlaciones
variables = ['LB', 'AC', 'FM', 'UC', 'ASTV']
heatmap = plot_correlation_heatmap(df_clean, variables)
heatmap.show()

# Diagrama de caja (Boxplot)
boxplot = plot_boxplot_astv_by_nsp(df_clean)
boxplot.show()
```

## Módulos Disponibles

### `ctg_viz.utils`
- `load_data(filepath)`: Carga datos desde un archivo CSV.
- `check_data_completeness(df)`: Realiza un análisis de completitud de los datos.

### `ctg_viz.preprocessing`
- `process_data(df)`: Ejecuta el flujo completo de preprocesamiento.

### `ctg_viz.categorization`
- `check_data_completeness_Arellano_Ortiz_Andre(df)`: Análisis personalizado de completitud.

### `ctg_viz.plots`
- `plot_histogram_lb_by_nsp(df)`: Histograma generado con Altair.
- `plot_violin_with_swarm(df)`: Gráfico de violín generado con Plotly.
- `plot_line_lb_evolution(df)`: Serie temporal generada con Altair.
- `plot_scatter_lb_astv(df)`: Diagrama de dispersión generado con Plotly.
- `plot_correlation_heatmap(df, variables)`: Mapa de calor generado con Altair.
- `plot_bar_class_counts(df)`: Gráfico de barras generado con Plotly.
- `plot_boxplot_astv_by_nsp(df)`: Diagrama de caja generado con Plotly.
- `plot_boxplot_uc_by_nsp(df)`: Diagrama de caja generado con Plotly.
- `plot_density_width_by_nsp(df)`: Gráfico de densidad generado con Altair.

## Pruebas

Para ejecutar las pruebas unitarias, utilice el siguiente comando:

```bash
python -m pytest tests/
```

## Documentación Adicional

Consulte el cuaderno de demostración `demostracion.ipynb` para ver ejemplos completos de uso de todos los módulos disponibles.

## Requisitos

### Dependencias Principales

- Python >= 3.8
- pandas >= 1.3.0
- numpy >= 1.21.0
- altair >= 4.2.0
- plotly >= 5.0.0
- seaborn >= 0.11.0
- matplotlib >= 3.4.0
- streamlit >= 1.0.0
- pytest >= 7.0.0
- pytest-cov >= 3.0.0
- jupyter >= 1.0.0
- notebook >= 6.4.0

## Autor

**Arellano Ortiz Andre**  
Correo: arellanoortizandre@gmail.com

## Licencia

Este proyecto está bajo la Licencia MIT.

MIT License

Copyright (c) 2025 Arellano Ortiz Andre

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y los archivos de documentación asociados (el "Software"), para utilizar el Software sin restricciones, incluidos, entre otros, los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del Software, y para permitir a las personas a las que se les proporcione el Software que lo hagan, con sujeción a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUIDAS, ENTRE OTRAS, LAS GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN CONTRACTUAL, EXTRACONTRACTUAL O DE OTRO TIPO, QUE SURJA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTRAS OPERACIONES EN EL SOFTWARE.
