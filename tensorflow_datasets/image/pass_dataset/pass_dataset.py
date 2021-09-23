"""PASS dataset."""

import tensorflow_datasets as tfds
import urllib.request

_DESCRIPTION = """
PASS is a large-scale image dataset that does not include any humans,
human parts, or other personally identifiable information.
It that can be used for high-quality self-supervised pretraining while significantly reducing privacy concerns.

PASS contains 1.440.191 images without any labels sourced from YFCC-100M.
"""

_CITATION = """
@Article{asano21pass,
author = "Yuki M. Asano and Christian Rupprecht and Andrew Zisserman and Andrea Vedaldi",
title = "PASS: An ImageNet replacement for self-supervised pretraining without humans",
journal = "NeurIPS Track on Datasets and Benchmarks",
year = "2021"
}
"""


class PASS(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for pass dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(None, None, 3)),
        }),
        supervised_keys=None,
        homepage='https://www.robots.ox.ac.uk/~vgg/research/pass/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    urls =  urllib.request.urlopen("https://www.robots.ox.ac.uk/~vgg/research/pass/pass_urls.txt")
    urls = [li.decode("utf-8").split('\n')[0] for li in urls]
    path = dl_manager.download(urls)

    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    for idx,f in enumerate(path):
      yield idx, {
          'image': f,
      }
