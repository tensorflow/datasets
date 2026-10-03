"""kaokore dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification.kaokore import kaokore


class KaokoreTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = kaokore.Kaokore
  BUILDER_CONFIG_NAMES_TO_TEST = ['gender', 'status']
  SKIP_CHECKSUMS = True
  SPLITS = {
    'train': 2,
    'validation': 1,
    'test': 1,
  }
  DL_EXTRACT_RESULT = {
    p: p
    for p in ['labels.csv', 'urls.txt'] +
    ['{:08d}.jpg'.format(i) for i in range(4)]
  }


if __name__ == '__main__':
  testing.test_main()
