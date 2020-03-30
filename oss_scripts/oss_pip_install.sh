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

# Make sure we have the latest version of numpy - avoid problems we were
# seeing with Python 3
pip install -q -U numpy

# First ensure that the base dependencies are sufficient for a full import and
# data load
pip install -e .
python -c "import tensorflow_datasets as tfds"
python -c "import tensorflow_datasets as tfds; tfds.load('mnist', split='train')"

# Then install the test dependencies
pip install -e .[tests]
