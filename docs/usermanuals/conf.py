import os
import sys

sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath('usermanuals/'))

import sphinx_rtd_theme

project = 'Apromore'
author = 'Apromore'
copyright = '2021, ' + project
version = '8.0'
tech_version = 'Apromore v8.0'

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.todo',
    'sphinx_reredirects'
]

# locale_dirs = ['locale/']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

templates_path = ['_templates']

source_suffix = ['.rst']

master_doc = 'index'

pygments_style = 'sphinx'

todo_include_todos = True

# -- Options for HTML output ----------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_css_files = [
    'css/apromore.css',
]
html_theme_options = {
    'logo_only': True,
    'display_version': False
}
html_context = {
    'current_version': version,
    'versions': [['' + version, '#']],
    'downloads': [['PDF', 'download/apromore.pdf']],
    'READTHEDOCS': True,
    'show_source': False,
}

html_extra_path = ['download/apromore.pdf']

redirects = {
    "gettingstarted/navigatingtheapromoreportal": "../theapromoreportal/navigatingtheapromoreportal.html",
    "gettingstarted/uploadafile": "../theapromoreportal/uploadafile.html",
    "gettingstarted/createoreditprocessmodel": "../theapromoreportal/createoreditprocessmodel.html",
    "gettingstarted/sharingandaccessrights": "../theapromoreportal/sharingandaccessrights.html",
    "gettingstarted/createnewfolder": "../theapromoreportal/createnewfolder.html",
    "gettingstarted/manageusersandgroups": "../theapromoreportal/manageusersandgroups.html"
}

html_logo = "_static/img/logo.png"
html_favicon = "_static/img/favicon.png"
