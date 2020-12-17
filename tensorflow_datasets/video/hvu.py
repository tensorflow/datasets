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

# Lint as: python3
"""Holistic Video Understanding dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from zipfile import ZipFile
import pandas as pd

from tensorflow_datasets.video.hvu_download import main as download_videos

_CITATION = """
@article{hvu2019,
  title={Large Scale Holistic Video Understanding},
  author={Diba, Ali and Fayyaz, Mohsen and Sharma, Vivek and Paluri, Manohar and Gall, J{\"u}rgen and Stiefelhagen, Rainer and Van Gool, Luc},
  journal={arXiv preprint arXiv:1904.11451},
  year={2019}
}
"""

_DESCRIPTION = """
Action recognition has been advanced in recent years by benchmarks with rich annotations.
However, research is still mainly limited to human action or sports recognition -
focusing on a highly specific video understanding task and thus leaving a significant
gap towards describing the overall content of a video. We fill in this gap by presenting
a large-scale "Holistic Video Understanding Dataset"~(HVU).

HVU is organized hierarchically in a semantic taxonomy that focuses on multi-label and
multi-task video understanding as a comprehensive problem that encompasses the recognition
of multiple semantic aspects in the dynamic scene.

HVU contains approx.~577k videos in total with ~13M annotations for training and
validation set spanning over ~3k classes.
HVU encompasses semantic aspects defined on categories of scenes, objects, actions, events,
attributes and concepts, which naturally captures the real-world scenarios.
"""

_URL = "https://github.com/holistic-video-understanding/HVU-Dataset/archive/master.zip"
_HOME = "https://holistic-video-understanding.github.io/"

TRAIN_FILENAME = 'HVU_Train_V1.0.zip'
VALIDATION_FILENAME = 'HVU_Val_V1.0.zip'
CATEGORIES = 'HVU_Tags_Categories_V1.0.csv'

class HvuConfig(tfds.core.BuilderConfig):
    """Configuration for HVU rescaling"""

    @tfds.core.disallow_positional_args
    def __init__(self,sample_dataset = False, width=None, height=None, **kwargs):
        """The parameters specifying how the dataset is processed

        If `width` and `height` are set, the videos
        will be rescaled to have those heights and widths (using ffmpeg).

        Args:
          width: An integer with the width or None.
          height: An integer with the height or None.
          **kwargs: Passed on to the constructor of `BuilderConfig`."""

        super(HvuConfig, self).__init__(
            version=tfds.core.Version('1.0.0'), **kwargs)
        if (width is None) ^ (height is None):
          raise ValueError('Either both dimensions should be set, or none of them')
        self.sample_dataset = sample_dataset
        self.width = width
        self.height = height

class Hvu(tfds.core.BeamBasedBuilder):
  """Holistic Video Understanding(HVU) dataset."""

  BUILDER_CONFIGS = [
      HvuConfig(
          name='hvu_sample_64',
          description='64x64 Sample HVU Dataset',
          sample_dataset = True,
          width=64,
          height=64,
      ),
      HvuConfig(
          name='hvu_sample_128',
          description='128x128 Sample HVU Dataset',
          sample_dataset = True,
          width=128,
          height=128,
      ),
      HvuConfig(
          name='hvu_64',
          description='64x64 HVU Dataset',
          sample_dataset = False,
          width=64,
          height=64,
      ),
      HvuConfig(
          name='hvu_128',
          description='128x128 HVU Dataset',
          sample_dataset=False,
          width=128,
          height=128,
      )
          ]

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    if self.builder_config.width is not None:
      if self.builder_config.height is None:
        raise ValueError('Provide either both height and width or none.')
      ffmpeg_extra_args = (
          '-vf', 'scale={}x{}'.format(self.builder_config.height,
                                      self.builder_config.width))
    else:
      ffmpeg_extra_args = []

    video_shape = (
        None, self.builder_config.height, self.builder_config.width, 3)

    features=tfds.features.FeaturesDict({
        # Video frames: uint8 [None, Time, Width, Height, Channels]
        'video': tfds.features.Video(
            video_shape,
            ffmpeg_extra_args=ffmpeg_extra_args,
            encoding_format='png'),
        #Annotation for the concerned video [String separated by '|']
        "annotations" : tfds.features.Text()
        })

    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        features=features,
        # Homepage of the dataset for documentation
        homepage=_HOME,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    #Downloading and extracting all the zip files to get the training and validation CSVs
    zip_dir = dl_manager.download(_URL)
    download_dir = zip_dir[: zip_dir.rfind('/') + 1]

    with ZipFile(zip_dir, 'r') as zip:
        zip.extractall(download_dir)
    extracted_dir = download_dir + 'HVU-Dataset-master/'

    with ZipFile(extracted_dir + TRAIN_FILENAME,'r') as zip:
        zip.extractall(extracted_dir)

    with ZipFile(extracted_dir + VALIDATION_FILENAME, 'r') as zip:
        zip.extractall(extracted_dir)

    print("\n###################        Data Downloaded        ####################\n")
    TRAIN_CSV = extracted_dir + 'HVU_Train_V1.0.csv'
    VALID_CSV = extracted_dir + 'HVU_Val_V1.0.csv'

    if self.builder_config.sample_dataset:
        data_train = download_videos(TRAIN_CSV,extracted_dir,sample_dataset=True)
        data_val = download_videos(VALID_CSV,extracted_dir,sample_dataset=True)
    else:
        data_train = download_videos(TRAIN_CSV,extracted_dir)
        data_val = download_videos(VALID_CSV,extracted_dir)

    print("\n####################        Videos downloaded and trimmed        ####################\n")

    data_train = pd.DataFrame(data_train)
    data_val = pd.DataFrame(data_val)
    #Removing the duplicates
    data_train.drop_duplicates(subset = 'Filename', keep = 'first', inplace = True)
    data_val.drop_duplicates(subset = 'Filename', keep = 'first', inplace = True)

    data_train.to_csv(extracted_dir + 'train.csv')
    data_val.to_csv(extracted_dir + 'val.csv')

    print("\n####################        Data Saved        ####################\n")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={ 'file_path' : extracted_dir + 'train.csv',
                         'video_path' : extracted_dir},
        ),
        tfds.core.SplitGenerator(
            name = tfds.Split.TEST,
            gen_kwargs = { 'file_path' : extracted_dir + 'val.csv',
                           'video_path' : extracted_dir},
        )
    ]

  def _build_pcollection(self,pipeline,file_path,video_path):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam
    data = pd.read_csv(file_path)
    filenames = data['Filename'].values.tolist()
    def _process_example(filename):
        features = {
            "video" : video_path + filename + '.mp4',
            "annotations" : data[data['Filename'] == filename]['Annotations'].values[0],
        }
        return filename, features
    return (
        pipeline
        | beam.Create(filenames)
        | beam.Map(_process_example)
    )
