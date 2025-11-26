"""
Setup de instalación para el paquete ctg_viz
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read version from __init__.py
version = {}
with open(os.path.join(this_directory, 'ctg_viz', '__init__.py'), encoding='utf-8') as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line, version)
            break

setup(
    name='ctg-viz',
    version=version.get('__version__', '0.1.0'),
    author='Arellano Ortiz Andre',
    author_email='arellanoortizandre@gmail.com',
    description='Un paquete para la visualización de datos de Cardiotocografía (CTG)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AAO-dev/practica3_Arellano_Ortiz_Andre',
    packages=find_packages(exclude=['tests', 'otros', 'data']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Publico objetivo :: Investigadores',
        'Publico objetivo :: Industria de la Salud',
        'Topico :: Investigación Científica :: Aplicaciones Médicas',
        'Topico :: Investigación Científica :: Visualización',
        'Licencia :: OSI Aprobada :: MIT License',
        'Lenguaje de Programación :: Python :: 3',
        'Lenguaje de Programación :: Python :: 3.8',
        'Lenguaje de Programación :: Python :: 3.9',
        'Lenguaje de Programación :: Python :: 3.10',
        'Lenguaje de Programación :: Python :: 3.11',
        'Lenguaje de Programación :: Python :: 3.12',
    ],
    python_requires='>=3.8',
    install_requires=[
        'pandas>=1.3.0',
        'numpy>=1.21.0',
        'altair>=4.2.0',
        'plotly>=5.0.0',
        'seaborn>=0.11.0',
        'matplotlib>=3.4.0',
        'streamlit>=1.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=3.0.0',
            'jupyter>=1.0.0',
            'notebook>=6.4.0',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords='cardiotocografía ctg datos médicos visualización análisis de datos',
)
