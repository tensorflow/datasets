"""wake_vision dataset."""

import tensorflow_datasets.public_api as tfds

_TRAIN_IMAGE_IDS = [9270406, 9270356, 9270408, 9270367, 9270349, 9270351, 9270390, 9270375, 9270387, 9270370, 9270396, 9270340, 9270411, 9270369, 9270357, 9270378, 9270386, 9270376, 9270341, 9270392, 9270334, 9270404, 9270330, 9270321, 9270364, 9270380, 9270343, 9270335, 9270412, 9270362, 9270339, 9270331, 9270399, 9270410, 9270393, 9270325, 9270346, 9270337, 9270391, 9270361, 9270363, 9270372, 9270326, 9270322, 9270329, 9270381, 9270338, 9270397, 9270405, 9270379, 9270352, 9270400, 9270384, 9270383, 9270388, 9270324, 9270407, 9270348, 9270347, 9270371, 9270358, 9270350, 9270323, 9270401, 9270368, 9270360, 9270328, 9270327, 9270382, 9270332, 9270394, 9270409, 9270345, 9270342, 9270353, 9270403, 9270398, 9270402, 9270395, 9270333, 9270373, 9270336, 9270385, 9270320, 9270366, 9270374, 9270377, 9270354, 9270344, 9270359]

_URLS = {
    'train_images': [
      tfds.download.Resource(
        url=f'https://dataverse.harvard.edu/api/access/datafile/{id}?format=original',
        extract_method=tfds.download.ExtractMethod.GZIP,
      )
      for id in _TRAIN_IMAGE_IDS
    ],
    'validation_images': tfds.download.Resource(
      url='https://dataverse.harvard.edu/api/access/datafile/9270355?format=original',
      extract_method=tfds.download.ExtractMethod.GZIP,
    ),
    'test_images': tfds.download.Resource(
      url='https://dataverse.harvard.edu/api/access/datafile/9270389?format=original',
      extract_method=tfds.download.ExtractMethod.GZIP,
    ),
    'train_image_metadata': 'https://dataverse.harvard.edu/api/access/datafile/9844933?format=original',
    'train_bbox_metadata': 'https://dataverse.harvard.edu/api/access/datafile/9844934?format=original',
    'validation_metadata': 'https://dataverse.harvard.edu/api/access/datafile/9844936?format=original',
    'test_metadata': 'https://dataverse.harvard.edu/api/access/datafile/9844935?format=original',
}

class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wake_vision dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial TensorFlow Datasets release. Note that this is based on the 2.0 version of Wake Vision on Harvard Dataverse.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        description=
        """
        The Wake Vision dataset for person detection.

        The dataset contains images with annotations of whether each image contains a person. Additional annotations about perceived gender, perceived age, subject distance, lighting conditions, depictions, and specific body parts are also available for some subsets of the dataset.

        We publish the annotations of this dataset under a CC BY 4.0 license. All images in the dataset are from the Open Images v7 dataset, which sourced images from Flickr listed as having a CC BY 2.0 license.
        """
        ,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(None, None, 3)),
            'filename': tfds.features.Text(),
            'person': tfds.features.ClassLabel(names=['No', 'Yes']),
            'depiction': tfds.features.ClassLabel(names=['No', 'Yes']),
            'body_part': tfds.features.ClassLabel(names=['No', 'Yes']),
            'predominantly_female': tfds.features.ClassLabel(names=['No', 'Yes']),
            'predominantly_male': tfds.features.ClassLabel(names=['No', 'Yes']),
            'gender_unknown': tfds.features.ClassLabel(names=['No', 'Yes']),
            'young': tfds.features.ClassLabel(names=['No', 'Yes']),
            'middle_age': tfds.features.ClassLabel(names=['No', 'Yes']),
            'older': tfds.features.ClassLabel(names=['No', 'Yes']),
            'age_unknown': tfds.features.ClassLabel(names=['No', 'Yes']),
            'near': tfds.features.ClassLabel(names=['No', 'Yes']),
            'medium_distance': tfds.features.ClassLabel(names=['No', 'Yes']),
            'far': tfds.features.ClassLabel(names=['No', 'Yes']),
            'dark': tfds.features.ClassLabel(names=['No', 'Yes']),
            'normal_lighting': tfds.features.ClassLabel(names=['No', 'Yes']),
            'bright': tfds.features.ClassLabel(names=['No', 'Yes']),
            'person_depiction': tfds.features.ClassLabel(names=['No', 'Yes']),
            'non-person_depiction': tfds.features.ClassLabel(names=['No', 'Yes']),
            'non-person_non-depiction': tfds.features.ClassLabel(names=['No', 'Yes']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'person'),  # Set to `None` to disable
        homepage='https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2F1HOPXC',
        license='See homepage for license information.',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    paths = dl_manager.download_and_extract(_URLS)

    return {
        'train_image': self._generate_examples(paths['train_images'], paths['train_image_metadata']),
        'train_bbox': self._generate_examples(paths['train_images'], paths['train_bbox_metadata']),
        'validation' : self._generate_examples(paths['validation_images'], paths['validation_metadata']),
        'test' : self._generate_examples(paths['test_images'], paths['test_metadata']),
    }

  def _generate_examples(self, image_paths, metadata_path):
    """Yields examples."""
    metadata = tfds.core.lazy_imports.pandas.read_csv(metadata_path, index_col='filename')

    for tar_file in image_paths:
      for sample_path, sample_object in tfds.download.iter_archive(tar_file, tfds.download.ExtractMethod.TAR_STREAM):
        file_name = sample_path

        if file_name not in metadata.index:
            continue

        sample_metadata = metadata.loc[file_name]

        yield file_name, {
            'image': sample_object,
            'filename': file_name,
            'person': sample_metadata['person'],
            'depiction': sample_metadata.get('depiction', -1),
            'body_part': sample_metadata.get('body_part', -1),
            'predominantly_female': sample_metadata.get('predominantly_female', -1),
            'predominantly_male': sample_metadata.get('predominantly_male',-1),
            'gender_unknown': sample_metadata.get('gender_unknown', -1),
            'young': sample_metadata.get('young', -1),
            'middle_age': sample_metadata.get('middle_age', -1),
            'older': sample_metadata.get('older', -1),
            'age_unknown': sample_metadata.get('age_unknown', -1),
            'near': sample_metadata.get('near', -1),
            'medium_distance': sample_metadata.get('medium_distance', -1),
            'far': sample_metadata.get('far', -1),
            'dark': sample_metadata.get('dark', -1),
            'normal_lighting': sample_metadata.get('normal_lighting', -1),
            'bright': sample_metadata.get('bright', -1),
            'person_depiction': sample_metadata.get('person_depiction', -1),
            'non-person_depiction': sample_metadata.get('non-person_depiction', -1),
            'non-person_non-depiction': sample_metadata.get('non-person_non-depiction', -1),
        }
