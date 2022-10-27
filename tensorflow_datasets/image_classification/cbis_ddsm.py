# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""CBIS-DDSM mammography dataset."""

import csv
import os
import re

from absl import logging
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
The CBIS-DDSM (Curated Breast Imaging Subset of DDSM) is an updated and
standardized version of the Digital Database for Screening Mammography (DDSM).
The DDSM is a database of 2,620 scanned film mammography studies.
It contains normal, benign, and malignant cases with verified pathology
information.

The default config is made of patches extracted from the original mammograms,
following the description from (http://arxiv.org/abs/1708.09427), in order to
frame the task to solve in a traditional image classification setting.

"""

_CITATION = """\
@misc{CBIS_DDSM_Citation,
  doi = {10.7937/k9/tcia.2016.7o02s9cy},
  url = {https://wiki.cancerimagingarchive.net/x/lZNXAQ},
  author = {Sawyer-Lee,  Rebecca and Gimenez,  Francisco and Hoogi,  Assaf and Rubin,  Daniel},
  title = {Curated Breast Imaging Subset of DDSM},
  publisher = {The Cancer Imaging Archive},
  year = {2016},
}
@article{TCIA_Citation,
  author = {
    K. Clark and B. Vendt and K. Smith and J. Freymann and J. Kirby and
    P. Koppel and S. Moore and S. Phillips and D. Maffitt and M. Pringle and
    L. Tarbox and F. Prior
  },
  title = {{The Cancer Imaging Archive (TCIA): Maintaining and Operating a
  Public Information Repository}},
  journal = {Journal of Digital Imaging},
  volume = {26},
  month = {December},
  year = {2013},
  pages = {1045-1057},
}
@article{DBLP:journals/corr/abs-1708-09427,
  author    = {Li Shen},
  title     = {End-to-end Training for Whole Image Breast Cancer Diagnosis using
               An All Convolutional Design},
  journal   = {CoRR},
  volume    = {abs/1708.09427},
  year      = {2017},
  url       = {http://arxiv.org/abs/1708.09427},
  archivePrefix = {arXiv},
  eprint    = {1708.09427},
  timestamp = {Mon, 13 Aug 2018 16:48:35 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1708-09427},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_CALC_TEST_CSV_URL = 'https://wiki.cancerimagingarchive.net/download/attachments/22516629/calc_case_description_test_set.csv?version=1&modificationDate=1506796343686&api=v2'
_CALC_TRAIN_CSV_URL = 'https://wiki.cancerimagingarchive.net/download/attachments/22516629/calc_case_description_train_set.csv?version=1&modificationDate=1506796349666&api=v2'
_MASS_TEST_CSV_URL = 'https://wiki.cancerimagingarchive.net/download/attachments/22516629/mass_case_description_test_set.csv?version=1&modificationDate=1506796343175&api=v2'
_MASS_TRAIN_CSV_URL = 'https://wiki.cancerimagingarchive.net/download/attachments/22516629/mass_case_description_train_set.csv?version=1&modificationDate=1506796355038&api=v2'

_IMAGE_VIEW_LABELS = (
    'CC',
    'MLO',
)
_BREAST_LABELS = (
    'LEFT',
    'RIGHT',
)
_BREAST_DENSITY_NUM_CLASSES = 4  # Original range: [1, 4]
_PATHOLOGY_LABELS = (
    'BENIGN',
    'BENIGN_WITHOUT_CALLBACK',
    'MALIGNANT',
)
_ASSESSMENT_NUM_CLASSES = 6  # Original range: [0, 5]
_SUBTELTY_NUM_CLASSES = 6  # Original range: [0, 5]
_DCIM_REGEX = re.compile(
    r'^.*/(?P<study>1.3.6.1.4.1.9590.100.1.2.[0-9.]+)/(?P<series>1.3.6.1.4.1.9590.100.1.2.[0-9.]+)/(?P<instance>.+).dcm$'
)


class CuratedBreastImagingDDSMConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CuratedBreastImagingDDSM."""

  def __init__(self, image_size=None, patch_size=None, **kwargs):
    kwargs['version'] = tfds.core.Version('3.0.0')
    kwargs['release_notes'] = {
        '3.0.0': """
        Better cropping sampling
        (https://github.com/tensorflow/datasets/pull/2502)
        """,
        '2.0.1': 'New split API (https://tensorflow.org/datasets/splits)',
    }
    super(CuratedBreastImagingDDSMConfig, self).__init__(**kwargs)
    self.image_size = image_size
    self.patch_size = patch_size


class CuratedBreastImagingDDSM(tfds.core.GeneratorBasedBuilder):
  """Curated Breast Imaging Subset of DDSM."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  You can download the images from
  https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM

  Because special software and libraries are needed to download and read the
  images contained in the dataset, TFDS assumes that the user has downloaded the
  original DCIM files and converted them to PNG.

  The following commands (or equivalent) should be used to generate the PNG
  files, in order to guarantee reproducible results:

  ```sh
  find $DATASET_DCIM_DIR -name '*.dcm' | \\
  xargs -n1 -P8 -I{} bash -c 'f={}; dcmj2pnm $f | convert - ${f/.dcm/.png}'
  ```

  Resulting images should be put in `manual_dir`, like:
  `<manual_dir>/Mass-Training_P_01981_RIGHT_MLO_1/1.3.6.../000000.png`.
  """

  BUILDER_CONFIGS = [
      CuratedBreastImagingDDSMConfig(
          name='patches',
          description=(
              'Patches containing both calsification and mass cases, '
              'plus pathces with no abnormalities. Designed as a '
              'traditional 5-class classification task.'
          ),
          image_size=(1152, 896),  # Note: (height, width).
          patch_size=(224, 224),
      ),
      CuratedBreastImagingDDSMConfig(
          name='original-calc',
          description=(
              'Original images of the calcification cases compressed '
              'in lossless PNG.'
          ),
      ),
      CuratedBreastImagingDDSMConfig(
          name='original-mass',
          description=(
              'Original images of the mass cases compressed in lossless PNG.'
          ),
      ),
  ]

  def _info(self):
    features_fn_map = {
        'original-calc': self._get_features_original_calc,
        'original-mass': self._get_features_original_mass,
        'patches': self._get_features_patches,
    }
    if self.builder_config.name not in features_fn_map:
      raise ValueError(
          'Builder config named {} not supported!'.format(
              self.builder_config.name
          )
      )

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=features_fn_map[self.builder_config.name](),
        homepage=(
            'https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM'
        ),
        citation=_CITATION,
    )

  def _get_features_original_base(self):
    return {
        'id': tfds.features.Text(),
        'breast': tfds.features.ClassLabel(names=_BREAST_LABELS),
        'image': tfds.features.Image(shape=(None, None, 1)),
        'view': tfds.features.ClassLabel(names=_IMAGE_VIEW_LABELS),
        'patient': tfds.features.Text(),
        'abnormalities': {
            'id': tfds.features.Tensor(shape=(), dtype=np.int32),
            'mask': tfds.features.Image(shape=(None, None, 1)),
            'assessment': tfds.features.ClassLabel(
                num_classes=_ASSESSMENT_NUM_CLASSES
            ),
            'pathology': tfds.features.ClassLabel(names=_PATHOLOGY_LABELS),
            'subtlety': tfds.features.ClassLabel(
                num_classes=_SUBTELTY_NUM_CLASSES
            ),
            # TODO(jpuigcerver): Include original crops when TFDS allows it.
            # The problem seems to be in the compute statistics steps, since
            # a given example may have crops of different sizes and this is
            # not handled properly.
            # 'crop': tfds.features.Image(shape=(None, None, 1)),
        },
    }

  def _get_features_original_calc(self):
    features = self._get_features_original_base()
    features['abnormalities'].update({
        'calc_type': tfds.features.ClassLabel(
            names_file=tfds.core.tfds_path(
                os.path.join('image_classification', 'cbis_ddsm_calc_types.txt')
            )
        ),
        'calc_distribution': tfds.features.ClassLabel(
            names_file=tfds.core.tfds_path(
                os.path.join(
                    'image_classification', 'cbis_ddsm_calc_distributions.txt'
                )
            )
        ),
    })
    features['abnormalities'] = tfds.features.Sequence(
        tfds.features.FeaturesDict(features['abnormalities'])
    )
    return tfds.features.FeaturesDict(features)

  def _get_features_original_mass(self):
    features = self._get_features_original_base()
    features['abnormalities'].update({
        'mass_shape': tfds.features.ClassLabel(
            names_file=tfds.core.tfds_path(
                os.path.join(
                    'image_classification', 'cbis_ddsm_mass_shapes.txt'
                )
            )
        ),
        'mass_margins': tfds.features.ClassLabel(
            names_file=tfds.core.tfds_path(
                os.path.join(
                    'image_classification', 'cbis_ddsm_mass_margins.txt'
                )
            )
        ),
    })
    features['abnormalities'] = tfds.features.Sequence(
        tfds.features.FeaturesDict(features['abnormalities'])
    )
    return tfds.features.FeaturesDict(features)

  def _get_features_patches(self):
    return tfds.features.FeaturesDict({
        'id': tfds.features.Text(),
        'image': tfds.features.Image(
            shape=(None, None, 1), encoding_format='jpeg'
        ),
        'label': tfds.features.ClassLabel(
            names_file=tfds.core.tfds_path(
                os.path.join(
                    'image_classification', 'cbis_ddsm_patch_labels.txt'
                )
            )
        ),
    })

  def _split_generators(self, dl_manager):
    if self.builder_config.name in ['original-calc', 'original-mass']:
      return self._split_generators_original(dl_manager)
    elif self.builder_config.name == 'patches':
      return self._split_generators_patches(dl_manager)
    else:
      raise ValueError(
          'Builder config named {} not supported!'.format(
              self.builder_config.name
          )
      )

  def _split_generators_original(self, dl_manager):
    if self.builder_config.name == 'original-calc':
      test_url = _CALC_TEST_CSV_URL
      train_url = _CALC_TRAIN_CSV_URL
    elif self.builder_config.name == 'original-mass':
      test_url = _MASS_TEST_CSV_URL
      train_url = _MASS_TRAIN_CSV_URL
    else:
      raise ValueError(
          'Builder config named {} not supported!'.format(
              self.builder_config.name
          )
      )

    resources = {'test': test_url, 'train': train_url}
    resource_paths = dl_manager.download_and_extract(resources)
    patients_data = _load_csv_files(dl_manager.manual_dir, resource_paths)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'generate_fn': self._generate_examples_original,
                'patients_data': patients_data,
                'yield_from_train_csv': True,  # Yield train examples.
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'generate_fn': self._generate_examples_original,
                'patients_data': patients_data,
                'yield_from_train_csv': False,  # Yield test examples.
            },
        ),
    ]

  def _split_generators_patches(self, dl_manager):
    resources_urls = {
        'calc-test': _CALC_TEST_CSV_URL,
        'calc-train': _CALC_TRAIN_CSV_URL,
        'mass-test': _MASS_TEST_CSV_URL,
        'mass-train': _MASS_TRAIN_CSV_URL,
    }
    resource_paths = dl_manager.download_and_extract(resources_urls)
    patients_data = _load_csv_files(dl_manager.manual_dir, resource_paths)

    # Statistics about the resulting splits.
    # Whole dataset:
    #   Num patients: 1566, of which have malignant abnormalities: 48.0%
    #   Num mamographies: 3103, of which have malignant abnormalities: 44.3%
    #   Num abnormalities: 3568, of which are malignant: 40.8%
    # Test split:
    #   Num patients: 234, of which have malignant abnormalities: 47.0%
    #   Num mamographies: 450, of which have malignant abnormalities: 44.2%
    #   Num abnormalities: 538, of which are malignant: 39.8%
    # Train split:
    #   Num patients: 1197, of which have malignant abnormalities: 48.0%
    #   Num mamographies: 2386, of which have malignant abnormalities: 44.1%
    #   Num abnormalities: 2722, of which are malignant: 41.0%
    # Validation split:
    #   Num patients: 135, of which have malignant abnormalities: 49.6%
    #   Num mamographies: 267, of which have malignant abnormalities: 46.4%
    #   Num abnormalities: 308, of which are malignant: 41.2%
    patients_test, patients_train, patients_valid = _split_patients(
        patients_data
    )
    patients_data_test = _select_patients_data(patients_data, patients_test)
    patients_data_train = _select_patients_data(patients_data, patients_train)
    patients_data_valid = _select_patients_data(patients_data, patients_valid)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'generate_fn': self._generate_examples_patches,
                'patients_data': patients_data_train,
                'image_size': self.builder_config.image_size,
                'patch_size': self.builder_config.patch_size,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'generate_fn': self._generate_examples_patches,
                'patients_data': patients_data_test,
                'image_size': self.builder_config.image_size,
                'patch_size': self.builder_config.patch_size,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'generate_fn': self._generate_examples_patches,
                'patients_data': patients_data_valid,
                'image_size': self.builder_config.image_size,
                'patch_size': self.builder_config.patch_size,
            },
        ),
    ]

  def _generate_examples(self, generate_fn, **kwargs):
    """Yields examples."""
    return generate_fn(**kwargs)

  def _generate_examples_original(self, patients_data, yield_from_train_csv):
    def _include_example_in_split(example):
      if yield_from_train_csv:
        return example['csv_key'] == 'train'
      else:
        return example['csv_key'] == 'test'

    for _, patient_examples in sorted(patients_data.items()):
      for _, example in sorted(patient_examples.items()):
        if _include_example_in_split(example):
          record = {
              'id': example['id'],
              'patient': example['patient'],
              'image': example['image'],
              'view': example['view'],
              'breast': example['breast'],
              # pylint: disable=g-complex-comprehension
              'abnormalities': [
                  {k: v for k, v in abnormality.items() if k not in ['type']}
                  for abnormality in example['abnormalities']
              ],
              # pylint: enable=g-complex-comprehension
          }
          yield example['id'], record

  def _generate_examples_patches(
      self,
      patients_data,
      image_size=(1152, 896),
      patch_size=(224, 224),
      num_positive_patches_per_abnormality=10,
      num_background_patches_per_image=10,
  ):
    # Set random seed so that we always get the same patches in each split.
    np.random.seed(0x12345 + len(patients_data))

    for _, patient_examples in sorted(patients_data.items()):
      for _, example in sorted(patient_examples.items()):
        # Read the mammography image.
        image = _read_image(example['image'], image_size=image_size)
        abnormalities_masks = [
            _read_image(abnormality['mask'], image_size=image.shape)
            for abnormality in example['abnormalities']
        ]
        abnormalities_areas = [np.sum(mask > 0) for mask in abnormalities_masks]
        # Sample positive (abnormal) patches from the given mammography.
        for abnormality, abnormality_mask, abnormality_area in zip(
            example['abnormalities'], abnormalities_masks, abnormalities_areas
        ):
          # Determine label for the given abnormality.
          if abnormality['pathology'].startswith('MALIGNANT'):
            benign_or_malignant = 'MALIGNANT'
          else:
            benign_or_malignant = 'BENIGN'
          if abnormality['type'] == 'calc':
            label = benign_or_malignant + '_CALCIFICATION'
          elif abnormality['type'] == 'mass':
            label = benign_or_malignant + '_MASS'
          else:
            raise ValueError(
                'Unknown abnormality type: %r' % abnormality['type']
            )
          # Sample positive patches from the given abnormality.
          for k, patch in enumerate(
              _sample_positive_patches(
                  image,
                  abnormality['mask'],
                  abnormality_mask,
                  abnormality_area,
                  patch_size,
                  num_positive_patches_per_abnormality,
              )
          ):
            patch_id = '%s/abnorm_%s/patch_%d' % (
                example['id'],
                abnormality['id'],
                k,
            )
            record = {
                'id': patch_id,
                # Note: TFDS needs the shape to be (?, ?, 1).
                'image': np.expand_dims(patch, axis=-1),
                'label': label,
            }
            yield patch_id, record

        # Sample background patches from the given mammography.
        for k, patch in enumerate(
            _sample_negative_patches(
                image,
                example['image'],
                abnormalities_masks,
                abnormalities_areas,
                patch_size,
                num_background_patches_per_image,
            )
        ):
          id_ = '%s/background_%d' % (example['id'], k)
          record = {
              'id': id_,
              # Note: TFDS needs the shape to be (?, ?, 1).
              'image': np.expand_dims(patch, axis=-1),
              'label': 'BACKGROUND',
          }
          yield id_, record


def _load_csv_files(manual_dir, dictionary_of_csv_files):
  """Load the ground-truth data from the given dictionary of CSV files.

  Args:
    manual_dir: Path of the directory containing the images.
    dictionary_of_csv_files: Dictionary containing the key and filepath of each
      CSV file to load.

  Returns:
    A dictionary containing the ground-truth loaded from the CSV files.
  """
  # Data maps patients -> examples -> list of abnormalities
  data = {}
  for csv_key, csv_path in sorted(dictionary_of_csv_files.items()):
    with tf.io.gfile.GFile(csv_path, 'r') as f:
      csv_reader = csv.DictReader(f)
      for i, row in enumerate(csv_reader, 2):
        row = {k: v.strip() for k, v in row.items()}  # Strip all cells.
        # Construct example ID from the study and series IDs.
        example_id = _DCIM_REGEX.sub(
            r'\g<study>/\g<series>', row['image file path']
        )
        # Get path to the
        for key in [
            'image file path',
            'ROI mask file path',
            'cropped image file path',
        ]:
          row[key] = row[key].replace('.dcm', '.png')
          row[key] = os.path.join(manual_dir, *row[key].split('/'))
          if not tf.io.gfile.exists(row[key]):
            raise ValueError(
                'Error processing line %d from csv file %s: '
                'Image %r does not exist!' % (i, csv_path, row[key])
            )

        mask_file_path = row['ROI mask file path']
        crop_file_path = row['cropped image file path']
        full_image = _read_image(row['image file path'])
        mask_image = _read_image(mask_file_path)
        crop_image = _read_image(crop_file_path)
        if full_image.shape == crop_image.shape:
          # TODO(jpuigcerver): THIS ASSUMES THAT THE CROP/MASK COLUMNS ARE JUST
          # REVERSED. I've checked that this is the case for a couple of rows,
          # but this issue happens a lot across all CSV files. Contact the
          # owners of the dataset to ask about this problem.
          mask_file_path, crop_file_path = crop_file_path, mask_file_path
        elif full_image.shape != mask_image.shape:
          # TODO(jpuigcerver): Contact the owners of the dataset to ask about
          # this problem.
          logging.error(
              (
                  'Error processing line %d from csv file %s: No suitable mask'
                  ' for the given image (expected size: %r, candidate sizes:'
                  ' %r). This abnormality will NOT be included in the dataset.'
              ),
              i,
              csv_path,
              full_image.shape,
              [mask_image.shape, crop_image.shape],
          )
          continue

        abnormality = {
            'id': int(row['abnormality id']),
            'mask': mask_file_path,
            'assessment': row['assessment'],
            'pathology': row['pathology'],
            'subtlety': row['subtlety'],
        }
        if 'calc type' in row and 'calc distribution' in row:
          abnormality['type'] = 'calc'
          abnormality['calc_type'] = row['calc type']
          abnormality['calc_distribution'] = row['calc distribution']
        elif 'mass shape' in row and 'mass margins' in row:
          abnormality['type'] = 'mass'
          abnormality['mass_shape'] = row['mass shape']
          abnormality['mass_margins'] = row['mass margins']
        else:
          raise ValueError('CSV file is missing required columns.')

        example = {
            'id': example_id,
            'breast': row['left or right breast'],
            'patient': row['patient_id'],
            'image': row['image file path'],
            'view': row['image view'],
            'abnormalities': [abnormality],
            # Note: Useful to know whether the example is from train or test.
            'csv_key': csv_key,
        }
        _append_example_to_data(data, example)

  return data


def _append_example_to_data(data, example):
  """Append the given example to the data dictionary."""
  example_id = example['id']
  patient_id = example['patient']
  if patient_id in data:
    if example_id in data[example['patient']]:
      assert example_id == data[patient_id][example_id]['id']
      assert patient_id == data[patient_id][example_id]['patient']
      assert example['breast'] == data[patient_id][example_id]['breast']
      assert example['image'] == data[patient_id][example_id]['image']
      assert example['view'] == data[patient_id][example_id]['view']
      data[patient_id][example_id]['abnormalities'].extend(
          example['abnormalities']
      )
    else:
      data[example['patient']][example['id']] = example
  else:
    data[example['patient']] = {example['id']: example}


def _split_patients(
    data, test_fraction=0.15, train_fraction=0.765, valid_fraction=0.085
):
  """Split the patients in the data dictionary into test, train and valid sets."""
  assert test_fraction > 0 and train_fraction > 0 and valid_fraction > 0
  assert np.abs(test_fraction + train_fraction + valid_fraction - 1.0) < 1e-9
  all_patient_ids = sorted(list(data.keys()))
  np.random.seed(seed=0x12345)  # To make sure we always get the same splits.
  np.random.shuffle(all_patient_ids)
  cutoff_test = int(test_fraction * len(all_patient_ids))
  patients_test = all_patient_ids[:cutoff_test]
  cutoff_train = cutoff_test + int(train_fraction * len(all_patient_ids))
  patients_train = all_patient_ids[cutoff_test:cutoff_train]
  patients_valid = all_patient_ids[cutoff_train:]
  return set(patients_test), set(patients_train), set(patients_valid)


def _select_patients_data(data, patient_ids):
  return {k: v for k, v in data.items() if k in patient_ids}


def _read_image(filepath, image_size=None):
  """Read an image and optionally resize it (size must be: height, width)."""
  cv2 = tfds.core.lazy_imports.cv2
  with tf.io.gfile.GFile(filepath, 'rb') as f:
    image = cv2.imdecode(
        np.frombuffer(f.read(), dtype=np.uint8), flags=cv2.IMREAD_GRAYSCALE
    )
    if image_size:
      # Note: cv2.resize actually expects (width, size).
      image = cv2.resize(image, (image_size[1], image_size[0]))
      assert image.shape == image_size
    return image


def _find_contours(*args, **kwargs):
  cv2 = tfds.core.lazy_imports.cv2
  tuple_ = cv2.findContours(*args, **kwargs)
  if len(tuple_) == 2:  # Recent opencv returns: (contours, hierachy)
    return tuple_[0]
  elif len(tuple_) == 3:  # Old opencv returns: (ret, contours, hierachy)
    return tuple_[1]
  else:
    raise AssertionError('Unknown {}')


def _get_breast_mask(image, min_breast_color_threshold=0.05):
  """Get the binary mask of the breast region of the image."""
  cv2 = tfds.core.lazy_imports.cv2
  threshold = int(image.max() * min_breast_color_threshold)
  _, image_binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
  contours = _find_contours(
      image_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
  )
  contours_areas = [cv2.contourArea(cont) for cont in contours]
  biggest_contour_idx = np.argmax(contours_areas)
  return cv2.drawContours(
      np.zeros_like(image_binary),
      contours,
      biggest_contour_idx,
      255,
      cv2.FILLED,
  )


def _get_roi_from_mask(mask):
  cv2 = tfds.core.lazy_imports.cv2
  contours = _find_contours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  contours_areas = [cv2.contourArea(cont) for cont in contours]
  biggest_contour_idx = np.argmax(contours_areas)
  return contours[biggest_contour_idx]


def _patch_overlaps_any_abnormality_above_threshold(
    y,
    x,
    patch_size,
    abnormalities_masks,
    abnormalities_areas,
    min_overlap_threshold,
):
  """Return True if the given patch overlaps significantly with any abnormality.

  Given a patch and a single abnormality, the overlap between the two is
  significant if, and only if, the relative area of the intersection of the two
  w.r.t. the area of the patch is above `min_overlap_threshold` OR the
  area of the intersection w.r.t. the total abnormality area is above
  `min_overlap_threshold`.

  Args:
    y: Top-most coordinate of the patch.
    x: Left-most coordinate of the patch.
    patch_size: Tuple with (height, width) of the patch.
    abnormalities_masks: List with the binary mask of each abnormality.
    abnormalities_areas: List with the total area of each abnormality.
    min_overlap_threshold:

  Returns:
    Returns True if the above condition is met for any of the given
    abnormalities, or False otherwise.
  """
  patch_area = patch_size[0] * patch_size[1]
  for abnorm_mask, abnorm_area in zip(abnormalities_masks, abnormalities_areas):
    abnorm_in_patch_area = np.sum(
        abnorm_mask[y : (y + patch_size[0]), x : (x + patch_size[1])] > 0
    )
    abnorm_in_patch_wrt_patch = abnorm_in_patch_area / patch_area
    abnorm_in_patch_wrt_abnorm = abnorm_in_patch_area / abnorm_area
    if (
        abnorm_in_patch_wrt_patch > min_overlap_threshold
        or abnorm_in_patch_wrt_abnorm > min_overlap_threshold
    ):
      return True
  return False


def _sample_positive_patches(
    image,
    abnormality_filepath,
    abnormality_mask,
    abnormality_area,
    patch_size,
    number_of_patches=10,
    min_overlap_threshold=0.90,
    max_number_of_trials_per_threshold=100,
):
  """Sample random patches from the image overlapping with the given abnormality.

  The abnormal area of the patch with respect to either (a) the total area of
  the patch, or (b) the total area of the abnormality, must be at least
  `min_overlap_threshold` (i.e. 90% by default).

  After `max_number_of_trials_per_threshold` samples, if not enough patches
  meeting this requirement have been generated, the `min_overlap_threshold` is
  reduced by 5%. This procedure is repeated until min_overlap_threshold < 0.1
  (which should not happen ever, if the dataset is correct).

  Args:
    image: Image to patch from.
    abnormality_filepath: Only used for logging.
    abnormality_mask: Binary mask of the abnormality in the image.
    abnormality_area: Precomputed area of the abnormality.
    patch_size: Size of the patch to extract.
    number_of_patches: Number of patches to sample around the abnormality ROI.
    min_overlap_threshold: Minimum relative area of the patch overlapping with
      the abnormality.
    max_number_of_trials_per_threshold: Maximum number of random samples to try
      before reducing the `min_overlap_threshold` by 5%.

  Yields:
    The patch cropped from the input image.
  """
  cv2 = tfds.core.lazy_imports.cv2

  # The paper trying to be reproduced states that 90% of the are of each
  # positive patch should correspond to abnormal tissue. Thus if the total area
  # of abnormality is smaller than 0.9 * patch_area, we are certain that no
  # patch can meet this requirement. This happens indeed quite often.
  #
  # However, in a piece of code release by the authors of the paper
  # (https://github.com/yuyuyu123456/CBIS-DDSM/blob/bf3abc6ac2890b9b51eb5125e00056e39295fa44/ddsm_train/sample_patches_combined.py#L26)
  # the authors accept a patch if the total area of abnormality in the patch is
  # greater than 75% OR if 75% of the total abnormal area is in the patch.
  # In addition, they reduce the overlapping threholds every 1000 trials to
  # handle some corner casses.

  abnormality_roi = _get_roi_from_mask(abnormality_mask)
  abnorm_x, abnorm_y, abnorm_w, abnorm_h = cv2.boundingRect(abnormality_roi)

  number_of_yielded_patches = 0
  while min_overlap_threshold > 0.1:
    # Determine the region where random samples should be sampled from.
    max_h, min_h = max(abnorm_h, patch_size[0]), min(abnorm_h, patch_size[0])
    max_w, min_w = max(abnorm_w, patch_size[1]), min(abnorm_w, patch_size[1])
    min_y = abnorm_y - max_h + min_overlap_threshold * min_h
    min_x = abnorm_x - max_w + min_overlap_threshold * min_w
    max_y = abnorm_y + abnorm_h - int(min_overlap_threshold * min_h)
    max_x = abnorm_x + abnorm_w - int(min_overlap_threshold * min_w)
    # Ensure that all sampled batches are within the image.
    min_y = max(min_y, 0)
    min_x = max(min_x, 0)
    max_y = max(min(max_y, image.shape[0] - patch_size[0] - 1), min_y)
    max_x = max(min(max_x, image.shape[1] - patch_size[1] - 1), min_x)
    # Cap the number of trials if the sampling region is too small.
    effective_range_size = max_number_of_trials_per_threshold
    if (max_y - min_y + 1) * (max_x - min_x + 1) < effective_range_size:
      logging.debug(
          (
              'The sampling region for patches of size %r with '
              'min_overlap_threshold=%f contains less possible patches than '
              'max_number_of_trials_per_threshold=%d, in abnormality %s'
          ),
          patch_size,
          min_overlap_threshold,
          max_number_of_trials_per_threshold,
          abnormality_filepath,
      )
      effective_range_size = (max_y - min_y + 1) * (max_x - min_x + 1)

    for _ in range(effective_range_size):
      patch_y = np.random.randint(min_y, max_y + 1)
      patch_x = np.random.randint(min_x, max_x + 1)
      if _patch_overlaps_any_abnormality_above_threshold(
          patch_y,
          patch_x,
          patch_size,
          [abnormality_mask],
          [abnormality_area],
          min_overlap_threshold,
      ):
        number_of_yielded_patches += 1
        yield image[
            patch_y : (patch_y + patch_size[0]),
            patch_x : (patch_x + patch_size[1]),
        ]
      # If we have yielded all requested patches return.
      if number_of_yielded_patches >= number_of_patches:
        return
    # We failed to produce patches with the minimum overlapping requirements.
    # Reduce those requirements and try again.
    min_overlap_threshold = min_overlap_threshold * 0.95
    logging.debug(
        (
            'Overlapping constraints relaxed to min_overlap_threshold=%f while '
            'sampling positive patches for the abnormality %s'
        ),
        min_overlap_threshold,
        abnormality_filepath,
    )

  # This should not happen ever.
  raise ValueError(
      'Only %d positive patches of size %r could be sampled satisfying the '
      'current conditions (min. relative overlapping area = %f) for the '
      'abnormality %s'
      % (
          number_of_yielded_patches,
          patch_size,
          min_overlap_threshold,
          abnormality_filepath,
      )
  )


def _sample_negative_patches(
    image,
    image_filepath,
    abnormalities_masks,
    abnormalities_areas,
    patch_size,
    number_of_patches=10,
    min_breast_overlap_threshold=0.75,
    max_abnorm_overlap_threshold=0.35,
    max_number_of_trials_per_threshold=100,
):
  """Sample background patches from the image.

  The relative area of breast tissue in the patch must be, at least,
  `min_breast_overlap_threshold` of the total patch area. This is to prevent
  too easy negative examples.

  Similarly, the relative area of the abnormal tissue in the patch must be,
  at most, `max_abnorm_overlap_threshold`

  The relative area of the patch must overlap with the breast tissue with,
  at least, `min_breast_overlap_threshold` (relative) pixels.
  In addition, it must also overlap with abnormal tissue with, at most,
  `max_abnorm_overlap_threshold` (relative) pixels.

  Args:
    image: Image to patch from.
    image_filepath: Only used for logging.
    abnormalities_masks: List of binary mask of each abnormality in the image.
    abnormalities_areas: List of precomputed area of each abnormality.
    patch_size: Size of the patch to extract.
    number_of_patches: Number of negative patches to sample from the image.
    min_breast_overlap_threshold: Minimum (relative) number of breast pixels in
      the patch.
    max_abnorm_overlap_threshold: Maximum (relative) number of abnormal pixels
      in the patch.
    max_number_of_trials_per_threshold: Maximum number of random samples to try
      before reducing the `min_breast_overlap_threshold` by 5% and increasing
      the `max_abnorm_overlap_threshold` by 5%.

  Yields:
    The patch cropped from the input image.
  """
  cv2 = tfds.core.lazy_imports.cv2

  breast_mask = _get_breast_mask(image)

  def patch_overlapping_breast_is_feasible(y, x):
    """Return True if the patch contains enough breast pixels."""
    breast_in_patch = breast_mask[
        y : (y + patch_size[0]), x : (x + patch_size[1])
    ]
    return (
        np.sum(breast_in_patch > 0) / (patch_size[0] * patch_size[1])
        > min_breast_overlap_threshold
    )

  breast_roi = _get_roi_from_mask(breast_mask)
  breast_x, breast_y, breast_w, breast_h = cv2.boundingRect(breast_roi)
  number_of_yielded_patches = 0
  while (
      min_breast_overlap_threshold > 0.1 and max_abnorm_overlap_threshold < 0.9
  ):
    # Determine the region where random samples should be sampled from.
    max_h, min_h = max(breast_h, patch_size[0]), min(breast_h, patch_size[0])
    max_w, min_w = max(breast_w, patch_size[1]), min(breast_w, patch_size[1])
    min_y = breast_y - int((1.0 - min_breast_overlap_threshold) * max_h)
    min_x = breast_x - int((1.0 - min_breast_overlap_threshold) * max_w)
    max_y = breast_y + breast_h - int(min_breast_overlap_threshold * min_h)
    max_x = breast_x + breast_w - int(min_breast_overlap_threshold * min_w)
    # Ensure that all sampled batches are within the image.
    min_y = max(min_y, 0)
    min_x = max(min_x, 0)
    max_y = max(min(max_y, image.shape[0] - patch_size[0] - 1), min_y)
    max_x = max(min(max_x, image.shape[1] - patch_size[1] - 1), min_x)
    # Cap the number of trials if the sampling region is too small.
    effective_range_size = max_number_of_trials_per_threshold
    if (max_y - min_y + 1) * (max_x - min_x + 1) < effective_range_size:
      logging.debug(
          (
              'The sampling region for negative patches of size %r with '
              'min_breast_overlap_threshold=%f contains less possible patches '
              'than max_number_of_trials_per_threshold=%d, in mammography %s'
          ),
          patch_size,
          min_breast_overlap_threshold,
          max_number_of_trials_per_threshold,
          image_filepath,
      )
      effective_range_size = (max_y - min_y + 1) * (max_x - min_x + 1)
    for _ in range(effective_range_size):
      patch_y = np.random.randint(min_y, max_y + 1)
      patch_x = np.random.randint(min_x, max_x + 1)
      if patch_overlapping_breast_is_feasible(
          patch_y, patch_x
      ) and not _patch_overlaps_any_abnormality_above_threshold(
          patch_y,
          patch_x,
          patch_size,
          abnormalities_masks,
          abnormalities_areas,
          max_abnorm_overlap_threshold,
      ):
        number_of_yielded_patches += 1
        yield image[
            patch_y : (patch_y + patch_size[0]),
            patch_x : (patch_x + patch_size[1]),
        ]
      # If we have yielded all requested patches return.
      if number_of_yielded_patches >= number_of_patches:
        return
    # We failed to produce patches with the given overlapping requirements.
    # Relaxate the requirements and try again.
    min_breast_overlap_threshold = min_breast_overlap_threshold * 0.95
    max_abnorm_overlap_threshold = max_abnorm_overlap_threshold * 1.05
    logging.debug(
        (
            'Overlapping constraints relaxed to min_breast_overlap_threshold=%f'
            ' and max_abnorm_overlap_threshold=%f while sampling negative'
            ' patches for the mammography %s'
        ),
        min_breast_overlap_threshold,
        max_abnorm_overlap_threshold,
        image_filepath,
    )  # Filepath to the abnormality mask image.

  # This should not happen ever.
  raise ValueError(
      'Only %d negative patches of size %r could be sampled satisfying the '
      'current conditions (min. relative overlapping area with breast = %f, '
      'max. relative overlapping area with abnormalities = %f) for the '
      'mammography %s'
      % (
          number_of_yielded_patches,
          patch_size,
          min_breast_overlap_threshold,
          max_abnorm_overlap_threshold,
          image_filepath,
      )
  )
