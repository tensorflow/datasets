"""Dataset class for Food-101 dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import os

_BASE_URL = "http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz"

_DESCRIPTION = ("This dataset consists of 101 food categories, with 101'000 images. For each class, "
"250 manually reviewed test images are provided as well as 750 training images. On purpose, the training images were not cleaned, "
"and thus still contain some amount of noise. This comes mostly in the form of intense colors and sometimes wrong labels. "
"All images were rescaled to have a maximum side length of 512 pixels.")

_LABELS_FNAME = 'image/food-101_classes.txt'

_CITATION = """\

 @inproceedings{bossard14,
  title = {Food-101 -- Mining Discriminative Components with Random Forests},
  author = {Bossard, Lukas and Guillaumin, Matthieu and Van Gool, Luc},
  booktitle = {European Conference on Computer Vision},
  year = {2014}
}

"""

class Food101(tfds.core.GeneratorBasedBuilder):
  """Food-101 Images dataset"""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
        """Define Dataset Info"""
        names_file = tfds.core.get_tfds_path(_LABELS_FNAME)
        return tfds.core.DatasetInfo(
            builder=self,
    
            description=(_DESCRIPTION),
            
            features=tfds.features.FeaturesDict({
                "image":tfds.features.Image(),
                "label": tfds.features.ClassLabel(names_file=names_file),
            }),

            supervised_keys=("image", "label"),
            
            urls=[_BASE_URL],
            
            citation=_CITATION
        )

  def _split_generators(self, dl_manager):
        """Define Splits"""
        path = dl_manager.download_and_extract(_BASE_URL)

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=4,
                gen_kwargs={
                    "data_dir_path": os.path.join(path,'images'),
                },
            ),
        ]

  def _generate_examples(self,data_dir_path):
      """Generate images and labels for splits"""
      for class_name in tf.io.gfile.listdir(data_dir_path):
          class_dir_path = os.path.join(data_dir_path,class_name)
          for image_name in tf.io.gfile.listdir(class_dir_path):
              image = os.path.join(class_dir_path,image_name)
              yield{
                  "image":image,
                  "label":class_name,
              }

