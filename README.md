Span League Ranking Application
==============================
# span-ldmckeen-league-ranking

The following repo houses the codebase for a production ready, maintainable, testable 
command-line application that will calculate the ranking table for a league.

In this repo you will find the Problem Statement PDF with Instructions, the application 
codebase and all supporting repository files necessary for the league-ranking python app.

# Tech Stack Details
Following is a full comprehensive list of all the requirements to use and setup this
application accordingly.
## Pre-requisites
When setting up a local environment for developing ensure you are using a local
virtual environment for optimal sandboxing and testing so as to minimize clashes with 
existing setups or environments on your machine.

####Virtual Environment Setup
#####Pyenv
Recommendation: Use Pyenv where possible to manage your python installations:
https://github.com/pyenv/pyenv
https://github.com/pyenv/pyenv-virtualenv
*Tutorial* - https://realpython.com/intro-to-pyenv/

Useful pyenv commands:
`pyenv install --list` - List all pyenv versions on offer
`pyenv versions` - List pyenv versions on your machine
`pyenv install <python version>` - Install python version eg. pyenv install 3.8.7
`pyenv virtualenvs` - List virtualenv versions
`pyenv virtualenv <python version> <venv-name>` - Create Pyenv Virtual Environment
`pyenv activate <name>` - Activate Virtual Environment
`pyenv deactivate`  -  Exit Virtual Environment
`pyenv virtualenv-delete <venv-name>` - Delete Virtual Environment

To note (On Mac):
Make sure to add the envs to your bash or zsh profiles (.zshrc/.zprofile, .bashrc)
`export PYENV_ROOT="$HOME/.pyenv"`
`export PATH="$PYENV_ROOT/bin:$PATH"`
`eval "$(pyenv init --path)"`
`eval "$(pyenv init -)"`

##### Standalone virtualenv
`python3 -m pip install --user virtualenv`
`python3 -m venv env`
`source ./env/bin/activate`


### Python Version
This application makes use of Python 3.8.7

### Git Config

In order to ensure that your local git structure mirrors that of the broader style
requirements, you must setup the use of git hooks. This is done via the `pre-commit`
application. If on a Mac, ensure you `brew install pre-commit` (Sometimes you need: `xcode-select --install`)

Run the following configuration in your local repo instance:
`git config core.hooksPath .githooks`

Make sure all the dev requirements are installed by running:
`pip install -r dev-requirements.txt`

Make sure all the application requirements are installed by running:
`pip install -r requirements.txt`

Configure pre-commit
`pre-commit install`