"""TODO(car_evaluation): Add a description here.
    Title: Car Evaluation Database
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
import tensorflow as tf

# TODO(car_evaluation): BibTeX citation
_CITATION = """
The hierarchical decision model, from which this dataset is
derived, was first presented in 

M. Bohanec and V. Rajkovic: Knowledge acquisition and explanation for
multi-attribute decision making. In 8th Intl Workshop on Expert
Systems and their Applications, Avignon, France. pages 59-78, 1988.

Within machine-learning, this dataset was used for the evaluation
of HINT (Hierarchy INduction Tool), which was proved to be able to
completely reconstruct the original hierarchical model. This,
together with a comparison with C4.5, is presented in

B. Zupan, M. Bohanec, I. Bratko, J. Demsar: Machine learning by
function decomposition. ICML-97, Nashville, TN. 1997 (to appear)
"""

# TODO(car_evaluation):
_DESCRIPTION = """
Car Evaluation Database was derived from a simple hierarchical
   decision model originally developed for the demonstration of DEX
   (M. Bohanec, V. Rajkovic: Expert system for decision
   making. Sistemica 1(1), pp. 145-157, 1990.). The model evaluates
   cars according to the following concept structure:

   CAR                      car acceptability
   . PRICE                  overall price
   . . buying               buying price
   . . maint                price of the maintenance
   . TECH                   technical characteristics
   . . COMFORT              comfort
   . . . doors              number of doors
   . . . persons            capacity in terms of persons to carry
   . . . lug_boot           the size of luggage boot
   . . safety               estimated safety of the car

   Input attributes are printed in lowercase. Besides the target
   concept (CAR), the model includes three intermediate concepts:
   PRICE, TECH, COMFORT. Every concept is in the original model
   related to its lower level descendants by a set of examples (for
   these examples sets see http://www-ai.ijs.si/BlazZupan/car.html).

   The Car Evaluation Database contains examples with the structural
   information removed, i.e., directly relates CAR to the six input
   attributes: buying, maint, doors, persons, lug_boot, safety.

   Because of known underlying concept structure, this database may be
   particularly useful for testing constructive induction and
   structure discovery methods.
"""

_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'

class CarEvaluation(tfds.core.GeneratorBasedBuilder):
  """TODO(car_evaluation): Short description of my dataset.
      Number of Instances: 1728
      Number of Attributes: 6
      Attribute Values:

        buying       v-high, high, med, low
        maint        v-high, high, med, low
        doors        2, 3, 4, 5-more
        persons      2, 4, more
        lug_boot     small, med, big
        safety       low, med, high
      
      Class Distribution (number of instances per class)

       class      N          N[%]
       -----------------------------
       unacc     1210     (70.023 %) 
       acc        384     (22.222 %) 
       good        69     ( 3.993 %) 
       v-good      65     ( 3.762 %) 
  """

  # TODO(car_evaluation): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(car_evaluation): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            "features":
                tfds.features.Tensor(shape=(6,), dtype=tf.string),              
            'prediction' : tfds.features.ClassLabel(names=['unacc', 'acc', 'good', 'vgood'])
            
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('features', 'prediction'),
        # Homepage of the dataset for documentation
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(car_evaluation): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    train_file = dl_manager.download(_URL)
    all_lines = tf.io.gfile.GFile(train_file).read().split("\n")
    train_records = [l for l in all_lines if l]
    print(len(train_records))
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
              "records": train_records
              },
        ),
    ]

  def _generate_examples(self, records):
    """Yields examples."""
    # TODO(car_evaluation): Yields (key, example) tuples from the dataset
    for i, row in enumerate(records):
        elems = row.split(",")
        yield i, {
            "features": [e.strip() for e in elems[:-1]],
            "prediction": elems[-1].split('.')[0].strip(),
        }

