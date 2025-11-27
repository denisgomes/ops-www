# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation: # https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./..'))

# -- Project information -----------------------------------------------------

project = 'OPS'
copyright = '2025, Denis Gomes'
author = 'Denis Gomes'

# The full version, including alpha/beta/rc tags
# release = '0.0.1'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Pipe Stress Blog"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['ablog',
              'sphinx.ext.napoleon',
              'sphinx.ext.mathjax',
              'jupyter_sphinx',
              'nbsphinx',
]

# jupyter-sphinx
jupyter_sphinx_thebelab_config = {
    # 'bootstrap': True,
    'requestKernel': True,
    'binderOptions': {
        'repo': "denisgomes/psi",
    },
}


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
html_theme = 'alabaster'


# ABLOG
#import ablog
# templates_path.append(ablog.get_html_templates_path())

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

blog_baseurl = 'https://openpipestress.com/'

# disqus config
disqus_shortname = 'openpipestress-1'
disqus_pages = False
disqus_drafts = False

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'ablog/recentposts.html',
        'ablog/tagcloud.html',
        'ablog/categories.html',
        'ablog/archives.html',
        'searchbox.html',
        #'useful_links.html',
        #'relations.html',
        #'donate.html',
    ]
}

html_theme_options = {
    'logo': 'images/logo.png',
    # 'logo_name': True,
    # 'logo_text_align': 'left',
    'github_user': 'denisgomes',
    'github_repo': 'ops-www',
    'description': 'The pipe stress blog.',
    'fixed_sidebar': False,
    'github_banner': True,
    'github_button': True,
    'analytics_id': 'UA-155102137-1',
    'donate_url': 'https://github.com/denisgomes/ops-www',
    #'extra_nav_links':
    #{'Documentation': 'https://pipe-stress-infinity.readthedocs.io/en/latest',
    # 'Issue Tracker': 'https://github.com/denisgomes/psi/issues',
    # 'Mailing List': 'https://groups.google.com/group/pipestressinfinity-users',
    # 'Discord Server': 'https://discord.gg/xnHnwbD',
    # 'GitHub Repository': 'https://github.com/denisgomes/psi',
    # 'PyPI Package': 'https://pypi.org',
    #},
}
