# TFDS CLI

TFDS CLI is a command-line tool that provides various commands to easily work
with TensorFlow Datasets.

To use the CLI tool, install `tensorflow-datasets`.

``` sh
pip install tensorflow-datasets
tfds --version
```

Run the following to view the list of all CLI commands.

``` sh
tfds --help
```

Some of the commands for working with TFDS via CLI include:

- `tfds new [--dir DIR] dataset_name` : Create a new dataset directory from the template.

## Creating a new Dataset

To create a new dataset, the following command will help you get started by
generating the required python files in the `dataset_name` directory.

``` sh
tfds new dataset_name
```

For further procedure, refer to [Adding a dataset](https://www.tensorflow.org/datasets/add_dataset) guide.
