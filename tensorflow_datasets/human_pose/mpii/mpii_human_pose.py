# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""MPII Human Pose Dataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
import tensorflow as tf

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.human_pose.mpii import annot_utils
from tensorflow_datasets.human_pose.mpii import skeleton

NUM_JOINTS = skeleton.s16.num_joints
_LABELS_PATH = tfds.core.get_tfds_path("human_pose/mpii/%s.txt")

MPII_CITATION = """\
@inproceedings{andriluka14cvpr,
        author = {Mykhaylo Andriluka and Leonid Pishchulin and Peter Gehler and Schiele, Bernt}
        title = {2D Human Pose Estimation: New Benchmark and State of the Art Analysis},
        booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
        year = {2014},
        month = {June}
}"""


class MpiiHumanPose(tfds.core.GeneratorBasedBuilder):
  """MPII Human Pose Dataset."""
  VERSION = tfds.core.Version('0.0.1')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="Human-annotated 2D human poses on in-the-wild images",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(encoding_format="jpeg"),
            "filename": tfds.features.Text(),
            # different joint attributes
            "joints": tfds.features.Tensor(
                shape=(None, NUM_JOINTS, 2), dtype=tf.int64),
            "joint_visible": tfds.features.Tensor(
                shape=(None, NUM_JOINTS,), dtype=tf.bool),
            "center": tfds.features.Tensor(shape=(None, 2,), dtype=tf.int64),
            "scale": tfds.features.Tensor(shape=(None,), dtype=tf.float32),
            # ymin, xmin, ymax, xmax
            # same order as BBoxFeature, but not scaled
            # everything else is in pixel coordinates, making a special
            # exception here feels inappropriate
            "head_box": tfds.features.Tensor(shape=(None, 4), dtype=tf.int64),
            "separated_individuals": tfds.features.Tensor(
                shape=(None,), dtype=tf.int64),
            "frame_sec": tfds.features.Tensor(shape=(), dtype=tf.int64),
            "activity": tfds.features.ClassLabel(
                names_file=_LABELS_PATH % "activity_names"),
            "category": tfds.features.ClassLabel(
                names_file=_LABELS_PATH % "category_names"),
            "youtube_id": tfds.features.Text(),
        }),
        homepage="http://human-pose.mpi-inf.mpg.de/",
        citation=MPII_CITATION)

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    paths = dl_manager.download({
        "images": "https://datasets.d2.mpi-inf.mpg.de/andriluka14cvpr/mpii_human_pose_v1.tar.gz",
        "annot": "https://datasets.d2.mpi-inf.mpg.de/andriluka14cvpr/mpii_human_pose_v1_u12_2.zip",
    })
    extracted = dl_manager.extract(paths)

    annot_dir = extracted["annot"]
    if isinstance(annot_dir, dict):
      # tests return the original dict
      annot_dir = paths["annot"]["annot"]
    annot_path = os.path.join(
        annot_dir, "mpii_human_pose_v1_u12_2", "mpii_human_pose_v1_u12_1.mat")
    annot = annot_utils.Annotations(annot_path)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                image_dir=os.path.join(extracted["images"], "images"),
                annot=annot,
                train_data=True,
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                image_dir=os.path.join(extracted["images"], "images"),
                annot=annot,
                train_data=False,
            )),
    ]

  def _generate_examples(self, image_dir, annot, train_data):
    """Generate examples as dicts.

    Args:
      image_dir: directory containing the images
      annot: annotation helper object
      train_data: (bool) True if training data should be generated

    Yields:
      example key and data
    """
    annot_indices = {f: i for i, f in enumerate(annot.filenames)}

    for filename in tf.io.gfile.listdir(image_dir):
      index = annot_indices[filename]
      assert annot.filenames[index] == filename
      if annot.is_train[index] != train_data:
        continue

      video_index = annot.video_indices[index]
      if video_index is None:
        youtube_id = "UNK"
      else:
        youtube_id = annot.youtube_ids[video_index]

      coord_helper = annot.coord_helpers[index]
      separated_individuals = coord_helper.reindex(
          annot.original_separated_indices[index])

      if train_data:
        if coord_helper.is_pointless:
          continue
        category, activity = annot.activities[index]
        category = category or -1
        activity = activity or -1
        joints, visible = coord_helper.coordinates
        head_box = coord_helper.head_boxes
      else:
        # test data
        head_box = np.zeros((0, 4), dtype=np.int64)
        num_valid_people = coord_helper.num_valid_people
        joints = -np.ones((num_valid_people, NUM_JOINTS, 2), dtype=np.int64)
        visible = np.zeros((num_valid_people, NUM_JOINTS), dtype=np.bool)

      features = dict(
          image=os.path.join(image_dir, filename),
          joints=joints,
          joint_visible=visible,
          center=coord_helper.centers,
          scale=coord_helper.scales.astype(np.float32),
          head_box=head_box,
          filename=filename,
          activity=activity if train_data else -1,
          category=category if train_data else -1,
          frame_sec=annot.frame_secs[index] if train_data else -1,
          youtube_id=youtube_id,
          separated_individuals=separated_individuals,
      )
      yield index, features
