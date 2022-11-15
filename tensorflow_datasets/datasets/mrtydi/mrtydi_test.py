"""mrtydi dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.mrtydi import mrtydi


class MrTydiTest(testing.DatasetBuilderTestCase):
    """Tests for MrTydi dataset."""
    DATASET_CLASS = mrtydi.MrTydiBuilder
    BUILDER_CONFIG_NAMES_TO_TEST = ['mmarco-en']
    SPLITS = {
        'query': 2,  # Number of fake queries
        'passage': 3,  # Number of fake passages
        'train': 1,  # Number of train pairs
        'validation': 1,  # Number of validation pairs
    }


if __name__ == '__main__':
    testing.test_main()