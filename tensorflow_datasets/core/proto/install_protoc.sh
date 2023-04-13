#!/bin/bash
# Install the .protoc compiler on Linux

# Make sure you grab the latest version
curl -OL https://github.com/google/protobuf/releases/download/v3.20.0/protoc-3.20.0-linux-x86_64.zip

# Unzip
unzip protoc-3.20.0-linux-x86_64.zip -d protoc3


# Move protoc to /usr/local/bin/
sudo mv protoc3/bin/* /usr/local/bin/

# Move protoc3/include to /usr/local/include/
sudo mv protoc3/include/* /usr/local/include/
