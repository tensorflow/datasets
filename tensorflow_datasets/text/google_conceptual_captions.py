"""
A new dataset of image captionannotations, Conceptual Captions, whichcontains an order of magnitude more im-ages than the MS-COCO dataset and  represents  a  wider  variety  of both images and image caption styles.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import csv
import tensorflow_datasets.public_api as tfds

_CITATION = """
Piyush Sharma, Nan Ding, Sebastian Goodman and Radu Soricut. 2018. Conceptual Captions: A Cleaned, Hypernymed, Image Alt-text Dataset For Automatic Image Captioning. Proceedings of ACL.
"""

_DESCRIPTION = """
A new dataset of image captionannotations, Conceptual Captions, whichcontains an order of magnitude more im-ages than the MS-COCO dataset and  represents  a  wider  variety  of both images and image caption styles.
"""


class GoogleConceptualCaptions(tfds.core.GeneratorBasedBuilder):
    """
    A new dataset of image captionannotations, Conceptual Captions, whichcontains an order of magnitude more im-ages than the MS-COCO dataset and  represents  a  wider  variety  of both images and image caption styles.
    """

    VERSION = tfds.core.Version('1.1.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "caption": tfds.features.Text(),
                "image_link": tfds.features.Text(),
            }),
            supervised_keys=None,
            urls=["https://ai.google.com/research/ConceptualCaptions"],
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={
                    "dataset_path": os.path.join(
                        dl_manager.manual_dir,
                        "Train_GCC-training.tsv")},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                gen_kwargs={
                    "dataset_path": os.path.join(
                        dl_manager.manual_dir,
                        "Validation_GCC-1.1.0-Validation.tsv")},
            ),
        ]

    def _generate_examples(self, dataset_path):
        with tf.io.gfile.GFile(dataset_path) as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            for idx, row in enumerate(reader):
                yield idx, {"caption": row[1],
                            "image_link": row[0]}
