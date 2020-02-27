#!/bin/bash

# Setup virtualenv
# create_virtualenv my_new_env
# or
# create_virtualenv my_new_env python3.6
function create_virtualenv() {
  local env_name=$1
  local env_python=${2:-python3.6}
  mkdir -p ~/virtualenv
  pushd ~/virtualenv
  rm -rf $env_name
  virtualenv -p $env_python $env_name
  source $env_name/bin/activate
  pip3 install --upgrade pip
  popd
}

function install_tf() {
  local version=$1
  if [[ "$version" == "tf-nightly"  ]]
  then
    pip3 install -q tf-nightly;
  else
    pip3 install -q "tensorflow==$version"
  fi
}
