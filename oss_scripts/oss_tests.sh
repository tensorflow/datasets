#!/bin/bash

set -vx  # print command from file as well as evaluated command

source ./oss_scripts/utils.sh

: "${TF_VERSION:?}"

pip freeze  # Display the list of modules/versions for debugging

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

# Run Tests
# Ignores:
# * Nsynth is run in isolation due to dependency conflict (crepe)
# * Lsun tests is disabled because the tensorflow_io used in open-source
#   is linked to static libraries compiled again specific TF version, which
#   makes test fails with linking error (libtensorflow_io_golang.so).
# * Imagenet2012Corrupted requires imagemagick binary.
# * Wmt19 is failing during tarfile extraction due to:
#   https://bugs.python.org/issue39430
#   TODO(tfds): Restore test with new Python release.
# * test_utils.py is not a test file
# * build_docs_test: See b/142892342
pytest \
  -n auto \
  --disable-warnings $EXTRA_IGNORE \
  --ignore="tensorflow_datasets/audio/nsynth_test.py" \
  --ignore="tensorflow_datasets/core/dataset_builder_notfdv_test.py" \
  --ignore="tensorflow_datasets/image/lsun_test.py" \
  --ignore="tensorflow_datasets/image_classification/imagenet2012_corrupted_test.py" \
  --ignore="tensorflow_datasets/translate/wmt19_test.py" \
  --ignore="tensorflow_datasets/testing/test_utils.py" \
  --ignore="tensorflow_datasets/scripts/documentation/build_api_docs_test.py"
set_status

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

exit $STATUS
