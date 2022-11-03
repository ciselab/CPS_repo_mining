#!/bin/bash

DIRS=$(find ./ -maxdepth 1 -type d | tail -n+2 | sed 's/^\.\///')

for project_name in $(find ./ -maxdepth 1 -type d | tail -n+2 | sed 's/^\.\///'); do
	pushd "$project_name"
	git log --pretty=oneline --no-decorate --color=never | tee "../${project_name}_commits.txt"
	popd
done
