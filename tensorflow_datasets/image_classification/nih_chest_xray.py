"""nih_chest_xray dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
from tensorflow_datasets.core import utils
from zipfile import ZipFile
import os
import io


_CITATION = """\
@InProceedings{wang2017chestxray,author = {Wang, Xiaosong and Peng, Yifan and Lu, Le and Lu, Zhiyong and Bagheri, Mohammadhadi and Summers, Ronald},title = {ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases},booktitle = {2017 IEEE Conference on Computer Vision and Pattern Recognition(CVPR)},pages = {3462--3471},year = {2017}}
"""

_DESCRIPTION = """\
ChestX-ray dataset comprises 112,120 frontal-view X-ray images of 30,805 unique patients with the text-mined fourteen disease image labels (where each image can have multi-labels), mined from the associated radiological reports using natural language processing. Fourteen common thoracic pathologies include Atelectasis, Consolidation, Infiltration, Pneumothorax, Edema, Emphysema, Fibrosis, Effusion, Pneumonia, Pleural_thickening, Cardiomegaly, Nodule, Mass and Hernia, which is an extension of the 8 common disease patterns listed in our CVPR2017 paper. Note that original radiology reports (associated with these chest x-ray studies) are not meant to be publicly shared for many reasons. The text-mined disease labels are expected to have accuracy >90%.Please find more details and benchmark performance of trained models based on 14 disease labels in our arxiv paper: 1705.02315
"""


class NihChestXray(tfds.core.GeneratorBasedBuilder):
  """(nih_chest_xray) dataset."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
          "image/name":
          tfds.features.Text(),
          "image":
          tfds.features.Image(shape=(None, None, 1),
                              dtype=tf.uint16,
                              encoding_format='png'),
          "labels":
          tfds.features.Sequence(tfds.features.Text()),
          "follow_up":
          tfds.features.Tensor(shape=(), dtype=tf.int32),
          "patient_id":
          tfds.features.Tensor(shape=(), dtype=tf.int32),
          "patient_age":
          tfds.features.Tensor(shape=(), dtype=tf.int32),
          "patient_gender":
          tfds.features.Text(),
          "view_position":
          tfds.features.Test(),
          "original_image_width":
          tfds.features.Tensor(shape=(), dtype=tf.int32),
          "original_image_height":
          tfds.features.Tensor(shape=(), dtype=tf.int32),
          "original_image_pixel_spacing_x":
          tfds.features.Tensor(shape=(), dtype=tf.float32),
          "original_image_pixel_spacing_y":
          tfds.features.Tensor(shape=(), dtype=tf.float32),

        }),
        supervised_keys=("image", 'labels'),
        homepage='https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/36938765345',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    links = {
      'zipfile01': 'https://nihcc.box.com/shared/static/vfk49d74nhbxq3nqjg0900w5nvkorp5c.gz',
      'zipfile02': 'https://nihcc.box.com/shared/static/i28rlmbvmfjbl8p2n3ril0pptcmcu9d1.gz',
      'zipfile03': 'https://nihcc.box.com/shared/static/f1t00wrtdk94satdfb9olcolqx20z2jp.gz',
      'zipfile04': 'https://nihcc.box.com/shared/static/0aowwzs5lhjrceb3qp67ahp0rd1l1etg.gz',
      'zipfile05': 'https://nihcc.box.com/shared/static/v5e3goj22zr6h8tzualxfsqlqaygfbsn.gz',
      'zipfile06': 'https://nihcc.box.com/shared/static/asi7ikud9jwnkrnkj99jnpfkjdes7l6l.gz',
      'zipfile07': 'https://nihcc.box.com/shared/static/jn1b4mw4n6lnh74ovmcjb8y48h8xj07n.gz',
      'zipfile08': 'https://nihcc.box.com/shared/static/tvpxmn7qyrgl0w8wfh9kqfjskv6nmm1j.gz',
      'zipfile09': 'https://nihcc.box.com/shared/static/upyy3ml7qdumlgk2rfcvlb9k6gvqq2pj.gz',
      'zipfile10': 'https://nihcc.box.com/shared/static/l6nilvfa9cg3s28tqv1qc1olm3gnz54p.gz',
      'zipfile11': 'https://nihcc.box.com/shared/static/hhq8fkdgvcari67vfhs7ppg2w6ni4jze.gz',
      'zipfile12': 'https://nihcc.box.com/shared/static/ioqwiy20ihqwyr8pf4c24eazhh281pbu.gz',
      'data_entry_2017': 'https://github.com/jason-zl190/host_of_open_access_files/blob/master/nih_chest_xray/Data_Entry_2017_v2020.csv',
      'train_val_list': 'https://github.com/jason-zl190/host_of_open_access_files/blob/master/nih_chest_xray/train_val_list.txt',
      'test_list': 'https://github.com/jason-zl190/host_of_open_access_files/blob/master/nih_chest_xray/test_list.txt',
    }

    # download all resources
    archive_paths = dl_manager.download(links)
    # get ann_file
    ann_path = archive_paths['data_entry_2017']
    train_val_list_path = archive_paths['train_val_list']
    test_list_path = archive_paths['test_list']
    del archive_paths['data_entry_2017']
    del archive_paths['train_val_list']
    del archive_paths['test_list']

    # create two helper instances:
    # `archiveUtils` to read images from archives
    # `annParser` to parse the annotation file `data_entry_2017.csv`
    with tf.io.gfile.GFile(train_val_list_path, 'r') as f:
      train_val_list = f.read().splitlines()
    with tf.io.gfile.GFile(test_list_path, 'r') as f:
      test_list = f.read().splitlines()
 
    archiveUtils = ArchiveUtils(archive_paths)
    annParser = AnnParser(ann_path, train_val_list, test_list)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": archiveUtils,
                "split": annParser.ann['train'],
            },
        ),
       tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": archiveUtils,
                "split": annParser.ann['test'],
            },
        ),
    ]

  def _generate_examples(self):
    """Yields examples."""
    # TODO(nih_chest_xray): Yields (key, example) tuples from the dataset
    yield 'key', {}


class ArchiveUtils():
  """Helper class to read image(s) from archives
  Attributes:
    path: `dict`, paths of archives
    lookup_table: `dict`, hash table to lookup file path in archives
  """
  def __init__(self, path):
    """Inits ArchiveUtils with paths of archives"""
    self.path = path

  @utils.memoized_property
  def lookup_table(self):
    return self._build_lut()

  def extract_image(self, fileName):
    """Returns a file object according to the fileName
    Args:
      fileName: `str`, a fileName from the annotation file
    Returns:
      a file object of the fileName
    """
    archive = tf.io.gfile.GFile(self.lookup_table[fileName], 'rb')
    with ZipFile(archive, 'r') as zipfile:
      fpath = os.path.join('images', fileName)
      fObj = io.BytesIO(zipfile.read(fpath))
    return fObj

  @utils.memoize()
  def _build_lut(self):
    """Returns a hash table to lookup path of an archive using fileName.
    """
    lut = {}
    for k, v in self.path.items():  # k:v, <zipfile#>:<path of the zipfile>
      archive = tf.io.gfile.GFile(v, 'rb')
      with ZipFile(archive, 'r') as zipfile:
        for name in zipfile.namelist():  
          # name has a format as "images/fileName"
          fileName = name.split('/')[1]
          lut[fileName] = v
    return lut


class AnnParser():
  """Deeplesion Annotation Parser
  Attributes:
    ann_path: `str`, path of the annotation file
    config: `tfds.core.BuilderConfig`, builder_config
    train_val_list: `list`, idx list
    test_list: `list`, idx list
    ann: `dict`, <split>:`pandas.Dataframe`, parsed annotation
  """
  def __init__(self, ann_path, train_val_list, test_list, config=None):
    """Inits with path of the annotation file
    """
    self.ann_path = ann_path
    self.config = config
    self.train_val_list = train_val_list
    self.test_list = test_list
  
  @utils.memoized_property
  def ann(self):
    _ann = self._ann_parser()
    return _ann

  def _ann_parser(self):
    """Returns annotions of three splits
    """
    pd = tfds.core.lazy_imports.pandas
    with tf.io.gfile.GFile(self.ann_path) as csv_f:
      # read file
      df = pd.read_csv(csv_f)

      # split
      return {'train_val': df[df['Image Index'].isin(self.train_val_list)],
              'test': df[df['Image Index'].isin(self.test_list)]
             }
