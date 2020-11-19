#!/bin/bash

set -vx  # print command from file as well as evaluated command
set -e   # fail and exit on any command erroring

source ./oss_scripts/utils.sh
function setup_env() {
  create_virtualenv $1 $2
  pip install -q --upgrade setuptools pip
  pip install -q wheel twine pyopenssl
}

GIT_COMMIT_ID=${1:-""}
[[ -z $GIT_COMMIT_ID ]] && echo "Must provide a commit" && exit 1
SETUP_ARGS=""
if [ "$GIT_COMMIT_ID" = "nightly" ]
then
  GIT_COMMIT_ID="master"
  SETUP_ARGS="--nightly"
  export TFDS_NIGHTLY_TIMESTAMP=$(date +"%Y%m%d%H%M")
fi

TMP_DIR=$(mktemp -d)
pushd $TMP_DIR

echo "Cloning tensorflow/datasets and checking out commit $GIT_COMMIT_ID"
git clone https://github.com/tensorflow/datasets.git
cd datasets


if [ "$GIT_COMMIT_ID" != "master" ]  # commit id = nightly is overwritten above
then
  # For stable version, we overwrite `version.py` by `version_stable.py` to
  # remove the `-nightly` suffix.
  mv tensorflow_datasets/version_stable.py tensorflow_datasets/version.py
fi
git checkout $GIT_COMMIT_ID

echo "Building source distribution"

# Build the wheels
setup_env tfds_py3 python3.6
python setup.py sdist $SETUP_ARGS
python setup.py bdist_wheel $SETUP_ARGS

# Publish to PyPI
read -p "Publish? (y/n) " -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
  echo "Publishing to PyPI"
  twine upload dist/*
else
  echo "Skipping upload"
  exit 1
fi

popd
rm -rf $TMP_DIR
