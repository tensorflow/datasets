import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds


class DummyDatasetChecksums(tfds.core.GeneratorBasedBuilder):

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        features=tfds.features.FeaturesDict({"x": tf.int64}),
    )

  def _split_generators(self, dl_manager):
    url = "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"
    path = dl_manager.download(url)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "path": os.path.join(path, "train.txt")
            },
        ),
    ]

  def _generate_examples(self, path):
    with tf.io.gfile.GFile(path) as f:
      value = f.read()
    range_ = int(value)
    for i in range(range_):
      x = i
      if self.builder_config:
        x += self.builder_config.increment
      yield i, {"x": x}
