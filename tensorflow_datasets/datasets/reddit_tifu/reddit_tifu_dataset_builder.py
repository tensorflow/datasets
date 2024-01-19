# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Reddit TIFU dataset using tifu or tldr from subreddit tifu."""

import json

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://drive.google.com/uc?export=download&id=1ffWfITKFMJeqjT8loC8aiCLRNJpc_XnF"
_LONG_SPLIT = "https://storage.googleapis.com/tfds-data/downloads/reddit_tifu/reddit_tifu_long_splits.json"

_DOCUMENT = "documents"
_TITLE = "title"
_TLDR = "tldr"
_ID = "id"
_ADDITIONAL_FEATURES = ["ups", "num_comments", "score", "upvote_ratio"]


class RedditTifuConfig(tfds.core.BuilderConfig):
  """BuilderConfig for RedditTifu."""

  def __init__(self, *, summary_key=None, **kwargs):
    """BuilderConfig for RedditTifu.

    Args:
      summary_key: key string of summary in downloaded json file.
      **kwargs: keyword arguments forwarded to super.
    """
    super(RedditTifuConfig, self).__init__(
        version=tfds.core.Version("1.1.2"), **kwargs
    )
    self.summary_key = summary_key


class Builder(tfds.core.GeneratorBasedBuilder):
  """Reddit TIFU Dataset."""

  RELEASE_NOTES = {
      "1.1.0": "Remove empty document and summary strings.",
      "1.1.1": (
          "Add train, dev and test (80/10/10) splits which are used in "
          "PEGASUS (https://arxiv.org/abs/1912.08777) in a separate config. "
          "These were created randomly using the tfds split function and are "
          "being released to ensure that results on Reddit Tifu Long are "
          "reproducible and comparable."
          "Also add `id` to the datapoints."
      ),
      "1.1.2": "Corrected splits uploaded.",
  }
  BUILDER_CONFIGS = [
      RedditTifuConfig(
          name="short",
          summary_key=_TITLE,
          description="Using title as summary.",
      ),
      RedditTifuConfig(
          name="long",
          summary_key=_TLDR,
          description="Using TLDR as summary.",
      ),
      RedditTifuConfig(
          name="long_split",
          summary_key=_TLDR,
          description="Using TLDR as summary and return train/test/dev splits.",
      ),
  ]

  def _info(self):
    features = {
        k: tfds.features.Tensor(shape=[], dtype=np.float32)
        for k in _ADDITIONAL_FEATURES
    }
    features.update(
        {k: tfds.features.Text() for k in [_DOCUMENT, _TLDR, _TITLE, _ID]}
    )
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(features),
        supervised_keys=(_DOCUMENT, self.builder_config.summary_key),
        homepage="https://github.com/ctr4si/MMN",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    if self.builder_config.name == "long_split":
      paths = dl_manager.download_and_extract(
          {"data": _URL, "split": _LONG_SPLIT}
      )
      dl_path = paths["data"]
      split_path = paths["split"]
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={
                  "path": dl_path,
                  "split_path": split_path,
                  "split": "train",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  "path": dl_path,
                  "split_path": split_path,
                  "split": "test",
              },
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={
                  "path": dl_path,
                  "split_path": split_path,
                  "split": "validation",
              },
          ),
      ]
    else:
      dl_path = dl_manager.download_and_extract(_URL)
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={"path": dl_path},
          )
      ]

  def _generate_examples(self, path=None, split_path=None, split=None):
    """Yields examples."""
    if split_path:
      split_data = json.load(tf.io.gfile.GFile(split_path))
    with tf.io.gfile.GFile(path, "rb") as f:
      for i, line in enumerate(f):
        # keys are 'title_tokenized','permalink','title','url','num_comments',
        #   'tldr'(optional),'created_utc','trimmed_title_tokenized','ups',
        #   'selftext_html','score','upvote_ratio','tldr_tokenized'(optional),
        #   'selftext','trimmed_title','selftext_without_tldr_tokenized',
        #   'id','selftext_without_tldr'
        d = json.loads(line)
        if not split or (split and d["id"] in split_data[split]):
          r = {
              _DOCUMENT: d["selftext_without_tldr"].strip(),
              _TITLE: d["trimmed_title"].strip(),
              _TLDR: (d["tldr"] or "").strip(),
              _ID: d["id"].strip(),
          }
          r.update({k: d[k] for k in _ADDITIONAL_FEATURES})
          # skip if document or summary is empty
          if r[_DOCUMENT] and r[self.builder_config.summary_key]:
            yield i, r
