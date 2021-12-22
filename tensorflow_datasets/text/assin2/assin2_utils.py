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
          'entailment should be in {}, got {}'.format(
              VALID_ENTAILMENT, entailment
          )
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
