"""CT_masks dataset."""

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
from tensorflow_datasets.core import utils
import numpy as np
import os
import io
import pydicom
import nibabel 




# BibTeX citation
_CITATION = """
\@misc{CT_Lymph_Nodes_Citation,
  doi = {10.1007/978-3-319-10404-1_65},
  url = {https://wiki.cancerimagingarchive.net/display/Public/CT+Lymph+Nodes#12d41e510fe547b59000cd90afb8dbf2},
  author = {Roth, Holger R., Lu, Le, Seff, Ari, Cherry, Kevin M., Hoffman, Joanne, Wang, Shijun, Liu, Jiamin, Turkbey, Evrim and Summers, Ronald M.},
  title = {A New 2.5D Representation for Lymph Node Detection Using Random Sets of Deep Convolutional Neural Network Observations},
  publisher = {Springer International Publishing},
  year = {2014},
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
  month = {Decembear},
  year = {2013},
  pages = {1045-1057},
}
"""

# Data Description
_DESCRIPTION = """
This dataset contains 110,013 Computed Tomography (CT) images of the mediastinum 
and abdomen in which lymph node positions are marked by radiologists at the 
National Institutes of Health, Clinical Center. These 10,013 images consist of 
388 mediastinal lymph nodes that come from 90 patients and a total of 595 
abdominal lymph nodes in 86 patients. All images are of 512*512 pixel arrays. 
"""

# Download Link
_masks_url = """https://wiki.cancerimagingarchive.net/download/attachments/19726546/MED_ABD_LYMPH_MASKS.zip?version=1&modificationDate=1449684916503&api=v2
"""

class CT_masks(tfds.core.GeneratorBasedBuilder):
  """This is a dataset containing CT images of lymph nodes from NIH"""

  #Set up version.
  VERSION = tfds.core.Version('1.0.0')

  
  

  def _info(self):
    # Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            
            # These are the features of your dataset like images, labels ...
     
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        
        
        ## The mask
        'mask' : tfds.features.Tensor(shape=(512,512),dtype = tf.int16),
            
        }),
        # supervised_keys=('id','mask'),
        # Homepage of the dataset for documentation
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    
    masks_path = dl_manager.download_and_extract(_masks_url)
        
    # There is no predefined train/val/test split for this dataset
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={'filepath':masks_path},
        )
    ]

  def _generate_examples(self,filepath=None):
    """Yields examples for the CT lymph nodes dataset
    Args:
        filepath: path to the CT lymph nodes files
    Yields:
        Dictionaries with images and masks
    
    """
    ## Each patient has his own folder of masks and images, and the patient id is the same in masks and images
    patients = tf.io.gfile.listdir(os.path.join(filepath,'MED_ABD_LYMPH_MASKS'))
    patients.sort()
    

    ## iterate over all masks folders
    
    for patient_id in patients:
        try:
            mask = tf.io.gfile.listdir(os.path.join(filepath,'MED_ABD_LYMPH_MASKS',patient_id))
            if mask[0].endswith('.nii.gz'):
                file_name = os.path.join(filepath,'MED_ABD_LYMPH_MASKS',patient_id,mask[0])
                yield file_name,
                {
                    
                    'mask' : nibabel.load(file_name).get_fdata(),
                    
                }
        except:
            pass

    

    
