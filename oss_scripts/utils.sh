#!/bin/bash

# Setup virtualenv
# create_virtualenv my_new_env
# or
# create_virtualenv my_new_env python2.7
function create_virtualenv() {
  local env_name=$1
  local env_python=${2:-python3.6}
  mkdir -p ~/virtualenv
  pushd ~/virtualenv
  rm -rf $env_name
  virtualenv -p $env_python $env_name
  source $env_name/bin/activate
  pip install --upgrade pip
  popd
}

function install_tf() {
  local version=$1
  if [[ "$version" == "tf-nightly"  ]]
  then
    pip install -q tf-nightly;
  else
    pip install -q "tensorflow==$version"
  fi
}
