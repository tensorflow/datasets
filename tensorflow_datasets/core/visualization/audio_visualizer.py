""" Audio Visualization
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.visualization import visualizer


def show_examples(ds_info, ds, rows=3, cols=3, plot_scale=3., image_key=None):
  """Visualize delimited audio objects and waveform plots of audio datasets under tfds. 
  Usage:
  ```python
  ds, ds_info = tfds.load('groove', split='train', with_info=True)
  fig = tfds.show_examples(ds_info, ds)
  ```
  Args:
    ds_info: The dataset info object to which extract the features
      info. Available either through `tfds.load('groove', with_info=True)` or
      `tfds.builder('groove').info`
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
  Returns:
    fig: The `matplotlib.Figure` object
  """
  plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot
  audio_keys = [
      k for k, feature in ds_info.features.items()
      if isinstance(feature, features_lib.Audio)
          ]
  
  # if not audio_keys:
  #   raise ValueError(
  #       "Visualisation not supported for dataset `{}`. Was not able to "
  #       "auto-infer audio dataset.".format(ds_info.name))

    # if len(image_keys) > 1:
    #   raise ValueError(
    #       "Multiple image features detected in the dataset. Using the first one. You can "
    #       "use `image_key` argument to override. Images detected: %s" %
    #       (",".join(image_keys)))

  key = audio_keys[0]

  # label_keys = [
  #     k for k, feature in ds_info.features.items()
  #     if isinstance(feature, features_lib.ClassLabel)
  # ]

  # label_key = label_keys[0] if len(label_keys) == 1 else None
  # if not label_key:
  #   logging.info("Was not able to auto-infer label.")

  # num_examples = rows * cols
  # examples = list(dataset_utils.as_numpy(ds.take(num_examples)))

  # fig = plt.figure(figsize=(plot_scale*cols, plot_scale*rows))
  # fig.subplots_adjust(hspace=1/plot_scale, wspace=1/plot_scale)
  # for i, ex in enumerate(examples):
  #   if not isinstance(ex, dict):
  #     raise ValueError(
  #         "tfds.show_examples requires examples as `dict`, with the same "
  #         "structure as `ds_info.features`. It is currently not compatible "
  #         "with `as_supervised=True`. Received: {}".format(type(ex)))
  #   ax = fig.add_subplot(rows, cols, i+1)

  #   # Plot the image
  #   image = ex[image_key]
  #   if len(image.shape) != 3:
  #     raise ValueError(
  #         "Image dimension should be 3. tfds.show_examples does not support "
  #         "batched examples or video.")
  #   _, _, c = image.shape
  #   if c == 1:
  #     image = image.reshape(image.shape[:2])
  #   ax.imshow(image, cmap="gray")
  #   ax.grid(False)
  #   plt.xticks([], [])
  #   plt.yticks([], [])

  #   # Plot the label
  #   if label_key:
  #     label = ex[label_key]
  #     label_str = ds_info.features[label_key].int2str(label)
  #     plt.xlabel("{} ({})".format(label_str, label))
  #   plt.show()
  #   return fig
  if audio_keys:
    audio_samples = []
    # if(ds_info.name == 'ljspeech'):
    #   key = 'speech'
    # else:
    #   key = 'audio'

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
