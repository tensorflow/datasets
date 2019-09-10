"""
Dense stuff, things and part annotations for over 20k images.

Example usage:
```python
import tensorflow_datasets as tfds
from tensorflow_datasets.images import ade20k
builder = ade20k.Ade20k()
builder.download_and_prepare()

cmap = ade20k.create_ade20k_label_colormap()

import matplotlib.pyplot as plt
for image, mask in tfds.as_numpy(
    builder.as_dataset(split='train', as_supervised=True)):
  fig, (ax0, ax1) = plt.subplots(1, 2)
  del fig
  ax0.imshow(image)
  ax1.imshow(colorize_mask(mask))
  plt.show()
```
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """@article{zhou2016semantic,
  title={Semantic understanding of scenes through the ade20k dataset},
  author={Zhou, Bolei and Zhao, Hang and Puig, Xavier and Fidler, Sanja and Barriuso, Adela and Torralba, Antonio},
  journal={arXiv preprint arXiv:1608.05442},
  year={2016}
}
"""

_DESCRIPTION = """
Dense stuff, things, and parts annotations for over 20k images.
This provides only the segmentation masks for the 151 classes.
"""

def create_ade20k_label_colormap():
  """Creates a label colormap used in ADE20K segmentation benchmark.

  Example usage:
  ```python
  colormap = create_ade20k_label_colormap()
  colored_mask = colormap[np.squeeze(mask, axis=-1)]
  ```

  See also `colorize_mask`.

  Returns:
    A colormap for visualizing segmentation results.
  """
  return np.asarray([
      [0, 0, 0],
      [120, 120, 120],
      [180, 120, 120],
      [6, 230, 230],
      [80, 50, 50],
      [4, 200, 3],
      [120, 120, 80],
      [140, 140, 140],
      [204, 5, 255],
      [230, 230, 230],
      [4, 250, 7],
      [224, 5, 255],
      [235, 255, 7],
      [150, 5, 61],
      [120, 120, 70],
      [8, 255, 51],
      [255, 6, 82],
      [143, 255, 140],
      [204, 255, 4],
      [255, 51, 7],
      [204, 70, 3],
      [0, 102, 200],
      [61, 230, 250],
      [255, 6, 51],
      [11, 102, 255],
      [255, 7, 71],
      [255, 9, 224],
      [9, 7, 230],
      [220, 220, 220],
      [255, 9, 92],
      [112, 9, 255],
      [8, 255, 214],
      [7, 255, 224],
      [255, 184, 6],
      [10, 255, 71],
      [255, 41, 10],
      [7, 255, 255],
      [224, 255, 8],
      [102, 8, 255],
      [255, 61, 6],
      [255, 194, 7],
      [255, 122, 8],
      [0, 255, 20],
      [255, 8, 41],
      [255, 5, 153],
      [6, 51, 255],
      [235, 12, 255],
      [160, 150, 20],
      [0, 163, 255],
      [140, 140, 140],
      [250, 10, 15],
      [20, 255, 0],
      [31, 255, 0],
      [255, 31, 0],
      [255, 224, 0],
      [153, 255, 0],
      [0, 0, 255],
      [255, 71, 0],
      [0, 235, 255],
      [0, 173, 255],
      [31, 0, 255],
      [11, 200, 200],
      [255, 82, 0],
      [0, 255, 245],
      [0, 61, 255],
      [0, 255, 112],
      [0, 255, 133],
      [255, 0, 0],
      [255, 163, 0],
      [255, 102, 0],
      [194, 255, 0],
      [0, 143, 255],
      [51, 255, 0],
      [0, 82, 255],
      [0, 255, 41],
      [0, 255, 173],
      [10, 0, 255],
      [173, 255, 0],
      [0, 255, 153],
      [255, 92, 0],
      [255, 0, 255],
      [255, 0, 245],
      [255, 0, 102],
      [255, 173, 0],
      [255, 0, 20],
      [255, 184, 184],
      [0, 31, 255],
      [0, 255, 61],
      [0, 71, 255],
      [255, 0, 204],
      [0, 255, 194],
      [0, 255, 82],
      [0, 10, 255],
      [0, 112, 255],
      [51, 0, 255],
      [0, 194, 255],
      [0, 122, 255],
      [0, 255, 163],
      [255, 153, 0],
      [0, 255, 10],
      [255, 112, 0],
      [143, 255, 0],
      [82, 0, 255],
      [163, 255, 0],
      [255, 235, 0],
      [8, 184, 170],
      [133, 0, 255],
      [0, 255, 92],
      [184, 0, 255],
      [255, 0, 31],
      [0, 184, 255],
      [0, 214, 255],
      [255, 0, 112],
      [92, 255, 0],
      [0, 224, 255],
      [112, 224, 255],
      [70, 184, 160],
      [163, 0, 255],
      [153, 0, 255],
      [71, 255, 0],
      [255, 0, 163],
      [255, 204, 0],
      [255, 0, 143],
      [0, 255, 235],
      [133, 255, 0],
      [255, 0, 235],
      [245, 0, 255],
      [255, 0, 122],
      [255, 245, 0],
      [10, 190, 212],
      [214, 255, 0],
      [0, 204, 255],
      [20, 0, 255],
      [255, 255, 0],
      [0, 153, 255],
      [0, 41, 255],
      [0, 255, 204],
      [41, 0, 255],
      [41, 255, 0],
      [173, 0, 255],
      [0, 245, 255],
      [71, 0, 255],
      [122, 0, 255],
      [0, 255, 184],
      [0, 92, 255],
      [184, 255, 0],
      [0, 133, 255],
      [255, 214, 0],
      [25, 194, 194],
      [102, 255, 0],
      [92, 0, 255],
  ], dtype=np.uint8)


def colorize_mask(mask, colormap=None):
  """
  Get an RGB representation of a segmentation mask consistent with original.

  Args:
    mask: (H, W, 1) or (H, W) int array, segmentation mask of class indices with
      values in [0, 151).
    colormap (optional): (151, 3) uint8 array giving the RGB color for each
      class. Uses `create_ade20k_label_colormap` if not provided.

  Returns:
    (H, W, 3) colored mask.
  """
  if len(mask.shape) == 3:
    mask = np.squeeze(mask, axis=-1)
  elif len(mask.shape) != 2:
    raise ValueError(
        'mask must be shape (H, W, 1) or (H, W), got {}'.format(mask.shape))
  if colormap is None:
    colormap = create_ade20k_label_colormap()
  return colormap[mask]


CLASSES = (
    None, "wall", "building, edifice", "sky", "floor, flooring", "tree",
    "ceiling", "road, route", "bed", "windowpane, window", "grass",
    "cabinet", "sidewalk, pavement",
    "person, individual, someone, somebody, mortal, soul", "earth, ground",
    "door, double door", "table", "mountain, mount",
    "plant, flora, plant life", "curtain, drape, drapery, mantle, pall",
    "chair", "car, auto, automobile, machine, motorcar", "water",
    "painting, picture", "sofa, couch, lounge", "shelf", "house", "sea",
    "mirror", "rug, carpet, carpeting", "field", "armchair", "seat",
    "fence, fencing", "desk", "rock, stone", "wardrobe, closet, press",
    "lamp", "bathtub, bathing tub, bath, tub", "railing, rail", "cushion",
    "base, pedestal, stand", "box", "column, pillar", "signboard, sign",
    "chest of drawers, chest, bureau, dresser", "counter", "sand", "sink",
    "skyscraper", "fireplace, hearth, open fireplace",
    "refrigerator, icebox", "grandstand, covered stand", "path",
    "stairs, steps", "runway", "case, display case, showcase, vitrine",
    "pool table, billiard table, snooker table", "pillow",
    "screen door, screen", "stairway, staircase", "river", "bridge, span",
    "bookcase", "blind, screen", "coffee table, cocktail table",
    "toilet, can, commode, crapper, pot, potty, stool, throne", "flower",
    "book", "hill", "bench", "countertop",
    "stove, kitchen stove, range, kitchen range, cooking stove",
    "palm, palm tree", "kitchen island",
    "computer, computing machine, computing device, data processor, "
    "electronic computer, information processing system", "swivel chair",
    "boat", "bar", "arcade machine", "hovel, hut, hutch, shack, shanty",
    "bus, autobus, coach, charabanc, double-decker, jitney, motorbus, "
    "motorcoach, omnibus, passenger vehicle", "towel",
    "light, light source", "truck, motortruck", "tower",
    "chandelier, pendant, pendent", "awning, sunshade, sunblind",
    "streetlight, street lamp", "booth, cubicle, stall, kiosk",
    "television receiver, television, television set, tv, tv set, idiot "
    "box, boob tube, telly, goggle box", "airplane, aeroplane, plane",
    "dirt track", "apparel, wearing apparel, dress, clothes", "pole",
    "land, ground, soil",
    "bannister, banister, balustrade, balusters, handrail",
    "escalator, moving staircase, moving stairway",
    "ottoman, pouf, pouffe, puff, hassock", "bottle",
    "buffet, counter, sideboard",
    "poster, posting, placard, notice, bill, card", "stage", "van", "ship",
    "fountain",
    "conveyer belt, conveyor belt, conveyer, conveyor, transporter",
    "canopy", "washer, automatic washer, washing machine", "plaything, toy",
    "swimming pool, swimming bath, natatorium", "stool", "barrel, cask",
    "basket, handbasket", "waterfall, falls", "tent, collapsible shelter",
    "bag", "minibike, motorbike", "cradle", "oven", "ball",
    "food, solid food", "step, stair", "tank, storage tank",
    "trade name, brand name, brand, marque", "microwave, microwave oven",
    "pot, flowerpot",
    "animal, animate being, beast, brute, creature, fauna",
    "bicycle, bike, wheel, cycle", "lake",
    "dishwasher, dish washer, dishwashing machine",
    "screen, silver screen, projection screen", "blanket, cover",
    "sculpture", "hood, exhaust hood", "sconce", "vase",
    "traffic light, traffic signal, stoplight", "tray",
    "ashcan, trash can, garbage can, wastebin, ash bin, ash-bin, ashbin, "
    "dustbin, trash barrel, trash bin", "fan",
    "pier, wharf, wharfage, dock", "crt screen", "plate",
    "monitor, monitoring device", "bulletin board, notice board", "shower",
    "radiator", "glass, drinking glass", "clock", "flag")


class Ade20k(tfds.core.GeneratorBasedBuilder):
  """
  Semantic/part segmentation dataset.

  Segmentation masks are stored as 1-channel png images.
  """

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(ade20k): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict(dict(
            # These are the features of your dataset like images, labels ...
            image=tfds.features.Image(
                shape=(None, None, 3), dtype=tf.uint8, encoding_format='jpeg'),
            segmentation=tfds.features.Image(
                shape=(None, None, 1), dtype=tf.uint8, encoding_format='png'),
            example_id=tfds.features.Text(),
        )),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('image', 'segmentation'),
        # Homepage of the dataset for documentation
        urls=[],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    base_dir = dl_manager.download_and_extract(
        "http://data.csail.mit.edu/places/ADEchallenge/ADEChallengeData2016.zip")

    dirs = '%s/ADEChallengeData2016/{data}/{split}/' % base_dir

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=16,
            gen_kwargs=dict(
                images_dir=dirs.format(split='training', data='images'),
                annotations_dir=dirs.format(
                    split='training', data='annotations'),
            ),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=2,
            gen_kwargs=dict(
                images_dir=dirs.format(split='validation', data='images'),
                annotations_dir=dirs.format(
                    split='validation', data='annotations'),
            ),
        )
    ]

  def _generate_examples(self, images_dir, annotations_dir):
    """Yields examples."""
    for filename in tf.io.gfile.listdir(images_dir):
      example_id = filename[:-4]
      example = dict(
          example_id=example_id,
          image=os.path.join(images_dir, filename),
          segmentation=os.path.join(
              annotations_dir, '{}.png'.format(example_id))
      )
      yield example_id, example
