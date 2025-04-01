import os
import sys

sys.path.insert(0, os.path.abspath('../..')) # Maybe now it will import the module properly?
# -- Project information -----------------------------------------------------

project = 'Python-NAbleAPI'
author = 'Fryan O'
release = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon'
]
autodoc_mock_imports = ['xmltodict','requests']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

highlight_language = 'python3'

html_theme = 'sphinx_rtd_theme'
# -- Options for HTML output -------------------------------------------------