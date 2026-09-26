"""Binary classification task on possible configurations of tic-tac-toe game"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import tic_tac_toe

class TicTacToeTest(testing.DatasetBuilderTestCase):

  DATASET_CLASS = tic_tac_toe.TicTacToe
  SPLITS = {
      "train": 1,
  }

  DL_EXTRACT_RESULT = 'tic-tac-toe.data'

if __name__ == "__main__":
  testing.test_main()

