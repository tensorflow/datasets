""" Audio Visualizer."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random

from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.visualization import visualizer


class AudioGridVisualizer(visualizer.Visualizer):
  """ Fixed grid Visualizer for audio datasets."""
  def match(self, ds_info):
    """ See base class."""
    audio_keys = visualizer.extract_keys(ds_info.features, features_lib.Audio)
    return len(audio_keys) > 0

  def show(
      self,
      ds_info,
      ds,
      rows=2,
      cols=2,
      plot_scale=3.,
      audio_key=None,
  ):
    """Display the audio dataset.

      Args:
        ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
        ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize.
        rows: `int`, number of rows of the display grid : Default is 2.Does not
        support user defined input as of now.
        cols: `int`, number of columns of the display grid : Default is 2.Does
        not support user defined input as of now.
        plot_scale: `float`, controls the plot size of the images. Not used for
        audio grid plots.
        audio_key: `string`, name of the feature that contains the audio. If not
          set, the system will try to auto-detect it.
      """
    import IPython.display as ipd
    if not audio_key:
      #Auto inferring the audio key
      audio_keys = visualizer.extract_keys(ds_info.features, features_lib.Audio)
    key = audio_keys[0]
    audio_samples = []

    samplerate = 16000
    for features in ds:
      audio_samples.append(features[key].numpy())
    to_gen = []
    for _ in range(4):
      value = random.randint(0, len(audio_samples))
      to_gen.append(audio_samples[value])
    t1 = 0
    t2 = 100 * 1000
    for audio in to_gen:
      audio = audio[t1:t2]
      ipd.display(ipd.Audio(audio, rate=samplerate))
    plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot
    fig, a = plt.subplots(2, 2)
    a[0][0].plot(to_gen[0])
    a[0][1].plot(to_gen[1])
    a[1][0].plot(to_gen[2])
    a[1][1].plot(to_gen[3])
    plt.show()
    return fig
