"""CT_Lymph_Nodes dataset."""

import tensorflow_datasets.public_api as tfds
import tensorflow.compat.v2 as tf
import os
import io
import pydicom
import nibabel 

# BibTeX citation
_CITATION = """
\@misc{CT_Lymph_Nodes_Citation,
  doi = {10.1007/978-3-319-10404-1_65},
  url = {https://wiki.cancerimagingarchive.net/display/Public/CT+Lymph+Nodes},
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



class CtLymphNodes(tfds.core.GeneratorBasedBuilder):
  """This is a dataset containing CT images of lymph nodes from NIH"""

  #Set up version.
  VERSION = tfds.core.Version('0.1.0')

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  You can download the images from
  https://console.cloud.google.com/storage/browser/bme590/jingjing
  Please put all files in manual_dir.
  """
  

  def _info(self):
    # Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
        
        #The CT image
        'image' : tfds.features.Tensor(shape=(512,512),dtype=tf.int16),
        ## The mask
        'mask' : tfds.features.Tensor(shape=(512,512),dtype = tf.int16),
        ## Patient Age
        'age'  : tfds.features.Text(),
        ## Patient Sex
        'sex'  : tfds.features.Text(),
        ## Body Part Examined
        'body_part'  : tfds.features.Text()
            
        }),
        supervised_keys=('image','mask'),
        # Homepage of the dataset for documentation
        homepage='https://wiki.cancerimagingarchive.net/display/Public/CT+Lymph+Nodes',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    
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
    """Yields examples for the CT lymph nodes dataset
    Args:
        filepath: path to the CT lymph nodes files
    Yields:
        Dictionaries with images and masks
    
    """
    ## Each patient has his own folder of masks and images, and the patient id is the same in masks and images
    patients = tf.io.gfile.listdir(os.path.join(filepath,'MED_ABD_LYMPH_MASKS'))
    for patient_id in patients:
            i = 0
            if patient_id.startswith('.'):
                pass
            else:
                mask_path = os.path.join(filepath,'MED_ABD_LYMPH_MASKS',patient_id,patient_id+'_mask.nii.gz')
                with tf.io.gfile.GFile(mask_path) as f:
                    mask_file = tfds.core.lazy_imports.nibabel.load(f.name).get_fdata().astype('int16')
                    images = tf.io.gfile.listdir(os.path.join(filepath,'MED_ABD_LYMPH_IMAGES',patient_id))
                    for file in images:
                        file_name= os.path.join(filepath,'MED_ABD_LYMPH_IMAGES',patient_id,file)
                        if file_name.endswith('dcm'):
                            with tf.io.gfile.GFile(file_name) as i_f:
                                image_file = tfds.core.lazy_imports.pydicom.read_file(i_f.name)
                                key = patient_id+'_'+str(i+1)

                                yield( key,
                                        {
                                                'image':image_file.pixel_array,
                                                'mask' : mask_file[:,:,i],
                                                'age' : image_file.PatientAge,
                                                'sex' :image_file.PatientSex,
                                                'body_part': image_file.BodyPartExamined

                                        })
                                i+=1


