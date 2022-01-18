# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""assin2 dataset."""

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.assin2.assin2_utils import parse_xml_string

_HOMEPAGE = 'https://sites.google.com/view/assin2/english'

# pylint: disable=line-too-long
_DESCRIPTION = f"""\
## Contextualization
ASSIN 2 is the second edition of the Avaliação de Similaridade Semântica e
Inferência Textual (Evaluating Semantic Similarity and Textual Entailment),
and was a workshop collocated with [STIL 2019](http://www.google.com/url?q=http%3A%2F%2Fcomissoes.sbc.org.br%2Fce-pln%2Fstil2019%2F&sa=D&sntz=1&usg=AFQjCNHN8DosAsJ-gd48TfkXFX5YD6xM7g). It follows the [first edition of ASSIN](http://www.google.com/url?q=http%3A%2F%2Fpropor2016.di.fc.ul.pt%2F%3Fpage_id%3D381&sa=D&sntz=1&usg=AFQjCNHV7ySeNzH4k6MWKBLqO9yUkqiUqw),
proposing a new shared task with new data.

The workshop evaluated systems that assess two types of relations between
two sentences: Semantic Textual Similarity and Textual Entailment.

Semantic Textual Similarity consists of quantifying the level of semantic
equivalence between sentences, while Textual Entailment Recognition consists of
classifying whether the first sentence entails the second.

## Data
The corpus used in ASSIN 2 is composed of rather simple sentences. Following
the procedures of SemEval 2014 Task 1, we tried to remove from the corpus named
entities and indirect speech, and tried to have all verbs in the present tense.
The [annotation instructions](https://drive.google.com/open?id=1aUPhywEHD0r_pxPiTqZwS0fRj-1Xda2w)
given to annotators are available (in Portuguese).

The training and validation data are composed, respectively, of 6,500 and 500
sentence pairs in Brazilian Portuguese, annotated for entailment and
semantic similarity. Semantic similarity values range from 1 to 5, and text
entailment classes are either entailment or none. The test data are composed of
approximately 3,000 sentence pairs with the same annotation. All data were
manually annotated.

## Evaluation
Evaluation
The evaluation of submissions to ASSIN 2 was with the same metrics as the first
ASSIN, with the F1 of precision and recall as the main metric for text
entailment and Pearson correlation for semantic similarity.
The [evaluation scripts](https://github.com/erickrf/assin) are the same as in
the last edition.

PS.: Description is extracted from [official homepage]({_HOMEPAGE}).
"""

# pylint: disable=line-too-longm anomalous-backslash-in-string
_CITATION = r"""
@inproceedings{DBLP:conf/propor/RealFO20,
  author    = {Livy Real and
               Erick Fonseca and
               Hugo Gon{\c{c}}alo Oliveira},
  editor    = {Paulo Quaresma and
               Renata Vieira and
               Sandra M. Alu{\'{\i}}sio and
               Helena Moniz and
               Fernando Batista and
               Teresa Gon{\c{c}}alves},
  title     = {The {ASSIN} 2 Shared Task: {A} Quick Overview},
  booktitle = {Computational Processing of the Portuguese Language - 14th International
               Conference, {PROPOR} 2020, Evora, Portugal, March 2-4, 2020, Proceedings},
  series    = {Lecture Notes in Computer Science},
  volume    = {12037},
  pages     = {406--412},
  publisher = {Springer},
  year      = {2020},
  url       = {https://doi.org/10.1007/978-3-030-41505-1_39},
  doi       = {10.1007/978-3-030-41505-1_39},
  timestamp = {Tue, 03 Mar 2020 09:40:18 +0100},
  biburl    = {https://dblp.org/rec/conf/propor/RealFO20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DOWNLOAD_URLS = {
    'train':
        'https://drive.google.com/u/0/uc?id=1Q9j1a83CuKzsHCGaNulSkNxBm7Dkn7Ln&export=download',
    'validation':
        'https://drive.google.com/u/0/uc?id=1kb7xq6Mb3eaqe9cOAo70BaG9ypwkIqEU&export=download',
    'test':
        'https://drive.google.com/u/0/uc?id=1J3FpQaHxpM-FDfBUyooh-sZF-B-bM_lU&export=download',
}


class Assin2(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for assin2 dataset."""

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
            'text':
                tfds.features.Text(),
            'hypothesis':
                tfds.features.Text(),
            'id':
                tf.int32,
            'entailment':
                tfds.features.ClassLabel(names=['None', 'Entailment']),
            'similarity':
                tf.float32
        }),
        supervised_keys=None,
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_DOWNLOAD_URLS)
    return {
        'train': self._generate_examples(path['train']),
        'validation': self._generate_examples(path['validation']),
        'test': self._generate_examples(path['test'])
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with tf.io.gfile.GFile(path) as f:
      pairs = parse_xml_string(f.read())

    for pair in pairs:
      yield pair.id, {
          'text': pair.text,
          'hypothesis': pair.hypothesis,
          'id': pair.id,
          'entailment': pair.entailment,
          'similarity': pair.similarity
      }
