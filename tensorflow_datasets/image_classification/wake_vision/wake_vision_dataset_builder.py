"""wake_vision dataset."""

import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wake_vision dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(wake_vision): Specifies the tfds.core.DatasetInfo object
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(None, None, 3)),
            'label': tfds.features.ClassLabel(names=['no', 'yes']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'label'),  # Set to `None` to disable
        homepage='https://dataset-homepage/',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(wake_vision): Downloads the data and defines the splits
    path = dl_manager.download_and_extract('https://todo-data-url')

    # TODO(wake_vision): Returns the Dict[split names, Iterator[Key, Example]]
    return {
        'train': self._generate_examples(path / 'train_imgs'),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    # TODO(wake_vision): Yields (key, example) tuples from the dataset
    for f in path.glob('*.jpeg'):
      yield 'key', {
          'image': f,
          'label': 'yes',
      }
