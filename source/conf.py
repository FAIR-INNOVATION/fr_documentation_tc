# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '法奧意威協作機器人使用手冊'
copyright = '2022-2025, 法奧意威（蘇州）機器人系統有限公司'
author = '法奧意威（蘇州）機器人系統有限公司'
release = '3.7.7'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_TW'
locale_dirs = ['locale/']  # 设置本地化数据目录

# 注：在生成html的时候这句话要注释
# latex_engine = 'xelatex'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_logo = '_static/logo.svg'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# highlight_language = "c,c++,python"

# def setup(app):
#     app.add_css_file('_static/custom.css')

# rst_epilog = '\n.. include:: .custom-style.rst\n'