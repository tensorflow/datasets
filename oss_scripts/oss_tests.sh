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

# Certain datasets/tests don't work with TF2
# Skip them here, and link to a GitHub issue that explains why it doesn't work
# and what the plan is to support it.
TF2_IGNORE_TESTS=""
if [[ "$TF_VERSION" == "tf2"  ]]
then
  # * lsun_test: https://github.com/tensorflow/datasets/issues/34
  TF2_IGNORE_TESTS="
  tensorflow_datasets/image/lsun_test.py
  "
fi
TF2_IGNORE=$(for test in $TF2_IGNORE_TESTS; do echo "--ignore=$test "; done)

# Run Tests
pytest $TF2_IGNORE --ignore="tensorflow_datasets/testing/test_utils.py"
set_status

# Test notebooks in isolated environments
NOTEBOOKS="
docs/overview.ipynb
docs/_index.ipynb
"
PY_BIN=$(python -c "import sys; print('python%s' % sys.version[0:3])")
function test_notebook() {
  local notebook=$1
  create_virtualenv tfds_notebook $PY_BIN
  pip install -q jupyter ipykernel
  ipython kernel install --user --name tfds-notebook
  jupyter nbconvert \
    --ExecutePreprocessor.timeout=600 \
    --ExecutePreprocessor.kernel_name=tfds-notebook \
    --to notebook \
    --execute $notebook
  set_status
}

# Re-enable as TF 2.0 gets closer to stable release
if [[ "$PY_BIN" = "python2.7" && "$TF_VERSION" = "tf2" ]]
  echo "Skipping notebook tests"
else
  for notebook in $NOTEBOOKS
  do
    test_notebook $notebook
  done
fi

exit $STATUS
