#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Example RING Documentation documentation build configuration file, created by
# sphinx-quickstart on Wed Jul 17 11:20:31 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys, os

sys.path.append(os.path.abspath('./_ext/'))
sys.path.append(os.path.abspath('./_ext/todo/'))
sys.path.append(os.path.abspath('./_ext/helloworld/'))
sys.path.append(os.path.abspath('./_ext/sphinxcontrib/lunrsearch'))

# sys.path.insert(0, os.path.abspath('.'))

import subprocess

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.images',
    'sphinx_design',
    'sphinxcontrib.lunrsearch'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Example RING Documentation'
copyright = '2019, Scality Technical Publications'
author = 'Scality Technical Publications'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# The full version, including alpha/beta/rc tags.
version = '7.4.3-dev'


def get_git_revision():
    try:
        data = subprocess.check_output([
            "git", "describe", "--always", "--long", "--tags", "--dirty"
        ])
        return data.decode("utf-8").rstrip()
    except subprocess.CalledProcessError:
        return None


if version.endswith('-dev'):
    release = get_git_revision()
else:
    release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_scality'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'social_links': [
        ("github", "https://www.github.com/scality/sphinx-tools"),
        ("linkedin", "https://www.linkedin.com/company/scality/"),
        ("twitter", "https://twitter.com/scality"),
        ("instagram", "https://instagram.com/scalitylife"),
        ("facebook", "https://www.facebook.com/scality/"),
    ],
    'footer_links': [
        ("Support", "https://support.scality.com"),
        ("Knowledge Base", "https://support.scality.com/hc/en-us"),
        ("Training", "https://training.scality.com"),
        ("Privacy Policy", "https://www.scality.com/privacy-policy/"),
    ],
    # If this is set, will be used as an additional suggestion for search
    # results
    'kblink': 'https://support.scality.com/hc/en-us',
    # If the pages are hosted on a website, configure the link to go back to
    'homelink': 'https://documentation.scality.com',
    # This is used for the back-arrow link
    'parentlink': 'https://documentation.scality.com/RING/{}'.format(version),
    # Release notes
    'releasenoteslinkpdf': 'https://en.wikipedia.org/wiki/Release_notes',
    'releasenoteslinkhtml': 'https://confluence.atlassian.com/jirasoftware/jira-software-release-notes-776821069.html',
    'termsandconditionspdf': 'https://en.wikipedia.org/wiki/Terms_of_service',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_last_updated_fmt = '%B %d, %Y'

html_show_sphinx = False
html_show_source = False

html_logo = '_static/RING_logo.svg'


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ExampleRINGDocumentationdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ExampleRINGDocumentation.tex',
     'Example RING Documentation Documentation',
     'Scality Technical Publications', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'exampleringdocumentation',
     'Example RING Documentation Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ExampleRINGDocumentation',
     'Example RING Documentation Documentation',
     author, 'ExampleRINGDocumentation', 'One line description of project.',
     'Miscellaneous'),
]

html_context={
    "feedback":True,
}