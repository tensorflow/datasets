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


# Certain datasets/tests don't work with Python 2
PY2_IGNORE_TESTS=""
if [[ "$PY_BIN" = "python2.7"  ]]
then
  PY2_IGNORE_TESTS="
  tensorflow_datasets/audio/nsynth_test.py
  tensorflow_datasets/text/c4_test.py
  tensorflow_datasets/text/c4_utils_test.py
  tensorflow_datasets/image/imagenet2012_corrupted_test.py
  "
fi
PY2_IGNORE=$(for test in $PY2_IGNORE_TESTS; do echo "--ignore=$test "; done)


# Run Tests
# Ignores:
# * Some Python2 tests if running against Python2 (see above)
# * Nsynth is run is isolation due to dependency conflict (crepe)
# * Lsun tests is disabled because the tensorflow_io used in open-source
#   is linked to static libraries compiled again specific TF version, which
#   makes test fails with linking error (libtensorflow_io_golang.so).
# * test_utils.py is not a test file
# * eager_not_enabled_by_default_test needs to be run separately because the
#   enable_eager_execution calls set global state and pytest runs all the tests
#   in the same process.
# * build_docs_test: See b/142892342
pytest \
  -n auto \
  --disable-warnings \
  $PY2_IGNORE \
  --ignore="tensorflow_datasets/audio/nsynth_test.py" \
  --ignore="tensorflow_datasets/image/lsun_test.py" \
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
function test_notebook() {
  local notebook=$1
  create_virtualenv tfds_notebook $PY_BIN
  ipython kernel install --user --name tfds-notebook
  jupyter nbconvert \
    --ExecutePreprocessor.timeout=600 \
    --ExecutePreprocessor.kernel_name=tfds-notebook \
    --to notebook \
    --execute $notebook
  set_status
}

for notebook in $NOTEBOOKS
do
  test_notebook $notebook
done

# Run NSynth, in a contained enviornement
function test_isolation_nsynth() {
  create_virtualenv tfds_nsynth $PY_BIN
  ./oss_scripts/oss_pip_install.sh
  pip install -e .[nsynth]
  pytest \
    --disable-warnings \
    "tensorflow_datasets/audio/nsynth_test.py"
  set_status
}

if [[ "$PY_BIN" != "python2.7" && "$TF_VERSION" == "2.0.0" ]]
then
  echo "============= Testing Isolation ============="
  test_isolation_nsynth
  set_status
fi


exit $STATUS
