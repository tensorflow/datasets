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

"""unnatural-instructions dataset."""

from __future__ import annotations
import json
from typing import Generator, Any, Tuple, Mapping
import tensorflow_datasets.public_api as tfds

_DS_PATH = 'https://github.com/orhonovich/unnatural-instructions/raw/main/data/full_data.zip'

_DESCRIPTION = """
Dataset described in the paper: Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor (2022).
Contains sets of natural-language instructions, with optional constraints / LLM-generated reformulations.
"""

_CITATION = """
@misc{honovich2022unnatural,
      title = {Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor},
      author = {Honovich, Or and Scialom, Thomas and Levy, Omer and Schick, Timo},
      url = {https://arxiv.org/abs/2212.09689},
      publisher = {arXiv},
      year={2022}
}
"""


class UnnaturalInstructions(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for unnatural_instructions dataset."""

  __count__ = 0

  VERSION = tfds.core.Version('0.0.1')
  RELEASE_NOTES = {
      '0.0.1': (
          'Initial release. Omit instructions / inputs, as they require '
          'additional processing to be used. Instruction_with_inputs and '
          'reformulations contain instructions and contexts.'
      ),
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        # Per author's recommendation, we discard the ans_simple field.
        features=tfds.features.FeaturesDict({
            'id': tfds.features.Text(doc='Unique identifier for example.'),
            'instruction': tfds.features.Text(
                doc='Instruction with placeholder for inputs.'
            ),
            'instances': tfds.features.Sequence({
                'input': tfds.features.Text(
                    doc=(
                        'Input to be fed into placeholders for given'
                        ' instruction.'
                    )
                ),
                'constraints': tfds.features.Text(
                    doc='Task-specific constraints.'
                ),
                'instruction_with_input': tfds.features.Text(
                    doc='Instructions with inputs supplied to placeholders.'
                ),
                'output': tfds.features.Text(
                    doc='Target output for given task.'
                ),
            }),
            'reformulations': tfds.features.Sequence({
                'input': tfds.features.Text(
                    doc=(
                        'Input to be fed into placeholders for given'
                        ' instruction.'
                    )
                ),
                'instruction': tfds.features.Text(
                    doc='Instruction with placeholder for inputs.'
                ),
                'instruction_with_input': tfds.features.Text(
                    doc='Instructions with inputs supplied to placeholders.'
                ),
                'output': tfds.features.Text(
                    doc='Target output for given task.'
                ),
            }),
        }),
        homepage='https://github.com/orhonovich/unnatural-instructions',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_DS_PATH)
    return {'train': self._generate_examples(path)}

  def _generate_examples(
      self,
      jsonl_path,
  ) -> Generator[Tuple[str, Mapping[str, Any]], None, None]:
    """Parses available JSON files in a given split, returns TF examples."""
    count = 0
    for file in [f.open() for f in jsonl_path.glob('*')]:
      for line in file:
        ex = json.loads(line)
        # Note: We perform minimal data massaging to preserve original struct.
        if 'reformulations' not in ex:
          ex['reformulations'] = []
        ex['id'] = str(count)
        count += 1
        yield str(count), ex  # Use count as a pseudo-id.
