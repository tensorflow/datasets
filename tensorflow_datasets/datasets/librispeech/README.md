LibriSpeech is a corpus of approximately 1000 hours of read English speech with
sampling rate of 16 kHz, prepared by Vassil Panayotov with the assistance of
Daniel Povey. The data is derived from read audiobooks from the LibriVox
project, and has been carefully segmented and aligned.

It's recommended to use lazy audio decoding for faster reading and smaller
dataset size: - install `tensorflow_io` library: `pip install tensorflow-io` -
enable lazy decoding: `tfds.load('librispeech', builder_kwargs={'config':
'lazy_decode'})`
