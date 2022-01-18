# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Oxford 102 Category Flower Dataset."""

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_BASE_URL = "https://www.robots.ox.ac.uk/~vgg/data/flowers/102/"

_NAMES = [
    "pink primrose", "hard-leaved pocket orchid", "canterbury bells",
    "sweet pea", "english marigold", "tiger lily", "moon orchid",
    "bird of paradise", "monkshood", "globe thistle", "snapdragon",
    "colt's foot", "king protea", "spear thistle", "yellow iris",
    "globe-flower", "purple coneflower", "peruvian lily", "balloon flower",
    "giant white arum lily", "fire lily", "pincushion flower", "fritillary",
    "red ginger", "grape hyacinth", "corn poppy", "prince of wales feathers",
    "stemless gentian", "artichoke", "sweet william", "carnation",
    "garden phlox", "love in the mist", "mexican aster", "alpine sea holly",
    "ruby-lipped cattleya", "cape flower", "great masterwort", "siam tulip",
    "lenten rose", "barbeton daisy", "daffodil", "sword lily", "poinsettia",
    "bolero deep blue", "wallflower", "marigold", "buttercup", "oxeye daisy",
    "common dandelion", "petunia", "wild pansy", "primula", "sunflower",
    "pelargonium", "bishop of llandaff", "gaura", "geranium", "orange dahlia",
    "pink-yellow dahlia?", "cautleya spicata", "japanese anemone",
    "black-eyed susan", "silverbush", "californian poppy", "osteospermum",
    "spring crocus", "bearded iris", "windflower", "tree poppy", "gazania",
    "azalea", "water lily", "rose", "thorn apple", "morning glory",
    "passion flower", "lotus", "toad lily", "anthurium", "frangipani",
    "clematis", "hibiscus", "columbine", "desert-rose", "tree mallow",
    "magnolia", "cyclamen", "watercress", "canna lily", "hippeastrum",
    "bee balm", "ball moss", "foxglove", "bougainvillea", "camellia", "mallow",
    "mexican petunia", "bromelia", "blanket flower", "trumpet creeper",
    "blackberry lily"
]

_CITATION = """\
@InProceedings{Nilsback08,
   author = "Nilsback, M-E. and Zisserman, A.",
   title = "Automated Flower Classification over a Large Number of Classes",
   booktitle = "Proceedings of the Indian Conference on Computer Vision, Graphics and Image Processing",
   year = "2008",
   month = "Dec"
}
"""

_DESCRIPTION = """
The Oxford Flowers 102 dataset is a consistent of 102 flower categories commonly occurring
in the United Kingdom. Each class consists of between 40 and 258 images. The images have
large scale, pose and light variations. In addition, there are categories that have large
variations within the category and several very similar categories.

The dataset is divided into a training set, a validation set and a test set.
The training set and validation set each consist of 10 images per class (totalling 1020 images each).
The test set consists of the remaining 6149 images (minimum 20 per class).

Note: The dataset by default comes with a test size larger than the train
size. For more info see this [issue](https://github.com/tensorflow/datasets/issues/3022).
"""


class OxfordFlowers102(tfds.core.GeneratorBasedBuilder):
  """Oxford 102 category flower dataset."""

  VERSION = tfds.core.Version("2.1.1")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names=_NAMES),
            "file_name": tfds.features.Text(),
        }),
        supervised_keys=("image", "label"),
        homepage=_BASE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Download images and annotations that come in separate archives.
    # Note, that the extension of archives is .tar.gz even though the actual
    # archives format is uncompressed tar.
    dl_paths = dl_manager.download_and_extract({
        "images": os.path.join(_BASE_URL, "102flowers.tgz"),
        "labels": os.path.join(_BASE_URL, "imagelabels.mat"),
        "setid": os.path.join(_BASE_URL, "setid.mat"),
    })

    gen_kwargs = dict(
        images_dir_path=os.path.join(dl_paths["images"], "jpg"),
        labels_path=dl_paths["labels"],
        setid_path=dl_paths["setid"],
    )

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(split_name="trnid", **gen_kwargs)),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(split_name="tstid", **gen_kwargs)),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs=dict(split_name="valid", **gen_kwargs)),
    ]

  def _generate_examples(self, images_dir_path, labels_path, setid_path,
                         split_name):
    """Yields examples."""
    with tf.io.gfile.GFile(labels_path, "rb") as f:
      labels = tfds.core.lazy_imports.scipy.io.loadmat(f)["labels"][0]
    with tf.io.gfile.GFile(setid_path, "rb") as f:
      examples = tfds.core.lazy_imports.scipy.io.loadmat(f)[split_name][0]

    for image_id in examples:
      file_name = "image_%05d.jpg" % image_id
      record = {
          "image": os.path.join(images_dir_path, file_name),
          "label": labels[image_id - 1] - 1,
          "file_name": file_name,
      }
      yield file_name, record
