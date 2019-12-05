from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import os

# TODO(my_dataset): BibTeX citation
_CITATION = """
  @inproceedings{modec13,
    title={MODEC: Multimodal Decomposable Models for Human Pose Estimation},
    author={Sapp, Benjamin and Taskar, Ben},
    booktitle={In Proc. CVPR},
    year={2013},
  }
"""

_DESCRIPTION = """FLIC Dataset for GCI 2019"""


class FLIC(tfds.core.GeneratorBasedBuilder):

    VERSION = tfds.core.Version('0.1.0')

    def _info(self):
        # TODO(my_dataset): Specifies the tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # tfds.features.FeatureConnectors
            features=tfds.features.FeaturesDict({
                "image_description": tfds.features.Text(),
                "image": tfds.features.Image(),
                # Here, labels can be of 5 distinct values.
                "label": tfds.features.ClassLabel(num_classes=5),

            }),
            # If there's a common (input, target) tuple from the features,
            # specify them here. They'll be used if as_supervised=True in
            # builder.as_dataset.
            supervised_keys=("image", "label"),
            # Homepage of the dataset for documentation
            urls=[],
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""

        dl_path = dl_manager.download_and_extract({
           'flic': 'https://drive.google.com/file/d/0B4K3PZp8xXDJN0Fpb0piVjQ3Y3M/view',
        })

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "images_dir_path": os.join(dl_path, "images"),
                    "labels": os.path.join(dl_path, "examples.mat"),

                },
            ),
        ]

    def _generate_examples(self, images_dir_path, labels):
        for image_file in tf.io.gfile.listdir(images_dir_path):
            with tf.io.gfile.GFile(labels) as f:
                for image_id, description, label in data:
                    yield image_id, {
                        "image_description": description,
                        "image": "%s/%s.jpeg" % (images_dir_path, image_id),
                        "label": label,
                    }


