from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets as tfds

_IMAGE_URL = ("http://people.duke.edu/~yx141/C_NMC_test_prelim_phase_data.zip")

_INFO_URL = "https://competitions.codalab.org/competitions/20395"

_CITATION = """\
@article{gupta2017stain,
  title={Stain Color Normalization and Segmentation of Plasma Cells in Microsc
  opic Images as a Prelude to Development of Computer Assisted Automated Disea
  se Diagnostic Tool in Multiple Myeloma},
  author={Gupta, Ritu and Mallick, Pramit and Duggal, Rahul and Gupta, Anubha
  and Sharma, Ojaswa},
  journal={Clinical Lymphoma, Myeloma and Leukemia},
  volume={17},
  number={1},
  pages={e99},
  year={2017},
  publisher={Elsevier}
}
@inproceedings{duggal2016overlapping,
  title={Overlapping cell nuclei segmentation in microscopic images using deep
  belief networks},
  author={Duggal, Rahul and Gupta, Anubha and Gupta, Ritu and Wadhwa, Manya
  and Ahuja, Chirag},
  booktitle={Proceedings of the Tenth Indian Conference on Computer Vision,
  Graphics and Image Processing},
  pages={82},
  year={2016},
  organization={ACM}
}
@article{duggal2016segmentation,
  title={Segmentation of overlapping/touching white blood cell nuclei using
  artificial neural networks},
  author={Duggal, R and Gupta, A and Gupta, R},
  journal={CME Series on Hemato-Oncopathology, All India Institute of Medical
  Sciences (AIIMS). New Delhi, India},
  year={2016}
}
@inproceedings{duggal2017sd,
  title={SD-layer: stain deconvolutional layer for CNNs in medical microscopic
  imaging},
  author={Duggal, Rahul and Gupta, Anubha and Gupta, Ritu and Mallick, Pramit}
  ,
  booktitle={International Conference on Medical Image Computing and Computer-
  Assisted Intervention},
  pages={435--443},
  year={2017},
  organization={Springer}
}
@under review{
title={GCTI-SN: Geometry-Inspired Chemical and Tissue Invariant Stain Normaliz
ation of Microscopic Medical Images},
author={Anubha Gupta, Rahul Duggal, Ritu Gupta, Lalit Kumar, Nisarg Thakkar,
and Devprakash Satpathy}
}"""

_DESCRIPTION = """\
 A large data set of  B-ALL white blood cancer microscopic images. The dataset
 contains total 1867 cropped images, which 1219 malignant cells images are
 labeled as class cancer, 648 normal cells images are labeled as class normal. The size
 of each image is 450 x 450 pixels x 3."""


class BAllWhiteBloodCancerMicroscopicImage(tfds.core.GeneratorBasedBuilder):
    """This is a binary classification problem."""
    VERSION = tfds.core.Version('0.1.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(),
                "label": tfds.features.ClassLabel(names=["cancer", "normal"]),
            }),
            supervised_keys=("image", "label"),
            urls=[_INFO_URL],
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        extracted_path = dl_manager.download_and_extract(_IMAGE_URL)

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=20,
                gen_kwargs={
                    "images_dir_path": extracted_path
                }),
        ]

    def _generate_examples(self, images_dir_path):
        parent_dir = tf.io.gfile.listdir(images_dir_path)[0]
        walk_dir = os.path.join(images_dir_path, parent_dir)
        dirs = tf.io.gfile.listdir(walk_dir)

        for d in dirs:
            if tf.io.gfile.isdir(os.path.join(walk_dir, d)):
                for full_path, _, fname in tf.io.gfile.walk(
                                                    os.path.join(walk_dir, d)):
                    for image_file in fname:
                        if image_file.endswith(".bmp"):
                            image_path = os.path.join(full_path, image_file)
                            record = {
                              "image": image_path,
                              "label": d.lower(),
                            }
                            yield "%s/%s" % (d, image_file), record
