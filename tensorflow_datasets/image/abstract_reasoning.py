# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""AbstractReasoning data set."""

import os
import random
import numpy as np
import six
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@InProceedings{pmlr-v80-barrett18a,
  title = 	 {Measuring abstract reasoning in neural networks},
  author = 	 {Barrett, David and Hill, Felix and Santoro, Adam and Morcos, Ari and Lillicrap, Timothy},
  booktitle = 	 {Proceedings of the 35th International Conference on Machine Learning},
  pages = 	 {511--520},
  year = 	 {2018},
  editor = 	 {Dy, Jennifer and Krause, Andreas},
  volume = 	 {80},
  series = 	 {Proceedings of Machine Learning Research},
  address = 	 {Stockholmsmassan, Stockholm Sweden},
  month = 	 {10--15 Jul},
  publisher = 	 {PMLR},
  pdf = 	 {http://proceedings.mlr.press/v80/barrett18a/barrett18a.pdf},
  url = 	 {http://proceedings.mlr.press/v80/barrett18a.html},
  abstract = 	 {Whether neural networks can learn abstract reasoning or whether\
they merely rely on superficial statistics is a topic of recent debate. Here, \
we propose a dataset and challenge designed to probe abstract reasoning, \
inspired by a well-known human IQ test. To succeed at this challenge, models \
must cope with various generalisation 'regimes' in which the training data and \
test questions differ in clearly-defined ways. We show that popular models \
such as ResNets perform poorly, even when the training and test sets differ \
only minimally, and we present a novel architecture, with structure designed \
to encourage reasoning, that does significantly better. When we vary the way \
in which the test questions and training data differ, we find that our model \
is notably proficient at certain forms of generalisation, but notably weak at \
others. We further show that the model's ability to generalise improves \
markedly if it is trained to predict symbolic explanations for its answers. \
Altogether, we introduce and explore ways to both measure and induce stronger \
abstract reasoning in neural networks. Our freely-available dataset should \
motivate further progress in this direction.}
}
"""

_URL = ("https://github.com/deepmind/abstract-reasoning-matrices")

_DESCRIPTION = """\
Procedurally Generated Matrices (PGM) data from the paper Measuring Abstract \
Reasoning in Neural Networks, Barrett, Hill, Santoro et al. 2018. The goal is \
to infer the correct answer from the context panels based on abstract \
reasoning.

To use this data set, please download all the *.tar.gz files from the data set \
page and place them in ~/tensorflow_datasets/abstract_reasoning/.

$R$ denotes the set of relation types (progression, XOR, OR, AND, \
consistent union), $O$ denotes the object types (shape, line), and $A$ denotes \
the attribute types (size, colour, position, number). The structure of a \
matrix, $S$, is the set of triples $S={[r, o, a]}$ that determine the \
challenge posed by a particular matrix.
"""

_DESCRIPTION_NEUTRAL = r"""The structures encoding the matrices in both the \
training and testing sets contain any triples $[r, o, a]$ for $r \\in R$, \
$o \\in O$, and $a \\in A$. Training and testing sets are disjoint, with \
separation occurring at the level of the input variables (i.e. pixel \
manifestations)."""

_DESCRIPTION_INTERPOLATION = r"""As in the neutral split, $S$ consisted of any \
triples $[r, o, a]$. For interpolation, in the training set, when the \
attribute was "colour" or "size" (i.e., the ordered attributes), the values of \
the attributes were restricted to even-indexed members of a discrete set, \
whereas in the test set only odd-indexed values were permitted. Note that all \
$S$ contained some triple $[r, o, a]$ with the colour or size attribute . \
Thus, generalisation is required for every question in the test set."""

_DESCRIPTION_EXTRAPOLATION = r"""Same as in interpolation, but the values of \
the attributes were restricted to the lower half of the discrete set during \
training, whereas in the test set they took values in the upper half."""

_DESCRIPTION_ATTR_REL_PAIRS = r"""All $S$ contained at least two triples, \
$([r_1,o_1,a_1],[r_2,o_2,a_2]) = (t_1, t_2)$, of which 400 are viable. We \
randomly allocated 360 to the training set and 40 to the test set. Members \
$(t_1, t_2)$ of the 40 held-out pairs did not occur together in structures $S$ \
in the training set, and all structures $S$ had at least one such pair \
$(t_1, t_2)$ as a subset."""

_DESCRIPTION_ATTR_RELS = r"""In our dataset, there are 29 possible unique \
triples $[r,o,a]$. We allocated seven of these for the test set, at random, \
but such that each of the attributes was represented exactly once in this set. \
These held-out triples never occurred in questions in the training set, and \
every $S$ in the test set contained at least one of them."""

_DESCRIPTION_ATTR_PAIRS = r"""$S$ contained at least two triples. There are 20 \
(unordered) viable pairs of attributes $(a_1, a_2)$ such that for some \
$r_i, o_i, ([r_1,o_1,a_1],[r_2,o_2,a_2])$ is a viable triple pair \
$([r_1,o_1,a_1],[r_2,o_2,a_2]) = (t_1, t_2)$. We allocated 16 of these pairs \
for training and four for testing. For a pair $(a_1, a_2)$ in the test set, \
$S$ in the training set contained triples with $a_1$ or $a_2$. In the test \
set, all $S$ contained triples with $a_1$ and $a_2$."""

_DESCRIPTION_ATTR_SHAPE_COLOR = r"""Held-out attribute shape-colour. $S$ in \
the training set contained no triples with $o$=shape and $a$=colour. \
All structures governing puzzles in the test set contained at least one triple \
with $o$=shape and $a$=colour."""

_DESCRIPTION_ATTR_LINE_TYPE = r"""Held-out attribute line-type. $S$ in \
the training set contained no triples with $o$=line and $a$=type. \
All structures governing puzzles in the test set contained at least one triple \
with $o$=line and $a$=type."""


class AbstractReasoningConfig(tfds.core.BuilderConfig):
  """BuilderConfig for AbstractReasoning."""

  def __init__(self, *, split_type="neutral", **kwargs):
    """BuilderConfig for AbstractReasoning.

    Args:
      split_type: String with split_type to use. Should be one of ["neutral",
        "interpolation", "extrapolation", "attr.rel.pairs", "attr.rels",
        "attrs.pairs", "attrs.shape.color", "attrs.line.type",].
      **kwargs: keyword arguments forwarded to super.
    """
    v100 = tfds.core.Version(
        "1.0.0", "New split API (https://tensorflow.org/datasets/splits)")
    super(AbstractReasoningConfig, self).__init__(
        version=v100,
        **kwargs)
    self.split_type = split_type


class AbstractReasoning(tfds.core.BeamBasedBuilder):
  """Abstract reasoning dataset."""
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  Data can be downloaded from
  https://console.cloud.google.com/storage/browser/ravens-matrices
  Please put all the tar.gz files in manual_dir.
  """

  BUILDER_CONFIGS = [
      AbstractReasoningConfig(
          name="neutral",
          description=_DESCRIPTION_NEUTRAL,
      ),
      AbstractReasoningConfig(
          name="interpolation",
          description=_DESCRIPTION_INTERPOLATION,
          split_type="interpolation",
      ),
      AbstractReasoningConfig(
          name="extrapolation",
          description=_DESCRIPTION_EXTRAPOLATION,
          split_type="extrapolation",
      ),
      AbstractReasoningConfig(
          name="attr.rel.pairs",
          description=_DESCRIPTION_ATTR_REL_PAIRS,
          split_type="attr.rel.pairs",
      ),
      AbstractReasoningConfig(
          name="attr.rels",
          description=_DESCRIPTION_ATTR_RELS,
          split_type="attr.rels",
      ),
      AbstractReasoningConfig(
          name="attrs.pairs",
          description=_DESCRIPTION_ATTR_PAIRS,
          split_type="attrs.pairs",
      ),
      AbstractReasoningConfig(
          name="attrs.shape.color",
          description=_DESCRIPTION_ATTR_SHAPE_COLOR,
          split_type="attrs.shape.color",
      ),
      AbstractReasoningConfig(
          name="attrs.line.type",
          description=_DESCRIPTION_ATTR_LINE_TYPE,
          split_type="attrs.line.type",
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "context": tfds.features.Video(shape=(8, 160, 160, 1)),
            "answers": tfds.features.Video(shape=(8, 160, 160, 1)),
            "target":
                tfds.features.ClassLabel(num_classes=8),
            "meta_target":
                tfds.features.Tensor(shape=[12], dtype=tf.int64),
            "relation_structure_encoded":
                tfds.features.Tensor(shape=[4, 12], dtype=tf.int64),
            "filename":
                tfds.features.Text(),
        }),
        homepage=_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.manual_dir
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "folder": path,
                "split": "train",
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "folder": path,
                "split": "val",
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "folder": path,
                "split": "test",
            }),
    ]

  def _build_pcollection(self, pipeline, folder, split):
    """Generate examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam

    split_type = self.builder_config.split_type
    filename = os.path.join(folder, "{}.tar.gz".format(split_type))

    def _extract_data(inputs):
      """Extracts files from the tar archives."""
      filename, split = inputs
      for name, fobj in tfds.download.iter_archive(
          filename, tfds.download.ExtractMethod.TAR_STREAM):
        split_name = name.split("_")
        if len(split_name) > 2 and split_name[2] == split:
          yield [name, fobj.read()]

    def _process_example(inputs):
      filename, data_string = inputs
      buf = six.BytesIO(data_string)
      buf.seek(0)
      data = np.load(buf)
      # Extract the images and convert to uint8. The reshape is required, see
      # https://github.com/deepmind/abstract-reasoning-matrices.
      all_images = np.uint8(data["image"].reshape(16, 160, 160, 1))
      return filename, {
          "relation_structure_encoded": data["relation_structure_encoded"],
          "target": data["target"],
          "meta_target": data["meta_target"],
          "context": all_images[:8],
          "answers": all_images[8:],
          "filename": filename,
      }

    # Beam might fuse together the _extract_data and _process_example which
    # defeats the purpose of parallel processing. As a result, we reshard by
    # doing a GroupByKey on random keys, and then flattening again.
    def _add_random_keys(inputs):
      key = str(random.randrange(10**10))
      return key, inputs

    def _remove_keys(inputs):
      _, rows = inputs
      for row in rows:
        yield row

    return (pipeline
            | beam.Create([(filename, split)])
            | beam.FlatMap(_extract_data)
            | beam.Map(_add_random_keys)
            | beam.GroupByKey()
            | beam.FlatMap(_remove_keys)
            | beam.Map(_process_example))
