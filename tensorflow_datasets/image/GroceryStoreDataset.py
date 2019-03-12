from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import tensorflow_datasets.public_api as tfds

_CITATION="""\
@inproceedings{klasson2019hierarchical,
  title={A Hierarchical Grocery Store Image Dataset with Visual and Semantic Labels},
  author={Klasson, Marcus and Zhang, Cheng and Kjellstr{\"o}m, Hedvig},
  booktitle={IEEE Winter Conference on Applications of Computer Vision (WACV)},
  year={2019}
}
"""
_DOWNLOAD_URL = "https://github.com/marcusklasson/GroceryStoreDataset-master.zip"

_CLASS_NAMES=['Golden-Delicious-Apple','Granny-Smith-Apple','Pink-Lady-Apple','Red-Delicious-Apple','Royal-Gala-Apple','Avocado','Banana','Kiwi','Lemon','Lime','mango','Cantaloupe Melon','Galia Melon','Honeydew-Melon','Watermelon','Nectarine','Orange','Papaya','Passion-Fruit','Peach','Pear Anjou','Pear Conference','Pear Kaiser','Pineapple','Plum','Pomegranate','Red-Grapefruit','Satsumas','Bravo-Apple-Juice','Bravo-Orange-Juice','God-Morgon-Apple-Juice','God-Morgon-Orange-Juice','God-Morgon-Orange-Red-Grapefruit-Juice','God-Morgon-Red-Grapefruit-Juice','Tropicana-Apple-Juice','Tropicana-Golden-Grapefruit','Tropicana-Juice-Smooth','Tropicana-Mandarin-Morning','Arla-Ecological-Medium-Fat-Milk','Arla-Lactose-Medium-Fat-Milk','Arla-Medium-Fat-Milk','Arla-Standard-Milk','Garant-Ecological-Medium-Fat-Milk','Garant-Ecological-Standard-Milk','Oatly-Natural-Oatghurt','Oatly-Oat-Milk','Arla-Ecological-Sour-Cream','Arla-Sour-Cream','Arla-Sour-Milk','Alpro-Blueberry-Soyghurt','Alpro-Vanilla-Soyghurt','Alpro-Fresh-Soy-Milk','Alpro-Shelf-Soy-Milk','Arla-Mild-Vanilla-Yoghurt','Arla-Natural-Mild-Low-Fat-Yoghurt','Arla-Natural-Yoghurt','Valio-Vanilla-Yoghurt','Yoggi-Strawberry-Yoghurt','Yoggi-Vanilla-Yoghurt','Asparagus','Aubergine','Cabbage','Carrots','Cucumber','Garlic','Ginger','Leek','Brown-Cap-Mushroom','Yellow-Onion','Green-Bell-Pepper','Orange-Bell-Pepper','Red-Bell-Pepper','Yellow-Bell-Pepper','Floury-Potato','Solid-Potato','Sweet-Potato','Red-Beet','Beef-Tomato','Regular-Tomato','Vine-Tomato','Zucchini']




class GroceryStore(tfds.core.GeneratorBasedBuilder):
  """Grocery Store Dataset"""

  VERSION = tfds.core.Version("0.0.2")

  def _info(self):
    
    return tfds.core.DatasetInfo(
       
        builder=self,
        
        description=("This is the dataset of natural images of grocery items. It contains 5125 natural images from 81 different classes. The "
                     " All natural images was taken with a smartphone camera."),
        
        features=tfds.features.FeaturesDict({
            "image_name": tfds.features.Text(),
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names=_CLASS_NAMES),
        }),
        
        supervised_keys=("image", "label"),
        
        urls=["https://github.com/marcusklasson/GroceryStoreDataset/"],
        
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    download_resource = tfds.download.Resource(
        url=_DOWNLOAD_URL,
        extract_method=tfds.download.ExtractMethod.ZIP)
    extracted_path = dl_manager.download_and_extract(download_resource)
    sub = os.listdir(download_path)[0]
    real_root = os.path.join(download_path, sub)
    train_path = os.path.join(real_root, 'Training')
    test_path = os.path.join(real_root, 'Test')
    # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs=dict(root_dir=train_path),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs=dict(root_dir=test_path),
        ),
    ]

  def _generate_examples(self,root_dir):
    # Yields examples from the dataset
    for class_name in _CLASS_NAMES:
      class_dir = os.path.join(root_dir, class_name)
      fns = os.listdir(class_dir)

      for fn in sorted(fns):
        image_fn = os.path.join(class_dir, fn)
        #image = _load_image(image_fn)
        yield {
        #    "image": image,
            "label": class_name,
            "file_name": image_fn,
        }