# -- Project information -----------------------------------------------------
project = 'YukkiMusic'
copyright = '2024, VivekKumar-IN'
author = 'VivekKumar-IN'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# Disable the search box
html_theme_options = {
    'search_box': False,  # Disable search box
}