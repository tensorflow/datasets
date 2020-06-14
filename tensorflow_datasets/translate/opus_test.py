"""opus dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import six
from tensorflow_datasets import testing
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.translate import opus


class OpusTest(tfds.testing.DatasetBuilderTestCase):

  config = opus.OpusConfig(
    version=tfds.core.Version('0.1.0'),
    language_pair=("de", "en"),
    subsets=["medical", "law"]
  )
  opus.Opus.BUILDER_CONFIGS = [config]

  DATASET_CLASS = opus.Opus
  SPLITS = {
      "train": 30,
  }

  SKIP_CHECKSUMS = True


if __name__ == "__main__":
  tfds.testing.test_main()

