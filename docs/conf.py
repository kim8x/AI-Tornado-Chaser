import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Tropical-Cyclone-chasers'
copyright = '2025'
author = 'Tropical Cyclone Team'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

language = 'fr'
