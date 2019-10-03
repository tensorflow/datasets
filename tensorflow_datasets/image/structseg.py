"""
Organ-at-risk segmentation dataset from head & neck CT scans
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import nibabel as nib
import numpy

_CITATION = """
@misc{li_zhou_deng_chen, title={StructSeg2019 - Grand Challenge}, 
url={https://structseg2019.grand-challenge.org/}, 
journal={Automatic Structure Segmentation for Radiotherapy Planning Challenge }, 
author={Li, Hongsheng and Zhou, Jinghao and Deng, Jincheng and Chen, Ming}}
"""

_DESCRIPTION = """
The dataset is used for evaluating automatic algorithms on segmentation of organ-at-risk(OAR)
of nasopharynx cancer, for radiation therapy planning. The dataset contains organ-at-risk 
segmentation from head & neck CT scans 
"""

_BASE_URL = """https://structseg2019.grand-challenge.org/"""

class Structseg(tfds.core.GeneratorBasedBuilder):
    """
    Organ-at-risk segmentation dataset from head & neck CT scans
    """

    VERSION = tfds.core.Version("1.0.0",
                                experiments={tfds.core.Experiment.S3: False})
    SUPPORTED_VERSIONS = [
        tfds.core.Version("2.0.0"),
    ]

    def get_all_file_paths(self, images_dir_path):
        """
        Images stored in the following format:
        HaN_OAR/1/image.nii.gz
        HaN_OAR/1/label.nii.gz
        HaN_OAR/2/image.nii.gz
        HaN_OAR/2/label.nii.gz ...
        Get the file path to all images
        """

        image_path = []
        parent_dir = tf.io.gfile.listdir(images_dir_path)[0]
        walk_dir = os.path.join(images_dir_path, parent_dir)
        dirs = tf.io.gfile.listdir(walk_dir)

        for subdir in dirs:

            if tf.io.gfile.isdir(os.path.join(walk_dir, subdir)):
                for full_path, _, fname in tf.io.gfile.walk(os.path.join(walk_dir, subdir)):
                    for image_file in fname:
                        if image_file.endswith("nii.gz"):
                            image_path.append(os.path.join(full_path, image_file))
                            # print(image_path)

        return image_path

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            # tfds.features.FeatureConnectors
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Tensor(shape=(512, 512, 1), dtype=tf.float64),
                "label": tfds.features.Tensor(shape=(512, 512, 1), dtype=tf.bool)
            }),
            # specify feature tuples
            supervised_keys=("image", "label"),
            # Homepage of the dataset for documentation
            urls=[_BASE_URL],
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        path = dl_manager.manual_dir
        if not tf.io.gfile.exists(path):
            raise AssertionError(
                'You must download the dataset manually from {},' \
                'extract it as a folder named HaN_OAR,' \
                ' and place it in {}.'.format(_BASE_URL, dl_manager.manual_dir))

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=20,
                gen_kwargs={
                    'file_path': path  # pylint: disable=no-value-for-parameter

                }
            )
        ]

    def _generate_examples(self, file_path):
        # file_path = filepath
        dirs = self.get_all_file_paths(file_path)

        label_dirs = []
        data_dirs = []

        # separate the directory paths into label subdir and data subdir

        for each_dir in dirs:
            if each_dir.endswith("/label.nii.gz"):
                label_dirs.append(each_dir)
            else:
                data_dirs.append(each_dir)

        # get index_list from label_dirs
        index_list = []

        for dir_name in label_dirs:
            index_ = re.search(r"(?<=HaN_OAR\/)(\d+)\/", dir_name)
            index_list.append(index_.group(1))

        for patient_index, label_dir, data_dir in zip(index_list, label_dirs, data_dirs):
            label_temp = nib.load(label_dir)
            data_temp = nib.load(data_dir)

            label_array = label_temp.get_fdata()
            data_array = data_temp.get_fdata()

            for slice_idx in range(label_array.shape[2]):
                patient = patient_index + "_" + str(slice_idx)

                record = {
                    "image": data_array[:, :, slice_idx].reshape(512, 512, 1),
                    "label": tf.dtypes.cast((label_array[:, :, slice_idx].reshape(512, 512, 1)), tf.bool),

                }

                yield patient, record
