# CPS repo mining
Repository mining using PyDriller.

## Setup
For portability and replicability of this tool, we use docker.
For easier docker setup, we provide two scripts for building docker image and running the docker container.

__! Note:__ For Windows, first install (and have it running) **_Docker for Windows_**. Then use **_Git Bash_** to run the following scripts.

### Docker image setup
Execute the following script for building the docker image:

`. docker_scripts/build-cps-repo-mining.sh`

### Docker image container
The script `docker_scripts/run-cps-repo-mining-container.sh` is created for this task. 
For running the mining for remote repositories, this script can be executed without any input parameter.
However, to perform the mining process for local repositories, we should pass the directory of local repositories as the input argument:

`. docker_scripts/run-cps-repo-mining-container.sh [local_repositories]`

__! Note:__ This input argument should be an absolute path.

## Usage
There are multiple scripts that can be used.

### Commit message
Mining the repository on content from commit messages, based on an input list of keywords:\
`docker exec -it cps-repo-mining-container bash -c "python3 pd/repository_commits_mining.py [lx/rx/la/ra]"`

The options are:\
lx = local\
rx = remote\
la = all local\
ra = all remote\
Where x stands for the number in the repository list.

### Commit diffs
Searching through the commit diffs, from the above script result, for specific code snippet.\
`docker exec -it cps-repo-mining-container bash -c "python3 pd/search_selection.py"`


### Current code state
Searching through the current state of the full repositories, for code snippets.\
`docker exec -it cps-repo-mining-container bash -c "python3 pd/search_current.py"`


## Generate reports
To generate coverage, mutation and docstring reports, run:\
`docker exec -it cps-repo-mining-container bash -c "./generate_reports"`

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
