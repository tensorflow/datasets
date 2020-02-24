"""Speech Command Dataset Tester"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.audio import speech_command


class SpeechCommandTest(testing.DatasetBuilderTestCase):
    DATASET_CLASS = speech_command.SpeechCommand
    SPLITS = {
        "train": 16,  # Number of fake train example
        "test": 2,  # Number of fake test example
        "validation": 2,  # Number of fake test example
    }

    DL_EXTRACT_RESULT = {
        "train": "speech_command-train.tfrecord",
        "test": "speech_command-test.tfrecord",
        "valid": "speech_command-validation.tfrecord",
        "labels": "label.labels.txt"
    }


if __name__ == "__main__":
    testing.test_main()
