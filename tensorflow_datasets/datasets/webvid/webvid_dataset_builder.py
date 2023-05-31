# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""WebVid dataset."""

import io
import os
import pathlib
import subprocess
from typing import List

from absl import logging
from etils import epath
import tensorflow_datasets.public_api as tfds

_FFMPEG_TIMEOUT_SECONDS = 20 * 60  # 20 minutes.
_MAX_SECONDS_PER_VIDEO = 10  # Max allowed length for videos.
# Max allowed size of texts. We assume max 64 words for an English average word
# length of 5. It is important to set a limit to this to avoid stragglers in
# t5x processing.
_MAX_TEXT_LENGTH = 5 * 64
_IMG_SIZE = (360, 640)  # height, width.

_TRAIN_CAPTIONS_GLOB: str = 'results_*_train.csv'
_VAL_CAPTIONS_GLOB: str = 'results_*_val.csv'

_CAPTION_KEY: str = 'name'
_PAGE_DIR_KEY: str = 'page_dir'
_VIDEO_ID_KEY: str = 'videoid'
_URL_KEY: str = 'contentUrl'

_NEW_VIDEO_ID_KEY: str = 'new_video_id'
_VIDEO_PATH_KEY: str = 'video_path'

_FPS = 30
_MAX_FRAMES = _MAX_SECONDS_PER_VIDEO * _FPS
_ENCODING_FORMAT = 'jpeg'


def _split_mjpeg_stream(s: bytes) -> List[bytes]:
  """Split a concatenated string of JPEG images into individual images."""
  # Jpeg files start with ffd8 and end with ffd9.
  start = b'\xff\xd8'
  end = b'\xff\xd9'
  if not (s.startswith(start) and s.endswith(end)):
    raise ValueError('Stream does not start and end correctly.')
  # Split by the start delimiter.
  parts = s.split(start)
  # The stream begins with the start delimiter so the first part should be empty
  assert not parts[0]
  # split() removes the delimiter, so add it back in.
  parts = [start + p for p in parts[1:]]
  # Check that each part starts and ends with the correct delimiters,
  # and check that the delimiters never occur elsewhere
  ok = all(
      (
          p.startswith(start)
          and p.endswith(end)
          and p.count(start) == p.count(end) == 1
      )
      for p in parts
  )
  if not ok:
    raise ValueError('Parts do not start and end correctly.')
  return parts


def _ffmpeg_decode_diskless(
    path,
    extra_ffmpeg_input_args,
    extra_ffmpeg_output_args,
    num_target_frames,
    timeout=None,
):
  """Reads a video from a file, without using the disk.

  Args:
    path: File to read the video from.
    extra_ffmpeg_input_args: Additional input arguments / flags for ffmpeg.
    extra_ffmpeg_output_args: Additional output arguments / flags for ffmpeg.
    num_target_frames: If not None, how many frames to return at most.
    timeout: If not None, maximum amount of seconds to use when running ffmpeg.

  Returns:
    Video frames encoded with encoding_format.
  """
  data = epath.Path(path).read_bytes()
  if not data:
    raise ValueError('Empty file.')

  # FFMPEG args: input from pipe.
  args = ['-i', 'pipe:0']
  args.extend(extra_ffmpeg_input_args)
  # output to pipe.
  args += ['-f', 'image2pipe']
  args.extend(extra_ffmpeg_output_args)

  # Extract the specified number of frames (or all frames if num_frames == 0).
  assert num_target_frames is None or (
      isinstance(num_target_frames, int) and num_target_frames >= 0
  )
  if num_target_frames:
    args += ['-frames:v', f'{num_target_frames}']

  # Output to pipe.
  args += ['-']
  output = tfds.core.utils.image_utils.ffmpeg_run(
      args=args, stdin=data, timeout=timeout
  )

  jpegs = _split_mjpeg_stream(output)
  if num_target_frames:
    jpegs = jpegs[:num_target_frames]
  return jpegs


class Builder(tfds.core.GeneratorBasedBuilder):
  """The WebVid dataset builder."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  Follow the download instructions in https://m-bain.github.io/webvid-dataset/
  to get the data. Place the csv files and the video directories in
  `manual_dir/webvid`, such that mp4 files are placed in
  `manual_dir/webvid/*/*_*/*.mp4`.

  First directory typically being an arbitrary part directory (for sharded
  downloading), second directory is the page directory (two numbers around
  underscore), inside of which there is one or more mp4 files.
  """

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  _homepage: str = 'https://m-bain.github.io/webvid-dataset/'
  _description: str = """\
        WebVid is a large-scale dataset of short videos 
        with textual descriptions sourced from the web. 
        The videos are diverse and rich in their content.

        WebVid-10M contains:

        10.7M video-caption pairs.
        52K total video hours.
        """
  _citation: str = """\
  @misc{bain2021frozen,
        title={Frozen in Time: A Joint Video and Image Encoder for End-to-End Retrieval},
        author={Max Bain and Arsha Nagrani and Gül Varol and Andrew Zisserman},
        year={2021},
        eprint={2104.00650},
        archivePrefix={arXiv},
        primaryClass={cs.CV}
  }
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    video_shape = (None,) + _IMG_SIZE + (3,)
    features = {
        'video': tfds.features.Video(
            video_shape, encoding_format=_ENCODING_FORMAT
        ),
        'id': tfds.features.Text(),
        'caption': tfds.features.Text(),
        'url': tfds.features.Text(),
    }

    return tfds.core.DatasetInfo(
        builder=self,
        description=self._description,
        features=tfds.features.FeaturesDict(features),
        supervised_keys=None,
        homepage=self._homepage,
        citation=self._citation,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    def get_captions_path(glob):
      paths = list(epath.Path(dl_manager.manual_dir).glob(glob))
      if len(paths) != 1:
        raise ValueError(
            f'Invalid amount of glob results in {paths} for'
            f' {dl_manager.manual_dir}/{glob}.'
        )
      return paths[0]

    return {
        'train': self._generate_examples(
            captions_csv_path=get_captions_path(_TRAIN_CAPTIONS_GLOB),
            image_base_path=dl_manager.manual_dir,
        ),
        'validation': self._generate_examples(
            captions_csv_path=get_captions_path(_VAL_CAPTIONS_GLOB),
            image_base_path=dl_manager.manual_dir,
        ),
    }

  def _generate_examples(self, captions_csv_path, image_base_path):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam
    pd = tfds.core.lazy_imports.pandas

    ns = 'ProcessExample'
    counter = beam.metrics.Metrics.counter
    total_counter = counter(ns, 'Total')
    process_error_counter = counter(ns, 'Processing error')
    empty_video_counter = counter(ns, 'Empty video')
    timeout_counter = counter(ns, 'Timed out')
    success_counter = counter(ns, 'Success')
    text_cropped_counter = counter(ns, 'Text cropped')

    distribution = beam.metrics.Metrics.distribution
    initial_caption_len_dist = distribution(ns, 'Original caption length')
    final_caption_len_dist = distribution(ns, 'Final caption length')
    frame_count_dist = distribution(ns, 'FrameCount')

    def _load_csv(path):
      # Read all columns as strings, to avoid buggily converting ids with
      # leading zeros into ints.
      return pd.read_csv(
          io.StringIO(epath.Path(path).read_text()),
          sep=',',
          encoding='utf-8',
          dtype='str',
      )

    def _process_example(data_row):
      """Load each video."""
      total_counter.inc()

      file_path = data_row[_VIDEO_PATH_KEY]
      new_video_id = data_row[_NEW_VIDEO_ID_KEY]
      caption = data_row[_CAPTION_KEY]
      url = data_row[_URL_KEY]

      # Read out videos and skip those that don't exist or fail to process.
      height, width = _IMG_SIZE
      extra_input_args = [
          # transform to fps and scale+crop (we must set fps because the input
          # videos don't have consistent fps).
          '-vf',
          f'fps={_FPS},scale={width}:{height}:force_original_aspect_ratio=increase,crop={width}:{height}',  # pylint: disable=line-too-long
          '-sws_flags',
          'lanczos+full_chroma_int+full_chroma_inp+accurate_rnd',
      ]
      extra_output_args = ['-vcodec', 'mjpeg', '-qmin', '1', '-q:v', '2']

      try:
        logging.info('Processing video %s', file_path)

        frames = _ffmpeg_decode_diskless(
            str(file_path),
            extra_ffmpeg_input_args=extra_input_args,
            extra_ffmpeg_output_args=extra_output_args,
            num_target_frames=_MAX_FRAMES,
            timeout=_FFMPEG_TIMEOUT_SECONDS,
        )
      except subprocess.TimeoutExpired as e:
        timeout_counter.inc()
        logging.warning(
            'Timed out while processing %s with exception: %s', file_path, e
        )
        return
      except Exception:  # pylint: disable=broad-except
        process_error_counter.inc()
        logging.exception('Failed to process video %s.', file_path)
        return

      if frames is None:
        empty_video_counter.inc()
        logging.warning('Empty video %s', file_path)
        return

      frame_count_dist.update(len(frames))
      logging.info(
          'Successfully processed %s with original frame count %d',
          file_path,
          len(frames),
      )

      initial_caption_len_dist.update(len(caption))
      if len(caption) > _MAX_TEXT_LENGTH:
        text_cropped_counter.inc()

      features = {
          'id': new_video_id,
          'video': frames[:_MAX_FRAMES],
          'caption': caption[:_MAX_TEXT_LENGTH],
          'url': url,
      }

      final_caption_len_dist.update(len(features['caption']))
      success_counter.inc()
      yield new_video_id, features

    # Get list of videos in file system.
    files = epath.Path(image_base_path).glob(os.path.join('*', '*_*', '*.mp4'))
    df_files = pd.DataFrame(list(files), columns=[_VIDEO_PATH_KEY])
    logging.info('df_files.shape %s', df_files.shape)

    # Read info CSV.
    df_info = _load_csv(captions_csv_path)
    logging.info('df_info.shape %s', df_info.shape)

    def path_to_id(path):
      return os.path.splitext('__'.join(pathlib.Path(path).parts[-2:]))[0]

    # Create base names to join
    df_info[_NEW_VIDEO_ID_KEY] = (
        df_info[_PAGE_DIR_KEY] + '__' + df_info[_VIDEO_ID_KEY]
    )
    df_files[_NEW_VIDEO_ID_KEY] = df_files[_VIDEO_PATH_KEY].map(path_to_id)

    # Merge the two
    df = df_files.merge(df_info, on=_NEW_VIDEO_ID_KEY)

    logging.info('df.shape %s', df.shape)
    logging.info('Number of rows %s', df.shape)
    df = df.to_dict('records')

    return beam.Create(df) | beam.FlatMap(_process_example)
