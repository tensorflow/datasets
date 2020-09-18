"""pancreas_ct dataset."""
import os
import pydicom
import nibabel
import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_CITATION = """\
@article{article,
  author = {Clark, Kenneth and Vendt, Bruce and Smith, Kirk and Freymann, John and Kirby, Justin and Koppel, Paul and Moore, Stephen and Phillips, Stanley and Maffitt,     David and Pringle, Michael and Tarbox, Lawrence and Prior, F.},
  year = {2013},
  month = {07},
  pages = {},
  title = {The Cancer Imaging Archive (TCIA): Maintaining and Operating a Public Information Repository},
  volume = {26},
  journal = {Journal of digital imaging},
  doi = {10.1007/s10278-013-9622-7}
}
"""

_DESCRIPTION = """\
The National Institutes of Health Clinical Center performed 82 abdominal contrast enhanced 3D CT scans from 53 male and 27 female subjects. Seventeen of the subjects are healthy kidney donors scanned prior to nephrectomy.  The remaining 65 patients were selected by a radiologist from patients who neither had major abdominal pathologies nor pancreatic cancer lesions.  Subjects' ages range from 18 to 76 years with a mean age of 46.8 ± 16.7. The CT scans have resolutions of 512x512 pixels with varying pixel sizes and slice thickness between 1.5 − 2.5 mm, acquired on Philips and Siemens MDCT scanners (120 kVp tube voltage). A medical student manually performed slice-by-slice segmentations of the pancreas as ground-truth and these were verified/modified by an experienced radiologist.
"""


class PancreasCt(tfds.core.GeneratorBasedBuilder):
  "Pancreas CT Scan Dataset"
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
    Data can be downloaded from
    https://console.cloud.google.com/storage/browser/bme590/krinke
    Please put all files in manual_dir.
    """

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description = _DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # The CT image itself
            'image' : tfds.features.Tensor(shape = (512,512), dtype = tf.int16),
            # A mask indicating whether a given pixel is part of the pancreas
            'mask' : tfds.features.Tensor(shape = (512,512), dtype = tf.bool)
        }),
        # Homepage of the dataset for documentation
        homepage='https://wiki.cancerimagingarchive.net/display/Public/Pancreas-CT',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    directory = dl_manager.manual_dir
    
    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_example
            gen_kwargs={'data_dir' : directory},
        ),
    ]

  def _generate_examples(self, data_dir= None):
    """Yields examples."""
    
    mask_files =  tf.io.gfile.listdir(os.path.join(data_dir,'PancreasLabels'))
    image_folders = tf.io.gfile.listdir(os.path.join(data_dir, 'Pancreas-CT'))
    mask_files.sort()
    image_folders.sort()
    i = 0 
    for folder in image_folders: # Iterate over all of the folders containing image
      mask = nibabel.load(os.path.join(data_dir, 'PancreasLabels/', mask_files[i])) # Load in one nii file containing many masks
      j = 0
      image_names = tf.io.gfile.listdir(os.path.join(data_dir, 
                                                     'Pancreas-CT/', folder)) 
      image_names.sort()
      array_data = mask.get_fdata().astype('bool') #Cast from float64
      for image_name in image_names: # Iterate over each folder to get each image
        image_file = pydicom.read_file(os.path.join(data_dir,
                                                    'Pancreas-CT/',folder,image_name)).pixel_array
        mask_array = array_data[:,:,j] # Get the corresponding mask from the nii file
        key =  image_name + str(i) + str(j)
        yield key, {'image': image_file, 'mask': mask_array}
        j += 1
    i+=1