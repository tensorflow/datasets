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

"""Tests for assin2_utils."""
from tensorflow_datasets import testing
from tensorflow_datasets.datasets.assin2.assin2_utils import Pair
from tensorflow_datasets.datasets.assin2.assin2_utils import parse_xml_string

# pylint: disable=line-too-long
_CAND_XML_STR = """\
<?xml version='1.0' encoding='utf-8'?>
<entailment-corpus>
         <pair entailment="Entailment" id="1" similarity="4.5">
             <t>Uma criança risonha está segurando uma pistola de água e sendo espirrada com água</t>
             <h>Uma criança está segurando uma pistola de água</h>
         </pair>
         <pair entailment="Entailment" id="2" similarity="4.5">
             <t>Os homens estão cuidadosamente colocando as malas no porta-malas de um carro</t>
             <h>Os homens estão colocando bagagens dentro do porta-malas de um carro</h>
         </pair>
         <pair entailment="Entailment" id="3" similarity="4.7">
             <t>Uma pessoa tem cabelo loiro e esvoaçante e está tocando violão</t>
             <h>Um guitarrista tem cabelo loiro e esvoaçante</h>
         </pair>
         <pair entailment="Entailment" id="4" similarity="4.7">
             <t>Batatas estão sendo fatiadas por um homem</t>
             <h>O homem está fatiando a batata</h>
         </pair>
         <pair entailment="Entailment" id="5" similarity="4.9">
             <t>Um caminhão está descendo rapidamente um morro</t>
             <h>Um caminhão está rapidamente descendo o morro</h>
         </pair>
</entailment-corpus>
"""

# Same data from ./dummy_data/assin2-train-only.xml
_EXPECTED_PAIRS = [
    Pair(
        text=(
            'Uma criança risonha está segurando uma pistola de água e sendo'
            ' espirrada com água'
        ),
        hypothesis='Uma criança está segurando uma pistola de água',
        id=1,
        entailment='Entailment',
        similarity=4.5,
    ),
    Pair(
        text=(
            'Os homens estão cuidadosamente colocando as malas no porta-malas'
            ' de um carro'
        ),
        hypothesis=(
            'Os homens estão colocando bagagens dentro do porta-malas de um'
            ' carro'
        ),
        id=2,
        entailment='Entailment',
        similarity=4.5,
    ),
    Pair(
        text='Uma pessoa tem cabelo loiro e esvoaçante e está tocando violão',
        hypothesis='Um guitarrista tem cabelo loiro e esvoaçante',
        id=3,
        entailment='Entailment',
        similarity=4.7,
    ),
    Pair(
        text='Batatas estão sendo fatiadas por um homem',
        hypothesis='O homem está fatiando a batata',
        id=4,
        entailment='Entailment',
        similarity=4.7,
    ),
    Pair(
        text='Um caminhão está descendo rapidamente um morro',
        hypothesis='Um caminhão está rapidamente descendo o morro',
        id=5,
        entailment='Entailment',
        similarity=4.9,
    ),
]


class Assin2UtilsTest(testing.TestCase):

  def test_parse_xml_string(self):
    cand_pairs = parse_xml_string(_CAND_XML_STR)
    self.assertLen(cand_pairs, len(_EXPECTED_PAIRS))
    self.assertEqual(_EXPECTED_PAIRS, cand_pairs)


if __name__ == '__main__':
  testing.test_main()
