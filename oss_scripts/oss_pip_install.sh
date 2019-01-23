#!/bin/bash

set -vx  # print command from file as well as evaluated command
set -e   # fail and exit on any command erroring

: "${TF_VERSION:?}"

# Install ffmpeg for Audio FeatureConnector tests
if command -v ffmpeg 2>/dev/null
then
  echo "Using installed ffmpeg"
else
  echo "Installing ffmpeg"
  sudo add-apt-repository -y ppa:mc3man/trusty-media
  sudo apt-get -qq update
  sudo apt-get install -y ffmpeg
fi

if [[ "$TF_VERSION" == "tf-nightly"  ]]
then
  pip install -q tf-nightly;
elif [[ "$TF_VERSION" == "tf2"  ]]
then
  pip install -q "tf-nightly-2.0-preview"
else
  pip install -q "tensorflow==$TF_VERSION"
fi

# Make sure we have the latest version of numpy - avoid problems we were
# seeing with Python 3
pip install -q -U numpy

# First ensure that the base dependencies are sufficient for a full import and
# data load
pip install -q -e .
python -c "import tensorflow_datasets as tfds"
python -c "import tensorflow_datasets as tfds; tfds.load('mnist', split=tfds.Split.TRAIN)"

# Then install the test dependencies
pip install -q -e .[tests]
