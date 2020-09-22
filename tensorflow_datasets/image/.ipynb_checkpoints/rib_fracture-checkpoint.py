"""rib_fracture dataset."""

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import nibabel as nib
import numpy as np
import os
import zipfile


_CITATION = """
@dataset{jiancheng_yang_2020_3893508,
  author       = {Jiancheng Yang and
                  Liang Jin and
                  Bingbing Ni and
                  Ming Li},
  title        = {{RibFrac Dataset: A Benchmark for Rib Fracture 
                   Detection, Segmentation and Classification
                   (Training Set Part 1)}},
  month        = jun,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {v1.0},
  doi          = {10.5281/zenodo.3893508},
  url          = {https://doi.org/10.5281/zenodo.3893508}
}
"""

_DESCRIPTION = """
This dataset is a benchmark for developing algorithms on rib fracture 
detection, segmentation. The RibFrac dataset, including 
CTs images and segmentation, including rib fracture images for each patient 
and their related masks. All files including images and masks in this 
dataset are the NIFTI format.
"""

_MASK_FILE = "https://zenodo.org/record/3893508/files/" \
             "ribfrac-train-labels-1.zip"
_IMAGE_FILE = "https://zenodo.org/record/3893508/files/" \
              "ribfrac-train-images-1.zip"


class RibFracture(tfds.core.GeneratorBasedBuilder):
  """TODO(rib_fracture): Short description of my dataset."""
  VERSION = tfds.core.Version('0.1.0')
  def _info(self):
    # TODO(rib_fracture): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'image_slice': tfds.features.Tensor(shape=(512, 512, 1),
                                                dtype=tf.int32),
            'mask_slice': tfds.features.Tensor(shape=(512, 512, 1),
                                               dtype=tf.int32)
        }),
        supervised_keys=('image_slice', 'mask_slice'),
        # Homepage of the dataset for documentation
        homepage='https://zenodo.org/record/3893508#.X2WRRWf0lQJ',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    dl_manager._register_checksums = True
    """Returns SplitGenerators."""
    path_dir = dl_manager.download({
        'image_slice': _IMAGE_FILE,
        'mask_slice': _MASK_FILE
    })

    image_path = path_dir['image_slice']
    mask_path = path_dir['mask_slice']
    extract_path1 = extract_zip(image_path,"/image")
    extract_path2 = extract_zip(mask_path,"/mask")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                "image_path": extract_path1,
                "mask_path": extract_path2
            },
        ),
    ]

  def _generate_examples(self, image_path=None,mask_path=None):
    list_files1 = tf.io.gfile.listdir(image_path)
    list_files2 = tf.io.gfile.listdir(mask_path)
    n = 0
    for img_path,mas_path in zip(list_files1,list_files2):

        img = nib.load(image_path+"/"+img_path)
        mask = nib.load(mask_path+"/"+mas_path)

        img_array = np.array(img.dataobj)
        mask_array =np.array(mask.dataobj)

        new_img = img_array.reshape(img_array.shape[0], img_array.shape[1],
                                    img_array.shape[2])
        new_mask = mask_array.reshape(mask_array.shape[0], mask_array.shape[1],
                                      mask_array.shape[2])

        slices1 = new_img.transpose()
        slices2 = new_mask.transpose()
        n = n + 1
        for i in range(len(slices1)):

            image = slices1[i]
            image = image[..., None]

            mask = slices2[i]
            mask = mask[..., None]
            j = i + 1
            count = "Patient_{} Rib CT_{}".format(n, j)
            imageTensor = np.array(image, dtype=np.int32)
            maskTensor = np.array(mask, dtype=np.int32)

            yield count, {
                'image_slice': imageTensor,
                'mask_slice': maskTensor
            }


def extract_zip(path,path_name):
  """Extracting the zip file"""
  root = os.path.dirname(path)
  with zipfile.ZipFile(path, "r") as zip_ref:
    zip_ref.extractall(root + path_name)
  file_name = tf.io.gfile.listdir(root + path_name)
  file_name = sorted(file_name)
  folder_name = str(file_name[0])
  data_path = root + path_name + "/" + folder_name
  return data_path


