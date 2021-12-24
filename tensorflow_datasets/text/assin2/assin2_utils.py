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
"""Util functions for assin2 dataset"""

from xml.etree import cElementTree as ET
from typing import List
from dataclasses import dataclass

VALID_ENTAILMENT = {'Entailment', 'None'}


@dataclass
class Pair:
  text: str
  hypothesis: str
  id: int
  entailment: str
  similarity: float


def parse_xml_string(xml_str: str) -> List[Pair]:
  """Process ASSIN2 xml files content.

    Modified from https://github.com/erickrf/assin

    Args:
        filename (str): string with XML contents

    Returns:
        list of Pair objects
    """
  pairs = []
  root = ET.fromstring(xml_str)

  for xml_pair in root.iter('pair'):
    # get fields
    text = xml_pair.find('t').text
    hypothesis = xml_pair.find('h').text
    attribs = dict(xml_pair.items())
    id_ = int(attribs['id'])
    entailment = attribs['entailment']
    similarity = float(attribs['similarity'])

    # assert valid fields
    if entailment not in VALID_ENTAILMENT:
      raise ValueError(
          'entailment should be in {VALID_ENTAILMENT}, got {entailment}'
      )
    pairs.append(
        Pair(
            text=text,
            hypothesis=hypothesis,
            id=id_,
            entailment=entailment,
            similarity=similarity
        )
    )
  return pairs
