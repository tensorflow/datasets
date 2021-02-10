# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""youtube-vis dataset."""

import collections
import json
import os
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import tensorflow as tf
import tensorflow_datasets.core.utils.type_utils as type_utils
import tensorflow_datasets.public_api as tfds


_DESCRIPTION = """
Youtube-vis is a video instance segmentation dataset. It contains 2,883
high-resolution YouTube videos, a per-pixel category label set including 40
common objects such as person, animals and vehicles, 4,883 unique video
instances, and 131k high-quality manual annotations.

The YouTube-VIS dataset is split into 2,238 training videos, 302 validation
videos and 343 test videos.

No files were removed or altered during preprocessing.
"""

_CITATION = """
@article{DBLP:journals/corr/abs-1905-04804,
  author    = {Linjie Yang and
               Yuchen Fan and
               Ning Xu},
  title     = {Video Instance Segmentation},
  journal   = {CoRR},
  volume    = {abs/1905.04804},
  year      = {2019},
  url       = {http://arxiv.org/abs/1905.04804},
  archivePrefix = {arXiv},
  eprint    = {1905.04804},
  timestamp = {Tue, 28 May 2019 12:48:08 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1905-04804.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

NestedDict = Dict[str, Any]


def _convert_bbox(box: List[float], height: int, width: int)->List[float]:
  """Converts bbox from coco x,y,w,h to xmin, ymin, xmax, ymax tfds format."""
  return tfds.features.BBox(
      xmin=box[0] / width,
      ymin=box[1] / height,
      xmax=(box[0] + box[2]) / width,
      ymax=(box[1] + box[3]) / height)


def _decode_segmentation(segmentation: Union[List[NestedDict], NestedDict],
                         video: NestedDict, desired_height: int,
                         desired_width: int):
  """Converts the run length encoded segmentation into an image."""
  pycocotools = tfds.core.lazy_imports.pycocotools
  rle = pycocotools.frPyObjects(segmentation, video['height'], video['width'])
  if isinstance(segmentation, list):  # Polygon
    rle = pycocotools.merge(rle)
  segmentation = pycocotools.decode(rle)
  assert segmentation.shape[0] == video['height']
  assert segmentation.shape[1] == video['width']
  if video['height'] != desired_height or video['width'] != desired_width:
    cv2 = tfds.core.lazy_imports.cv2
    segmentation = cv2.resize(segmentation, (desired_width, desired_height),
                              interpolation=cv2.INTER_NEAREST)
  segmentation = np.expand_dims(segmentation, axis=-1)
  assert len(segmentation.shape) == 3
  return segmentation


def _find_frame_index(frame_filename: str,
                      all_video_frame_paths: List[type_utils.PathLike])->int:
  for index, path in enumerate(all_video_frame_paths):
    if frame_filename in os.fspath(path):
      return index
  assert False, (f'Annotations are corrupt or videos have not been properly '
                 f'downloaded. File {frame_filename} not found in '
                 f'{all_video_frame_paths}.')


def _create_per_track_annotation(
    video: NestedDict,
    all_video_frame_paths: List[type_utils.PathLike],
    track_annotation: NestedDict,
    desired_height: Optional[int] = None,
    desired_width: Optional[int] = None) -> NestedDict:
  """Creates an anntation for a single object track.

  Args:
    video: The annotation for the video containing metadata info.
    all_video_frame_paths: List of all the frames belonging to the video.
    track_annotation: The annotation for a single object track in the video.
    desired_height: The height the video will be resized to. If None, no
      resizing occurs.
    desired_width: The width the video will be resized to. If None, no resizing.
      occurs.
  Returns:
    A data entry for a single object track for the video.
  """
  assert video['id'] == track_annotation['video_id']
  height = desired_height or video['height']
  width = desired_width or video['width']
  per_track_anno = {}

  per_track_anno['bboxes'] = []  # Temporally ordered bounding boxes for track.
  per_track_anno['frames'] = []  # List of frames the track appears on.
  frames_with_labels = []
  for frame_idx, box in enumerate(track_annotation['bboxes']):
    if box is None:
      continue
    frames_with_labels.append(frame_idx)
    per_track_anno['bboxes'].append(_convert_bbox(box, video['height'],
                                                  video['width']))
    # all_video_frame_paths is a superset of the annotated frames, and we
    # need to convert the index into the annotated frames to an index into
    # all_video_frame_paths.
    per_track_anno['frames'].append(
        _find_frame_index(video['file_names'][frame_idx],
                          all_video_frame_paths))
  frames_with_labels = set(frames_with_labels)

  per_track_anno['segmentations'] = []  # Temporally ordered segmentations.
  for frame_idx, segmentation in enumerate(track_annotation['segmentations']):
    if segmentation is None:
      assert frame_idx not in frames_with_labels
      continue
    per_track_anno['segmentations'].append(
        _decode_segmentation(segmentation, video, height, width))
    assert frame_idx in frames_with_labels

  per_track_anno['areas'] = []  # List of per-pixel segmentation areas.
  for frame_idx, area in enumerate(track_annotation['areas']):
    if area is None:
      assert frame_idx not in frames_with_labels
      continue
    size_ratio = float(video['height'] * video['width']) / (height * width)
    area = int(size_ratio * area)
    per_track_anno['areas'].append(area)
    assert frame_idx in frames_with_labels

  # TFDS ids are zero indexed whereas youtube-vis ids are not.
  per_track_anno['category'] = track_annotation['category_id'] - 1
  per_track_anno['is_crowd'] = track_annotation['iscrowd']

  return per_track_anno


def _create_metadata(video: NestedDict, height: int, width: int,
                     num_frames: int)->NestedDict:
  """Creates the metadata entry for a video."""

  metadata = {}
  metadata['height'] = height or video['height']
  metadata['width'] = width or video['width']
  metadata['num_frames'] = num_frames
  metadata['video_name'] = video['file_names'][0].split('/')[0]
  return metadata


def _build_annotations_index(
    annotations: NestedDict
) -> Tuple[Dict[int, List[NestedDict]], Dict[int, NestedDict]]:
  """Builds some indices to make data generation more convenient."""
  video_id_to_annos = collections.defaultdict(list)
  videos = {}
  if 'annotations' in annotations:
    for anno in annotations['annotations']:
      video_id_to_annos[anno['video_id']].append(anno)
  else:  # Testing or validation data contains no annotations.
    video_id_to_annos = {v['id']: [] for v in annotations['videos']}
  videos = {v['id']: v for v in annotations['videos']}
  return video_id_to_annos, videos


class YoutubeVisConfig(tfds.core.BuilderConfig):
  """"Configuration for Youtube-vis video instance segmentation dataset.

  Attributes:
    height: An optional integer height to resize all videos to. If None,
      no resizing will occur.
    width: An optional integer width to resize all videos to. If None,
      no resizing will occur.
    only_frames_with_labels: A bool indicating whether we should include
      only frames which have labels (True) or whether all frames,
      including those without labels, should be included (False).
  """

  def __init__(self,
               *,
               height: Optional[int] = None,
               width: Optional[int] = None,
               only_frames_with_labels: bool = False,
               **kwargs):
    """The parameters specifying how the dataset will be processed.

    This allows the option to preprocess the images to a smaller fixed
    resolution. If height and width are left as None, the native size
    will be used. It also allows dropping all frames which don't include
    labels.

    Args:
      height: optional height to resize all images to
      width: optional width to resize all images to
      only_frames_with_labels: whether or not to include the frames
        which don't have labels in the data export.
      **kwargs: Passed on to the constructor of `BuilderConfig`.
    """
    super(YoutubeVisConfig, self).__init__(**kwargs)
    if height is not None or width is not None:
      if height is None or width is None:
        raise ValueError('Provide either both height and width or None.')
    self.height = height
    self.width = width
    self.only_frames_with_labels = only_frames_with_labels


class YoutubeVis(tfds.core.BeamBasedBuilder):
  """DatasetBuider for Youtube-vis dataset."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  Please download all files for the 2019 version of the dataset
  (test_all_frames.zip, test.json, train_all_frames.zip, train.json,
  valid_all_frames.zip, valid.json) from the youtube-vis website
  and move them to ~/tensorflow_datasets/downloads/manual/.

  Note that the dataset landing page is located at
  https://youtube-vos.org/dataset/vis/, and it will then redirect you to a page
  on https://competitions.codalab.org where you can download the 2019 version
  of the dataset. You will need to make an account on codalab to download the
  data. Note that at the time of writing this, you will need to bypass a
  "Connection not secure" warning when accessing codalab.
  """
  BUILDER_CONFIGS = [
      YoutubeVisConfig(
          name='full',
          description='The full resolution version of the dataset, with all '
          'frames, including those without labels, included.',
      ),
      YoutubeVisConfig(
          name='480_640_full',
          description='All images are bilinearly resized to 480 X 640 with all '
                      'frames included.',
          height=480,
          width=640,
      ),
      YoutubeVisConfig(
          name='480_640_only_frames_with_labels',
          description='All images are bilinearly resized to 480 X 640 with only'
                      ' frames with labels included.',
          height=480,
          width=640,
          only_frames_with_labels=True,
      ),
      YoutubeVisConfig(
          name='only_frames_with_labels',
          description='Only images with labels included at their native '
                      'resolution.',
          only_frames_with_labels=True,
      ),
  ]
  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    names_file = tfds.core.tfds_path('video/youtube_vis/labels.txt')
    video_shape = (
        None, self.builder_config.height, self.builder_config.width, 3)
    seg_shape = (
        None, self.builder_config.height, self.builder_config.width, 1)
    all_features = {
        'video': tfds.features.Video(video_shape),
        'metadata': {
            'height':
                tf.int32,
            'width':
                tf.int32,
            'num_frames':
                tf.int32,
            'video_name':
                tf.string,
        },
        'tracks':
            tfds.features.Sequence({
                'bboxes': tfds.features.Sequence(tfds.features.BBoxFeature()),
                'segmentations': tfds.features.Video(seg_shape,
                                                     use_colormap=True),
                'category': tfds.features.ClassLabel(names_file=names_file),
                'is_crowd': tf.bool,
                'areas': tfds.features.Sequence(tf.float32),
                # Labels do not occur for all frames. This indicates the
                # indices of the frames that have labels.
                'frames': tfds.features.Sequence(tf.int32)
            })
    }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(all_features),
        supervised_keys=None,
        homepage='https://youtube-vos.org/dataset/vis/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    manually_downloaded_files = {
        'test_all_frames': dl_manager.manual_dir / 'test_all_frames.zip',
        'test_annotations': dl_manager.manual_dir / 'test.json',
        'train_all_frames': dl_manager.manual_dir / 'train_all_frames.zip',
        'train_annotations': dl_manager.manual_dir / 'train.json',
        'valid_all_frames': dl_manager.manual_dir / 'valid_all_frames.zip',
        'valid_annotations': dl_manager.manual_dir / 'valid.json',
    }

    extracted_files = dl_manager.extract(manually_downloaded_files)

    return {
        tfds.Split.TRAIN:
            self._generate_examples(
                annotations=extracted_files['train_annotations'],
                all_frames=extracted_files['train_all_frames'] /
                'train_all_frames' / 'JPEGImages',
            ),
        tfds.Split.VALIDATION:
            self._generate_examples(
                annotations=extracted_files['valid_annotations'],
                all_frames=extracted_files['valid_all_frames'] /
                'valid_all_frames' / 'JPEGImages',
            ),
        tfds.Split.TEST:
            self._generate_examples(
                annotations=extracted_files['test_annotations'],
                all_frames=extracted_files['test_all_frames'] /
                'test_all_frames' / 'JPEGImages',
            ),
    }

  def _maybe_resize_video(self, frames_list):
    """Resizes the video depending on the build_config."""
    if self.builder_config.height is None:
      return frames_list  # Don't waste compute loading and resizing.
    resized_images = []
    cv2 = tfds.core.lazy_imports.cv2
    for frame in frames_list:
      with tf.io.gfile.GFile(frame, 'rb') as f:
        image = tfds.core.lazy_imports.PIL_Image.open(f).convert('RGB')
        image = np.asarray(image)
      image = cv2.resize(image, (self.builder_config.width,
                                 self.builder_config.height))
      resized_images.append(image)
    return resized_images

  def _generate_examples(self, annotations, all_frames):
    beam = tfds.core.lazy_imports.apache_beam
    annotations = json.loads(annotations.read_text())
    video_id_to_tracks, videos = _build_annotations_index(annotations)
    height = self._builder_config.height
    width = self._builder_config.width
    only_frames_with_labels = self._builder_config.only_frames_with_labels
    data_example = {}

    def _frame_index(frame_filename):
      """Convert a video frame filename into a numerical index."""
      basename = os.path.basename(os.fspath(frame_filename))
      return int(basename.split('.')[0])

    def _process_example(video_id):
      """Process a single video into a data example."""
      video = videos[video_id]
      if only_frames_with_labels:
        frames_list = [all_frames / file for file in video['file_names']]
      else:
        video_dir = os.path.dirname(video['file_names'][0])
        video_directory = all_frames / video_dir
        frames_list = list(video_directory.glob('*'))
      frames_list = sorted(frames_list, key=_frame_index)
      data_example['metadata'] = _create_metadata(video, height, width,
                                                  len(frames_list))
      data_example['tracks'] = []
      track_annotations = video_id_to_tracks[video_id]
      for track in track_annotations:
        data_example['tracks'].append(
            _create_per_track_annotation(video, frames_list, track,
                                         height, width))
      data_example['video'] = self._maybe_resize_video(frames_list)
      return data_example['metadata']['video_name'], data_example

    return beam.Create(list(videos.keys())) | beam.Map(_process_example)
