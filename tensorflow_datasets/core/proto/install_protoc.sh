#!/bin/bash
# Install the .protoc compiler on Linux

# Make sure you grab the latest version
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v22.2/protoc-22.2-linux-x86_64.zip
curl -OL https://github.com/protocolbuffers/protobuf/archive/refs/tags/v22.2.zip

# Unzip
unzip protoc-22.2-linux-x86_64.zip -d protoc3
unzip v22.2.zip -d protoc3-source


# Move protoc to /usr/local/bin/
sudo mv protoc3/bin/* /usr/local/bin/

# Move protoc3/include to /usr/local/include/
sudo mv protoc3/include/* /usr/local/include/

# Move source files to /usr/local/include/
sudo mv -n protoc3-source/protobuf-22.2/src/google/protobuf/* /usr/local/include/google/protobuf/
