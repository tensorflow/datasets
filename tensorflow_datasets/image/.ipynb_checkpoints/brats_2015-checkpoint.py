"""brats_2015 dataset."""
import tensorflow_datasets as tfds
import tensorflow as tf

import numpy as np
import os
import io
from medpy.io import load
# TODO(brats_2015): BibTeX citation
_CITATION = """
"""

# TODO(brats_2015):
_DESCRIPTION = """
"""

class Brats2015(tfds.core.GeneratorBasedBuilder):
  """TODO(brats_2015): Short description of my dataset."""

  # TODO(brats_2015): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  You can download the images from
  BRATS 2015 website
  Please put all files in manual_dir.
  """

  def _info(self):
    # TODO(brats_2015): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
        #The MRI image
        'image' : tfds.features.Tensor(shape=(240,240),dtype=tf.int16),
        ## The mask
        'mask' : tfds.features.Tensor(shape=(240,240),dtype = tf.int16),
        ## Tumor Type
        'type' : tfds.features.Text(),
        ## Modality
        'modality': tfds.features.Text(),
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('image','mask'),
        # Homepage of the dataset for documentation
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(brats_2015): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    if not tf.io.gfile.exists(dl_manager.manual_dir):
        msg = "You must download the dataset files manually and place them in: "
        msg += dl_manager.manual_dir
        raise AssertionError(msg)
        
    # There is no predefined train/val/test split for this dataset
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "filepath": dl_manager.manual_dir
            },
        ),
    ]
  def _generate_examples(self,filepath=None):
    """Yields examples."""
    # TODO(brats_2015): Yields (key, example) tuples from the dataset
    brats = filepath +'/BRATS2015_Training'
    for tumor_type in tf.io.gfile.listdir(brats):
        if tumor_type.startswith('.'):
            pass
        else:
            tumor_type_path = os.path.join(brats,tumor_type)
            for pat in tf.io.gfile.listdir(tumor_type_path):
                if pat.startswith('.'):
                    pass
                else:
                    pat_path = os.path.join(tumor_type_path,pat)
                    image_files = []
                    for file in tf.io.gfile.listdir(pat_path):
                        if file.startswith('.'):
                            pass
                        else:
                            if 'OT.' in file:
                                for image in tf.io.gfile.listdir(os.path.join(pat_path,file)):
                                    if image.endswith('.mha'):
                                        mask_file = os.path.join(pat_path,file,image)
                                        break

                            else:
                                for image in tf.io.gfile.listdir(os.path.join(pat_path,file)):
                                    if image.endswith('.mha'):
                                        image_files.append(os.path.join(pat_path,file,image))
                    mask_array,mask_header = load(mask_file)
                    mask_array  = mask_array.astype('int16')
                    total_slices = mask_array.shape[2]
                    for image in image_files:
                        modality = image.split('/')[-1].split('.')[-3].split('_')[-1]
                        image_array, image_header = load(image)
                        for current_slice in range(0,total_slices):
                            key = image.split('/')[-1].split('.')[-2]+'_'+modality+'_'+str(current_slice+1)
                            yield( key,
                                            {

                                                    'type' : tumor_type,
                                                    'modality': modality,
                                                    'image':image_array[:,:,current_slice],
                                                    'mask' : mask_array[:,:,current_slice],

                                            })

