"""Dataset class for Malaria dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import fnmatch

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://ceb.nlm.nih.gov/proj/malaria/cell_images.zip"

_DESCRIPTION = ("""The Malaria dataset contains a total of 27,558 cell images with equal instances of
parasitized and uninfected cells from the thin blood smear slide images of segmented cells.""")

_NAMES = ["parasitized", "uninfected"]

_IMAGE_SHAPE = (None, None, 3)

_CITATION = """\

 @article{rajaraman2018pre,
  title={Pre-trained convolutional neural networks as feature extractors toward improved malaria parasite detection in thin blood smear images},
  author={Rajaraman, Sivaramakrishnan and Antani, Sameer K and Poostchi, Mahdieh and Silamut, Kamolrat and Hossain, Md A and Maude, Richard J and Jaeger, Stefan and Thoma, George R},
  journal={PeerJ},
  volume={6},
  pages={e4568},
  year={2018},
  publisher={PeerJ Inc.}
}

"""

class Malaria(tfds.core.GeneratorBasedBuilder):
  """Malaria Cell Image Dataset Class"""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    """Define Dataset Info"""

    return tfds.core.DatasetInfo(
        builder=self,
        description=(_DESCRIPTION),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(names=_NAMES),
        }),
        supervised_keys=("image", "label"),
        urls=[_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Define Splits"""

    path = dl_manager.download_and_extract(_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "data_dir_path": os.path.join(path, "cell_images"),
            },
        ),
    ]

  def _generate_examples(self, data_dir_path):
    """Generate images and labels for splits"""

    path1 = os.path.join(data_dir_path, "Parasitized")
    path2 = os.path.join(data_dir_path, "Uninfected")
    folder_names = [path1, path2]

    for folder in folder_names:
      for file_name in tf.io.gfile.listdir(folder):
        if fnmatch.fnmatch(file_name, '*.png'):
          image = os.path.join(folder, file_name)
          label = os.path.split(folder)[1].lower()
          yield{
              "image": image,
              "label": label
          }
