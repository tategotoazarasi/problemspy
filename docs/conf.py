import os
import sys

# 将项目根目录加入路径，以便 Sphinx 能找到代码
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'ProblemsPy'
copyright = '2025, Wang Zhiheng'
author = 'Wang Zhiheng'

# -- General configuration ---------------------------------------------------
extensions = [
	'sphinx.ext.autodoc',  # 自动从 Docstring 生成文档
	'sphinx.ext.napoleon',  # 支持 Google 和 NumPy 风格注释
	'sphinx.ext.viewcode',  # 添加指向源代码的链接
	'sphinx.ext.githubpages',  # 生成 .nojekyll 文件，防止 GitHub 忽略下划线开头的文件夹
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# 使用 Read the Docs 主题，美观且经典
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
