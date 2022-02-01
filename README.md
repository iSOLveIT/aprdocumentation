
# Apromore Sphinx Documentation

The user guide is available on https://documentation.apromore.org/

## Prerequisites
- Python for Windows: https://www.python.org/downloads/
- Sphinx: https://www.sphinx-doc.org/en/master/usage/installation.html#windows
- ActivePerl: https://www.activestate.com/products/perl/downloads/
- MikTex: https://miktex.org/download

## Sphinx Setup
`pip3 install Sphinx==3.2.1`

`pip install sphinx-rtd-theme`

`pip3 install sphinx-reredirects`

## Steps
- Clone the git repository: `git clone https://github.com/apromore/aprdocumentation.git`
- Check out the relevant branch e.g main
- Open the project in Editor of your choice e.g Atom

## Structure
- Each section in the user guide is represented by individual directories. We have 6 main sections in the user guide, the contents of which are present in their respective folders. For example, the contents of Getting Started section of the user guide are present in the gettingstarted folder. 
- The Makefile and conf.py files have all the configurations related to Sphinx and Readthedocs theme.
- The table of contents and directory structure is present in index.rst located in the main directory. 
- Each individual section directory has its own individual index.rst that consists of its own sub-sections. In order to add a new sub-section please remember to add the title in the index.rst.
- The _templates folder has a breadcrumbs.html file that is needed to alter the existing readthedocs theme.
- The apromore.css file is located in _build\html\_static\css\ directory.
- All logos and favicons are present in _build\html_static\img directory.

## Build
- Run the `make.html` command in the `\aprdocumentation\docs\usermanuals` directory to build all the .rst pages. Open the index.html page in your preferred browser to verify your changes.
- Run the make `latexpdf` in the `\aprdocumentation\docs\usermanuals` directory to create the pdf.
