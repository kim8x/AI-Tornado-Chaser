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
    'myst_parser',
    'sphinx_rtd_theme',
]

# Configuration for myst_parser
myst_enable_extensions = [
    "colon_fence",
    "deflist"
]

# Source parsing
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document
master_doc = 'index'

# Language settings
language = 'fr'
locale_dirs = ['locale/']
gettext_compact = False

# Theme configuration
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
templates_path = ['_templates']

# Files to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Other settings
nitpicky = True
smartquotes = False
