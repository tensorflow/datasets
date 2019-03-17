import tensorflow_datasets.public_api as tfds
import os
import tensorflow as tf
import pickle


_MINI_IMAGENET_DESCRIPTION = """\
miniImageNet (Vinyals et al., 2016) is a modified version of the ILSVRC-12
dataset (Russakovsky et al., 2015), in which 600 images for each of 100 classes
were randomly chosen to be part of the dataset. We rely on the class split used
by Ravi & Larochelle (2017). These splits use 64 classes for training, 16 for
validation, and 20 for test. All images are of size 84 × 84 pixels.
"""

_MINI_IMAGENET_URL_HOME = \
    "https://github.com/renmengye/few-shot-ssl-public#miniimagenet"
_MINI_IMAGENET_URL_DOWNLOAD = \
    "https://drive.google.com/uc?export=download&id=16V_ZlkW4SsnNDtnGmaBRq2OoPmUOc5mY"

_MINI_IMAGENET_CITATION = """\
@inproceedings{vinyals2016matching,
  title={Matching networks for one shot learning},
  author={Vinyals, Oriol and Blundell, Charles and Lillicrap, Timothy and Wierstra, Daan and others},
  booktitle={Advances in neural information processing systems},
  pages={3630--3638},
  year={2016}
}
"""

_NUM_CLASSES = 100
_NUM_CLASSES_TRAIN = 64
_NUM_CLASSES_VALIDATION = 16
_NUM_CLASSES_TEST = 20


class MiniImagenet(tfds.core.GeneratorBasedBuilder):
    """mini_imagenet: a modified version of the ILSVRC-12 dataset."""

    VERSION = tfds.core.Version("1.0.2")

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_MINI_IMAGENET_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(),
                "label": tfds.features.ClassLabel(num_classes=_NUM_CLASSES),
            }),
            supervised_keys=("image", "label"),
            urls=[_MINI_IMAGENET_URL_HOME],
            citation=_MINI_IMAGENET_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Downloads the data and defines the split."""

        extracted_path = dl_manager.download_and_extract(
            _MINI_IMAGENET_URL_DOWNLOAD)

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=1,
                gen_kwargs={
                    "idx_split": 0,
                    "path_data": os.path.join(extracted_path,
                                              "mini-imagenet-cache-train.pkl"),
                }
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=1,
                gen_kwargs={
                    "idx_split": 1,
                    "path_data": os.path.join(extracted_path,
                                              "mini-imagenet-cache-val.pkl"),
                }
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=1,
                gen_kwargs={
                    "idx_split": 2,
                    "path_data": os.path.join(extracted_path,
                                              "mini-imagenet-cache-test.pkl"),
                }
            ),
        ]

    def _generate_examples(self, idx_split, path_data):
        """yields examples from the dataset.

        Note: Class indices are as follows:
        train [0, 63]; val [64, 79]; test [79, 99]

        Args:
            idx_split (int): used to identify split.
            path_data (string): path to extracted data.

        Yields:
            dict_data (dict): data dictionary of image and label.
                keys:
                    "image_data" (np.ndarray, shape=[num_data, 84, 84, 3],
                                  dtype=np.uint8)
                    "class_dict" (dict): class name to list of image indices.
                        value: (list of int, len=600)
        """

        # offset classass indices based on split
        if idx_split == 0:
            idx_class_start = 0
        elif idx_split == 1:
            idx_class_start = _NUM_CLASSES_TRAIN
        elif idx_split == 2:
            idx_class_start = _NUM_CLASSES_TRAIN + _NUM_CLASSES_VALIDATION

        # read data
        with tf.gfile.GFile(path_data, "rb") as f:
            data = pickle.load(f)
            img_data = data["image_data"]
            class_dict = data["class_dict"]

            for idx_class, (class_name, idx_img_list) in \
                    enumerate(class_dict.items()):
                idx_class_split = idx_class + idx_class_start
                for idx_img in idx_img_list:
                    img = img_data[idx_img]

                    dict_data = {
                        "image": img,
                        "label": idx_class_split
                    }

                    yield dict_data
