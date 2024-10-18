# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""TAO dataset."""

from __future__ import annotations

import collections
from collections.abc import Mapping
import json
import os
from typing import Any

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_VIDEO_URL = 'https://motchallenge.net/data/'
_ANNOTATIONS_URL = (
    'https://github.com/TAO-Dataset/annotations/archive/v1.2.tar.gz'
)

_DESCRIPTION = """
The TAO dataset is a large video object detection dataset consisting of
2,907 high resolution videos and 833 object categories. Note that this dataset
requires at least 300 GB of free space to store.
"""

_CITATION = """
@article{Dave_2020,
   title={TAO: A Large-Scale Benchmark for Tracking Any Object},
   ISBN={9783030585587},
   ISSN={1611-3349},
   url={http://dx.doi.org/10.1007/978-3-030-58558-7_26},
   DOI={10.1007/978-3-030-58558-7_26},
   journal={Lecture Notes in Computer Science},
   publisher={Springer International Publishing},
   author={Dave, Achal and Khurana, Tarasha and Tokmakov, Pavel and Schmid, Cordelia and Ramanan, Deva},
   year={2020},
   pages={436-454}
}
"""

NestedDict = Mapping[str, Any]


def _build_annotations_index(
    annotations: NestedDict,
) -> tuple[NestedDict, NestedDict, NestedDict, NestedDict]:
  """Builds several dictionaries to aid in looking up annotations."""
  vids = {x['id']: x for x in annotations['videos']}
  images = {x['id']: x for x in annotations['images']}
  ann_to_images = {}
  track_to_anns = collections.defaultdict(list)
  vid_to_tracks = collections.defaultdict(list)
  for track in annotations['tracks']:
    vid_to_tracks[track['video_id']].append(track)
  for ann in annotations['annotations']:
    ann_to_images[ann['id']] = images[ann['image_id']]
    track_to_anns[ann['track_id']].append(ann)
  return vids, ann_to_images, track_to_anns, vid_to_tracks


def _merge_categories_map(annotations: NestedDict) -> dict[str, str]:
  """Some categories should be renamed into others.

  This code segment is based on the TAO provided preprocessing API.

  Args:
    annotations: a dictionary containing all the annotations

  Returns:
    merge_map: dictionary mapping from category id to merged id
  """
  merge_map = {}
  for category in annotations['categories']:
    if 'merged' in category:
      for to_merge in category['merged']:
        merge_map[to_merge['id']] = category['id']
  return merge_map


def _maybe_prepare_manual_data(
    dl_manager: tfds.download.DownloadManager,
) -> tuple[epath.Path | None, epath.Path | None]:
  """Return paths to the manually downloaded data if it is available."""

  # The file has a different name each time it is downloaded.
  manually_downloaded_files = [
      '1_AVA_HACS_TRAIN_*.zip',
      '2_AVA_HACS_VAL_*.zip',
      '3_AVA_HACS_TEST_*.zip',
  ]
  files = []
  for file in manually_downloaded_files:
    file_glob = [_ for _ in dl_manager.manual_dir.glob(file)]
    if not file_glob:  # No manually downloaded files.
      return None, None
    if len(file_glob) == 1:
      files.append(file_glob[0])
    else:
      raise ValueError(
          'Unexpected multiple files matching pattern: '
          f'{file} inside {os.fspath(dl_manager.manual_dir)}. '
          'There should only be one file matching this pattern.'
      )
  return dl_manager.extract(files)


def _get_category_id_map(annotations_root) -> dict[str, int]:
  """Gets a map from the TAO category id to a tfds category index.

  The tfds category index is the index which a category appears in the
  label list.

  Args:
    annotations_root: directory containing the train and validation annotations.

  Returns:
    id_map: A dict mapping from TAO category id to tfds category index,
      filtered to contain only categories appearing in the train and val set.
  """

  train = json.loads((annotations_root / 'train.json').read_text())
  val = json.loads((annotations_root / 'validation.json').read_text())

  merge_map = _merge_categories_map(train)
  merge_map.update(_merge_categories_map(val))

  classes = set()
  classes |= {a['category_id'] for a in train['annotations']}
  classes |= {a['category_id'] for a in val['annotations']}

  id_map = {}

  for tfds_id, lvis_id in enumerate(
      sorted([merge_map.get(x, x) for x in classes])
  ):
    id_map[lvis_id] = tfds_id

  return id_map


def _preprocess_annotations(
    annotations_file: str, id_map: dict[str, int]
) -> NestedDict:
  """Preprocesses the data to group together some category labels."""
  with epath.Path(annotations_file).open('r') as f:
    annotations = json.load(f)
  for ann in annotations['annotations'] + annotations['tracks']:
    ann['category_id'] = id_map[ann['category_id']]

  for ann in annotations['videos']:
    filtered_neg_ids = []
    for neg_cat_id in ann['neg_category_ids']:
      if neg_cat_id in id_map:
        filtered_neg_ids.append(id_map[neg_cat_id])
    ann['neg_category_ids'] = filtered_neg_ids
    filtered_not_exhaustive_ids = []

    for not_exhaustive_id in ann['not_exhaustive_category_ids']:
      if not_exhaustive_id in id_map:
        filtered_not_exhaustive_ids.append(id_map[not_exhaustive_id])
    ann['not_exhaustive_category_ids'] = filtered_not_exhaustive_ids
  # The frame index in the image starts at an arbitrary number. Make it
  # zero indexed.
  vid_to_frame_start = collections.defaultdict(lambda: np.inf)
  for image in annotations['images']:
    vid = image['video_id']
    vid_to_frame_start[vid] = min(vid_to_frame_start[vid], image['frame_index'])
  for image in annotations['images']:
    image['frame_index'] -= vid_to_frame_start[image['video_id']]
  return annotations


def _create_per_track_annotation(
    track,
    track_to_anns: NestedDict,
    anns_to_image: NestedDict,
    height: int,
    width: int,
) -> NestedDict:
  """Prepares annotation for a single track within a video."""
  per_track_anno = {}
  per_track_anno['bboxes'] = []
  per_track_anno['frames'] = []
  track_annos = track_to_anns[track['id']]
  assert len(np.unique([a['category_id'] for a in track_annos])) == 1
  assert len(np.unique([a['scale_category'] for a in track_annos])) == 1
  assert len(np.unique([a['iscrowd'] for a in track_annos])) == 1
  per_track_anno['category'] = track['category_id']
  per_track_anno['is_crowd'] = track_annos[0]['iscrowd']
  per_track_anno['scale_category'] = track_annos[0]['scale_category']
  per_track_anno['track_id'] = track['id']
  for ann in track_to_anns[track['id']]:
    # NOTE: Some bbox annotations extend off the boundary of the image.
    # Below we clip them to lie within the image boundaries.
    ymin = max(0.0, ann['bbox'][1] / height)
    ymax = min(1.0, (ann['bbox'][1] + ann['bbox'][3]) / height)
    xmin = max(0.0, ann['bbox'][0] / width)
    xmax = min(1.0, (ann['bbox'][0] + ann['bbox'][2]) / width)
    per_track_anno['bboxes'].append(
        tfds.features.BBox(ymin=ymin, ymax=ymax, xmin=xmin, xmax=xmax)
    )
    per_track_anno['frames'].append(anns_to_image[ann['id']]['frame_index'])

  # Frame indices should be sorted.
  assert all(
      per_track_anno['frames'][i - 1] <= per_track_anno['frames'][i]
      for i in range(1, len(per_track_anno['frames']))
  )
  return per_track_anno


class TaoConfig(tfds.core.BuilderConfig):
  """Configuration for Tao video dataset."""

  def __init__(
      self,
      *,
      height: int | None = None,
      width: int | None = None,
      **kwargs,
  ):
    """The parameters specifying how the dataset will be processed.

    This allows the option to preprocess the images to a smaller fixed
    resolution. If height and width are left as None, the native size
    will be used.

    Args:
      height: optional height to resize all images to
      width: optional width to resize all images to
      **kwargs: Passed on to the constructor of `BuilderConfig`.
    """
    super(TaoConfig, self).__init__(**kwargs)
    if height is not None or width is not None:
      if height is None or width is None:
        raise ValueError('Provide either both height and width or None.')
    self.height = height
    self.width = width


class Tao(tfds.core.BeamBasedBuilder):
  """DatasetBuilder for tao dataset."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  Some TAO files (HVACS and AVA videos) must be manually downloaded because
  a login to MOT is required. Please download and those data following
  the instructions at https://motchallenge.net/tao_download.php

  Download this data and move the resulting .zip files to
  ~/tensorflow_datasets/downloads/manual/

  If the data requiring manual download is not present, it will be skipped over
  and only the data not requiring manual download will be used.
  """
  BUILDER_CONFIGS = [
      TaoConfig(
          name='480_640',
          description='All images are bilinearly resized to 480 X 640',
          height=480,
          width=640,
      ),
      TaoConfig(
          name='full_resolution',
          description='The full resolution version of the dataset.',
          height=None,
          width=None,
      ),
  ]
  VERSION = tfds.core.Version('1.1.0')
  RELEASE_NOTES = {
      '1.1.0': 'Added test split.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    names_file = tfds.core.tfds_path('video/tao/labels.txt')
    video_shape = (
        None,
        self.builder_config.height,
        self.builder_config.width,
        3,
    )
    all_features = {
        'video': tfds.features.Video(video_shape),  # pytype: disable=wrong-arg-types  # gen-stub-imports
        'metadata': {
            'height': np.int32,
            'width': np.int32,
            'num_frames': np.int32,
            'video_name': np.str_,
            'neg_category_ids': tfds.features.Tensor(
                shape=(None,), dtype=np.int32
            ),
            'not_exhaustive_category_ids': tfds.features.Tensor(
                shape=(None,), dtype=np.int32
            ),
            'dataset': np.str_,
        },
        'tracks': tfds.features.Sequence({
            'bboxes': tfds.features.Sequence(tfds.features.BBoxFeature()),
            'category': tfds.features.ClassLabel(names_file=names_file),
            'is_crowd': np.bool_,
            'track_id': np.int32,
            'scale_category': np.str_,
            # Labels do not occur for all frames. This indicates the
            # indices of the frames that have labels.
            'frames': tfds.features.Sequence(np.int32),
        }),
    }

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(all_features),
        supervised_keys=None,
        homepage='https://taodataset.org/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    data = dl_manager.download_and_extract({
        'train': _VIDEO_URL + '1-TAO_TRAIN.zip',
        'val': _VIDEO_URL + '2-TAO_VAL.zip',
        'test': _VIDEO_URL + '3-TAO_TEST.zip',
        'annotations': _ANNOTATIONS_URL,
    })

    manual_train, manual_val = _maybe_prepare_manual_data(dl_manager)
    id_map = _get_category_id_map(data['annotations'] / 'annotations-1.2')

    return {
        tfds.Split.TRAIN: self._generate_examples(
            data_path=data['train'],
            manual_path=manual_train,
            annotations_path=data['annotations']
            / 'annotations-1.2'
            / 'train.json',
            id_map=id_map,
        ),
        tfds.Split.VALIDATION: self._generate_examples(
            data_path=data['val'],
            manual_path=manual_val,
            annotations_path=data['annotations']
            / 'annotations-1.2'
            / 'validation.json',
            id_map=id_map,
        ),
        tfds.Split.TEST: self._generate_examples(
            data_path=data['test'],
            manual_path=None,
            annotations_path=data['annotations']
            / 'annotations-1.2'
            / 'test_without_annotations.json',
            id_map=id_map,
        ),
    }

  def _maybe_resize_video(self, frames_list):
    """Resizes the video depending on the build_config."""
    if self.builder_config.height is None:
      return frames_list  # Don't waste compute loading and resizing.
    resized_images = []
    cv2 = tfds.core.lazy_imports.cv2
    for frame in frames_list:
      with epath.Path(frame).open('rb') as f:
        image = tfds.core.lazy_imports.PIL_Image.open(f).convert('RGB')
        image = np.asarray(image)
      image = cv2.resize(
          image, (self.builder_config.width, self.builder_config.height)
      )
      resized_images.append(image)
    return resized_images

  def _create_metadata(
      self, video_ann: NestedDict, num_frames: int
  ) -> NestedDict:
    """Creates the metadata object for each video data example."""
    metadata = {}
    metadata['num_frames'] = num_frames
    metadata['height'] = self.builder_config.height or video_ann['height']
    metadata['width'] = self.builder_config.width or video_ann['width']
    metadata['neg_category_ids'] = video_ann['neg_category_ids']
    metadata['not_exhaustive_category_ids'] = video_ann[
        'not_exhaustive_category_ids'
    ]
    metadata['dataset'] = video_ann['metadata']['dataset']
    metadata['video_name'] = video_ann['name']
    return metadata

  def _generate_examples(
      self,
      data_path: epath.PathLike,
      manual_path: epath.Path | None,
      annotations_path: epath.Path,
      id_map: dict[str, int],
  ):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam
    annotations = _preprocess_annotations(os.fspath(annotations_path), id_map)
    outs = _build_annotations_index(annotations)
    vids, ann_to_images, track_to_anns, vid_to_tracks = outs

    def _process_example(video_id_and_path):
      """Generate a data example for a single video."""
      # The video_id_and_path are passed together because beam expects
      # a function of a single param (see usage below).
      video_id, path = video_id_and_path
      video_ann = vids[video_id]
      data_example = {}
      frames = self._maybe_resize_video(list(path.iterdir()))
      data_example['video'] = frames
      data_example['metadata'] = self._create_metadata(video_ann, len(frames))
      data_example['tracks'] = []

      for track in vid_to_tracks[video_id]:
        data_example['tracks'].append(
            _create_per_track_annotation(
                track,
                track_to_anns,
                ann_to_images,
                video_ann['height'],
                video_ann['width'],
            )
        )
      return video_ann['name'], data_example

    filtered_ids = []
    for video_id, video_ann in list(vids.items()):
      # These must be manually downloaded.
      is_manual = (
          'HACS' in video_ann['metadata']['dataset']
          or 'AVA' in video_ann['metadata']['dataset']
      )
      if is_manual and manual_path is None:
        continue
      path = (
          (manual_path if is_manual else data_path)
          / 'frames'
          / vids[video_id]['name']
      )
      filtered_ids.append((video_id, path))
    return beam.Create(filtered_ids) | beam.Map(_process_example)
