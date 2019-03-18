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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from collections import defaultdict
import numpy as np
import os
import re

_DESCRIPTION = """\
Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos 
of 200 bird species (mostly North American). The total number of 
categories of birds is 200 and there are 6033 images in the dataset.
Annotations include bounding boxes, segmentation labels.
"""

_URL = ("http://www.vision.caltech.edu/visipedia/CUB-200.html")
_CITATION = """\
@techreport{WelinderEtal2010,
Author = {P. Welinder and S. Branson and T. Mita and C. Wah and F. Schroff and S. Belongie and P. Perona},
Institution = {California Institute of Technology},
Number = {CNS-TR-2010-001},
Title = {{Caltech-UCSD Birds 200}},
Year = {2010}
}
"""
_IMAGES_URL = "http://www.vision.caltech.edu/visipedia-data/CUB-200/images.tgz"
_SPLIT_URL = "http://www.vision.caltech.edu/visipedia-data/CUB-200/lists.tgz"
_ANNOTATIONS_URL = "http://www.vision.caltech.edu/visipedia-data/CUB-200/annotations.tgz"
_NAME_RE = re.compile(r"(\w*)/(\d*).(\w*)/(\w*.jpg)$")


class CaltechBirds2010(tfds.core.GeneratorBasedBuilder):
    '''Caltech Birds dataset'''

    VERSION = tfds.core.Version("0.1.0")

    def _info(self):

        return tfds.core.DatasetInfo(
                builder=self,
                description=_DESCRIPTION,
                features=tfds.features.FeaturesDict({
                    # Images are of varying size
                    # TODO: Need to add attributes and their annotations
                    "image": tfds.features.Image(),
                    "image/filename": tfds.features.Text(),
                    "label": tfds.features.ClassLabel(num_classes=200),
                    "label_name": tfds.features.Text(),
                    "bbox": tfds.features.BBoxFeature(),
                    "segmentation_mask": tfds.features.Image(shape=(None, None, 1)),
                }),
                supervised_keys=("image", "label"),
                urls=_URL,
                citation=_CITATION
                )

    def _split_generators(self, dl_manager):

        download_path = dl_manager.download([_SPLIT_URL, _ANNOTATIONS_URL, _IMAGES_URL])
        extracted_path = dl_manager.download_and_extract([_SPLIT_URL, _ANNOTATIONS_URL])

        train_path = os.path.join(extracted_path[0], "lists/train.txt")
        test_path = os.path.join(extracted_path[0], "lists/test.txt")

        with tf.io.gfile.GFile(train_path) as f:
            train_list = f.read().splitlines()

        with tf.io.gfile.GFile(test_path) as f:
            test_list = f.read().splitlines()

        attributes = defaultdict(list)

        for root, _, files in tf.io.gfile.walk(extracted_path[1]):
            # Parsing the .mat files which have the image annotations
            for fname in files:
                if fname.endswith(".mat"):
                    path = os.path.join(root, fname)
                    mat = tfds.core.lazy_imports.scipy_io.loadmat(path, squeeze_me=True, variable_names=["bbox", "seg"])
                    attributes[fname.split(".")[0]].append(mat["bbox"])
                    attributes[fname.split(".")[0]].append(mat["seg"])

        return [tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=10,
                gen_kwargs={
                            "archive": dl_manager.iter_archive(download_path[2]),
                            "file_names": train_list,
                            "annotations": attributes,
                            }),

                tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=1,
                gen_kwargs={
                            "archive": dl_manager.iter_archive(download_path[2]),
                            "file_names": test_list,
                            "annotations": attributes,
                            }),
                ]

    def _generate_examples(self, archive, file_names, annotations):
        """Generate birds images, labels and bounding box given the directory path

        Args:
        archive: object that iterates over the zip
        file_names : list of train/test image file names obtained from mat file
        annotations : dict of image file names and bbox attributes,
                     segmentation labels

        Yields:
        Image path, Image file name, its corresponding label and 
        bounding box values

        """

        for fname, fobj in archive:
            res = _NAME_RE.match(fname)
            if not res or not fname.split("/", 1)[-1] in file_names:
                continue

            label_name = res.group(3).lower()
            label_key = int(res.group(2))-1
            file_name = res.group(4).split(".")[0]
            segmentation_mask = annotations[file_name][1]

            height, width = segmentation_mask.shape

            # BBox attributes in range of 0.0 to 1.0
            def normalize_bbox(bbox_side, image_side):

                return int(bbox_side)/image_side

            yield {"image": fobj,
                   "image/filename": fname,
                   "label": label_key,
                   "label_name": label_name,
                   "bbox": tfds.features.BBox(
                        ymin=normalize_bbox(annotations[file_name][0]["top"],
                                            height),
                        xmin=normalize_bbox(annotations[file_name][0]["left"],
                                            width),
                        ymax=normalize_bbox(annotations[file_name][0]["bottom"],
                                            height),
                        xmax=normalize_bbox(annotations[file_name][0]["right"],
                                            width)),
                   "segmentation_mask": segmentation_mask[:, :, np.newaxis],
                  }