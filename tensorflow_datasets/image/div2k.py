"""DIV2K dataset: DIVerse 2K resolution high quality images as used for the challenges @ NTIRE (CVPR 2017 and CVPR 2018) and @ PIRM (ECCV 2018)"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow_datasets.public_api as tfds

_CITATION = """@InProceedings{Ignatov_2018_ECCV_Workshops,
author = {Ignatov, Andrey and Timofte, Radu and others},
title = {PIRM challenge on perceptual image enhancement on smartphones: report},
booktitle = {European Conference on Computer Vision (ECCV) Workshops},
url = "http://www.vision.ee.ethz.ch/~timofter/publications/Agustsson-CVPRW-2017.pdf",
month = {January},
year = {2019}
}
"""

_DESCRIPTION = """
DIV2K dataset: DIVerse 2K resolution high quality images as used for the challenges @ NTIRE (CVPR 2017 and CVPR 2018) and @ PIRM (ECCV 2018)
"""

class Div2k(tfds.core.GeneratorBasedBuilder):
  """DIV2K dataset: DIVerse 2K resolution high quality images"""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "downscale_factor": tfds.features.ClassLabel(
                names=["1", "2", "3", "4"]),
            "operator": tfds.features.ClassLabel(
                names=["none", "bicubic"])
        }),
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    #note: root_path is not a .zip file, must hardcode paths
    root_path = "https://data.vision.ee.ethz.ch/cvl/DIV2K/"
    train_paths = dl_manager.download_and_extract({
        "HR": root_path + "DIV2K_train_HR.zip",
        "bicubic": root_path + "DIV2K_train_LR_bicubic.zip",
        })
    valid_paths = dl_manager.download_and_extract({
        "HR": root_path + "DIV2K_valid_HR.zip",
        "bicubic": root_path + "DIV2K_valid_LR_bicubic.zip",
        })
    #note: test and unknown files not provided
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "data_paths": train_paths,
                "split": "train",
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "data_paths": valid_paths,
                "split": "valid",
            },
        ),
    ]

  def _generate_examples(self, data_paths, split):
    """Yields examples."""

    file_range = range(1, 801) if split == "train" else range(801, 901)

    #note: uncomment below line if testing with div2k_test.py
    #file_range = range(1,2) if split == "train" else range(2,3)

    for i in file_range:
      file_num = "".join(["0" for _ in range(4 - len(str(i)))]) + str(i)
      image_path = os.path.join(data_paths["HR"],
                                "DIV2K_"+split+"_HR", file_num+".png")
      yield file_num, {
          "image": image_path,
          "downscale_factor": 1,
          "operator": "none",
      }

    for i in file_range:
      for j in range(2, 5):
        file_num = "".join(["0" for _ in range(4 - len(str(i)))]) + str(i)
        image_path = os.path.join(data_paths["bicubic"],
                                  "DIV2K_"+split+"_LR_bicubic",
                                  "X"+str(j), file_num+"x"+str(j)+".png")
        yield file_num+"x"+str(j), {
            "image": image_path,
            "downscale_factor": str(j),
            "operator": "bicubic",
        }
