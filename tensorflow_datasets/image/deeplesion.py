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

"""DeepLesion dataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets as tfds


# info of deeplesion dataset
_URL = ("https://www.nih.gov/news-events/news-releases/nih-clinical-center-releases-dataset-32000-ct-images")

_DESCRIPTION = """\
The DeepLesion dataset contains 32,120 axial computed tomography (CT) slices 
from 10,594 CT scans (studies) of 4,427 unique patients. There are 1–3 lesions 
in each image with accompanying bounding  boxes  and  size  measurements,  
adding  up  to  32,735  lesions  altogether.  The  lesion annotations were 
mined from NIH’s picture archiving and communication system (PACS).
"""

_URL = ("https://www.nih.gov/news-events/news-releases/nih-clinical-center-releases-dataset-32000-ct-images")
_BOX_URL = ("https://nihcc.app.box.com/v/DeepLesion")

_CITATION = """\
@article{DBLP:journals/corr/abs-1710-01766,
  author    = {Ke Yan and
               Xiaosong Wang and
               Le Lu and
               Ronald M. Summers},
  title     = {DeepLesion: Automated Deep Mining, Categorization and Detection of
               Significant Radiology Image Findings using Large-Scale Clinical Lesion
               Annotations},
  journal   = {CoRR},
  volume    = {abs/1710.01766},
  year      = {2017},
  url       = {http://arxiv.org/abs/1710.01766},
  archivePrefix = {arXiv},
  eprint    = {1710.01766},
  timestamp = {Mon, 13 Aug 2018 16:48:13 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-01766},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""


# link for download data
_BOX_URL = ("https://nihcc.app.box.com/v/DeepLesion")
_CSV_URL = ("https://raw.githubusercontent.com/anir16293/Deep-Lesion/master/DL_info.csv")


# location where local resource should be
_VERSION_DIR = "Deeplesion-v0.1.0"
_IMAGE_DIR = "Images_png"
_TRAIN_LABELS_FNAME = os.path.join("train.csv")
_VALIDATION_LABELS_FNAME = os.path.join("valid.csv")


# addtional definition for data parsing
_ANNOTATION_CATEGORY = collections.OrderedDict({
    '1':'Bone', 
    '2':'Abdomen', 
    '3':'Mediastinum', 
    '4':'Liver', 
    '5':'Lung', 
    '6':'Kidney', 
    '7':'Soft tissue', 
    '8':'Pelvis', 
    '-1':'unknown',
})


class Deeplesion(tfds.core.GeneratorBasedBuilder):
  """DeepLesion dataset builder.
  
    **Attention**: 
    The version only support manually data download.
    To properly make use of this dataset with tfds, users are expected to 
    download the dataset(56 zip files) and csv file (DL_info.csv) from 
    [box](https://nihcc.app.box.com/v/DeepLesion) manually.
    `batch_download_zips.py` are recommanded to download the zip files. 
    After download the data and unzip all zip files, please place the folder
    `Images_png` into `<manual_dir>/Deeplesion-v0.1.0`. Also, 
    Two Split files(train.csv, valid.csv) are expected inside 
    `<manual_dir>/Deeplesion-v0.1.0`. 
    Each split files should contain a header line. the name of columns should be 
    in the following order: 'slice_uid', 'xmin', 'ymin', 'xmax', 'ymax', 'label'"
  """

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image":tfds.features.Image(encoding_format='png'),
            "image/filename":tfds.features.Text(),
            "label":tfds.features.ClassLabel(num_classes=9),
            "bbox":tfds.features.BBoxFeature(),
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        # supervised_keys=("image", "label"),
        # Homepage of the dataset for documentation
        urls=[_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    path = os.path.join(dl_manager.manual_dir, _VERSION_DIR)
    imgs_path = os.path.join(path, _IMAGE_DIR)
    csv_path_train = os.path.join(path, _TRAIN_LABELS_FNAME)
    csv_path_valid = os.path.join(path, _VALIDATION_LABELS_FNAME)

    if not tf.io.gfile.exists(imgs_path):
      msg = ("You must download the dataset(56 zip files) and csv file \
        (DL_info.csv) from {} manually. `batch_download_zips.py` are \
        recommanded to download the zip files. After download the data, \
        unzip all zip files, collect all subfolders under `Images_png` \
        folder and place them into {}. Also, Two Split files(train.csv, \
        valid.csv) are expected placed into {}. Each split files should \
        contain columns in the following order: \
        'slice_uid, xmin, ymin, xmax, ymax, label'".format(_BOX_URL, \
          image_path, path))
      raise AssertionError(msg)


    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=100,
            gen_kwargs={
                "imgs_path": imgs_path,
                "csv_path": csv_path_train,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=10,
            gen_kwargs={
                "imgs_path": imgs_path,
                "csv_path": csv_path_valid,
            },
        ),
    ]


  def _generate_examples(self, imgs_path, csv_path):
    """
    :type imgs_path: string, path to read image files
    :type csv_path: string, path to read split files
    :rtype: dict, yield examples
    """
    def _decode_name(slice_uid):
      """decode name to get valid path

      :type slice_uid: string, with format patient_study_series_slice.png
      :rtype: string, path to find the slice
      """
      folder = '_'.join(slice_uid.split('_')[0:-1])
      fname = slice_uid.split('_')[-1]
      return os.path.join(folder, fname)
    

    with tf.io.gfile.GFile(csv_path) as csv_f:
      pd = tfds.core.lazy_imports.pandas
      data = pd.read_csv(csv_path).values

    for idx, value in enumerate(data):
      slice_uid, xmin, ymin, xmax, ymax, label = value
      record = {
          "name": slice_uid,
          "image": os.path.join(imgs_path, _decode_name(slice_uid)),
          "bbox": tfds.features.BBox(ymin=ymin, xmin=xmin, ymax=ymax, xmax=xmax),
          "label": label
      }
      yield idx, record
