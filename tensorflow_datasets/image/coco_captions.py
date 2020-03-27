"""MSCOCO Captioning Dataset from 2014."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{DBLP:journals/corr/LinMBHPRDZ14,
  author    = {Tsung{-}Yi Lin and
               Michael Maire and
               Serge J. Belongie and
               Lubomir D. Bourdev and
               Ross B. Girshick and
               James Hays and
               Pietro Perona and
               Deva Ramanan and
               Piotr Doll{\'{a}}r and
               C. Lawrence Zitnick},
  title     = {Microsoft {COCO:} Common Objects in Context},
  journal   = {CoRR},
  volume    = {abs/1405.0312},
  year      = {2014},
  url       = {http://arxiv.org/abs/1405.0312},
  archivePrefix = {arXiv},
  eprint    = {1405.0312},
  timestamp = {Mon, 13 Aug 2018 16:48:13 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/LinMBHPRDZ14},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DESCRIPTION = """
COCO is a large-scale object detection, segmentation, and captioning dataset.
COCO has several features:

Object segmentation
Recognition in context
Superpixel stuff segmentation
330K images (>200K labeled)
1.5 million object instances
80 object categories
91 stuff categories
5 captions per image
250,000 people with keypoints

In this dataset, there are 414113 captions, but 82783 images. Each image-caption
pair is represented once in the dataset - thus, each image appears 5 times.
"""

_HOMEPAGE = "http://cocodataset.org/"

class CocoCaptions(tfds.core.GeneratorBasedBuilder):
  """MSCOCO Image Captioning Dataset - 2014"""

  VERSION = tfds.core.Version('0.0.1')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'caption': tfds.features.Text()
        }),
        supervised_keys=('image', 'caption'),
        homepage=_HOMEPAGE,
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    data_paths = dl_manager.download_and_extract({
        'images': 'http://images.cocodataset.org/zips/val2014.zip',
        'annotations': 'http://images.cocodataset.org/annotations/annotations_trainval2014.zip'
    })

    img_path, ann_path = data_paths['images'], data_paths['annotations']

    return [tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                gen_kwargs={
                    "images_path": img_path + '/val2014',
                    "annotations_path": ann_path + '/annotations'
                })]

  def _generate_examples(self, images_path, annotations_path):
    """
    Generates examples as dictionaries of images and captions.
    Args:
      images_path: `str`, directory containing the images
      annotations_path: `str`, directory containing the annotations
    Yields:
      key (image id) and datapoint of (image, caption)
    """
    caption_file = '/captions_val2014.json'
    with tf.io.gfile.GFile(annotations_path + caption_file) as f:
      data = json.load(f)
    path_head = images_path + '/COCO_val2014_'
    ann = data['annotations'] # Contains annotations
    
    img_names = [path_head + '%012d.jpg' % i['image_id'] for i in ann] 
    captions = ['<start> ' + i['caption'] + ' <end>' for i in ann]
    ids = [i['id'] for i in ann]
    
    # The above lines create the captions (start and end tokens), the 
    # image names (which consist of the path head and a 12 digit number,
    # right-aligned with the id), and the id to distinguish each unique image.

    for (i, name) in enumerate(img_names):
      yield ids[i], {
          'image': name,
          'caption': captions[i]
      }
