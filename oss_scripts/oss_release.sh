#!/bin/bash

set -v  # print commands as they're executed
set -e  # fail and exit on any command erroring

GIT_COMMIT_ID=${1:-""}
[[ -z $GIT_COMMIT_ID ]] && echo "Must provide a commit" && exit 1

TMP_DIR=$(mktemp -d)
pushd $TMP_DIR

echo "Cloning tensorflow/datasets and checking out commit $GIT_COMMIT_ID"
git clone https://github.com/tensorflow/datasets.git
cd datasets
git checkout $GIT_COMMIT_ID

pip install wheel twine pyopenssl

# Build the distribution
echo "Building distribution"
python setup.py sdist
python setup.py bdist_wheel --universal

# Publish to PyPI
echo "Publishing to PyPI"
twine upload dist/*

# Cleanup
rm -rf build/ dist/ tensorflow_datasets.egg-info/
popd
rm -rf $TMP_DIR
