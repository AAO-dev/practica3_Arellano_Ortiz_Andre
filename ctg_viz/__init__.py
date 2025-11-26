"""
ctg_viz: Una biblioteca para el análisis y visualización 
de datos de cardiotocografía (CTG).
"""
from .preprocessing import process_data
from .categorization import check_data_completeness_Arellano_Ortiz_Andre
from .utils import load_data, check_data_completeness

__version__ = "0.1.0"
