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
if [[ "$TF_VERSION" == "2.0.0"  ]]
then
  # * lsun_test: https://github.com/tensorflow/datasets/issues/34
  TF2_IGNORE_TESTS="
  tensorflow_datasets/image/lsun_test.py
  "
fi
TF2_IGNORE=$(for test in $TF2_IGNORE_TESTS; do echo "--ignore=$test "; done)

# Run Tests
# Ignores:
# * Some TF2 tests if running against TF2 (see above)
# * Nsynth is run is isolation due to dependency conflict (crepe)
# * test_utils.py is not a test file
# * eager_not_enabled_by_default_test needs to be run separately because the
#   enable_eager_execution calls set global state and pytest runs all the tests
#   in the same process.
# * build_docs_test: See b/142892342
pytest \
  -n auto \
  --disable-warnings \
  $TF2_IGNORE \
  --ignore="tensorflow_datasets/audio/nsynth_test.py" \
  --ignore="tensorflow_datasets/testing/test_utils.py" \
  --ignore="tensorflow_datasets/scripts/build_docs_test.py" \
  --ignore="tensorflow_datasets/eager_not_enabled_by_default_test.py"
set_status
# If not running with TF2, ensure Eager is not enabled by default
if [[ "$TF_VERSION" != "2.0.0" ]]
then
  pytest \
    --disable-warnings \
    tensorflow_datasets/eager_not_enabled_by_default_test.py
  set_status
fi

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

# TODO(tfds): Re-enable as TF 2.0 gets closer to stable release
if [[ "$PY_BIN" = "python2.7" && "$TF_VERSION" = "2.0.0" ]]
then
  echo "Skipping notebook tests"
else
  for notebook in $NOTEBOOKS
  do
    test_notebook $notebook
  done
fi


# Run NSynth, in a contained enviornement
function test_nsynth() {
  create_virtualenv tfds_nsynth $PY_BIN
  ./oss_scripts/oss_pip_install.sh
  pip install -e .[tests_nsynth]
  pytest \
    --disable-warnings \
    "tensorflow_datasets/audio/nsynth_test.py"
  set_status
}

if [[ "$PY_BIN" != "python2.7" && "$TF_VERSION" == "2.0.0" ]]
then
  echo "Testing NSynth"
  test_nsynth
  set_status
fi


exit $STATUS
