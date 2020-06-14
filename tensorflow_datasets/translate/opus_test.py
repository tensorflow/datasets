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
    subsets=["medical"]
  )
  opus.Opus.BUILDER_CONFIGS = [config]

  DATASET_CLASS = opus.Opus
  SPLITS = {
      "train": 15,  # Number of fake train example
  }

  SKIP_CHECKSUMS = True

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  tfds.testing.test_main()

