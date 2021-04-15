#!/bin/sh

if [ -d "html" ]; then
    rm -r html
fi
if [ -d "htmlmut" ]; then
    rm -r htmlmut
fi
if [ -d "htmlpdoc" ]; then
    rm -r htmlpdoc
fi

pdoc --html pd
mv html htmlpdoc

pytest --cov-report html --cov=pd

mutmut run
mutmut html
mv html htmlmut
