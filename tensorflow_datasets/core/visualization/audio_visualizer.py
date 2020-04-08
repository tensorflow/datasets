""" Audio Visualizer."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.visualization import visualizer

def _make_audio_grid(ds, key, samplerate, rows, cols, plot_scale):
  """Plot the waveforms and IPython objects of some samples of the argument audio dataset

  Args:
    ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize.
    key: The inferred key for the dataset
    samplerate : Inferred samplerate of the dataset.
    rows: `int`, number of rows of the display grid.
    cols: `int`, number of columns of the display grid.
    plot_scale: `float`, controls the plot size of the images. Keep this
      value around 3 to get a good plot. High and low values may cause
      the labels to get overlapped.
  Returns:
    fig: Waveform figure to display. IPython objects are not returned. 
  """
  import IPython.display as ipd
  plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot

  num_examples = rows * cols
  examples = list(dataset_utils.as_numpy(ds.take(num_examples)))

  fig = plt.figure(figsize=(plot_scale * cols, plot_scale * rows))
  fig.subplots_adjust(hspace=1 / plot_scale, wspace=1 / plot_scale)
  t1 = 0
  t2 = 100 * 1000

  for i, ex in enumerate(examples):
    ax = fig.add_subplot(rows, cols, i+1)
    ax.plot(ex[key])
    audio = ex['audio']
    newaudio = audio[t1:t2]
    ipd.display(ipd.Audio(newaudio, rate=samplerate))


  plt.show()
  return fig


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
        rows: `int`, number of rows of the display grid : Default is 2.
        cols: `int`, number of columns of the display grid : Default is 2.
        plot_scale: `float`, controls the plot size of the images. Keep this
        value around 3 to get a good plot. High and low values may cause
        the labels to get overlapped.
        audio_key: `string`, name of the feature that contains the audio. If not
          set, the system will try to auto-detect it.
      """
    if not audio_key:
      #Auto inferring the audio key
      audio_keys = visualizer.extract_keys(ds_info.features, features_lib.Audio)
    key = audio_keys[0]
    # Identifying the sample rate  If None - 16000KHz is used as default
    samplerate = ds_info.features[key].sample_rate
    if not samplerate:
      samplerate = 16000
    _make_audio_grid(ds, key, samplerate, rows, cols, plot_scale)
    
