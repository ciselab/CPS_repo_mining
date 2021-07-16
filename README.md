# CPS repo mining
Repository mining using PyDriller.

## Setup
To make the setup a bit faster, a script has been created.

Execute the script as follows:\
`./build_virtual_env.sh`

After this script has run, activate the virtual environment:\
`. env/bin/activate`

Everything is now setup and ready to go!

## Virtual Environment usage
Start the virtual environment by:\
`. env/bin/activate`

Deactivate by:\
`deactivate`

## Usage
There are multiple scripts that can be used.

### Commit message
Mining the repository on content from commit messages, based on an input list of keywords:\
`python3 pd/repository_commits_mining.py [lx/rx/la/ra]`

The options are:\
lx = local\
rx = remote\
la = all local\
ra = all remote\
Where x stands for the number in the repository list.

### Commit diffs
Searching through the commit diffs, from the above script result, for specific code snippet.\
`python3 pd/search_selection.py`

### Current code state
Searching through the current state of the full repositories, for code snippets.\
`python3 pd/search_current.py`

## Generate reports
To generate coverage, mutation and docstring reports, run:\
`./generate_reports`

## Manual generating reports
Be aware that the location for the reports that are made for pdoc and mutmut end in the same directory.\
Run pdoc with --force to run it anyway.

### Pytest
In order to run pytest:\
`pytest`

To generate the pytest report:\
`pytest --cov-report html --cov=pd`

### Mutation testing
In order to run mutmut:\
`mutmut run`

To generate the mutmut report:\
`mutmut html`

### PDoc
In order to run python docstring documentation report:\
`pdoc --html pdoc`
