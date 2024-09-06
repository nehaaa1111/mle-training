# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))  # Adjust the path as needed


# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',  # Include this for automatic documentation of docstrings
    'sphinx.ext.napoleon',  # To support Google and NumPy style docstrings
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The theme to use for HTML and HTML Help pages. See the documentation for a list of built-in themes.
html_theme = 'sphinx_rtd_theme'


project = 'Housing Project'
copyright = '2024, Neha Rawat'
author = 'Neha Rawat'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'Python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
