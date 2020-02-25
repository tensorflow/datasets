"""REalistic and Dynamic Scenes (REDS) dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds

# Shared constants
_REDS_HD_IMAGE_HEIGHT = 720
_REDS_HD_IMAGE_WIDTH = 1280
_REDS_HD_IMAGE_SHAPE = (_REDS_HD_IMAGE_HEIGHT, _REDS_HD_IMAGE_WIDTH, 3)
_REDS_BICUBIC_IMAGE_HEIGHT = 180
_REDS_BICUBIC_IMAGE_WIDTH = 320
_REDS_BICUBIC_IMAGE_SHAPE = (_REDS_BICUBIC_IMAGE_HEIGHT,
                             _REDS_BICUBIC_IMAGE_WIDTH, 3)

_CITATION = """\
@InProceedings{Nah_2019_CVPR_Workshops_REDS,
  author = {Nah,
            Seungjun and Baik,
            Sungyong and Hong,
            Seokil and Moon,
            Gyeongsik and Son,
            Sanghyun and Timofte,
            Radu and Lee,
            Kyoung Mu},
  title = {NTIRE 2019 Challenge on Video Deblurring and Super-Resolution: Dataset and Study},
  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
  month = {June},
  year = {2019}
}
"""

_DESCRIPTION = """\
The REalistic and Dynamic Scenes (REDS) dataset is a high-quality
dataset consisting of 300 video sequences having length of 100 frames
with 720x1280 resolution. 40 sequences are for training, 30 for validation and
30 for testing purposes.

Four different degradations are applied to the
original images: blur, blur with compression, bicubic downsampling and
bicubic downsampling with blur. Each of these degradations constitutes a
sub-dataset.
"""

_URL = "https://seungjunnah.github.io/Datasets/reds.html"

_DATA_OPTIONS = {
    "sharp": _REDS_HD_IMAGE_SHAPE,
    "blur": _REDS_HD_IMAGE_SHAPE,
    "blur_comp": _REDS_HD_IMAGE_SHAPE,
    "sharp_bicubic": _REDS_BICUBIC_IMAGE_SHAPE,
    "blur_bicubic": _REDS_BICUBIC_IMAGE_SHAPE
}

_DL_URL = "https://cv.snu.ac.kr/~snah/Deblur/dataset/REDS/"
_DL_URLS = {
    name: [
        _DL_URL + split + "_" + name + ".zip"
        for split in ["train", "val", "test"]
    ] for name in list(_DATA_OPTIONS.keys())[1:]
}
_DL_URLS["sharp"] = [
    _DL_URL + split + "_sharp.zip" for split in ["train", "val"]
]


class REDSConfig(tfds.core.BuilderConfig):
  """BuilderConfig for REDS."""

  @tfds.core.disallow_positional_args
  def __init__(self, data, image_shape, **kwargs):
    """Constructs a REDSConfig.

    Args:
      data: (`str`) One of `_DATA_OPTIONS.keys()`.
      image_shape: (tuple of (`int`, `int`, `int`)) The shape of the images.
      **kwargs: keyword arguments forwarded to super.
    """
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of {:s}".format(
          list(_DATA_OPTIONS.keys())))

    super(REDSConfig, self).__init__(**kwargs)
    self.data = data
    self.image_shape = image_shape


class REDS(tfds.core.GeneratorBasedBuilder):
  """REDS dataset."""

  BUILDER_CONFIGS = [
      REDSConfig(name=config_name,
                 description=_DESCRIPTION,
                 version=tfds.core.Version("0.1.0"),
                 data=config_name,
                 image_shape=image_shape)
      for config_name, image_shape in _DATA_OPTIONS.items()
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=self.builder_config.description,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=self.builder_config.image_shape)
        }),
        homepage=_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    urls = _DL_URLS[self.builder_config.name]
    dl_paths = dl_manager.download(urls)

    split_generators = [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"archive": dl_manager.iter_archive(dl_paths[0])},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"archive": dl_manager.iter_archive(dl_paths[1])})
    ]
    if self.builder_config.name != "sharp":
      split_generators.append(
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={"archive": dl_manager.iter_archive(dl_paths[2])},
          ))

    return split_generators

  def _generate_examples(self, archive):
    """Generate REDS images given the downloaded archive."""

    for fname, fobj in archive:
      if fname.endswith(".png"):
        yield fname[-16:], {"image": fobj}
