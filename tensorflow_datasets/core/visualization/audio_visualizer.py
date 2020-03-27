""" Audio Visualization
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np 
import IPython.display

from absl import logging

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.visualization import visualizer

class AudioGridVisualizer(visualizer.Visualizer): 
  def match(self, ds_info):
     audio_keys = visualizer.extract_keys(ds_info.features, features_lib.Audio)
    if audio_keys:
      return true 
    return false
      

  def show(
      self,
      ds_info,
      ds,
      rows=3,
      cols=3,
      plot_scale=3.,
      image_key=None,
  ):
    """Display the dataset.

      Args:
        ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
        ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
          should not be batched. Examples will be consumed in order until
          (rows * cols) are read or the dataset is consumed.
        rows: `int`, number of rows of the display grid.
        cols: `int`, number of columns of the display grid.
        plot_scale: `float`, controls the plot size of the images. Keep this
          value around 3 to get a good plot. High and low values may cause
          the labels to get overlapped.
        image_key: `string`, name of the feature that contains the image. If not
          set, the system will try to auto-detect it.
      """
    key = audio_keys[0]
    audio_samples = []

    samplerate = 16000
    for features in ds:
        audio_samples.append(features[key].numpy())
    to_gen = []
    for _ in range(4):
      value = randint(0, len(audio_samples))
      to_gen.append(audio_samples[value])

    t1 = 0
    t2 = 100 * 1000
    for audio in to_gen:
      newAudio = audio[t1:t2]
      IPython.display.Audio(newAudio,rate=samplerate) 

    fig, a = plt.subplots(2, 2)

    a[0][0].plot(to_gen[0])
    a[0][1].plot(to_gen[1])
    a[1][0].plot(to_gen[2])
    a[1][1].plot(to_gen[3])
    plt.show()
    return fig
