"""https://stanfordmlgroup.github.io/competitions/chexpert/"""

import csv
import os

import tensorflow_datasets.public_api as tfds
import tensorflow as tf


_DESCRIPTION = '''\
CheXpert is a large dataset of chest X-rays and competition for automated chest 
x-ray interpretation, which features uncertainty labels and radiologist-labeled 
reference standard evaluation sets. It consists of 224,316 chest radiographs 
of 65,240 patients, where the chest radiographic examinations and the associated 
radiology reports were retrospectively collected from Stanford Hospital. Each 
report was labeled for the presence of 14 observations as positive, negative, 
or uncertain. We decided on the 14 observations based on the prevalence in the 
reports and clinical relevance.
'''

_CITATION = '''\
@article{DBLP:journals/corr/abs-1901-07031,
  author    = {Jeremy Irvin and Pranav Rajpurkar and Michael Ko and Yifan Yu and Silviana Ciurea{-}Ilcus and Chris Chute and Henrik Marklund and Behzad Haghgoo and Robyn L. Ball and Katie Shpanskaya and Jayne Seekins and David A. Mong and Safwan S. Halabi and Jesse K. Sandberg and Ricky Jones and David B. Larson and Curtis P. Langlotz and Bhavik N. Patel and Matthew P. Lungren and Andrew Y. Ng},
  title     = {CheXpert: {A} Large Chest Radiograph Dataset with Uncertainty Labels and Expert Comparison},
  journal   = {CoRR},
  volume    = {abs/1901.07031},
  year      = {2019},
  url       = {http://arxiv.org/abs/1901.07031},
  archivePrefix = {arXiv},
  eprint    = {1901.07031},
  timestamp = {Fri, 01 Feb 2019 13:39:59 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1901-07031},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
'''

# Path to images and category labels in data dir
_DATA_DIR =                   'CheXpert-v1.0-small'
_TRAIN_DIR =                   f'{_DATA_DIR}/train'
_VALIDATION_DIR =              f'{_DATA_DIR}/valid'
_TRAIN_LABELS_FNAME =      f'{_DATA_DIR}/train.csv'
_VALIDATION_LABELS_FNAME = f'{_DATA_DIR}/valid.csv'

# Labels per category
_LABELS = ['', '-1.0', '0.0', '1.0']


class Chexpert(tfds.core.GeneratorBasedBuilder):
    """CheXpert 2019."""

    VERSION = tfds.core.Version('1.0.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "name": tfds.features.Text(),  # patient info
                "image": tfds.features.Image(),
                "label": tfds.features.Sequence(
                    tfds.features.ClassLabel(names=_LABELS)),
            }),
            supervised_keys=("image", "label"),
            urls=["https://stanfordmlgroup.github.io/competitions/chexpert/"],
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        path = dl_manager.manual_dir
        train_path = os.path.join(path, _TRAIN_DIR)
        val_path = os.path.join(path, _VALIDATION_DIR)

        if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
            msg = 'You must download the dataset folder from CheXpert' + \
                  f'website manually and place it into {path}.'
            raise AssertionError(msg)

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=100,
                gen_kwargs={
                    "imgs_path": path,  # Relative img path is provided in csv
                    "csv_path": f'{path}/{_TRAIN_LABELS_FNAME}',
                },
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=10,
                gen_kwargs={
                    "imgs_path": path,
                    "csv_path": f'{path}/{_VALIDATION_LABELS_FNAME}',
                },
            ),
        ]

    def _generate_examples(self, imgs_path, csv_path):
        with tf.io.gfile.GFile(csv_path) as csv_f:
            reader = csv.DictReader(csv_f)
            # Get keys for each label from csv
            label_keys = reader.fieldnames[5:]
            data = []
            for row in reader:
                # Get image based on indicated path in csv
                name = row['Path']
                labels = [row[key] for key in label_keys]
                data.append((name, labels))

        for name, labels in data:
            yield {
                'name': name,
                'image': f'{imgs_path}/{name}',
                'label': labels
            }
