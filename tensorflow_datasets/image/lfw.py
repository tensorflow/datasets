# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Labeled faces in wild."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow_datasets.public_api as tfds


_URL = "http://vis-www.cs.umass.edu/lfw/lfw.tgz"

LFW_IMAGE_SHAPE = (250, 250, 3)

LFW_CITATION = """\
@TechReport{LFWTech,
    author = {Gary B. Huang and Manu Ramesh and Tamara Berg and Erik Learned-Miller},
    title = {Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments},
    institution = {University of Massachusetts, Amherst},
    year = 2007,
    number = {07-49},
    month = {October}
}
"""


class LFW(tfds.core.GeneratorBasedBuilder):
    URL = "http://vis-www.cs.umass.edu/lfw/#resources"
    VERSION = tfds.core.Version("2.0.0")   
    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=("Labeled Faces in the Wild:\
             A Database for Studying Face Recognition in Unconstrained Environments"),
            features=tfds.features.FeaturesDict({
              "anchor": tfds.features.Image(shape=LFW_IMAGE_SHAPE),
              "positive": tfds.features.Image(shape=LFW_IMAGE_SHAPE),
              "negative": tfds.features.Image(shape=LFW_IMAGE_SHAPE),
            }),
            urls=[self.URL],
            citation=LFW_CITATION,
        )

    def _split_generators(self, dl_manager):
        path = dl_manager.download_and_extract(_URL)

        # There is no train/test split predefined 
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=20,
                gen_kwargs={
                  "data_path": path,}
            ),
        ]

    def _generate_examples(self, data_path):
        print("Generating triplets, this will take a while")
        # a list of dictionary will be recieved and each element(dict) will have 3 keys, each of which will store the path to the image 
        triplet_list = self.triplet_maker(data_path)
        
        for triplet in triplet_list:
            yield {
              "anchor": triplet["anchor"],
              "positive": triplet["positive"],
              "negative": triplet["negative"],
            }

    #This is a helper function for making all possible triplets for siamese network(eg. FaceNet)
    def triplet_maker(self, _path):
        triplet_list = []
        lfw = os.listdir(_path)
        lfw_mod = []
        for lst in lfw:
            lst_path = os.path.join(_path, lst)
            temp1 = os.listdir(lst_path)
            if len(temp1) > 1:
                lfw_mod.append(lst)
        for it, i in enumerate(lfw_mod):
            temp = 0
            path = os.path.join(_path, i)
            path_list = os.listdir(path)
            total_images = len(path_list)
            if total_images > 1:
                for img_no in range(temp, total_images):
                    for offset in range(1, total_images-temp):  
                        if (img_no+1) == total_images:
                            break
                        else:
                            for _it, _i in enumerate(lfw_mod):
                                path_list_negative = os.path.join(_path, _i)
                                total_images_negative = os.listdir(path_list_negative)
                                if len(total_images_negative) > 1:
                                    if _it == it:
                                        break
                                    else:
                                        for __i in total_images_negative:
                                            triplet_dict = {
                                              'anchor':os.path.join(path, path_list[img_no]), 
                                              'positive':os.path.join(path, path_list[img_no+offset]), 
                                              'negative':os.path.join(path_list_negative, __i),
                                                }
                                            triplet_list.append(triplet_dict)
                    temp = temp+1
        return triplet_list
