#!/bin/bash

# Steps taken:
# - find all files
# - remove directory name & _commits.txt end of the name
PROJECTS=$(find dir_commits -type f | awk '{ print substr( $0, 13, length($0)-24)}')
DIR_SPLIT="dir_split_files"

if [ -d "$DIR_SPLIT" ]
then
    rm -r $DIR_SPLIT
fi

mkdir $DIR_SPLIT

for project_name in $PROJECTS; do
    FILE_NAME=$project_name"_commits.txt"

    DIR_LOC_COMMITS=$DIR_SPLIT/$project_name
    mkdir $DIR_LOC_COMMITS

    cp "dir_commits"/$FILE_NAME $DIR_LOC_COMMITS/.
    pushd $DIR_LOC_COMMITS
    NEW_TMP=$FILE_NAME"_new"
    cut -f 2- -d ' ' $FILE_NAME > $NEW_TMP
    grep "\S" $NEW_TMP > $FILE_NAME

    rm $NEW_TMP
    split -l 1 $FILE_NAME
    rm $FILE_NAME
    popd
done
