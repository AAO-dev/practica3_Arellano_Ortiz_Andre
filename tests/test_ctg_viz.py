import unittest
import pandas as pd
import numpy as np
import os
import sys

# Agregue el directorio principal a sys.path para permitir la importación de ctg_viz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ctg_viz.utils import load_data, check_data_completeness
from ctg_viz.preprocessing import process_data
from ctg_viz.categorization import check_data_completeness_Arellano_Ortiz_Andre

class TestCtgViz(unittest.TestCase):

    def setUp(self):
        # Crear un DataFrame de muestra para pruebas
        self.data = {
            'A': [1, 2, np.nan, 4, 100], # Numerico con valores nulos y atipicos
            'B': ['x', 'y', 'x', np.nan, 'z'], # Categorico con valores nulos
            'C': [10, 20, 30, 40, 50], # Numerico limpio
            'NSP': [1, 1, 2, 1, 3] # Columna objetivo
        }
        self.df = pd.DataFrame(self.data)
        
        # Crear un archivo CSV temporal
        self.csv_path = 'test_data.csv'
        self.df.to_csv(self.csv_path, index=False)

    def tearDown(self):
        # Eliminar el archivo CSV temporal
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)

    def test_load_data(self):
        """Test loading data from a CSV file."""
        df_loaded = load_data(self.csv_path)
        self.assertIsInstance(df_loaded, pd.DataFrame)
        self.assertEqual(len(df_loaded), 5)
        self.assertEqual(list(df_loaded.columns), ['A', 'B', 'C', 'NSP'])

    def test_check_data_completeness(self):
        """Test the check_data_completeness function."""
        summary = check_data_completeness(self.df)
        self.assertIsInstance(summary, pd.DataFrame)
        self.assertEqual(len(summary), 4) # 4 columns in input
        
        # Verificar valores especificos para la columna 'A'
        row_a = summary[summary['Columna'] == 'A'].iloc[0]
        self.assertEqual(row_a['Nulos'], 1)
        self.assertEqual(row_a['Tipo Dato'], np.float64) # pandas moldea un float si NaN esta presente
        
        # Verificar clasificacion
        self.assertEqual(row_a['Clasificación'], 'Discreta') # < 10 valores unicos

    def test_process_data(self):
        """Test the process_data function."""
        df_proc = process_data(self.df)
        
        # Verificar imputacion de valores nulos
        self.assertEqual(df_proc['A'].isnull().sum(), 0)
        self.assertEqual(df_proc['B'].isnull().sum(), 0)
        
        # Verificar tratamiento de valores atipicos (clipping) para la columna 'A'
        # Mediana de A (ignorando NaN) es (1, 2, 4, 100) -> 3.0
        # Q1=1.75, Q3=28.0. IQR=26.25. Upper=28 + 1.5*26.25 = 67.375
        # El valor 100 debe ser clippado
        self.assertLess(df_proc['A'].max(), 100)
        
        # Verificar que NSP no es tratado (se excluye)
        self.assertEqual(df_proc['NSP'].max(), 3)

    def test_check_data_completeness_categorization(self):
        """Test the check_data_completeness function from categorization module."""
        summary = check_data_completeness_Arellano_Ortiz_Andre(self.df)
        self.assertIsInstance(summary, pd.DataFrame)
        self.assertEqual(len(summary), 4)
        
        row_b = summary[summary['Columna'] == 'B'].iloc[0]
        self.assertEqual(row_b['Nulos'], 1)
        self.assertEqual(row_b['Clasificación'], 'Discreta (Categórica)')

if __name__ == '__main__':
    unittest.main()
