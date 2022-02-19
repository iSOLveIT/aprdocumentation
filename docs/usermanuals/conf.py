import os
import sys
from datetime import datetime as dt

sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath('usermanuals/'))

# import sphinx_rtd_theme
import sphinx_material

project = 'Apromore'
author = 'Apromore'
copyright = "{0}, {1}".format(dt.utcnow().year, project)
version = '8.0'
tech_version = 'Apromore v8.0'

extensions = [
    'sphinx_material',
    'sphinx.ext.todo',
    'sphinx_reredirects'
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

templates_path = ['_templates']

source_suffix = ['.rst']

master_doc = 'index'

pygments_style = 'sphinx'

todo_include_todos = True

# -- Options for HTML output ----------------------------------------------
html_static_path = ['_static']
html_css_files = [
    'css/apromore.css',
]

# Required theme setup
html_theme = 'sphinx_material'
# Set the logo and favicon
html_logo = "_static/img/apromore_logo.png"
html_favicon = "_static/img/favicon.png"
# Set link name generated in the top bar.
html_title = 'Apromore'
# Material theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    'nav_title': 'Home',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://randy-aprdocs.readthedocs.io/en/latest/',
    # Set the color and the accent color
    'color_primary': 'deep-orange',
    'color_accent': 'deep-orange',
    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/iSOLveIT/aprdocumentation',
    'repo_name': 'Apromore',
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 2,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,
    'html_minify': True,
    'css_minify': True,
    'theme_color': 'bb3a50'
}
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}


html_context = {
    'current_version': version,
    'versions': [['' + version, '#']],
    'downloads': [['PDF', 'downloads/apromore.pdf']],
    'READTHEDOCS': True,
    'show_source': False,
}
html_show_sphinx = False
html_extra_path = ['download/apromore.pdf']

redirects = {
    "gettingstarted/navigatingtheapromoreportal": "../theapromoreportal/navigatingtheapromoreportal.html",
    "gettingstarted/uploadafile": "../theapromoreportal/uploadafile.html",
    "gettingstarted/createoreditprocessmodel": "../theapromoreportal/createoreditprocessmodel.html",
    "gettingstarted/sharingandaccessrights": "../theapromoreportal/sharingandaccessrights.html",
    "gettingstarted/createnewfolder": "../theapromoreportal/createnewfolder.html",
    "gettingstarted/manageusersandgroups": "../theapromoreportal/manageusersandgroups.html"
}

rst_epilog = """

.. |Apromore| replace:: Apromore\ :sup:`®`

.. |br| raw:: html 

   <br>

"""

# Internationalization options
locale_dirs = ['locale/']
gettext_compact = False
gettext_uuid = True
