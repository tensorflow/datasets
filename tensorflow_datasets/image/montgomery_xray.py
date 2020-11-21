from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
import os
import tensorflow as tf

_CITATION = """
@ARTICLE{Jaeger2014-xx,
  title    = "Two public chest X-ray datasets for computer-aided screening of
              pulmonary diseases",
  author   = "Jaeger, Stefan and Candemir, Sema and Antani, Sameer and
              W{\'a}ng, Y{\`\i}-Xi{\'a}ng J and Lu, Pu-Xuan and Thoma, George",
  abstract = "The U.S. National Library of Medicine has made two datasets of
              postero-anterior (PA) chest radiographs available to foster
              research in computer-aided diagnosis of pulmonary diseases with a
              special focus on pulmonary tuberculosis (TB). The radiographs
              were acquired from the Department of Health and Human Services,
              Montgomery County, Maryland, USA and Shenzhen No. 3 People's
              Hospital in China. Both datasets contain normal and abnormal
              chest X-rays with manifestations of TB and include associated
              radiologist readings.",
  journal  = "Quant. Imaging Med. Surg.",
  volume   =  4,
  number   =  6,
  pages    = "475--477",
  month    =  dec,
  year     =  2014,
  keywords = "Tuberculosis (TB); automatic screening; chest X-rays;
              computer-aided diagnosis; medical imaging",
  language = "en"
}"""

_DESCRIPTION = """
The U.S. National Library of Medicine has made two datasets of
postero-anterior (PA) chest radiographs available to foster
research in computer-aided diagnosis of pulmonary diseases with a
special focus on pulmonary tuberculosis (TB). The radiographs
were acquired from the Department of Health and Human Services,
Montgomery County, Maryland, USA. Dataset contain normal and abnormal
chest X-rays with manifestations of TB and include associated
radiologist readings, as well as lung segmentation masks.
"""

_DATA_URL = {
    'public': 'http://openi.nlm.nih.gov/imgs/collections/NLM-MontgomeryCXRSet.zip'
}

class MontgomeryXray(tfds.core.GeneratorBasedBuilder):
  """Dataset from the montgomery dataset."""
  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(None, None, 1), encoding_format='png', dtype=tf.uint16),
            'leftMask': tfds.features.Image(shape=(None, None, 1), encoding_format='png', dtype=tf.uint8),
            'rightMask': tfds.features.Image(shape=(None, None, 1), encoding_format='png', dtype=tf.uint8),
            'age': tfds.features.Tensor(shape=(), dtype=tf.uint8),
            'sex': tfds.features.ClassLabel(names=['male', 'female', 'other']),
            'text': tfds.features.Tensor(shape=(), dtype=tf.string),
            'abnormal': tfds.features.Tensor(shape=(), dtype=tf.bool)
        }),
        homepage='https://lhncbc.nlm.nih.gov/publication/pub9931',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract(_DATA_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'datapath': dl_paths['public']
            }
        )
    ]

  def _generate_examples(self, datapath):
    """Yields examples."""

    for fname in tf.io.gfile.listdir('{}/MontgomerySet/ClinicalReadings'.format(datapath)):
        filename = os.path.basename(fname)[:-4]

        with open('{}/MontgomerySet/ClinicalReadings/{}.txt'.format(datapath, filename), 'r') as f:
            text = f.read()
            sex = text.split('\n')[0][15]
            age = int(text.split('\n')[1][15:18])
            diag = text.split('\n')[2]

        if sex == 'M': sex = 'male'
        elif sex == 'F': sex = 'female'
        else: sex = 'other'

        yield int(filename[7:11]), {
            'image': '{}/MontgomerySet/CXR_png/{}.png'.format(datapath, filename),
            'leftMask': '{}/MontgomerySet/ManualMask/leftMask/{}.png'.format(datapath, filename),
            'rightMask': '{}/MontgomerySet/ManualMask/rightMask/{}.png'.format(datapath, filename),
            'sex': sex,
            'age': age,
            'text': diag,
            'abnormal': bool(int(filename[12]))
        }
