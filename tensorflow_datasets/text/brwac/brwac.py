# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""brwac dataset."""

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tqdm import tqdm
from tensorflow_datasets.text.brwac.brwac_utils import parse_vert_file

_HOMEPAGE = 'https://www.inf.ufrgs.br/pln/wiki/index.php?title=BrWaC'


# pylint: disable=line-too-long
_DESCRIPTION = f"""\
The Brazilian Portuguese Web as Corpus is a large corpus constructed following
the Wacky framework, which was made public for research purposes.

The current corpus version, released in January 2017, is composed by 3.53
million documents and 2.68 billion tokens. In order to use this dataset, you
must request access by filling the form in the [official homepage]({_HOMEPAGE}).

Please note that this resource is available solely for academic research
purposes, and you agreed not to use it for any commercial applications.


Title and text fields are preprocessed using [ftfy](https://github.com/rspeer/python-ftfy) ([Speer, 2019](http://doi.org/10.5281/zenodo.2591652)) Python library.

PS.: Description is extracted from [official homepage]({_HOMEPAGE}).
"""

_CITATION = """
@inproceedings{wagner2018brwac,
  title={The brWaC Corpus: A New Open Resource for Brazilian Portuguese},
  author={{Wagner Filho}, Jorge A and Wilkens, Rodrigo and Idiart, Marco and Villavicencio, Aline},
  booktitle={Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year={2018}
}
"""


class Brwac(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for brwac dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
    Fill the form in https://www.inf.ufrgs.br/pln/wiki/index.php?title=BrWaC in
    order to get download access. Then download brwac.vert.gz (~7 GB), extract
    the file and put brwac.vert (~22 GB after decompression) in manual_dir.
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(
            {
              'doc_id': tfds.features.Text(),
              'doc_idx': tf.int64,
              'title': tfds.features.Text(),
              'uri': tfds.features.Text(),
              'text': tfds.features.Sequence({
                'paragraphs':tfds.features.Sequence(tfds.features.Text())
                }),
            }
        ),
        supervised_keys=None,
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.manual_dir

    return {
        'train': self._generate_examples(path / 'brwac.vert'),
    }

  def _generate_examples(self, path):
    #   """Yields examples."""
    for doc in parse_vert_file(path=path, show_progress=True):
      yield doc['doc_idx'], {
          k: doc[k] for k in ['doc_id', 'title', 'uri', 'text', 'doc_idx']
      }
