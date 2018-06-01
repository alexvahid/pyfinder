#!/bin/sh
# This script serves more as a demonstration of how 
# to combine pyexz3 with coverage tools
# It does the following steps
# 0: Setup, don't worry about these
# 1: Arguments: the test file (#1) and the solver (#2) - either '--cvc' or '--' (default)
# 2: PyExZ3 expects python 3.2.3 but coverage requires 
# whatever version is installed. Mine happens to be 3.6.5. 
# Before running PyExZ3, this script sets pyenv to use the right version.
# 3: Run pyexz3 as usual, making sure to use the --generate_test_suite flag.
# 4: Switch python versions back to 3.6.5
# 5: Run coverage analysis on the generated test suite
# 6: coverage-specific: generate html output for what has been collected.
# 7: open htmlcov/index.html for a more general view (which includes branch information)
# If desired, I have code to also open the more specific test file in question.
# Unfortunately, the html doesn't seem to illustrate branches though.

# https://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/..
SOLVER=${2:-"--z3"} # use z3 by default, but cvc if provided. I assume you know what you're doing.
FILE=$1

pyenv local 3.2.3
python $DIR/pyexz3.py $FILE $SOLVER --generate_test_suite
pyenv local 3.6.5
# hack: hope it's the most recently created file in test suite dir
TEST_FILE=$(ls -t $DIR/generated_test_suites | head -n 1)
coverage run --branch generated_test_suites/$TEST_FILE

coverage html
# for general viewing/high level view
# open htmlcov/index.html 
# However, we care mostly about the specific input file, so try to open that one.
# ugly sed usage: replace / or . with _ for the filename.
open htmlcov/$(sed -e 's/[\/.]/_/g' <<<"$FILE").html