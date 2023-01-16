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

"""Utilities for the assin2 dataset."""

import dataclasses
from typing import List
from xml.etree import cElementTree as ET

_VALID_ENTAILMENT = ('Entailment', 'None')


@dataclasses.dataclass
class Pair:
  text: str
  hypothesis: str
  id: int
  entailment: str
  similarity: float


def get_element_text(xml_pair: ET.Element, tag: str) -> str:
  """Returns the text associated with a given tag."""
  element = xml_pair.find(tag)
  assert element is not None, f'The tag "{tag}" was not found.'
  return element.text


def parse_xml_string(xml_str: str) -> List[Pair]:
  """Process ASSIN2 xml files content.

  Modified from https://github.com/erickrf/assin.

  Args:
    xml_str: string with XML contents

  Returns:
    list of Pair objects
  """
  pairs = []
  root = ET.fromstring(xml_str)

  for xml_pair in root.iter('pair'):
    # Get fields.
    text = get_element_text(xml_pair, 't')
    hypothesis = get_element_text(xml_pair, 'h')

    attribs = dict(xml_pair.items())
    id_ = int(attribs['id'])
    entailment = attribs['entailment']
    similarity = float(attribs['similarity'])

    # Assert valid fields.
    if entailment not in _VALID_ENTAILMENT:
      raise ValueError(
          f'Entailment should be in {_VALID_ENTAILMENT}, got {entailment}.'
      )
    pairs.append(
        Pair(
            text=text,
            hypothesis=hypothesis,
            id=id_,
            entailment=entailment,
            similarity=similarity,
        )
    )
  return pairs
