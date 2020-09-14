"""covid_cxr dataset."""

import tensorflow_datasets.public_api as tfds
import os

_CITATION = """
@misc{wang2020covidnet,
    title={COVID-Net: A Tailored Deep Convolutional Neural Network Design for Detection of COVID-19 Cases from Chest Radiography Images},
    author={Linda Wang, Zhong Qiu Lin and Alexander Wong},
    year={2020},
    eprint={2003.09871},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
"""


_DESCRIPTION = """
    This dataset contains....
    
    We have provided three builder configurations for the user to choose from. The 'original' config includes images in varying resolutions and in .png image format. The 224 config has all images in 224x224 resolution and in the .png format. The 480 config has all the images in 480x480 resolution and in .png format. Both these resolutions were used by Wang et al. to build COVID-Net - a deep CNN for detecting COVID-19 cases from chest radiography images. 

    The test set was created as per Wang et al.'s split. We have kept this consistent to faciliate comparison and encourage uniformity. Details and the code about the split can be found https://github.com/lindawangg/COVID-Net/blob/master/create_COVIDx.ipynb 
    
    The training set has 507 COVID-19, 7966 normal, and 5468 pneumonia images. The test set has 100 COVID-19, 885 normal, and 594 pneumonia images. These counts remain consistent along all resolution configurations.
"""


_TEST_224_URL       = 'https://drive.google.com/uc?export=download&id=1ZzrVZlDSzzHew92lWF5VWoabXQXeeZh2'
_TEST_480_URL       = 'https://drive.google.com/uc?export=download&id=1WDoHmfsrSGivArnZoLujUEbJBsFEnOid'
_TEST_ORIGINAL_URL  = 'https://drive.google.com/uc?export=download&id=1Wq5fqLkzfDDv4iEF5MTyBAbp50Bz1RHl'

_TRAIN_224_URL      = 'https://drive.google.com/uc?export=download&id=1LsC-a1Ig5sUmFbWFg2sus9XB-Ex8bkC_'
_TRAIN_480_URL      = 'https://drive.google.com/uc?export=download&id=1slHH_yHdiiHc0q5OTL7txcG47HA-yjfQ'
_TRAIN_ORIGINAL_URL = 'https://drive.google.com/uc?export=download&id=1FrxYfLLg1FDOUzvGyZBnVt5vwGAErjtN'

_DATA_OPTIONS = ['original', 480, 224] #The 3 builder configurations

class CovidCxrConfig(tfds.core.BuilderConfig):
  """BuilderConfig for covid_cxr."""

  def __init__(self, resolution, **kwargs):
    """BuilderConfig
    Args:
      resolution: Resolution of the image. Values supported: original, 480, 224
      **kwargs: keyword arguments forwarded to super.
    """
    if resolution not in _DATA_OPTIONS:
        raise ValueError('selection must be one of %s' % _DATA_OPTIONS)
        
    v2 = tfds.core.Version(
        '2.0.0', 'New split API (https://tensorflow.org/datasets/splits)')
    
    super(CovidCxrConfig, self).__init__(version = v2, 
                                name = '%s' % resolution, 
                                description = 'Covid-19 Chest X-ray images in %s x %s resolution' % (resolution, resolution),
                                **kwargs)
    self.resolution = resolution
    
class CovidCxr(tfds.core.GeneratorBasedBuilder):

  VERSION = tfds.core.Version('0.1.0')
    
  BUILDER_CONFIGS = [
      CovidCxrConfig(resolution='original'),
      CovidCxrConfig(resolution=480),
      CovidCxrConfig(resolution=224),
  ]

  def _info(self):
    if self.builder_config.resolution == 'original':
        shape_res = None
    elif self.builder_config.resolution == 480:
        shape_res = (self.builder_config.resolution, self.builder_config.resolution, 3)
    elif self.builder_config.resolution == 224:
        shape_res = (self.builder_config.resolution, self.builder_config.resolution, 3)
        
    return tfds.core.DatasetInfo(
        builder = self,
        description = _DESCRIPTION,
        
        features = tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape = shape_res, 
                                         dtype = 'uint8', 
                                         encoding_format = 'png'),
            
            "label": tfds.features.ClassLabel(
                names = ["COVID-19", "normal", "pneumonia"]), # 3 labels
        }),

        supervised_keys = ('image', 'label'), 
        
        homepage = 'https://github.com/lindawangg/COVID-Net',
        citation = _CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    
    if self.builder_config.resolution == 'original':
        train_path, test_path = dl_manager.download([_TRAIN_ORIGINAL_URL, _TEST_ORIGINAL_URL])
    elif self.builder_config.resolution == 480:
        train_path, test_path = dl_manager.download([_TRAIN_480_URL, _TEST_480_URL])
    elif self.builder_config.resolution == 224:
        train_path, test_path = dl_manager.download([_TRAIN_224_URL, _TEST_224_URL])
        
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": dl_manager.iter_archive(train_path),
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": dl_manager.iter_archive(test_path),
            }),
    ]

  def _generate_examples(self, archive):
    """Yields examples.
  
    Generate chest x-ray images and labels given the directory path.
    
    Args:
      archive: object iterating the zip file.
    Yields:
      The image and its corresponding label.
      
    """

    for fname, fobj in archive:
            image_dir, image_file = os.path.split(fname)
            d = os.path.basename(image_dir)
            record = {"image": fobj, "label": d}
            yield "%s/%s" % (image_file, d), record

