# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""controlled_noisy_web_labels dataset."""

import csv
import dataclasses
import io
import json
import os

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Controlled Noisy Web Labels is a collection of ~212,000 URLs to images in which
every image is carefully annotated by 3-5 labeling professionals by Google Cloud
Data Labeling Service. Using these annotations, it establishes the first
benchmark of controlled real-world label noise from the web.

We provide the Red Mini-ImageNet (real-world web noise) and Blue Mini-ImageNet
configs:
  - controlled_noisy_web_labels/mini_imagenet_red
  - controlled_noisy_web_labels/mini_imagenet_blue

Each config contains ten variants with ten noise-levels p from 0% to 80%. The
validation set has clean labels and is shared across all noisy training sets.
Therefore, each config has the following splits:

  - train_00
  - train_05
  - train_10
  - train_15
  - train_20
  - train_30
  - train_40
  - train_50
  - train_60
  - train_80
  - validation

The details for dataset construction and analysis can be found in the paper.
All images are resized to 84x84 resolution.

"""

_CITATION = """
@inproceedings{jiang2020beyond,
  title={Beyond synthetic noise: Deep learning on controlled noisy labels},
  author={Jiang, Lu and Huang, Di and Liu, Mason and Yang, Weilong},
  booktitle={International Conference on Machine Learning},
  pages={4804--4815},
  year={2020},
  organization={PMLR}
}
"""

_PERCENTS = [0, 5, 10, 15, 20, 30, 40, 50, 60, 80]

# n01440764 is not part of mini-ImageNet but we add it here for testing
_IMNET_MINI_SYNSETS = [
    'n01704323',
    'n04515003',
    'n02101006',
    'n03062245',
    'n04509417',
    'n03854065',
    'n02110063',
    'n03998194',
    'n02111277',
    'n04443257',
    'n02165456',
    'n03075370',
    'n02747177',
    'n01558993',
    'n04149813',
    'n03220513',
    'n03584254',
    'n04243546',
    'n03770439',
    'n02108915',
    'n02971356',
    'n02108551',
    'n03908618',
    'n01981276',
    'n03535780',
    'n04275548',
    'n03272010',
    'n02138441',
    'n03337140',
    'n07584110',
    'n01910747',
    'n03146219',
    'n02443484',
    'n04146614',
    'n02113712',
    'n02981792',
    'n04251144',
    'n03838899',
    'n04604644',
    'n02116738',
    'n02099601',
    'n02966193',
    'n02687172',
    'n03924679',
    'n02120079',
    'n03476684',
    'n04435653',
    'n02091244',
    'n01843383',
    'n01532829',
    'n03980874',
    'n07613480',
    'n03544143',
    'n03347037',
    'n02114548',
    'n06794110',
    'n04258138',
    'n02606052',
    'n02105505',
    'n02871525',
    'n03127925',
    'n04418357',
    'n04389033',
    'n02074367',
    'n02110341',
    'n13133613',
    'n03773504',
    'n13054560',
    'n07747607',
    'n04522168',
    'n02089867',
    'n02129165',
    'n02457408',
    'n03676483',
    'n09256479',
    'n04067472',
    'n02823428',
    'n01749939',
    'n03400231',
    'n04596742',
    'n01855672',
    'n02174001',
    'n04612504',
    'n03047690',
    'n02091831',
    'n03017168',
    'n04296562',
    'n02108089',
    'n09246464',
    'n02219486',
    'n02950826',
    'n01770081',
    'n03775546',
    'n01930112',
    'n03888605',
    'n03417042',
    'n03527444',
    'n02795169',
    'n07697537',
    'n03207743',
    'n01440764',
]

MINI_IMAGENET_TRAIN = 'https://raw.githubusercontent.com/yaoyao-liu/mini-imagenet-tools/main/csv_files/train.csv'
MINI_IMAGENET_VAL = 'https://raw.githubusercontent.com/yaoyao-liu/mini-imagenet-tools/main/csv_files/val.csv'
MINI_IMAGENET_TEST = 'https://raw.githubusercontent.com/yaoyao-liu/mini-imagenet-tools/main/csv_files/test.csv'


@dataclasses.dataclass
class ControlledNoisyWebLabelsConfig(tfds.core.BuilderConfig):
  name: str = ''
  dataset: str = 'mini_imagenet'
  color: str = ''
  num_classes: int = 100


class ControlledNoisyWebLabels(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for controlled_noisy_web_labels dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  In order to manually download this data, a user must perform the
  following operations:
  
  1. Download the splits and the annotations [here](https://storage.googleapis.com/cnlw/dataset_no_images.zip)
  2. Extract dataset_no_images.zip to dataset_no_images/.
  3. Download all images in dataset_no_images/mini-imagenet-annotations.json into
  a new folder named dataset_no_images/noisy_images/. The output filename must
  agree with the image id provided in mini-imagenet-annotations.json. For example,
  if "image/id": "5922767e5677aef4", then the downloaded image should be
  dataset_no_images/noisy_images/5922767e5677aef4.jpg.
  4.Register on https://image-net.org/download-images and download
  ILSVRC2012_img_train.tar and ILSVRC2012_img_val.tar.

  The resulting directory structure may then be processed by TFDS:

  - dataset_no_images/
    - mini-imagenet/
      - class_name.txt
      - split/
        - blue_noise_nl_0.0
        - blue_noise_nl_0.1
        - ...
        - red_noise_nl_0.0
        - red_noise_nl_0.1
        - ...
        - clean_validation
    - mini-imagenet-annotations.json
  - ILSVRC2012_img_train.tar
  - ILSVRC2012_img_val.tar
  - noisy_images/
    - 5922767e5677aef4.jpg

  """
  # pytype: disable=wrong-keyword-args
  BUILDER_CONFIGS = [
      ControlledNoisyWebLabelsConfig(
          name='mini_imagenet_red',
          dataset='mini_imagenet',
          color='red',
          num_classes=100,
      ),
      ControlledNoisyWebLabelsConfig(
          name='mini_imagenet_blue',
          dataset='mini_imagenet',
          color='blue',
          num_classes=100,
      ),
  ]

  # pytype: enable=wrong-keyword-args

  def _read_mini_imagenet_csv(self, path):
    fnames = []
    with tf.io.gfile.GFile(path, 'r') as f:
      reader = csv.reader(f)
      next(reader, None)
      for data in reader:
        fnames.append(data[0])
    return fnames

  def _resize_image(self, buf, resolution=84):
    cv2 = tfds.core.lazy_imports.cv2

    image = cv2.imdecode(np.frombuffer(buf, dtype=np.uint8), flags=3)
    im_resized = cv2.resize(
        image, (resolution, resolution), interpolation=cv2.INTER_AREA
    )
    _, buff = cv2.imencode(
        '.jpg', im_resized, [int(cv2.IMWRITE_JPEG_QUALITY), 72]
    )
    return buff.tobytes()

  def _get_clean_images(self, fnames, archive):
    clean_image_dict = {}

    fnames = set(fnames)

    # The files names in mini-ImageNet contain the absolute index wrt to the
    # synset. For example, {synset_name}_{idx}.jpg, where synset_name is
    # something like n01440764, and idx is between 1 and 1000. We want to create
    # a mapping between synset and the indices of the images that we need for
    # the corresponding synset
    synset_to_index = {}
    for name in fnames:
      # Remove .jpg
      name = name[:-4]
      # Synset name is the first 8 characters
      synset_name = name[:9]
      # Synset index is the last 8 characters
      synset_index = int(name[-4:])

      if synset_name in synset_to_index:
        synset_to_index[synset_name].append(synset_index)
      else:
        synset_to_index[synset_name] = [synset_index]

    for fname, fobj in archive:
      label = fname[:-4]  # fname is something like 'n01632458.tar'
      # TODO(b/117643231): in py3, the following lines trigger tarfile module
      # to call `fobj.seekable()`, which Gfile doesn't have. We should find an
      # alternative, as this loads ~150MB in RAM.

      if label not in _IMNET_MINI_SYNSETS or label not in synset_to_index:
        continue
      fobj_mem = io.BytesIO(fobj.read())

      # We obtain all filenames for a given subset (i.e. n01440764_10,
      # n0144076_2020) and sort them, so that we can find the indices of images
      # that we need to keep
      all_image_names = [
          image_fname
          for image_fname, _ in tfds.download.iter_archive(
              fobj_mem, tfds.download.ExtractMethod.TAR_STREAM
          )
      ]

      # Remove .JPEG, and remove the part after _, i.e. want to retain
      # 1 from n01440764_1
      image_indices = [
          int(name[:-5].split('_')[-1]) for name in all_image_names
      ]

      # Sort filenames
      sorted_indices = np.argsort(image_indices)

      # Get the indices of images to select
      images_to_select = np.asarray(synset_to_index[label]) - 1

      # Get the filenames of images to select
      selected_indices = sorted_indices[images_to_select]
      selected_fnames = [all_image_names[idx] for idx in selected_indices]
      fname_to_idx = dict(zip(selected_fnames, synset_to_index[label]))

      # We use set here for faster lookup in the loop
      selected_fnames = set(selected_fnames)

      # integer label corresponding to the synset
      synset_int_label = _IMNET_MINI_SYNSETS.index(label)

      # Go to the beginning of the file
      fobj.seek(0)
      fobj_mem = io.BytesIO(fobj.read())

      for image_fname, image in tfds.download.iter_archive(
          fobj_mem, tfds.download.ExtractMethod.TAR_STREAM
      ):  # pytype: disable=wrong-arg-types  # gen-stub-imports
        if image_fname in selected_fnames:
          # Convert the image ID back to mini-Imagenet style, e.g.
          # n0144076400000009.jpg, for a quick access later
          image_index = str(fname_to_idx[image_fname]).zfill(8)
          new_image_id = label + image_index + '.jpg'
          buf = image.read()
          clean_image_dict[new_image_id] = (
              self._resize_image(buf),
              synset_int_label,
          )

    return clean_image_dict

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features = {}
    features['image'] = tfds.features.Image()
    features['label'] = tfds.features.ClassLabel(
        num_classes=self.builder_config.num_classes
    )
    features['is_clean'] = tfds.features.Tensor(shape=(), dtype=np.bool_)
    features['id'] = tfds.features.Text()

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'label'),  # Set to `None` to disable
        homepage=(
            'https://google.github.io/controlled-noisy-web-labels/index.html'
        ),
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    imnet_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_train.tar')
    noisy_images_path = os.path.join(dl_manager.manual_dir, 'noisy_images')
    noisy_split_path = os.path.join(
        dl_manager.manual_dir, 'dataset_no_images', 'mini-imagenet', 'split'
    )
    noisy_annot_path = os.path.join(
        dl_manager.manual_dir,
        'dataset_no_images',
        'mini-imagenet-annotations.json',
    )
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')

    with epath.Path(noisy_annot_path).open() as json_file:
      data = json.load(json_file)

    image_data = data['data']
    noisy_image_ids = [elem[0]['image/id'] + '.jpg' for elem in image_data]

    # We first load all mini-ImageNet images in the memory, and
    # will access them for the other splits
    paths = dl_manager.download({
        'mini_train': MINI_IMAGENET_TRAIN,
        'mini_val': MINI_IMAGENET_VAL,
        'mini_test': MINI_IMAGENET_TEST,
    })

    train_fnames = self._read_mini_imagenet_csv(paths['mini_train'])
    val_fnames = self._read_mini_imagenet_csv(paths['mini_val'])
    test_fnames = self._read_mini_imagenet_csv(paths['mini_test'])
    mini_imnet_fnames = train_fnames + val_fnames + test_fnames

    mini_imnet_images = self._get_clean_images(
        mini_imnet_fnames, dl_manager.iter_archive(imnet_path)
    )

    val_split_file = os.path.join(noisy_split_path, 'clean_validation')

    split_to_generator = {}

    split_to_generator[tfds.Split.VALIDATION] = self._generate_val_examples(
        val_split_file, dl_manager.iter_archive(val_path)
    )

    for percent in _PERCENTS:
      split_name = tfds.Split.TRAIN + '_' + '{:02d}'.format(percent)
      split_file = os.path.join(
          noisy_split_path,
          '{}_noise_nl_{}'.format(
              self.builder_config.color, str(percent / 100)
          ),
      )
      split_to_generator[split_name] = self._generate_examples(
          split_file, noisy_image_ids, noisy_images_path, mini_imnet_images
      )

    return split_to_generator

  def _generate_val_examples(self, split_file, archive):
    """Yields examples for the validation set."""
    with epath.Path(split_file).open() as fp:
      split_info = fp.read().splitlines()

    split_names, split_labels = map(
        list, zip(*[elem.split(' ') for elem in split_info])
    )

    for fname, fobj in archive:
      # Remove the .JPEG
      fname = fname[:-5]
      if fname + '.jpg' in split_names:
        label_idx = split_names.index(fname + '.jpg')
        example = {}
        example['is_clean'] = 1
        buf = fobj.read()
        example['image'] = self._resize_image(buf)
        example['label'] = int(split_labels[label_idx])
        example['id'] = fname

        yield fname, example

  def _generate_examples(
      self, split_file, noisy_image_ids, noisy_images_path, clean_images
  ):
    """Yields examples."""

    with epath.Path(split_file).open() as fp:
      split_info = fp.read().splitlines()

    split_names, split_labels = map(
        list, zip(*[elem.split(' ') for elem in split_info])
    )

    # We use a set here because searching in a set is faster than a list
    noisy_image_ids = set(noisy_image_ids)

    for imname, label in zip(split_names, split_labels):
      example = {}
      if imname in noisy_image_ids:
        # If the image comes from noise image list, it's not clean
        example['is_clean'] = 0
        with tf.io.gfile.GFile(
            os.path.join(noisy_images_path, imname), 'rb'
        ) as f:
          example['image'] = self._resize_image(f.read())
      else:
        example['image'] = clean_images[imname][0]
        # Check if the assigned label and the real label is the same
        if clean_images[imname][1] == int(label):
          example['is_clean'] = 1
        else:
          example['is_clean'] = 0

      example['label'] = int(label)
      example['id'] = imname[:-4]
      yield imname[:-4], example
