#!/bin/bash

# This script use the protoc compiler to generate the python code of the
# download.proto file.

if [[ $(protoc --version) != 'libprotoc 3.6.1' ]]; then
  echo 'Please use version 3.6.1 of protoc for compatibility with Python 2 and 3.'
  exit
fi
protoc download.proto --python_out=.
mv download_pb2.py download_generated_pb2.py
