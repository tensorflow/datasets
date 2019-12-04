"""TODO(fgvc_aircraft): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import fgvc_aircraft

class FgvcAircraftTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = fgvc_aircraft.FgvcAircraft
  SPLITS = {
      "train": 2,
      "validation": 2,
      "test": 2,
  }

if __name__ == "__main__":
  testing.test_main()