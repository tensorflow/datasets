"""Shapenet renderings/voxelizations based on the work of Choy et al.

3D Reconstruction from images.

`meta` values are those released by the authors (See `META_KEYS` for
interpretation). See [this discussion](https://github.com/chrischoy/3D-R2N2/issues/39)
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
flags.DEFINE_bool("single", False, "single/multi view dataset")
flags.DEFINE_bool(
    "download", True, "setting to false after initial run makes things faster")
flags.DEFINE_integer("image_index", 0, "image index to use if single is False")

def vis(image, voxels):
  # visualize a single image/voxel pair
  import matplotlib.pyplot as plt
  # This import registers the 3D projection, but is otherwise unused.
  from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

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
  config = ShapenetR2n2Config(cat=FLAGS.cat, single_view=FLAGS.single)
  dataset = tfds.load(
      "shapenet_r2n2/%s" % config.name, split=tfds.Split.TRAIN,
      download=FLAGS.download)

  for example in dataset:
    voxels = example["voxels"]
    image = example["rendering"]["image"]
    if not FLAGS.single:
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
from tensorflow_datasets.core.features.rle_feature.rle import binvox as bv
from tensorflow_datasets.core.features.rle_feature.rle import np_impl

RENDERINGS_PER_EXAMPLE = 24
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


class ShapenetR2n2Config(tfds.core.BuilderConfig):
  def __init__(self, cat, single_view):
    """Create the config object for `ShapenetR2n2` `DatasetBuilder`.

    Args:
      cat: str, category name or id
      single_view: bool. If True, each example constitutes a single rendering,
        otherwise all RENDERINGS_PER_EXAMPLE == 24 renderings are provided.
        Note that an epoc of the single-view variant is has 24x as many examples
        as the multi-view variant, as each CAD model is represented for each
        rendering.
    """
    version = "0.0.1"
    assert(isinstance(cat, six.string_types))
    self.cat_id = cat_id(cat)
    self.cat_name = cat_name(cat)
    self.single_view = single_view
    view_str = 'single' if single_view else 'multi'
    super(ShapenetR2n2Config, self).__init__(
        name='%s-%s' % (self.cat_id, view_str),
        version=version,
        description='%s: %s, %s' % (self.cat_id, self.cat_name, view_str)
    )


def _image_loader(cat_renderings_dir):
  from scipy.ndimage import imread

  def f(example_id, image_index):
    image_path = os.path.join(
        cat_renderings_dir, example_id, "rendering", "%02d.png" % image_index)
    with tf.io.gfile.GFile(image_path, "rb") as fp:
      image = imread(fp)
    background = (image[..., -1] == 0)
    image = image[..., :3]
    image[background] = BACKGROUND_COLOR
    return image

  return f


def _meta_loader(cat_renderings_dir):
  def f(example_id):
    meta_path = os.path.join(
        cat_renderings_dir, example_id, "rendering", "rendering_metadata.txt")
    with tf.io.gfile.GFile(meta_path, "rb") as fp:
      meta = np.loadtxt(fp)
    return meta.astype(np.float32)

  return f


def _voxel_loader(cat_voxels_dir):
  def f(example_id):
    binvox_path = os.path.join(cat_voxels_dir, example_id, "model.binvox")
    with tf.io.gfile.GFile(binvox_path, mode="rb") as fp:
      binvox = bv.parse_binvox(fp)
    return np_impl.rle_to_brle(binvox.rle)

  return f


class ShapenetR2n2(tfds.core.GeneratorBasedBuilder):
  """Builder for rendered/voxelized subset of Shapenet 3D dataset."""
  VERSION = tfds.core.Version("0.0.1")

  BUILDER_CONFIGS = [
      ShapenetR2n2Config(cat=cat, single_view=single_view) for
      (cat, single_view) in itertools.product(sorted(_cat_ids), (True, False))]

  def _info(self):
    features = dict(
        cat_id=tfds.features.ClassLabel(names=cat_ids()),
        example_id=tfds.features.Text(),
        voxels=tfds.features.SkipEncodingFeature(
            tfds.features.StaticShapedTensor(
                tfds.features.BrleFeature(),
                shape=(32, 32, 32),
            )
        )
    )
    rendering_feature_dict = dict(
        image=tfds.features.Image(shape=(137, 137, 3)),
        meta=tfds.features.Tensor(shape=(5,), dtype=tf.float32))

    if self.builder_config.single_view:
      rendering_feature = tfds.features.FeaturesDict(rendering_feature_dict)
      features["rendering_index"] = tfds.features.Tensor(
          shape=(), dtype=tf.int64)
    else:
      rendering_feature = tfds.features.SequenceDict(
          rendering_feature_dict, length=RENDERINGS_PER_EXAMPLE)
    features["rendering"] = rendering_feature

    features = tfds.features.FeaturesDict(features)
    return tfds.core.DatasetInfo(
        builder=self,
        description=(
            "Shapenet is a large collection of 3D CAD models. "
            "This dataset provides renderings and voxelizations "
            "of a subset of 13 categories as used by Choy et al."),
        features=features,
        supervised_keys=("rendering", "voxels"),
        urls=["http://cvgl.stanford.edu/3d-r2n2/", "https://www.shapenet.org/"],
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    # Unfortunately the files at these urls are twice the size they need to be
    # since the archives contain an inner archive containing the almost
    # everything in the rest of the outer archive.
    urls_to_download = dict(
        voxels_path="http://cvgl.stanford.edu/data2/ShapeNetVox32.tgz",
        renderings_path="http://cvgl.stanford.edu/data2/ShapeNetRendering.tgz")
    downloaded_urls = dl_manager.download_and_extract(urls_to_download)

    train_kwargs = dict(split=tfds.Split.TRAIN)
    test_kwargs = dict(split=tfds.Split.TEST)
    for kwargs in (train_kwargs, test_kwargs):
      kwargs.update(downloaded_urls)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, num_shards=10, gen_kwargs=train_kwargs),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST, num_shards=2, gen_kwargs=test_kwargs)
    ]

  def _get_id_split(self, example_ids, split):
    example_ids.sort()
    n_examples = len(example_ids)
    split_index = int(0.8 * n_examples)
    if split == tfds.Split.TRAIN:
      return example_ids[:split_index]
    elif split == tfds.Split.TEST:
      return example_ids[split_index:]
    else:
      raise ValueError("Invalid split '%s'" % split)

  def _generate_examples(self, split, voxels_path, renderings_path):
    cat_id = self.builder_config.cat_id
    cat_voxels_dir = os.path.join(voxels_path, "ShapeNetVox32", cat_id)
    cat_renderings_dir = os.path.join(
        renderings_path, "ShapeNetRendering", cat_id)
    example_ids = self._get_id_split(
        tf.gfile.ListDirectory(cat_voxels_dir), split)

    load_meta = _meta_loader(cat_renderings_dir)
    load_image = _image_loader(cat_renderings_dir)
    load_voxels = _voxel_loader(cat_voxels_dir)

    if self.builder_config.single_view:
      # single view config
      for example_id in example_ids:
        voxels = load_voxels(example_id)
        meta = load_meta(example_id)
        assert(meta.shape == (RENDERINGS_PER_EXAMPLE, 5))
        for i, m in enumerate(meta):
          image = load_image(example_id, i)
          yield dict(
              voxels=voxels,
              rendering=dict(image=image, meta=m),
              cat_id=cat_id,
              example_id=example_id,
              rendering_index=i)
    else:
      # multi view config
      for example_id in example_ids:
        images = [
            load_image(example_id, i) for i in range(RENDERINGS_PER_EXAMPLE)]
        voxels = load_voxels(example_id)
        meta = load_meta(example_id)
        yield dict(
              voxels=voxels,
              rendering=dict(image=images, meta=meta),
              example_id=example_id,
              cat_id=cat_id)
