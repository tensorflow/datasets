"""ribfrac dataset."""

import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np
import nibabel as nib
from itertools import chain

_DESCRIPTION = """
This challenge establishes a large-scale benchmark dataset
to automatically detect and classify around 5,000 rib fractures
from 660 computed tomography (CT) scans, which consists of
420 training CTs (all with fractures), 80 validation CTs (20
without fractures) and 160 evaluation CTs. Each annotation
consists of a pixel-level mask of rib fracture regions (for serving
detection), plus a 4-type classification.
"""

_CITATION = """
@article{
  ribfrac2020,
  title={
    Deep-Learning-Assisted Detection and Segmentation of Rib Fractures from CT
    Scans: Development and Validation of FracNet
  },
  author={
    Jin,
    Liang and Yang,
    Jiancheng and Kuang,
    Kaiming and Ni,
    Bingbing and Gao,
    Yiyi and Sun,
    Yingli and Gao,
    Pan and Ma,
    Weiling and Tan,
    Mingyu and Kang,
    Hui and Chen,
    Jiajun and Li, Ming
  },
  journal={EBioMedicine},
  year={2020},
  publisher={Elsevier}
}
"""

_BUCKET_PATH = 's3://gradient-scratch/william'
using_bucket = True

class Ribfrac(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for ribfrac dataset."""
  VERSION = tfds.core.Version('1.0.1')
  RELEASE_NOTES = {
      '1.0.1': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
      builder=self,
      description=_DESCRIPTION,
      features=tfds.features.FeaturesDict({
          'patient_id': tfds.features.Tensor(shape=(), dtype=tf.string),
          'image_pair': tfds.features.Sequence({
              'image': tfds.features.Image(
                shape=(512, 512, 1),
                dtype=tf.uint16,
              ),
              'mask' : tfds.features.Tensor(
                shape=(512, 512, 1),
                dtype=tf.bool,
              ),
          }, length=None),
          'label_id': tfds.features.Tensor(shape=(None,), dtype=tf.int8),
          'label_code': tfds.features.Tensor(shape=(None,), dtype=tf.int8),
      }),
      supervised_keys=(None),
      homepage='https://ribfrac.grand-challenge.org/',
      citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.core.download.DownloadManager):
    """Returns SplitGenerators."""
    if(using_bucket):
      return {
        'train': self._generate_train(_BUCKET_PATH, _BUCKET_PATH),
        'valid': self._generate_examples(
          images_path=_BUCKET_PATH + '/ribfrac-val-images',
          masks_path=_BUCKET_PATH + '/ribfrac-val-labels',
          csv_path=_BUCKET_PATH + '/ribfrac-val-info.csv',
        ),
      }
    else:
      path = dl_manager.download_and_extract({
        'train_1': {
          'train_images_1':
            'https://zenodo.org/record/3893508/files/ribfrac-train-images-1.zip',
          'train_masks_1':
            'https://zenodo.org/record/3893508/files/ribfrac-train-labels-1.zip',
        },
        'train_2': {
          'train_images_2':
            'https://zenodo.org/record/3893498/files/ribfrac-train-images-2.zip',
          'train_masks_2':
            'https://zenodo.org/record/3893498/files/ribfrac-train-labels-2.zip',
        },
        'valid': {
          'valid_images_1':
            'https://zenodo.org/record/3893496/files/ribfrac-val-images.zip',
          'valid_masks_1':
            'https://zenodo.org/record/3893496/files/ribfrac-val-labels.zip',
        },
      })
      csvpath = dl_manager.download({
        'train_1': {
          'csv_1':
            'https://zenodo.org/record/3893508/files/ribfrac-train-info-1.csv',
        },
        'train_2': {
          'csv_2':
            'https://zenodo.org/record/3893498/files/ribfrac-train-info-2.csv',
        },
        'valid': {
          'csv_1':
            'https://zenodo.org/record/3893496/files/ribfrac-val-info.csv',
        }
      })
      return {
        'train': self._generate_train(path, csvpath),
        'valid': self._generate_examples(
          images_path=path['valid']['valid_images_1'] / 'ribfrac-val-images',
          masks_path=path['valid']['valid_masks_1'] / 'ribfrac-val-labels',
          csv_path=csvpath['valid']['csv_1'],
        ),
      }

  def _generate_train(self, path, csvpath):
    if(using_bucket):
      part1 = self._generate_examples(
        images_path=path + '/Part1',
        masks_path=path + '/Part1-labels',
        csv_path=csvpath + '/ribfrac-train-info-1.csv',
      )
      part2 = self._generate_examples(
        images_path=path + '/Part2',
        masks_path=path + '/Part2-labels',
        csv_path=csvpath + '/ribfrac-train-info-2.csv',
      )
    else:
      part1 = self._generate_examples(
        images_path=path['train_1']['train_images_1'] / 'Part1',
        masks_path=path['train_1']['train_masks_1'] / 'Part1',
        csv_path=csvpath['train_1']['csv_1'],
      )
      part2 = self._generate_examples(
        images_path=path['train_2']['train_images_2'] / 'Part2',
        masks_path=path['train_2']['train_masks_2'] / 'Part2',
        csv_path=csvpath['train_2']['csv_2'],
      )

    for example in chain(part1, part2):
      yield example

  def _generate_examples(self, images_path, masks_path, csv_path):
    """Yields examples."""
    os = tfds.core.lazy_imports.os
    pd = tfds.core.lazy_imports.pandas
    filepath_list = tf.io.gfile.listdir(images_path)
    if(using_bucket):
      for f in filepath_list:
        image_path = os.path.join(images_path, f)
        byte = tf.io.gfile.GFile(image_path, mode='rb')
        temp = open(f, 'ab')
        temp.write(byte.read())
        temp.close()
        image = nib.load(os.path.abspath(temp.name))
        image_image_data = np.array(image.dataobj, dtype=np.uint16)
        image_stack = np.expand_dims(np.transpose(image_image_data), -1)
        img_list = []
        for img_slice in image_stack:
            img_list.append(img_slice)
        os.remove(os.path.abspath(temp.name))

        mask_id = f.replace('-image.nii.gz', '-label.nii.gz')
        mask_path = os.path.join(masks_path, mask_id)
        byte = tf.io.gfile.GFile(mask_path, mode='rb')
        temp1 = open(mask_id, 'ab')
        temp1.write(byte.read())
        temp1.close()
        mask = nib.load(os.path.abspath(temp1.name))
        mask_image_data = np.array(mask.dataobj, dtype=np.uint8)
        mask_stack = np.expand_dims(np.transpose(mask_image_data), -1).astype(np.bool)
        mask_list = []
        for mask_slice in mask_stack:
            mask_list.append(mask_slice)
        os.remove(os.path.abspath(temp1.name))

        patient_id = f.replace('-image.nii.gz','').replace('-label.nii.gz','')
        label_csv = pd.read_csv(tf.io.gfile.GFile(csv_path), index_col='public_id')
        label_id = np.array(
          label_csv.loc[patient_id]['label_id'],
          ndmin=1,
          dtype=np.int8
        )
        label_code = np.array(
          label_csv.loc[patient_id]['label_code'],
          ndmin=1,
          dtype=np.int8
        )

        yield f, {
          'patient_id': str(patient_id),
          'image_pair': {
              'image': img_list,
              'mask': mask_list,
          },
          'label_id': label_id,
          'label_code': label_code,
        }
    else:
      for f in filepath_list:
        image = nib.load(os.path.join(str(images_path), f))
        image_image_data = np.array(image.dataobj, dtype=np.int16)
        image_stack = np.expand_dims(np.transpose(image_image_data),-1) #[None, 512, 512, 1]
        img_list = []
        for img_slice in image_stack:
            img_list.append(img_slice)

        mask_id = f.replace('-image.nii.gz', '-label.nii.gz')
        mask = nib.load(os.path.join(str(masks_path), mask_id))
        mask_image_data = np.array(mask.dataobj, dtype=np.int16)
        mask_stack = np.expand_dims(np.transpose(mask_image_data),-1)
        mask_list = []
        for mask_slice in mask_stack:
            mask_list.append(mask_slice)

        patient_id = f.replace('-image.nii.gz','').replace('-label.nii.gz','')
        label_csv = pd.read_csv(csv_path, index_col='public_id')
        label_id = np.array(
          label_csv.loc[patient_id]['label_id'],
          ndmin=1,
          dtype=np.int8
        )
        label_code = np.array(
          label_csv.loc[patient_id]['label_code'],
          ndmin=1,
          dtype=np.int8
        )

        yield f, {
          'patient_id': str(patient_id),
          'image_pair': {
            'image': img_list,
            'mask': mask_list,
          },
          'label_id': label_id,
          'label_code': label_code,
        }
