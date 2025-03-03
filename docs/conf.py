# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import shutil
sys.path.insert(0, os.path.abspath('..'))

# Add the karta_benchmarks directory to the Python path

# Copy over specific files from the karta_benchmarks directory to the docs directory
domains = ["ecommerce"]

for domain in domains:
    # Define the source file location (1 levels up)
    source_file = os.path.abspath(f"../karta_benchmarks/evaluation_datasets/{domain}/knowledge_base/domain_knowledge.md")
    destination_file = os.path.abspath("./knowledge/ecommerce/domain_knowledge.md")
    # Copy the Markdown file if it exists
    # If the destination folder does not exist, create it
    if not os.path.exists(os.path.dirname(destination_file)):
        os.makedirs(os.path.dirname(destination_file))
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)



# -- Project information -----------------------------------------------------

project = 'Karta Open Evaluations'
copyright = '2025, GetKarta.ai'
author = 'GetKarta.ai'
html_theme = 'furo'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser'
]

myst_enable_extensions = [
    "colon_fence",  # For ::: fenced code blocks
    "deflist",       # Definition lists
    "tasklist"       # Checklists [ ] and [x]
]

# Ensuring the logo is displayed in the sidebar
html_static_path = ["_static"]
html_logo = "_static/getkarta.png"
html_css_files = ["custom.css"]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']