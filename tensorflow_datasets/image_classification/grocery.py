"""grocery dataset."""

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import os

# TODO(grocery): BibTeX citation
_CITATION = """
@inproceedings{klasson2019hierarchical,
  title={A Hierarchical Grocery Store Image Dataset with Visual and Semantic Labels},
  author={Klasson, Marcus and Zhang, Cheng and Kjellstr{\"o}m, Hedvig},
  booktitle={IEEE Winter Conference on Applications of Computer Vision (WACV)},
  year={2019}
}
"""

# TODO(grocery):
_DESCRIPTION = """
The dataset of natural images of grocery items. All natural images was taken with a 
smartphone camera in different grocery stores. We ended up with 5125 natural images from
81 different classes of fruits, vegetables, and carton items (e.g. juice, milk, yoghurt).
The 81 classes are divided into 42 coarse-grained classes, where e.g. the fine-grained classes
'Royal Gala' and 'Granny Smith' belong to the same coarse-grained class 'Apple'. For each 
fine-grained class, we have downloaded an iconic image and a product description of the item,
where some samples of these can be seen on this page below. The dataset was presented in the paper 
"A Hierarchical Grocery Store Image Dataset with Visual and Semantic Labels", which 
appeared at WACV 2019.
"""

_URL = "https://github.com/marcusklasson/GroceryStoreDataset/archive/master.zip"


class Grocery(tfds.core.GeneratorBasedBuilder):
  """TODO(grocery): Short description of my dataset."""

  # TODO(grocery): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(grocery): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            "image":tfds.features.Image(),
            "label":tfds.features.ClassLabel(num_classes=81),
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=("image","label"),
        # Homepage of the dataset for documentation
        homepage='https://github.com/marcusklasson/GroceryStoreDataset',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(grocery): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    extracted_path = dl_manager.download_and_extract(_URL)
    dataset_path = os.path.join(extracted_path,"GroceryStoreDataset-master","dataset")
    train_txt = os.path.join(dataset_path,"train.txt")
    val_txt = os.path.join(dataset_path,"val.txt")
    test_txt = os.path.join(dataset_path,"test.txt")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                "data_path" : dataset_path,
                "data_file" : train_txt,
                "classes":classes,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                "data_path" : dataset_path,
                "data_file" : test_txt,
                "classes":classes,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                "data_path" : dataset_path,
                "data_file" : val_txt,
                "classes":classes,
            },
        ),
    ]

  def _generate_examples(self,data_path,data_file,classes):
    """Yields examples."""
    # TODO(grocery): Yields (key, example) tuples from the dataset
    with tf.io.gfile.GFile(data_file) as f:
        lines = f.readlines()
    for line in lines:
        img_rel_path = os.path.normpath(line.strip().split(',')[0])
        img_path = os.path.join(data_path,img_rel_path)
        img_label = int(line.strip().split(',')[1])
        key = "%s / %s" %(img_label,os.path.basename(img_path))
        
        yield key, {
            "image":img_path,
            "label":img_label.numpy(),
        }

