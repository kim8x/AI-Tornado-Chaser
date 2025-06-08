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
    'myst_parser',  # for Markdown support
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Language settings
language = 'fr'
locale_dirs = ['locale/']   # path is example but recommended
gettext_compact = False     # optional
gettext_uuid = True        # optional

# Source file parsers
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst'
}

# The master toctree document
master_doc = 'contents'
