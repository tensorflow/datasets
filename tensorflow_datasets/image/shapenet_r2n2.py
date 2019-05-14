"""Shapenet renderings/voxelizations based on the work of Choy et al.

3D Reconstruction from images.

`meta` values are those released by the authors (See `META_KEYS` for
interpretation). See
[this discussion](https://github.com/chrischoy/3D-R2N2/issues/39)
regarding the consistency/accuracy of the values.

Example usage:
```python
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.image import ShapenetR2n2Config

tf.enable_eager_execution()
flags = tf.flags
FLAGS = flags.FLAGS

flags.DEFINE_string("cat", "rifle", "category name or id")
flags.DEFINE_bool(
    "download", True, "setting to false after initial run makes things faster")
flags.DEFINE_integer("image_index", 0, "image index to use if single is False")

def vis(image, voxels):
  # visualize a single image/voxel pair
  import matplotlib.pyplot as plt
  # This import registers the 3D projection, but is otherwise unused.
  from mpl_toolkits.mplot3d import Axes3D

  # and plot everything
  fig = plt.figure()
  ax = fig.gca()
  ax.imshow(image)
  ax.axis("off")
  fig = plt.figure()
  ax = fig.gca(projection="3d")
  ax.voxels(voxels)
  ax.axis("square")
  plt.show()

def main(argv):
  config = ShapenetR2n2Config(cat=FLAGS.cat)
  dataset = tfds.load(
      "shapenet_r2n2/%s" % config.name, split=tfds.Split.TRAIN,
      download=FLAGS.download)

  for example in dataset:
    voxels = example["voxels"]
    image = example["rendering"]["image"][FLAGS.image_index]
    vis(image.numpy(), voxels.numpy())

if __name__ == "__main__":
  tf.app.run()
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import collections
import six
import contextlib
import numpy as np
import tensorflow as tf
import itertools

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core.features.run_length_encoded_feature.rle import binvox as bv
from tensorflow_datasets.core.features.run_length_encoded_feature.rle import np_impl
from tensorflow_datasets.core import lazy_imports

VOXEL_SHAPE = (32, 32, 32)
RENDERINGS_PER_EXAMPLE = 24
IMAGE_SHAPE = (137, 137, 3)
BACKGROUND_COLOR = (255, 255, 255)  # white
META_KEYS = (
    "azimuth",
    "elevation",
    "in_plane_rotation",
    "distance",
    "field_of_view",
)


def cat_ids():
  """Ordered list of category ids."""
  return sorted(_cat_names)


def cat_names():
  """List of category names in `cat_id` order."""
  return [_cat_names[c] for c in cat_ids()]


def cat_id(name):
  """Get the category id for the given id.

  If `name` is not a valid name but is a valid id, returns it instead.

  Args:
    name: string name, e.g. "sofa"

  Returns:
    string category id, e.g. "04256520"

  Raises:
    ValueError if `name` is not a valid category id or name.
  """
  if name in _cat_ids:
    return _cat_ids[name]
  elif name in _cat_names:
    return name
  else:
    raise ValueError(
        "cat '%s' is not a valid category name or id."
        "\nValid category `id: name`s:\n%s" % (name, _valid_cats_string()))


def cat_name(id_):
  """Get the category name for the given category id.

  If `id_` is not a valid id_ but is a valid name, returns it instead.

  Args:
    id_: string id, e.g. "04256520"

  Returns:
    string category name, e.g. "sofa"

  Raises:
    ValueError if `id_` is not a valid category id or name.
  """
  if id_ in _cat_ids:
    return id_
  elif id_ in _cat_names:
    return _cat_names[id_]
  else:
    raise ValueError(
        "cat '%s' is not a valid category name or id."
        "\nValid category `id: name`s:\n%s" % (id_, _valid_cats_string()))


_CITATION = """
@inproceedings{choy20163d,
  title={3D-R2N2: A Unified Approach for Single and Multi-view 3D Object Reconstruction},
  author={Choy, Christopher B and Xu, Danfei and Gwak, JunYoung and Chen, Kevin and Savarese, Silvio},
  booktitle = {Proceedings of the European Conference on Computer Vision ({ECCV})},
  year={2016}
}
"""

_cat_ids = {
    "bench": "02828884",
    "cabinet": "02933112",
    "car": "02958343",
    "chair": "03001627",
    "lamp": "03636649",
    "monitor": "03211117",
    "plane": "02691156",
    "rifle": "04090263",
    "sofa": "04256520",
    "speaker": "03691459",
    "table": "04379243",
    "telephone": "04401088",
    "watercraft": "04530566"
}

_cat_names = {v: k for k, v in _cat_ids.items()}


def _valid_cats_string():
  return "\n".join('%s : %s' % (_cat_ids[k], k) for k in sorted(_cat_ids))


_TRAIN_FRAC = 0.8


def _get_id_split(example_ids):
    example_ids.sort()
    n_examples = len(example_ids)
    split_index = int(_TRAIN_FRAC * n_examples)
    return example_ids[:split_index], example_ids[split_index:]


class ShapenetR2n2Config(tfds.core.BuilderConfig):
  def __init__(self, cat):
    """Create the config object for `ShapenetR2n2` `DatasetBuilder`.

    Args:
      cat: str, category name or id
    """
    assert(isinstance(cat, six.string_types))
    self.cat_id = cat_id(cat)
    self.cat_name = cat_name(cat)
    super(ShapenetR2n2Config, self).__init__(
        name=self.cat_id,
        version=tfds.core.Version(0, 0, 1),
        description=(
          "Multi-view renderings/voxels for ShapeNet category %s (%s)"
          % (self.cat_name, self.cat_id))
    )


class ShapenetR2n2(tfds.core.GeneratorBasedBuilder):
  """Builder for rendered/voxelized subset of Shapenet 3D dataset."""

  BUILDER_CONFIGS = [
      ShapenetR2n2Config(cat=cat) for cat in sorted(_cat_ids)]

  def _info(self):
    features = dict(
        cat_id=tfds.features.ClassLabel(names=cat_ids()),
        example_id=tfds.features.Text(),
        voxels=tfds.features.BinaryRunLengthEncodedFeature(shape=VOXEL_SHAPE))

    features["renderings"] = tfds.features.Sequence({
        "image": tfds.features.Image(shape=IMAGE_SHAPE),
        "meta": tfds.features.Tensor(shape=(5,), dtype=tf.float32)
    }, length=RENDERINGS_PER_EXAMPLE)

    features = tfds.features.FeaturesDict(features)
    return tfds.core.DatasetInfo(
        builder=self,
        description=(
            "Shapenet is a large collection of 3D CAD models. "
            "This dataset provides renderings and voxelizations "
            "of a subset of 13 categories as used by Choy et al."),
        features=features,
        supervised_keys=("renderings", "voxels"),
        urls=["http://cvgl.stanford.edu/3d-r2n2/", "https://www.shapenet.org/"],
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    from tensorflow_datasets.core.download import resource
    # Unfortunately the files at these urls are twice the size they need to be
    # since the archives contain an inner archive containing almost
    # everything in the rest of the outer archive.
    resources = dict(
        voxels="http://cvgl.stanford.edu/data2/ShapeNetVox32.tgz",
        renderings="http://cvgl.stanford.edu/data2/ShapeNetRendering.tgz")

    data_dirs = dl_manager.download_and_extract(resources)
    base_renderings_dir = os.path.join(
      data_dirs["renderings"], "ShapeNetRendering")
    base_voxels_dir = os.path.join(data_dirs["voxels"], "ShapeNetVox32")

    # We manually delete the inner duplicate archive after extraction
    duplicate_paths = [
      os.path.join(base_renderings_dir, "rendering_only.tgz"),
      os.path.join(base_voxels_dir, "binvox.tgz")
    ]
    for path in duplicate_paths:
      if tf.io.gfile.exists(path):
        tf.io.gfile.remove(path)

    cat_id = self.builder_config.cat_id
    voxels_dir = os.path.join(base_voxels_dir, cat_id)
    example_ids = tf.io.gfile.listdir(voxels_dir)
    train_ids, test_ids = _get_id_split(example_ids)
    kwargs = dict(
      cat_id=cat_id,
      voxels_dir=voxels_dir,
      renderings_dir=os.path.join(base_renderings_dir, cat_id),
    )

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, num_shards=len(train_ids) // 1000 + 1,
            gen_kwargs=dict(example_ids=train_ids, **kwargs)),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST, num_shards=len(test_ids) // 1000 + 2,
            gen_kwargs=dict(example_ids=test_ids, **kwargs))
    ]

  def _generate_examples(
      self, cat_id, example_ids, voxels_dir, renderings_dir):

    def load_image(example_id, image_index):
      image_path = os.path.join(
          renderings_dir, example_id, "rendering", "%02d.png" % image_index)
      with tf.io.gfile.GFile(image_path, "rb") as fp:
        image = np.array(lazy_imports.PIL_Image.open(fp))  # pylint: disable=no-member
      # tfds image features can't have 4 channels.
      background = (image[..., -1] == 0)
      image = image[..., :3]
      image[background] = BACKGROUND_COLOR
      return image

    def load_meta(example_id):
      meta_path = os.path.join(
          renderings_dir, example_id, "rendering", "rendering_metadata.txt")
      with tf.io.gfile.GFile(meta_path, "rb") as fp:
        meta = np.loadtxt(fp)
      return meta.astype(np.float32)

    def load_voxels(example_id):
      binvox_path = os.path.join(voxels_dir, example_id, "model.binvox")
      with tf.io.gfile.GFile(binvox_path, mode="rb") as fp:
        binvox = bv.parse_binvox(fp)
      return (VOXEL_SHAPE,
              np.asarray(np_impl.rle_to_brle(binvox.rle), dtype=np.int64))

    for example_id in example_ids:
      images = [
          load_image(example_id, i) for i in range(RENDERINGS_PER_EXAMPLE)]
      voxels = load_voxels(example_id)
      meta = load_meta(example_id)
      yield dict(
        voxels=voxels,
        renderings=dict(image=images, meta=meta),
        example_id=example_id,
        cat_id=cat_id)
