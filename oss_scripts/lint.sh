#!/bin/bash

LINT_DIR=${1:-tensorflow_datasets}

if [ ! -f /tmp/pylintrc ]
then
  wget -O /tmp/pylintrc \
    https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/tools/ci_build/pylintrc
fi
pylint --rcfile=/tmp/pylintrc $1
