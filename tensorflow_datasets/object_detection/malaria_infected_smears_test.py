"""Malaria Infected Human Blood Smears Dataset"""

from tensorflow_datasets import testing
from tensorflow_datasets.object_detection import malaria_infected_smears


class MalariaInfectedSmearsTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = malaria_infected_smears.MalariaInfectedSmears
  SPLITS = {
      "train": 3,  # Number of fake train example
      "test": 1,  # Number of fake test example
  }



if __name__ == "__main__":
  testing.test_main()
