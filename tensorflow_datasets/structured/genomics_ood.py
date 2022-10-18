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

"""genomics_ood dataset."""

import csv
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{ren2019likelihood,
  title={Likelihood ratios for out-of-distribution detection},
  author={Ren, Jie and
  Liu, Peter J and
  Fertig, Emily and
  Snoek, Jasper and
  Poplin, Ryan and
  Depristo, Mark and
  Dillon, Joshua and
  Lakshminarayanan, Balaji},
  booktitle={Advances in Neural Information Processing Systems},
  pages={14707--14718},
  year={2019}
}
"""

_DESCRIPTION = """
Bacteria identification based on genomic sequences holds the promise of early
detection of diseases, but requires a model that can output low confidence
predictions on out-of-distribution (OOD) genomic sequences from new bacteria
that were not present in the training data.

We introduce a genomics dataset for OOD detection that allows other researchers
to benchmark progress on this important problem. New bacterial classes are
gradually discovered over the years. Grouping classes by years is a natural way
to mimic the in-distribution and OOD examples.

The dataset contains genomic sequences sampled from 10 bacteria classes that
were discovered before the year 2011 as in-distribution classes, 60 bacteria
classes discovered between 2011-2016 as OOD for validation, and another 60
different bacteria classes discovered after 2016 as OOD for test, in total 130
bacteria classes. Note that training, validation, and test data are provided for
the in-distribution classes, and validation and test data are proviede for OOD
classes. By its nature, OOD data is not available at the training time.

The genomic sequence is 250 long, composed by characters of {A, C, G, T}. The
sample size of each class is 100,000 in the training and 10,000 for the
validation and test sets.

For each example, the features include:
  seq: the input DNA sequence composed by {A, C, G, T}.
  label: the name of the bacteria class.
  seq_info: the source of the DNA sequence, i.e., the genome name, NCBI
  accession number, and the position where it was sampled from.
  domain: if the bacteria is in-distribution (in), or OOD (ood)

The details of the dataset can be found in the paper supplemental.
"""

_DATA_URL = tfds.core.gcs_path('downloads/genomics_ood/genomics_ood.zip')

_LABELS_IN = [
    'Bacillus', 'Burkholderia', 'Clostridium', 'Escherichia', 'Mycobacterium',
    'Pseudomonas', 'Salmonella', 'Staphylococcus', 'Streptococcus', 'Yersinia'
]
_LABELS_OOD_VAL = [
    'Actinoplanes', 'Advenella', 'Alicycliphilus', 'Altererythrobacter',
    'Anabaena', 'Archangium', 'Bibersteinia', 'Blastochloris', 'Calothrix',
    'Carnobacterium', 'Cedecea', 'Cellulophaga', 'Chondromyces',
    'Chryseobacterium', 'Collimonas', 'Corallococcus', 'Cyclobacterium',
    'Dehalobacter', 'Desulfosporosinus', 'Devosia', 'Dyella', 'Elizabethkingia',
    'Glaciecola', 'Granulicella', 'Haliscomenobacter', 'Hymenobacter',
    'Kibdelosporangium', 'Kutzneria', 'Labilithrix', 'Leptolyngbya',
    'Leptospirillum', 'Lysobacter', 'Mannheimia', 'Massilia',
    'Methanobacterium', 'Microbacterium', 'Myroides', 'Neorhizobium',
    'Niastella', 'Oblitimonas', 'Octadecabacter', 'Oscillatoria', 'Pandoraea',
    'Pelosinus', 'Phaeobacter', 'Piscirickettsia', 'Planococcus',
    'Pseudonocardia', 'Pseudoxanthomonas', 'Rahnella', 'Raoultella',
    'Rufibacter', 'Saccharothrix', 'Sandaracinus', 'Singulisphaera',
    'Sphaerochaeta', 'Sphingobacterium', 'Spiroplasma', 'Tannerella',
    'Terriglobus'
]
_LABELS_OOD_TEST = [
    'Actinoalloteichus', 'Aeromicrobium', 'Agromyces', 'Aminobacter',
    'Aneurinibacillus', 'Blastomonas', 'Blautia', 'Bosea', 'Brevibacterium',
    'Cellulosimicrobium', 'Chryseolinea', 'Cryobacterium', 'Cystobacter',
    'Dietzia', 'Ensifer', 'Faecalibacterium', 'Fictibacillus', 'Filimonas',
    'Flammeovirga', 'Fuerstia', 'Gemmata', 'Granulosicoccus', 'Halioglobus',
    'Hydrogenophaga', 'Labrenzia', 'Leclercia', 'Lelliottia', 'Lentzea',
    'Luteitalea', 'Melittangium', 'Microbulbifer', 'Microvirga', 'Minicystis',
    'Moorea', 'Mucilaginibacter', 'Natronolimnobius', 'Nitratireductor',
    'Nitrospirillum', 'Nonomuraea', 'Olleya', 'Paludisphaera', 'Pannonibacter',
    'Petrimonas', 'Planctomyces', 'Plantactinospora', 'Plesiomonas',
    'Porphyrobacter', 'Rhizobacter', 'Rhodoplanes', 'Roseomonas', 'Roseovarius',
    'Salinimonas', 'Shinella', 'Sphingorhabdus', 'Sporosarcina',
    'Sulfitobacter', 'Tatumella', 'Tessaracoccus', 'Thiodictyon', 'Tumebacillus'
]
_LABELS_ALL = _LABELS_IN + _LABELS_OOD_VAL + _LABELS_OOD_TEST


class GenomicsOod(tfds.core.GeneratorBasedBuilder):
  """Genomic sequence dataset for out-of-distribution (OOD) detection."""

  VERSION = tfds.core.Version('0.0.1')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'seq': tfds.features.Text(),
            'label': tfds.features.ClassLabel(names=_LABELS_ALL),
            'seq_info': tfds.features.Text(),
            'domain': tfds.features.Text()
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('seq', 'label'),
        # Homepage of the dataset for documentation
        homepage='https://github.com/google-research/google-research/tree/master/genomics_ood',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    data_path = dl_manager.extract(_DATA_URL)
    return [
        tfds.core.SplitGenerator(
            name='train',  # name=tfds.Split.TRAIN,
            gen_kwargs={
                'filename': os.path.join(data_path, 'before_2011_in_tr.txt')
            },
        ),
        tfds.core.SplitGenerator(
            name='validation',
            gen_kwargs={
                'filename':
                    os.path.join(data_path, 'between_2011-2016_in_val.txt')
            },
        ),
        tfds.core.SplitGenerator(
            name='test',
            gen_kwargs={
                'filename': os.path.join(data_path, 'after_2016_in_test.txt')
            },
        ),
        tfds.core.SplitGenerator(
            name='validation_ood',
            gen_kwargs={
                'filename':
                    os.path.join(data_path, 'between_2011-2016_ood_val.txt')
            },
        ),
        tfds.core.SplitGenerator(
            name='test_ood',
            gen_kwargs={
                'filename': os.path.join(data_path, 'after_2016_ood_test.txt')
            },
        ),
    ]

  def _generate_examples(self, filename):
    """Yields examples."""
    with epath.Path(filename).open() as f:
      reader = csv.DictReader(f, delimiter='\t')
      for row_id, row in enumerate(reader):
        example = {}
        example['seq'] = row['seq']
        example['label'] = row['label']
        example['seq_info'] = row['seq_info']
        example['domain'] = row['domain']

        yield row_id, example
