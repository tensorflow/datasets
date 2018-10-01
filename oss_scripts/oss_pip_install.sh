#!/bin/bash

set -v  # print commands as they're executed
set -e  # fail and exit on any command erroring

: "${TF_VERSION:?}"

if [[ "$TF_VERSION" == "tf-nightly"  ]]
then
  pip install tf-nightly;
else
  pip install -q "tensorflow==$TF_VERSION"
fi

# First ensure that the base dependencies are sufficient for a full import
pip install -q -e .
python -c "import tensorflow_datasets as tfds"

pip install -q -e .[tests]
