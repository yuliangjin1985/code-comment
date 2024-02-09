# Introduction

This python code read a cpp file program.txt and for each line with length greater than 100, make a open api call to retrieve the comment of this line. Need to export OPENAI_API_KEY from the .zshrc, then internally it will retrieve the env vironment: `os.environ.get("OPENAI_API_KEY")`.

## Install the python environment 3.11.0

pyenv install 3.11.0
pyenv virtualenv 3.11.0 llm-env
pyenv activate llm-env
pip install python-dotenv
pip install openai
pip install typer
