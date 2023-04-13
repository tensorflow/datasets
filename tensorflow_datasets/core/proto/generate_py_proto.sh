#!/bin/bash

# This script use the protoc compiler to generate the python code of the
# all of our proto files.

set -e # Fail on errors

# Ensure we have the desired protoc version.
MIN_VERSION="libprotoc 3.20.0"
CURR_VERSION="$(protoc --version)"
if ["$(printf '%s\n' "$MIN_VERSION" "$CURR_VERSION" | sort -V | head -n1)" != "$MIN_VERSION"]; then
  echo 'Please use version 3.20.0 or above.'
  echo 'Please run install_protoc.sh to install it.'
  exit
else
  echo "Using $CURR_VERSION"
fi


# Setup tmp directories
TMP_DIR=$(mktemp -d)
TMP_TFDS_DIR="$PWD"
TMP_METADATA_DIR=${TMP_DIR}/metadata

echo "Temporary directory created: "
echo ${TMP_DIR}


function check_file_exists() {
  local file_name=$1
  if [ ! -f ${file_name} ]; then
      echo "${file_name} not found."
      echo "Please run this script from the appropriate root directory."
      exit 1
  fi
}

TMP_TFDS_PROTO_DIR="${TMP_TFDS_DIR}/tensorflow_datasets/core/proto"
DATASET_INFO_PROTO="${TMP_TFDS_PROTO_DIR}/dataset_info.proto"
FEATURE_PROTO="${TMP_TFDS_PROTO_DIR}/feature.proto"
check_file_exists ${DATASET_INFO_PROTO}
check_file_exists ${FEATURE_PROTO}

# Clone tf.metadata
git clone https://github.com/tensorflow/metadata.git ${TMP_METADATA_DIR}

# Invoke protoc compiler on dataset_info.proto
protoc ${DATASET_INFO_PROTO} \
  --python_out=${TMP_TFDS_PROTO_DIR} \
  --proto_path=${TMP_METADATA_DIR} \
  --proto_path=${TMP_TFDS_PROTO_DIR}
# Invoke protoc compiler on feature.proto
protoc ${FEATURE_PROTO} \
  --python_out=${TMP_TFDS_PROTO_DIR} \
  --proto_path=${TMP_METADATA_DIR} \
  --proto_path=${TMP_TFDS_PROTO_DIR}


LICENSING_TEXT=$(cat <<-END
# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
END
)

# Prepends the following to the given file:
# - a pylint directive to skip the generated python file
# - a license
# Writes the result to the target file.
function add_preamble() {
  local file_name=$1
  local target_file_name=$2
  printf "%s\n%s\n%s" \
    "# pylint: skip-file" \
    "${LICENSING_TEXT}" \
    "$(cat ${file_name})" \
    > ${target_file_name}
}

GENERATED_DATASET_INFO_PY="${TMP_TFDS_PROTO_DIR}/dataset_info_generated_pb2.py"
add_preamble "${TMP_TFDS_PROTO_DIR}/dataset_info_pb2.py" "${GENERATED_DATASET_INFO_PY}"

GENERATED_FEATURE_PY="${TMP_TFDS_PROTO_DIR}/feature_generated_pb2.py"
add_preamble "${TMP_TFDS_PROTO_DIR}/feature_pb2.py" "${GENERATED_FEATURE_PY}"

