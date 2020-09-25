"""audioset dataset."""

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
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
def process_examples(my_files, datas ,data_dir=None):
    try:
        label_list = []
        filepath = os.path.join(data_dir,'trimmed_audio',f)
        audio_binary = tf.io.read_file(filepath)
        audio_tensor = tfio.audio.decode_mp3(audio_binary)
        
        ids = my_files.replace(".mp3","")
        for x in datajson[ids]:
            for y in x:
                label_list.append(y)
            label_tensor=np.zeros(527, dtype=np.int16)
            for i in label_list:
                label_tensor[i] = 1
            label_tensor = tf.convert_to_tensor(label_tensor,dtype=tf.int16)
            break
        yield filepath, {
            'audio': audio_tensor,
            'label': label_tensor
        }
    except:
        pass

class Audioset(tfds.core.GeneratorBasedBuilder):
    """TODO(audioset): Short description of my dataset."""

  # TODO(audioset): Set up version.
    VERSION = tfds.core.Version('0.1.0')
    MANUAL_DOWNLOAD_INSTRUCTIONS = 'give bucket path bme590/william/manual'
    def _info(self):
        # TODO(audioset): Specifies the tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # tfds.features.FeatureConnectors
            features=tfds.features.FeaturesDict({
                'audio': tfds.features.Tensor(shape=(None,1),dtype=tf.float32),
                'label': tfds.features.Tensor(shape=(527,),dtype=tf.int16),
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
        # TODO(audioset): Yields (key, example) tuples from the dataset

        my_files = tf.io.gfile.listdir(os.path.join(data_dir, 'trimmed_audio'))
        with open(os.path.join(data_dir, 'id2label.json'), "r") as read_file:
            datas = json.load(read_file)
#         with Pool(12) as p:
#             p.map(process_examples, my_files, datas, data_dir) #multiprocessing
        
        for f in my_files:
            try:
                label_list = []
                filepath = os.path.join(data_dir,'trimmed_audio',f)
                audio_binary = tf.io.read_file(filepath)
                audio_tensor = tfio.audio.decode_mp3(audio_binary)
                ids = f.replace(".mp3","")
                for x in datas[ids]:
                    for y in x:
                        label_list.append(y)
                    label_tensor=np.zeros(527, dtype=np.int16)
                    for i in label_list:
                        label_tensor[i] = 1
                    label_tensor = tf.convert_to_tensor(label_tensor,dtype=tf.int16)
                    break
                yield f, {
                    'audio': audio_tensor,
                    'label': label_tensor
                }
            except:
                pass
    

