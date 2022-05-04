# Protobuf

This page describe how to update the protobuf generated python file. By
default, the protobuf is already compiled into python file so you won't have to
do anything. Those steps are required only if you update the `.proto` file. The
instruction are for linux.

## Install the proto compiler


```
./install_protoc.sh
```

## Re-generate the python file

```
./generate_py_proto.sh
```

