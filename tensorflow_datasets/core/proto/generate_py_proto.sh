#!/bin/bash

# This script use the protoc compiler to generate the python code of the
# all of our proto files.


# Ensure we have the desired protoc version.
if [[ $(protoc --version) != 'libprotoc 3.11.2' ]]; then
  echo 'Please use version 3.11.2 or above.'
  echo 'Please run install_protoc.sh to install it.'
  exit
fi

# Function to prepend a pylint directive to skip the generated python file.
function pylint_skip_file() {
  local file_name=$1
  printf "%s\n%s" "# pylint: skip-file" "$(cat ${file_name})" > ${file_name}
}


# Setup tmp directories
TMP_DIR=$(mktemp -d)
TMP_TFDS_DIR="$PWD"
TMP_METADATA_DIR=${TMP_DIR}/metadata

echo "Temporary directory created: "
echo ${TMP_DIR}


TMP_TFDS_PROTO_DIR="${TMP_TFDS_DIR}/tensorflow_datasets/core/proto"
DATASET_INFO_PROTO="${TMP_TFDS_PROTO_DIR}/dataset_info.proto"
if [ ! -f ${DATASET_INFO_PROTO} ]; then
    echo "${DATASET_INFO_PROTO} not found."
    echo "Please run this script from the appropriate root directory."
fi

# Clone tf.metadata
git clone https://github.com/tensorflow/metadata.git ${TMP_METADATA_DIR}

# Invoke protoc compiler on dataset_info.proto
protoc ${DATASET_INFO_PROTO} \
  --python_out=${TMP_TFDS_PROTO_DIR} \
  --proto_path=${TMP_METADATA_DIR} \
  --proto_path=${TMP_TFDS_PROTO_DIR}

# Add pylint ignore and name the file as generated.
GENERATED_DATASET_INFO_PY="${TMP_TFDS_PROTO_DIR}/dataset_info_generated_pb2.py"
mv ${TMP_TFDS_PROTO_DIR}/dataset_info_pb2.py \
  ${GENERATED_DATASET_INFO_PY}
pylint_skip_file "${GENERATED_DATASET_INFO_PY}"


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

printf "%s\n%s" "${LICENSING_TEXT}" "$(cat ${GENERATED_DATASET_INFO_PY})" > \
  ${GENERATED_DATASET_INFO_PY}

