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

"""Movie reviews with human annotated rationales."""

import json
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_CITATION = """
@unpublished{eraser2019,
    title = {ERASER: A Benchmark to Evaluate Rationalized NLP Models},
    author = {Jay DeYoung and Sarthak Jain and Nazneen Fatema Rajani and Eric Lehman and Caiming Xiong and Richard Socher and Byron C. Wallace}
}
@InProceedings{zaidan-eisner-piatko-2008:nips,
  author    =  {Omar F. Zaidan  and  Jason Eisner  and  Christine Piatko},
  title     =  {Machine Learning with Annotator Rationales to Reduce Annotation Cost},
  booktitle =  {Proceedings of the NIPS*2008 Workshop on Cost Sensitive Learning},
  month     =  {December},
  year      =  {2008}
}
"""

_DESCRIPTION = """
The movie rationale dataset contains human annotated rationales for movie
reviews.
"""

_DOWNLOAD_URL = 'http://www.eraserbenchmark.com/zipped/movies.tar.gz'


class MovieRationales(tfds.core.GeneratorBasedBuilder):
  """Movie reviews with human annotated rationales."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'review': tfds.features.Text(),
            'label': tfds.features.ClassLabel(names=['NEG', 'POS']),
            'evidences': tfds.features.Sequence(tfds.features.Text()),
        }),
        supervised_keys=None,
        homepage='http://www.cs.jhu.edu/~ozaidan/rationales/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_dir = dl_manager.download_and_extract(_DOWNLOAD_URL)
    data_dir = os.path.join(dl_dir, 'movies')

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'data_dir': data_dir,
                'filepath': os.path.join(data_dir, 'train.jsonl')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'data_dir': data_dir,
                'filepath': os.path.join(data_dir, 'val.jsonl')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'data_dir': data_dir,
                'filepath': os.path.join(data_dir, 'test.jsonl')
            },
        ),
    ]

  def _generate_examples(self, data_dir, filepath):
    """Yields examples."""
    reviews_dir = os.path.join(data_dir, 'docs')

    with epath.Path(filepath).open() as f:
      for line in f:
        row = json.loads(line)
        doc_id = row['annotation_id']
        review_file = os.path.join(reviews_dir, doc_id)
        with epath.Path(review_file).open() as f1:
          review_text = f1.read()

        evidences = []
        for evidence in row['evidences']:
          for e in evidence:
            evidences.append(e['text'])

        yield doc_id, {
            'review': review_text,
            'label': row['classification'],
            'evidences': evidences,
        }
