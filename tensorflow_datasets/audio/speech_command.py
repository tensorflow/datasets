"""Speech Command Dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import re
import hashlib
import os
import tensorflow_datasets as tfds
import tensorflow as tf
from tensorflow.python.ops import io_ops
from tensorflow.python.util import compat

_CITATION = """
@article{warden2018speech,
  title={Speech commands: A dataset for limited-vocabulary speech recognition},
  author={Warden, Pete},
  journal={arXiv preprint arXiv:1804.03209},
  year={2018}
}
"""

_DESCRIPTION = """
Speech Command is a audio dataset of spoken words designed to help train and evaluate keyword spotting
systems. Speech Command consist of a set of one-second .wav audio files, each containing a single spoken
English word. These words are from a small set of commands, and are spoken by a
variety of different speakers. The audio files are organized into folders based
on the word they contain, and this data set is designed to help train simple
machine learning models. The data set contains 105,829 audio files in total.
"""

_URL = "https://arxiv.org/abs/1804.03209"
_DL_URL = "https://storage.googleapis.com/download.tensorflow.org/data/speech_commands_v0.02.tar.gz"
MAX_NUM_WAVS_PER_CLASS = 2 ** 27 - 1  # ~134M
VALIDATION_PERCENTAGE = 10
TESTING_PERCENTAGE = 10
_SAMPLE_LENGTH = 16000


class SpeechCommand(tfds.core.GeneratorBasedBuilder):
    """Speech Command is a audio dataset of spoken words designed to help train and evaluate keyword spotting
  systems."""

    VERSION = tfds.core.Version('0.2.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "audio": tfds.features.Tensor(
                        shape=(
                            _SAMPLE_LENGTH,
                        ),
                        dtype=tf.float32),
                    "speaker_id": tf.string,
                    "label": tfds.features.ClassLabel(
                        names=[
                            'backward',
                            'bed',
                            'bird',
                            'cat',
                            'dog',
                            'down',
                            'eight',
                            'five',
                            'follow',
                            'forward',
                            'four',
                            'go',
                            'happy',
                            'house',
                            'learn',
                            'left',
                            'marvin',
                            'nine',
                            'no',
                            'off',
                            'on',
                            'one',
                            'right',
                            'seven',
                            'sheila',
                            'six',
                            'stop',
                            'three',
                            'tree',
                            'two',
                            'up',
                            'visual',
                            'wow',
                            'yes',
                            'zero']),
                }),
            supervised_keys=(
                "speech",
                "label"),
            urls=[_URL],
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        extracted_dirs = dl_manager.download_and_extract(_DL_URL)
        print(_DL_URL)
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={
                    "dirs": extracted_dirs,
                    "par": 'training'
                }),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                gen_kwargs={
                    "dirs": extracted_dirs,
                    "par": 'validation'
                }),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={
                    "dirs": extracted_dirs,
                    "par": 'testing'
                }),
        ]

    def _generate_examples(self, dirs, par):
        """Yields examples."""
        if not os.path.exists(dirs):
            return
        numerator = 0
        for _, directories, _ in os.walk(dirs):
            for dir in directories:
                for file in os.listdir(os.path.join(dirs, dir)):
                    if '_background_noise_' in dir:
                        continue
                    if par == which_set(file):
                        record = {
                            "audio": load_wav_file(
                                os.path.join(
                                    dirs,
                                    dir,
                                    file)),
                            "speaker_id": file.split('_')[0],
                            "label": dir}
                        numerator += 1
                        yield numerator, record


def load_wav_file(filename):
    """Loads an audio file and returns a float PCM-encoded array of samples.
        This function is from the dataset github page:
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/speech_commands/input_data.py
    Args:
      filename: Path to the .wav file to load.
    Returns:
      Numpy array holding the sample data as floats between -1.0 and 1.0.
    """
    with tf.compat.v1.Session(graph=tf.Graph()) as sess:
        wav_filename_placeholder = tf.compat.v1.placeholder(tf.string, [])
        wav_loader = io_ops.read_file(wav_filename_placeholder)
        wav_decoder = tf.audio.decode_wav(
            wav_loader, desired_channels=1, desired_samples=16000)
        return sess.run(
            wav_decoder,
            feed_dict={wav_filename_placeholder: filename}).audio.flatten()


def which_set(
        filename,
        validation_percentage=VALIDATION_PERCENTAGE,
        testing_percentage=TESTING_PERCENTAGE):
    """Determines which data partition the file should belong to.

    This function is from the dataset github page:
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/speech_commands/input_data.py

    We want to keep files in the same training, validation, or testing sets even
    if new ones are added over time. This makes it less likely that testing
    samples will accidentally be reused in training when long runs are restarted
    for example. To keep this stability, a hash of the filename is taken and used
    to determine which set it should belong to. This determination only depends on
    the name and the set proportions, so it won't change as other files are added.
    It's also useful to associate particular files as related (for example words
    spoken by the same person), so anything after '_nohash_' in a filename is
    ignored for set determination. This ensures that 'bobby_nohash_0.wav' and
    'bobby_nohash_1.wav' are always in the same set, for example.
    Args:
      filename: File path of the data sample.
      validation_percentage: How much of the data set to use for validation.
      testing_percentage: How much of the data set to use for testing.
    Returns:
      String, one of 'training', 'validation', or 'testing'.
    """
    base_name = os.path.basename(filename)
    # We want to ignore anything after '_nohash_' in the file name when
    # deciding which set to put a wav in, so the data set creator has a way of
    # grouping wavs that are close variations of each other.
    hash_name = re.sub(r'_nohash_.*$', '', base_name)
    # This looks a bit magical, but we need to decide whether this file should
    # go into the training, testing, or validation sets, and we want to keep
    # existing files in the same set even if more files are subsequently
    # added.
    # To do that, we need a stable way of deciding based on just the file name
    # itself, so we do a hash of that and then use that to generate a
    # probability value that we use to assign it.
    hash_name_hashed = hashlib.sha1(compat.as_bytes(hash_name)).hexdigest()
    percentage_hash = ((int(hash_name_hashed, 16) %
                        (MAX_NUM_WAVS_PER_CLASS + 1)) *
                       (100.0 / MAX_NUM_WAVS_PER_CLASS))
    if percentage_hash < validation_percentage:
        result = 'validation'
    elif percentage_hash < (testing_percentage + validation_percentage):
        result = 'testing'
    else:
        result = 'training'
    return result
