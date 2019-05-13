from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core import download
import os


SHAPENET_CITATION = """\
@article{chang2015shapenet,
  title={Shapenet: An information-rich 3d model repository},
  author={Chang, Angel X and Funkhouser, Thomas and Guibas, Leonidas and Hanrahan, Pat and Huang, Qixing and Li, Zimo and Savarese, Silvio and Savva, Manolis and Song, Shuran and Su, Hao and others},
  journal={arXiv preprint arXiv:1512.03012},
  year={2015}
}
"""

SHAPENET_URL = "https://www.shapenet.org/"


class ShapenetCoreConfig(tfds.core.BuilderConfig):

  @abc.abstractproperty
  def synset_id(self):
    raise NotImplementedError

  @abc.abstractmethod
  def features(self):
    raise NotImplementedError

  @abc.abstractmethod
  def get_example_data(self, model_id, obj_dir):
    raise NotImplementedError

  def supervised_keys(self):
    return None

  def __enter__(self):
    pass

  def __exit__(self, *args, **kwargs):
    pass


def load_synset_ids():
  path = os.path.join(os.path.dirname(__file__), 'core_synset.txt')
  synset_ids = {}
  synset_names = {}
  with tf.io.gfile.GFile(path, "rb") as fp:
    for line in fp.readlines():
      line = line.rstrip()
      if line == '':
        continue
      id_, names = line.split('\t')
      names = tuple(names.split(','))
      synset_names[id_] = names
      for n in names:
        synset_ids[n] = id_
  return synset_ids, synset_names


BASE_URL = 'http://shapenet.cs.stanford.edu/shapenet/obj-zip/'
DL_URL = '%s/ShapeNetCore.v1/{synset_id}.zip' % BASE_URL
SPLIT_URL = '%s/SHREC16/all.csv' % BASE_URL
TAXONOMY_URL = '%s/ShapeNetCore.v1/taxonomy.json' % BASE_URL


def load_taxonomy(path):
  with tf.io.gfile.GFile(path, 'r') as fp:
    return json.load(fp)


def load_splits(path, synset_id):
  splits = ('train', 'test')
  model_ids = {k: [] for k in splits}
  with tf.io.gfile.GFile(split_path, 'rb') as fp:
    fp.readline()  # header
    for line in fp.readlines():
      line = line.rstrip()
      if line == '':
        pass
      record_id, synset_id_, sub_synset_id, model_id, split = line.split(',')
      if synset_id_ == synset_id:
        model_ids[split].append(model_id)
  return model_ids


class ShapenetCore(tfds.core.GeneratorBasedBuilder):
  BUILDER_CONFIGS = []

  def _info(self):
    return tfds.core.DatasetInfo(
      builder=self,
      features=self.builder_config.features(),
      citation=SHAPENET_CITATION,
      supervised_keys=self.builder_config.supervised_keys(),
      urls=[SHAPENET_URL],
    )

  def _split_generators(self, dl_manager):
    synset_id = self.builder_config.synset_id
    synset_url = DL_URL.format(synset_id=synset_id)
    split_path = dl_manager.download(SPLIT_URL)
    synset_dir = dl_manager.download_and_extract(synset_url)
    # paths = dl_manager.download_and_extract({
    #   'taxonomy': TAXONOMY_URL,
    #   'split': SPLIT_URL,
    #   'synset': synset_url,
    # })

    model_ids = load_splits(split_path, synset_id)
    splits = sorted(model_ids)
    return [tfds.core.SplitGenerator(
      name=split, num_shards=len(ids[split]) // 1000 + 2,
      gen_kwargs=dict(synset_dir=synset_dir, model_ids=ids[split]))
            for split in splits]

  def _generate_examples(self, synset_dir, model_ids):
    config = self.builder_config
    with config:
      for model_id in model_ids:
        model_dir = os.path.join(synset_dir, model_id)
        example = config.get_example_data(model_id, model_dir)
        if example is not None:
          yield example
