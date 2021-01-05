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

"""SCAN tasks with various different splits."""

import json
import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{Lake2018GeneralizationWS,
  title={Generalization without Systematicity: On the Compositional Skills of
         Sequence-to-Sequence Recurrent Networks},
  author={Brenden M. Lake and Marco Baroni},
  booktitle={ICML},
  year={2018},
  url={https://arxiv.org/pdf/1711.00350.pdf},
}
@inproceedings{Keysers2020,
  title={Measuring Compositional Generalization: A Comprehensive Method on
         Realistic Data},
  author={Daniel Keysers and Nathanael Sch\"{a}rli and Nathan Scales and
          Hylke Buisman and Daniel Furrer and Sergii Kashubin and
          Nikola Momchev and Danila Sinopalnikov and Lukasz Stafiniak and
          Tibor Tihon and Dmitry Tsarkov and Xiao Wang and Marc van Zee and
          Olivier Bousquet},
  note={Additional citation for MCD splits},
  booktitle={ICLR},
  year={2020},
  url={https://arxiv.org/abs/1912.09713.pdf},
}
"""

_DESCRIPTION = """SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

Most splits are described at https://github.com/brendenlake/SCAN. For the MCD
splits please see https://arxiv.org/abs/1912.09713.pdf.

Basic usage:

```
data = tfds.load('scan/length')
```

More advanced example:

```
data = tfds.load(
    'scan',
    builder_kwargs=dict(
        config=tfds.text.ScanConfig(
            name='simple_p8', directory='simple_split/size_variations')))
```
"""

_DATA_URL = 'https://github.com/brendenlake/SCAN/archive/master.zip'
_MCD_SPLITS_URL = (
    'https://storage.googleapis.com/cfq_dataset/scan-splits.tar.gz')


class ScanConfig(tfds.core.BuilderConfig):
  """BuilderConfig for SCAN.

  Splits can be read in two formats:

  1) As a pair of train and test files where each file contains one example
     input and output per line.
  2) With a 'splitfile' which contains for each split the indices into the full
     (unsplit) dataset.
  """

  def __init__(self, *, name, directory=None, splitfile=None, **kwargs):
    """BuilderConfig for SCAN.

    Args:
      name: Unique name of the split.
      directory: Which subdirectory to read the data files from.
      splitfile: If set the samples are read from the original archive
        (tasks.txt) but the splits are created using this index file.
      **kwargs: keyword arguments forwarded to super.
    """
    # Version history:
    super(ScanConfig, self).__init__(
        name=name,
        version=tfds.core.Version('1.1.1'),
        **kwargs)
    self.splitfile = splitfile
    if 'mcd' in name:
      self.splitfile = name + '.json'
    if self.splitfile and directory is None:
      self.directory = ''
    elif directory is None:
      self.directory = name + '_split'
    else:
      self.directory = directory


_COMMANDS = 'commands'
_ACTIONS = 'actions'


class Scan(tfds.core.GeneratorBasedBuilder):
  """SCAN task / splits as proposed by Brenden M. Lake and Marco Baroni."""

  BUILDER_CONFIGS = [
      ScanConfig(name='simple'),
      ScanConfig(name='addprim_jump', directory='add_prim_split'),
      ScanConfig(name='addprim_turn_left', directory='add_prim_split'),
      ScanConfig(name='filler_num0', directory='filler_split'),
      ScanConfig(name='filler_num1', directory='filler_split'),
      ScanConfig(name='filler_num2', directory='filler_split'),
      ScanConfig(name='filler_num3', directory='filler_split'),
      ScanConfig(name='length'),
      ScanConfig(name='template_around_right', directory='template_split'),
      ScanConfig(name='template_jump_around_right', directory='template_split'),
      ScanConfig(name='template_opposite_right', directory='template_split'),
      ScanConfig(name='template_right', directory='template_split'),
      ScanConfig(name='mcd1'),
      ScanConfig(name='mcd2'),
      ScanConfig(name='mcd3'),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _COMMANDS: tfds.features.Text(),
            _ACTIONS: tfds.features.Text(),
        }),
        supervised_keys=(_COMMANDS, _ACTIONS),
        homepage='https://github.com/brendenlake/SCAN',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    data_dir = dl_manager.download_and_extract(_DATA_URL)
    data_dir = os.path.join(data_dir, 'SCAN-master',
                            self.builder_config.directory)
    split = self.builder_config.name
    splitfile = self.builder_config.splitfile
    if 'mcd' in split:
      split_dir = dl_manager.download_and_extract(_MCD_SPLITS_URL)
      split_dir = os.path.join(split_dir, 'scan-splits')
      splitfile = os.path.join(split_dir, splitfile)
    if splitfile:
      kwargs = {
          'datapath': os.path.join(data_dir, 'tasks.txt'),
          'splitpath': splitfile
      }
      train_kwargs = kwargs.copy()
      train_kwargs['splitname'] = 'train'
      test_kwargs = kwargs.copy()
      test_kwargs['splitname'] = 'test'
    else:
      train_kwargs = {
          'datapath': os.path.join(data_dir, 'tasks_train_' + split + '.txt')
      }
      test_kwargs = {
          'datapath': os.path.join(data_dir, 'tasks_test_' + split + '.txt')
      }
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs=train_kwargs),
        tfds.core.SplitGenerator(name=tfds.Split.TEST, gen_kwargs=test_kwargs)
    ]

  def _read_examples(self, datapath):
    with tf.io.gfile.GFile(datapath) as infile:
      for i, line in enumerate(infile):
        if not line.startswith('IN: '):
          continue
        # Chop the prefix and split string between input and output
        commands, actions = line[len('IN: '):].strip().split(' OUT: ', 1)
        yield i, {_COMMANDS: commands, _ACTIONS: actions}

  def _generate_examples(self, datapath, splitpath=None, splitname=None):
    """Yields examples."""
    if splitpath:
      all_samples = list(self._read_examples(datapath))
      with tf.io.gfile.GFile(splitpath) as infile:
        split = json.load(infile)
      for idx in split[splitname + 'Idxs']:
        yield all_samples[idx]
    else:
      for example in self._read_examples(datapath):
        yield example
