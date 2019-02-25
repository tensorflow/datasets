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

# Number of observations (labels) per image
_NUM_CLASSES = 14

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

# Files contain paths to images and category labels
_TRAIN_DIR = 'train'
_VALIDATION_DIR = 'valid'
_TRAIN_LABELS_FNAME = 'train.csv'
_VALIDATION_LABELS_FNAME = 'valid.csv'


class Chexpert(tfds.core.GeneratorBasedBuilder):
    """CheXpert 2019."""

    VERSION = tfds.core.Version('2.0.0')
    # 1.0.0 to 2.0.0: fix validation labels.

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(),
                "label": tfds.features.ClassLabel(num_classes=_NUM_CLASSES),
                "file_name": tfds.features.Text(),
            }),
            supervised_keys=("image", "label"),
            urls=["https://stanfordmlgroup.github.io/competitions/chexpert/"],
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        # Downloads the data and defines the splits
        # dl_manager is a tfds.download.DownloadManager that can be used to
        # download and extract URLs
        path = dl_manager.manual_dir
        train_path = os.path.join(path, _TRAIN_DIR)
        val_path = os.path.join(path, _VALIDATION_DIR)

        if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
            msg = 'You must download the dataset files manually and place them in: '
            msg += f'{train_path}, {val_path}'
            raise AssertionError(msg)

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=1000,
                gen_kwargs={
                    "archive": dl_manager.iter_archive(train_path),
                    "csv_path": os.path.join(path, _TRAIN_LABELS_FNAME),
                },
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=10,
                gen_kwargs={
                    "archive": dl_manager.iter_archive(val_path),
                    "csv_path": os.path.join(path, _VALIDATION_LABELS_FNAME),
                },
            ),
        ]

    def _generate_examples(self, archive, csv_path):
        # Yields examples from the dataset
        for name, img in archive:
            pass
