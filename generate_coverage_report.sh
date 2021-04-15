#!/bin/sh

pytest --cov-report html --cov=pd
mutmut run
mutmut html
