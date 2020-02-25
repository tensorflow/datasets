"""The  MSRA Salient Object Database, which originally provides salient\
 object annotation in terms of bounding boxes provided by 3-9 users, is\
 widely used in salient object detection and segmentation community.\
 Although an invaluable resource to evaluate saliency detection algorithms,\
 the database with the marked bounding boxes, however, is often too coarse for\
 fine-grained evaluation as observed by Wang and Li, and Achanta et al."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_CITATION = """
@article{ChengPAMI,
  author = {Ming-Ming Cheng and Niloy J. Mitra and Xiaolei Huang and Philip H. S. Torr and Shi-Min Hu},
  title = {Global Contrast based Salient Region Detection},
  year  = {2015},
  journal= {IEEE TPAMI},
  volume={37},
  number={3},
  pages={569--582},
  doi = {10.1109/TPAMI.2014.2345401},
}


@conference{13iccv/Cheng_Saliency,
  title={Efficient Salient Region Detection with Soft Image Abstraction},
  author={Ming-Ming Cheng and Jonathan Warrell and Wen-Yan Lin and Shuai Zheng and Vibhav Vineet and Nigel Crook},
  booktitle={IEEE ICCV},
  pages={1529--1536},
  year={2013},
}


@article{SalObjSurvey,
  author = {Ali Borji and Ming-Ming Cheng and Huaizu Jiang and Jia Li},
  title = {Salient Object Detection: A Survey},
  journal = {ArXiv e-prints},
  archivePrefix = {arXiv},
  eprint = {arXiv:1411.5878},
  year = {2014},
}


@article{SalObjBenchmark,
  author = {Ali Borji and Ming-Ming Cheng and Huaizu Jiang and Jia Li},
  title = {Salient Object Detection: A Benchmark},
  journal = {IEEE TIP},
  year={2015},
  volume={24},
  number={12},
  pages={5706-5722},
  doi={10.1109/TIP.2015.2487833},
}
"""


_DESCRIPTION = """
The  MSRA Salient Object Database, which originally provides salient\
 object annotation in terms of bounding boxes provided by 3-9 users, is\
 widely used in salient object detection and segmentation community.\
 Although an invaluable resource to evaluate saliency detection algorithms,\
 the database with the marked bounding boxes, however, is often too coarse for\
 fine-grained evaluation as observed by Wang and Li, and Achanta et al.
"""


class Msra10k(tfds.core.GeneratorBasedBuilder):
    """
    The  MSRA Salient Object Database, which originally provides salient object\
    annotation in terms of bounding boxes provided by 3-9 users,\
    is widely used in salient object detection and segmentation community
    """

    VERSION = tfds.core.Version('0.1.0')

    def _info(self):
        # TODO(msra10k): Specifies the tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # tfds.features.FeatureConnectors
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(),
                "mask": tfds.features.Image(),
            }),
            supervised_keys=("image", "mask"),
            # Homepage of the dataset for documentation
            homepage='http://mmcheng.net/msra10k/',
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""

        dl_paths = dl_manager.download_and_extract({
            'msra10k': 'http://mftp.mmcheng.net/Data/MSRA10K_Imgs_GT.zip',
        })
        extracted_path = dl_paths['msra10k']
        return[
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "images_dir_path": os.path.join(extracted_path, "MSRA10K_Imgs_GT/Imgs/")
                },
            ),
        ]

    def _generate_examples(self, images_dir_path):
        """Yields examples."""

        images_jpeg = []
        images_png = []
        for image_file in tf.io.gfile.listdir(images_dir_path):
            if(image_file.endswith('.png')):
                images_png.append(image_file)
            else:
                images_jpeg.append(image_file)
        for i, image_name in enumerate(images_jpeg):
            fname = (image_name.split("."))[0]
            yield i, {"image": images_dir_path + image_name,
                      "mask": images_dir_path + fname + ".png"}
