"""ribfrac dataset."""

import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np
import nibabel as nib

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
@article{ribfrac2020,
  title={Deep-Learning-Assisted Detection and Segmentation of Rib Fractures from
   CT Scans: Development and Validation of FracNet},
  author={Jin, Liang and Yang, Jiancheng and Kuang, Kaiming and Ni, Bingbing and
   Gao, Yiyi and Sun, Yingli and Gao, Pan and Ma, Weiling and Tan, Mingyu and 
  Kang, Hui and Chen, Jiajun and Li, Ming},
  journal={EBioMedicine},
  year={2020},
  publisher={Elsevier}
}
"""

class Ribfrac(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for ribfrac dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'patient_id': tfds.features.Tensor(shape=(), dtype=tf.string),
            'image': tfds.features.Tensor(
              shape=(None, 512, 512),
              dtype=tf.int16
            ),
            'mask' : tfds.features.Tensor(
              shape=(None, 512, 512),
              dtype=tf.int16
            ),
            'label_id': tfds.features.Tensor(shape=(None,), dtype=tf.int8),
            'label_code': tfds.features.Tensor(shape=(None,), dtype=tf.int8),
        }),
        supervised_keys=(None),
        homepage='https://ribfrac.grand-challenge.org/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.core.download.DownloadManager):
    """Returns SplitGenerators."""
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
        'train_1': self._generate_examples(
          images_path=path['train_1']['train_images_1'] / 'Part1',
          masks_path=path['train_1']['train_masks_1'] / 'Part1',
          csv_path=csvpath['train_1']['csv_1'],
        ),
        'train_2': self._generate_examples(
          images_path=path['train_2']['train_images_2'] / 'Part2',
          masks_path=path['train_2']['train_masks_2'] / 'Part2',
          csv_path=csvpath['train_2']['csv_2'],
        ),
        'valid': self._generate_examples(
            images_path=path['valid']['valid_images_1'] / 'ribfrac-val-images',
            masks_path=path['valid']['valid_masks_1'] / 'ribfrac-val-labels',
            csv_path=csvpath['valid']['csv_1'],
        ),
    }

  def _generate_examples(self, images_path, masks_path, csv_path):
    """Yields examples."""
    os = tfds.core.lazy_imports.os
    pd = tfds.core.lazy_imports.pandas

    filepath_list = tf.io.gfile.listdir(images_path)
    for f in filepath_list:
      image = nib.load(os.path.join(str(images_path), f))
      image_image_data = np.array(image.dataobj, dtype=np.int16)
      mask_id = f.replace('-image.nii.gz', '-label.nii.gz')
      mask = nib.load(os.path.join(str(masks_path), mask_id))
      mask_image_data = np.array(mask.dataobj, dtype=np.int16)

      label_csv = pd.read_csv(csv_path, index_col='public_id')
      label_id = np.array(
        label_csv.loc[f.replace('-image.nii.gz','').replace('-label.nii.gz','')]['label_id'],
        ndmin=1,
        dtype=np.int8
      )
      label_code = np.array(
        label_csv.loc[f.replace('-image.nii.gz','').replace('-label.nii.gz','')]['label_code'],
        ndmin=1,
        dtype=np.int8
      )
      yield f, {
          'patient_id': str(f).replace('-image.nii.gz', '').replace('-label.nii.gz',''),
          'image': np.transpose(image_image_data),
          'mask': np.transpose(mask_image_data),
          'label_id': label_id,
          'label_code': label_code,
      }
