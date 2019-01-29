#!/bin/bash

set -vx  # print command from file as well as evaluated command

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

# Run Tests
pytest --ignore="tensorflow_datasets/core/test_utils.py"
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
