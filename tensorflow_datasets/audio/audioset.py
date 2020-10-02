"""audioset dataset."""

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import tensorflow_io as tfio
import os
import json
import numpy as np
from multiprocessing import Pool
# TODO(audioset): BibTeX citation
_CITATION = """
"""

# TODO(audioset):
_DESCRIPTION = """
"""
"""Audio feature."""

class Audioset(tfds.core.GeneratorBasedBuilder):
    """TODO(audioset): Short description of my dataset."""

  # TODO(audioset): Set up version.
    VERSION = tfds.core.Version('0.1.0')
    MANUAL_DOWNLOAD_INSTRUCTIONS = 'give bucket path gs://bme590/william/manual'
    def _info(self):
        # TODO(audioset): Specifies the tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # tfds.features.FeatureConnectors
            features=tfds.features.FeaturesDict({
                'audio': tfds.features.Tensor(shape=(None,1), dtype=tf.float32),
                'label': tfds.features.Tensor(shape=(527,), dtype=tf.int32)
                # These are the features of your dataset like images, labels ...
            }),
            # If there's a common (input, target) tuple from the features,
            # specify them here. They'll be used if as_supervised=True in
            # builder.as_dataset.
            supervised_keys=('audio','label'),
            # Homepage of the dataset for documentation
            homepage='https://dataset-homepage/',
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        # TODO(audioset): Downloads the data and defines the splits
        # dl_manager is a tfds.download.DownloadManager that can be used to
        # download and extract URLs
        data_dir = dl_manager.manual_dir

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    'data_dir': data_dir
                },
            ),
        ]


        
    def _generate_examples(self, data_dir=None):
        """Yields examples."""
        my_files = tf.io.gfile.listdir(os.path.join(data_dir, 'trimmed_audio')) #gets list of files in folder given
        with tf.io.gfile.GFile(os.path.join(data_dir, 'id2label.json'), "r") as read_file: #uses json to match ids to labels
            datas = json.load(read_file)
        
        for f in my_files:
            try:
                label_list = []
                filepath = os.path.join(data_dir,'trimmed_audio',f)
                audio_binary = tf.io.read_file(filepath)
                audio_tensor = tfio.audio.decode_mp3(audio_binary) #audio_tensor read and decoded
                ids = f.replace(".mp3","")
                for x in datas[ids]:
                    indices_list = []
                    for y in x:
                        label_list.append(y) #gets multiple labels that apply to audio in a list in label_list
                    for i in label_list:
                        indice = []
                        indice.append(i)
                        indices_list.append(indice)
                    indices = tf.constant(indices_list, dtype=tf.int32)
                    updates = tf.ones(len(indices_list), dtype=tf.int32)
                    label_tensor = tf.zeros(527, dtype=tf.int32)
                    label_tensor = tf.tensor_scatter_nd_add(label_tensor, indices, updates) # creates a tensor of zeros with ones at indices that indicate positive for a label
                    break
                yield f, {
                    'audio': audio_tensor,
                    'label': label_tensor,
                }
            except:
                pass
    

