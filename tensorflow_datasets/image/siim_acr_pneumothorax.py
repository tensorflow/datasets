"""siim_acr_pneumothorax dataset."""

import tensorflow as tf
import pandas as pd
import numpy as np
import tensorflow_datasets.public_api as tfds

_CITATION = """
@ONLINE {societyforimaginginformaticsinmedicine(siim)2019,
author = "Society for Imaging Informatics in Medicine (SIIM)",
title  = "SIIM-ACR Pneumothorax Segmentation",
month  = "aug",
year   = "2019",
url    = "https://www.kaggle.com/c/siim-acr-pneumothorax"
"-segmentation/overview/description"
}"""

_DESCRIPTION = """
This dataset comes from the SIIM-ACR Pneumothorax Segmentation, 
held by SIIM in 2019. It contains over 15,000 chest X-ray scans
(~12,100 for training, ~3,100 for testing) and corresponding masks 
for pneumothorax diagnosis segmentation. All scans are stored in 
DICOM format, which consists of patient demographic information
(de-identified) and scan metadata. All scans are identified with
unique file names and the labels are stored in separate csv files.
The annotation information consists of 3 columns: scan ID, scan
unique name and the encoded pixels. Scans without pneumothorax
have “-1” value under “encoded pixels” column while positive
scans have masks of pneumothorax air regions stored in
RLE(run-length encoding) format. 
"""


class SiimAcrPneumothorax(tfds.core.GeneratorBasedBuilder):
  """Siim-Acr-Pneumothorax dataset, train images only"""
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
      builder=self,
      description=_DESCRIPTION,
      features=tfds.features.FeaturesDict({
        "image": tfds.features.Tensor(shape=(1024, 1024, 1),
                                      dtype=tf.uint8),
        "mask": tfds.features.Tensor(shape=(1024, 1024, 1),
                                     dtype=tf.bool)
      }),
      homepage='https://www.kaggle.com/c/siim-acr-pneumothorax'
               '-segmentation',
      citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Google bucket download link
    google_bucket_url = 'https://storage.googleapis.com/bme590/jiacheng_lin' \
                        '/siim-train-test.zip '
    data_dir = dl_manager.download_and_extract(google_bucket_url)
    #  Kaggle download link, not compatible with testing
    #  kaggle_data = 'seesee/siim-train-test'
    #  data_dir = dl_manager.download_kaggle_data(kaggle_data)

    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.TRAIN,
        gen_kwargs={
          'data_dir': data_dir
        },
      ),
    ]

  def _generate_examples(self, data_dir):
    """Yields examples."""
    dataset_dir = data_dir
    train_glob = dataset_dir + '/siim/dicom-images-train/*/*/*.dcm'
    train_fns = sorted(tfds.core.lazy_imports.glob.glob(train_glob))
    df_full = pd.read_csv(dataset_dir + '/siim/train-rle.csv',
                          index_col='ImageId')

    im_height = 1024
    im_width = 1024

    # Get images and masks
    for patient_id in train_fns:
      dataset = tfds.core.lazy_imports.pydicom.read_file(patient_id)
      image = np.expand_dims(dataset.pixel_array, axis=2)
      try:
        if '-1' in df_full.loc[
          patient_id.split('/')[-1][:-4], ' EncodedPixels']:
          mask = np.zeros((im_height, im_width, 1))
        else:
          if isinstance(df_full.loc[patient_id.split('/')[-1][:-4],
                                    ' EncodedPixels'], str):
            mask = np.expand_dims(
              self.rle2mask(df_full.loc[patient_id.split('/')[-1][:-4],
                                        ' EncodedPixels'],
                            im_height, im_width), axis=2)
          else:
            mask = np.zeros((im_height, im_width, 1),
                            dtype=np.bool)
            for x in df_full.loc[
              patient_id.split('/')[-1][:-4], ' EncodedPixels']:
              mask = mask + np.expand_dims(
                self.rle2mask(x, im_height, im_width), axis=2)
      except KeyError:
        # Assume missing masks are empty masks.
        mask = np.zeros((im_height, im_width, 1), dtype=np.bool)
      mask = mask.astype(np.bool)
      yield patient_id, {
        #  'image': tf.convert_to_tensor(image),
        #  'mask': tf.convert_to_tensor(mask)
        'image': image,
        'mask': mask
      }

  def rle2mask(self, rle, width, height):
    """Translate rle string to mask array"""
    mask = np.zeros(width * height)
    array = np.asarray([int(x) for x in rle.split()])
    starts = array[0::2]
    lengths = array[1::2]

    current_position = 0
    for index, start in enumerate(starts):
      current_position += start
      mask[current_position:current_position + lengths[index]] = 255
      current_position += lengths[index]

    return mask.reshape(width, height)
