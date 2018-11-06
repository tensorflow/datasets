#!/bin/bash

set -v  # print commands as they're executed
set -e  # fail and exit on any command erroring

: "${TF_VERSION:?}"

if [[ "$TF_VERSION" == "tf-nightly"  ]]
then
  pip install --user tf-nightly;
else
  pip install -q --user "tensorflow==$TF_VERSION"
fi

# Make sure we have the latest version of numpy - avoid problems we were
# seeing with Python 3
pip install -q -U --user numpy

# First ensure that the base dependencies are sufficient for a full import
pip install --user -q -e .
python -c "import tensorflow_datasets as tfds"

# Then install the test dependencies
pip install --user -q -e .[tests]
