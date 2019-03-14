from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
import tensorflow as tf
from absl import logging

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.human_pose.mpii import annot_utils
from tensorflow_datasets.human_pose.mpii import skeleton
from tensorflow_datasets.core import lazy_imports
from tensorflow_datasets.core.download import extractor

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
  VERSION = tfds.core.Version(0, 0, 1)

  def _info(self):
    return tfds.core.DatasetInfo(
      builder=self,
      description="Human-annotated 2D human poses on in-the-wild images",
      features=tfds.features.FeaturesDict({
        "image": tfds.features.Image(encoding_format="jpeg"),
        "filename": tfds.features.Text(),
        "targets": tfds.features.SequenceDict({
          "joints": tfds.features.Tensor(shape=(NUM_JOINTS, 2), dtype=tf.int64),
          "visible": tfds.features.Tensor(shape=(NUM_JOINTS,), dtype=tf.bool),
          "center": tfds.features.Tensor(shape=(2,), dtype=tf.int64),
          "scale": tfds.features.Tensor(shape=(), dtype=tf.float32),
        }),
        # ymin, xmin, ymax, xmax
        # same order as BBoxFeature, but not scaled
        # everything else is in pixel coordinates, making a special exception
        # here feels inappropriate
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
      urls=["http://human-pose.mpi-inf.mpg.de/"],
      citation=MPII_CITATION)

  def _split_generators(self, dl_manager):
    paths = dl_manager.download({
      "images": "https://datasets.d2.mpi-inf.mpg.de/andriluka14cvpr/mpii_human_pose_v1.tar.gz",
      "annot": "https://datasets.d2.mpi-inf.mpg.de/andriluka14cvpr/mpii_human_pose_v1_u12_2.zip",
    })

    annot_dir = paths["annot"]
    # don't extract images
    annot_dir = dl_manager.extract(annot_dir)
    if isinstance(annot_dir, dict):
      # tests return the original dict
      annot_dir = annot_dir["annot"]

    annot_path = os.path.join(
      annot_dir, "mpii_human_pose_v1_u12_2", "mpii_human_pose_v1_u12_1.mat")
    images_gen = lambda: extractor.iter_tar_gz(paths["images"])
    annot = annot_utils.Annotations(annot_path)
    annot_indices = {f: i for i, f in enumerate(annot.filenames)}

    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.TRAIN,
        num_shards=32,
        gen_kwargs=dict(
          images_fn=images_gen,
          annot=annot,
          annot_indices=annot_indices,
          generate_train_data=True,
        )),
      tfds.core.SplitGenerator(
        name=tfds.Split.TEST,
        num_shards=8,
        gen_kwargs=dict(
          images_fn=images_gen,
          annot=annot,
          annot_indices=annot_indices,
          generate_train_data=False,
        )),
    ]

  def _generate_examples(
      self, images_fn, annot, annot_indices, generate_train_data):
    logging.info(
      "Iterating over %s examples. Progress bar for .tar.gz has issues, "
      "so it may look like things have hanged. They probably haven't."
      % ("train" if generate_train_data else "test"))
    original_separated_indices = annot.original_separated_indices
    video_indices = annot.video_indices
    frame_secs = annot.frame_secs
    activities = annot.activities
    is_train = annot.is_train
    video_indices = annot.video_indices
    coord_helpers = annot.coord_helpers
    filenames = annot.filenames
    youtube_ids = annot.youtube_ids

    if not generate_train_data:
      # constant over all iterations
      activity = -1
      category = -1
      frame_sec = -1
      # could be shape (0, 4), but statistics have issues with completely empty
      # structures
      head_box = np.zeros((0, 4), dtype=np.int64)

    for path, image in images_fn():
      filename = path.split('/')[-1]
      index = annot_indices[filename]
      assert(filenames[index] == filename)
      if is_train[index] != generate_train_data:
        continue
      coord_helper = coord_helpers[index]

      video_index = video_indices[index]
      youtube_id = "UNK" if video_index is None else youtube_ids[video_index]

      center = coord_helper.centers
      scale = coord_helper.scales.astype(np.float32)
      separated_individuals = coord_helper.reindex(
          original_separated_indices[index])

      if generate_train_data:
        # train data
        if coord_helper.is_pointless:
          continue
        category, activity = activities[index]
        category = category or -1
        activity = activity or -1
        joints, visible = coord_helper.coordinates

        frame_sec = frame_secs[index]
        head_box = coord_helper.head_boxes
      else:
        # test data
        num_valid_people = coord_helper.num_valid_people
        joints = -np.ones((num_valid_people, NUM_JOINTS, 2), dtype=np.int64)
        visible = np.zeros((num_valid_people, NUM_JOINTS), dtype=np.bool)

      yield dict(
          image=image,
          targets=dict(
            joints=joints,
            visible=visible,
            center=center,
            scale=scale,
          ),
          head_box=head_box,
          filename=filename,
          activity=activity,
          category=category,
          frame_sec=frame_sec,
          youtube_id=youtube_id,
          separated_individuals=separated_individuals,
        )
