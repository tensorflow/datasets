#!/bin/bash

set -vx  # print command from file as well as evaluated command
set -e   # fail and exit on any command erroring

: "${TF_VERSION:?}"

source ./oss_scripts/utils.sh

# Install ffmpeg for Audio FeatureConnector tests
if command -v ffmpeg 2>/dev/null
then
  echo "Using installed ffmpeg"
else
  echo "Installing ffmpeg"
  sudo add-apt-repository -y ppa:mc3man/trusty-media
  sudo apt-get update -qq
  sudo apt-get install -qq -y ffmpeg
fi

install_tf "$TF_VERSION"

# Beam requires Python header files for Python3 during YAML compilation
# This shouldn't be needed for Python2
sudo apt-get install -qq -y libpython${PY_VERSION}-dev

# Make sure we have the latest version of numpy - avoid problems we were
# seeing with Python 3
pip install -q -U numpy

# First ensure that the base dependencies are sufficient for a full import and
# data load
pip install -e .
python -c "import tensorflow_datasets as tfds"
python -c "import tensorflow_datasets as tfds; tfds.load('mnist', split=tfds.Split.TRAIN)"

# Then install the test dependencies
pip install -e .[tests]
