# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SEDAS documentation'
copyright = '2024, Daniel Pojhan'
author = 'Daniel Pojhan'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_tabs.tabs'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = "_static/sedas.png"
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}



# -- Options for EPUB output
epub_show_urls = 'footnote'
