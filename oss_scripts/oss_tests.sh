#!/bin/bash

set -vx  # print command from file as well as evaluated command

source ./oss_scripts/utils.sh

: "${TF_VERSION:?}"

# Instead of exiting on any failure with "set -e", we'll call set_status after
# each command and exit $STATUS at the end.
STATUS=0
function set_status() {
    local last_status=$?
    if [[ $last_status -ne 0 ]]
    then
      echo "<<<<<<FAILED>>>>>> Exit code: $last_status"
    fi
    STATUS=$(($last_status || $STATUS))
}

PY_BIN=$(python -c "import sys; print('python%s' % sys.version[0:3])")


# Test notebooks in isolated environments
NOTEBOOKS="
docs/overview.ipynb
docs/_index.ipynb
"
function test_notebook() {
  local notebook=$1
  create_virtualenv tfds_notebook $PY_BIN
  pip install -q jupyter ipykernel
  ipython kernel install --user --name tfds-notebook
  jupyter nbconvert \
    --ExecutePreprocessor.timeout=10000 \
    --ExecutePreprocessor.kernel_name=tfds-notebook \
    --to notebook \
    --execute $notebook
  set_status
}


for notebook in $NOTEBOOKS
do
  test_notebook $notebook
done


exit $STATUS
