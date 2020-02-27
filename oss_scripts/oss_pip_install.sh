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
  sudo add-apt-repository -y ppa:jonathonf/ffmpeg-4
  sudo apt-get update -qq
  sudo apt-get install -qq -y ffmpeg
fi

# Required for opencv2
sudo apt-get install -qq -y libsm6

install_tf "$TF_VERSION"

# Beam requires Python header files for Python3 during YAML compilation
sudo apt-get install -qq -y libpython${PY_VERSION}-dev

# Make sure we have the latest version of numpy - avoid problems we were
# seeing with Python 3
pip3 install -q -U numpy

# First ensure that the base dependencies are sufficient for a full import and
# data load
pip3 install -e .
python3 -c "import tensorflow_datasets as tfds"
python3 -c "import tensorflow_datasets as tfds; tfds.load('mnist', split='train')"

# Then install the test dependencies
pip3 install -e .[tests]
