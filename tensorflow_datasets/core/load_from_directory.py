import os

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info


class ReadOnlyBuilder(dataset_builder.FileReaderBuilder):

  def __init__(self, data_dir):
    self._data_dir = os.path.expanduser(data_dir)
    parsed_proto = dataset_info.read_from_json(
        os.path.join(self._data_dir, 'dataset_info.json'))
    self.name = parsed_proto.name
    self._version = parsed_proto.version
    self._builder_config = dataset_builder.BuilderConfig(
        name=parsed_proto.config_name, version=self._version)
    self.info.read_from_directory(self._data_dir)

  def _info(self) -> dataset_info.DatasetInfo:
    return dataset_info.DatasetInfo(builder=self)

  def _download_and_prepare(self, **kwargs):
    pass


def builder_from_directory(builder_dir: str) -> dataset_builder.DatasetBuilder:
  """Returns Builder for the Dataset at for the given path.

  Usage:

  ```py

  builder = tfds.core.builder_from_directory('path/to/my_dataset/config/1.0.0')
  ds = builder.as_dataset(split='train')
  ```

  Args:
    builder_dir: `str`, path to directory to read data.

  Returns:
    builder: `tf.core.DatasetBuilder`, builder for dataset at the given path.
  """
  return ReadOnlyBuilder(data_dir=builder_dir)
