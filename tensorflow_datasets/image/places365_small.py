"""Dataset class for Places365-Standard small(256x256) dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six.moves.urllib as urllib
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import os
import fnmatch
import numpy as np

_BASE_URL = "http://data.csail.mit.edu/places/places365/"
_TRAIN_URL = "train_256_places365standard.tar"
_TEST_URL = "test_256.tar"
_VALID_URL = "val_256.tar"

_IMAGE_SHAPE = (256,256,3)

_DESCRIPTION = ("The Places365-Standard dataset contains 1.8 million train images from 365 scene categories,which are used to train the Places365 CNNs."
"There are 50 images per category in the validation set and 900 images per category in the testing set.")

_LABELS_FNAME = 'image/categories_places365.txt'

_CITATION = """\

 @article{zhou2017places,
  title={Places: A 10 million Image Database for Scene Recognition},
  author={Zhou, Bolei and Lapedriza, Agata and Khosla, Aditya and Oliva, Aude and Torralba, Antonio},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2017},
  publisher={IEEE}
}

"""

class Places365Small(tfds.core.GeneratorBasedBuilder):
  """Places365 Images dataset"""

  VERSION = tfds.core.Version('1.0.0')

#   @staticmethod
#   def getLabels():
#       with tf.io.gfile.GFile(_LABELS_FNAME) as f:
#         label_list = f.read().split("\n")
#       labels = []
#       for ele in label_list:
#         #Labels are in format /a/abbey 0
#         alphabet = ele[1]
#         m = ele.split('/'+alphabet+'/')[1] 
#         labels.append(m.split(" ")[0])
#       return labels


  def _info(self):
        names_file = tfds.core.get_tfds_path(_LABELS_FNAME)
        return tfds.core.DatasetInfo(
            builder=self,
    
            description=(_DESCRIPTION),
            
            features=tfds.features.FeaturesDict({
                "image":tfds.features.Image(shape=_IMAGE_SHAPE),
                "label": tfds.features.ClassLabel(names_file=names_file),
            }),

            supervised_keys=("image", "label"),
            
            urls=[_BASE_URL],
            
            citation=_CITATION
        )

  def _split_generators(self, dl_manager):
    
        output_files = dl_manager.download_and_extract({
            "train":urllib.parse.urljoin(_BASE_URL, _TRAIN_URL),
            "test":urllib.parse.urljoin(_BASE_URL, _TEST_URL),
            "validation":urllib.parse.urljoin(_BASE_URL, _VALID_URL),
        })

        return [
            tfds.core.SplitGenerator(
                name="train",
                num_shards=4,
                gen_kwargs={
                    "data_dir_path": output_files['train'],
                    "split_name":"train",
                },
            ),

            tfds.core.SplitGenerator(
                name="test",
                num_shards=4,
                gen_kwargs={
                    "data_dir_path": output_files['test'],
                    "split_name":"test",
                },
            ),

            tfds.core.SplitGenerator(
                name="validation",
                num_shards=4,
                gen_kwargs={
                    "data_dir_path": output_files['validation'],
                    "split_name":"validation",
                },
            ),
        
        ]

  def _generate_examples(self,data_dir_path,split_name):

        if split_name == 'test' or split_name == 'validation':
            for filename in tf.io.gfile.listdir(data_dir_path):
                image = os.path.join(data_dir_path,filename)
                class_name = 'test'
                yield{
                    "image":image,
                    "label":class_name,
                    }
        else:

      
            for dir in tf.io.gfile.listdir(data_dir_path):
                alphabet_dir = os.path.join(data_dir_path,dir)
                for class_name_dir in tf.io.gfile.listdir(alphabet_dir):
                    class_dir = os.path.join(alphabet_dir,class_name_dir)
                    class_name = class_name_dir
                    for image_name in tf.io.gfile.listdir(class_dir):
                        if fnmatch.fnmatch(image_name,"*.jpg"):
                            image = os.path.join(class_dir,image_name)
                        else:
                            for class_dir1 in tf.io.gfile.listdir(class_dir):
                                class_dir_path = os.path.join(class_dir,class_dir1)
                                for image_name in tf.io.gfile.listdir(class_dir_path):
                                    image = os.path.join(class_dir_path,image_name)
                                    class_name = class_name+'/'+class_dir1

                        yield{
                            "image":image,
                            "label":class_name,
                        }
