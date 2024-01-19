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

"""Utilities to manipulate images.

Note: these functions are not meant to be used inside of a TF graph.
"""
from __future__ import annotations

import csv
import subprocess
from typing import Any, List, Optional

import numpy as np
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import resource_utils
from tensorflow_datasets.core.utils import tf_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

PilImage = Any  # Require lazy deps.
THUMBNAIL_SIZE = 128


@py_utils.memoize()
def _get_runner():
  return tf_utils.TFGraphRunner()


def decode_image(image_bytes: bytes) -> np.ndarray:
  """Returns np.array corresponding to encoded image."""
  runner = _get_runner()
  return runner.run(tf.image.decode_image, image_bytes)


def png_to_jpeg(image_bytes: bytes, quality: int = 100) -> bytes:
  """Converts PNG image (bytes or str) to JPEG (bytes)."""
  runner = _get_runner()
  decode_fn = lambda img: tf.image.decode_png(img, channels=3)
  image = runner.run(decode_fn, image_bytes)
  fn = lambda img: tf.image.encode_jpeg(img, format='rgb', quality=quality)
  return runner.run(fn, image)


def jpeg_cmyk_to_rgb(image_bytes: bytes, quality: int = 100) -> bytes:
  """Converts JPEG CMYK image (bytes) to RGB JPEG (bytes)."""
  runner = _get_runner()
  image = runner.run(tf.image.decode_jpeg, image_bytes)
  fn = lambda img: tf.image.encode_jpeg(img, format='rgb', quality=quality)
  return runner.run(fn, image)


def ffmpeg_run(
    args: List[str],
    stdin: Optional[bytes] = None,
    timeout: Optional[int] = None,
) -> bytes:
  """Executes the ffmpeg function.

  Args:
    args: A list of string args and flags to send to the ffmpeg binary.
    stdin: Bytes to provide as standard input, or None.
    timeout: Maximum amount of seconds to wait for, before interrupting the
      command. None to wait forever.

  Returns:
    The stdout output.
  """
  ffmpeg_path = 'ffmpeg'
  try:
    cmd_args = [ffmpeg_path] + args
    return subprocess.run(
        cmd_args,
        check=True,
        input=stdin,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    ).stdout
  except subprocess.CalledProcessError as e:
    raise ValueError(
        f'Command {e.cmd} returned error code {e.returncode}:\n'
        f'stdout={e.stdout.decode("utf-8")}\n'
        f'stderr={e.stderr.decode("utf-8")}\n'
    ) from e
  except FileNotFoundError as e:
    raise FileNotFoundError(
        'It seems that ffmpeg is not installed on the system. Please follow '
        'the instrutions at https://ffmpeg.org/. '
        f'Original exception: {e}'
    ) from e


@py_utils.memoize()
def get_colormap() -> np.ndarray:
  """Loads the colormap.

  The colormap was precomputed using Glasbey et al. algorythm (Colour Displays
  for Categorical Images, 2017) to generate maximally distinct colors.

  It was generated using https://github.com/taketwo/glasbey:

  ```python
  gb = glasbey.Glasbey(
      base_palette=[(0, 0, 0), (228, 26, 28), (55, 126, 184), (77, 175, 74)],
      no_black=True,
  )
  palette = gb.generate_palette(size=256)
  gb.save_palette(palette, 'colormap.csv')
  ```

  Returns:
    colormap: A `np.array(shape=(255, 3), dtype=np.uint8)` representing the
      mapping id -> color.
  """
  colormap_path = resource_utils.tfds_path() / 'core/utils/colormap.csv'
  with colormap_path.open() as f:
    return np.array(list(csv.reader(f)), dtype=np.uint8)


def apply_colormap(image: np.ndarray) -> np.ndarray:
  """Apply colormap from grayscale (h, w, 1) to colored (h, w, 3) image."""
  image = image.squeeze(axis=-1)  # (h, w, 1) -> (h, w)
  cmap = get_colormap()  # Get the (256, 3) colormap
  # Normalize uint16 and convert each value to a unique color
  return cmap[image % len(cmap)]


# Visualization single image


def _postprocess_noop(img: PilImage) -> PilImage:
  return img


def _postprocess_convert_rgb(img: PilImage) -> PilImage:
  return img.convert('RGB')


def create_thumbnail(
    ex: np.ndarray, *, use_colormap: bool, default_dimensions: bool = True
) -> PilImage:
  """Creates the image from the np.array input."""
  PIL_Image = lazy_imports_lib.lazy_imports.PIL_Image  # pylint: disable=invalid-name

  if use_colormap:  # Apply the colormap first as it modify the shape/dtype
    ex = apply_colormap(ex)

  _, _, c = ex.shape
  postprocess = _postprocess_noop
  if c == 1:
    ex = ex.squeeze(axis=-1)
    mode = 'L'
  elif ex.dtype == np.uint16:
    mode = 'I;16'
    postprocess = _postprocess_convert_rgb
  else:
    mode = None
  img = PIL_Image.fromarray(ex, mode=mode)
  img = postprocess(img)
  if default_dimensions:
    img.thumbnail((THUMBNAIL_SIZE, THUMBNAIL_SIZE))  # Resize the image in-place
  return img
