#!/bin/bash

# Create directories
mkdir -p .vscode
mkdir -p .github/workflows
mkdir -p src
mkdir -p notebooks
mkdir -p tests
mkdir -p scripts

# Create files
touch .vscode/settings.json
touch .github/workflows/unittests.yml

# Create a .gitignore files and add neccessary files to the project
touch .gitignore
cat <<EOL > .gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook files
.ipynb_checkpoints/

# IPython
profile_default/
ipython_config.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# PyCharm IDE
.idea/

# VSCode IDE
.vscode/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre
.pyre/

# pyright
pyrightconfig.json

# Jupyter Notebook outputs
**/.ipynb_checkpoints/*
*.ipynb~  # Temporary notebook saves
**/*.nbconvert/  # Converted notebooks

# Data and model artifacts
*.h5
*.csv
*.dat
*.pkl
*.joblib
*.db
*.log
*.tar.gz
*.zip

# Temporary files
*.temp
*.tmp
*.bak
*.swp
*.swo
*.orig

# Test result files
*.out
*.err

# Editor and OS files
.DS_Store
Thumbs.db
desktop.ini
*.~lock.*

# Logs and debug files
*.log
debug.log
*.trace

# Dependency directories
__pypackages__/

# Docker
*.pid
docker-compose.override.yml

# AWS
*.pem
EOL

touch requirements.txt
touch README.md
touch src/__init__.py
touch notebooks/__init__.py
touch notebooks/README.md
touch tests/__init__.py
touch scripts/__init__.py
touch scripts/README.md
