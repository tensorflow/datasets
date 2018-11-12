#!/bin/bash

set -v  # print commands as they're executed

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

# Run Eager tests
# These tests call tf.enable_eager_execution at the top-level and must be run
# separately so as not to run other tests in Eager mode.
EAGER_TESTS="
tensorflow_datasets/core/dataset_builder_test.py
tensorflow_datasets/core/file_format_adapter_test.py
"
EAGER_IGNORE=$(for test in $EAGER_TESTS; do echo "--ignore=$test "; done)
pytest $EAGER_TESTS
set_status

# Run other tests
pytest $EAGER_IGNORE --ignore="tensorflow_datasets/core/test_utils.py"
set_status

# Test notebooks
NOTEBOOKS="
docs/overview.ipynb
"
for notebook in $NOTEBOOKS
do
  jupyter nbconvert --ExecutePreprocessor.timeout=600 --to notebook --execute $notebook
  set_status
done

exit $STATUS
