"""mrnet dataset."""
import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import os
import numpy as np
import pandas as pd

_CITATION = """
@article{10.1371/journal.pmed.1002699,
  Abstract = {Nicholas Bien and colleagues present an automated system for interpreting knee 
  magnetic resonance (MR) images to prioritize high-risk patients and assist clinicians in making diagnoses.},
  Author = {Bien, Nicholas AND Rajpurkar, Pranav AND Ball, Robyn L. AND Irvin, Jeremy AND Park, 
  Allison AND Jones, Erik AND Bereket, Michael AND Patel, Bhavik N. AND Yeom, Kristen W. AND Shpanskaya, Katie AND 
  Halabi, Safwan AND Zucker, Evan AND Fanton, Gary AND Amanatullah, Derek F. AND Beaulieu, Christopher F. AND Riley, 
  Geoffrey M. AND Stewart, Russell J. AND Blankenberg, Francis G. AND Larson, David B. AND Jones, Ricky H. AND 
  Langlotz, Curtis P. AND Ng, Andrew Y. AND Lungren, Matthew P.},
  Doi = {10.1371/journal.pmed.1002699},
  Journal = {PLOS Medicine},
  Month = {11},
  Number = {11},
  Pages = {1-19},
  Publisher = {Public Library of Science},
  Title = {Deep-learning-assisted diagnosis for knee magnetic resonance imaging: Development and retrospective 
  validation of MRNet},
  Url = {https://doi.org/10.1371/journal.pmed.1002699},
  Volume = {15},
  Year = {2018},
  Bdsk-Url-1 = {https://doi.org/10.1371/journal.pmed.1002699}}
"""

_DESCRIPTION = """
The MRNet dataset consists of 1,370 knee MRI exams performed at Stanford University Medical Center. 
The dataset contains 1,104 (80.6%) abnormal exams, with 319 (23.3%) ACL tears and 508 (37.1%) meniscal tears; 
labels were obtained through manual extraction from clinical reports.

The most common indications for the knee MRI examinations in this study included acute and chronic pain, follow-up or 
preoperative evaluation, injury/trauma. Examinations were performed with GE scanners (GE Discovery, GE Healthcare, 
Waukesha, WI) with standard knee MRI coil and a routine non-contrast knee MRI protocol that included the following 
sequences: coronal T1 weighted, coronal T2 with fat saturation, sagittal proton density (PD) weighted, sagittal T2 
with fat saturation, and axial PD weighted with fat saturation. A total of 775 (56.6%) examinations used a 3.0-T 
magnetic field; the remaining used a 1.5-T magnetic field.

The exams have been split into a training set (1,130 exams, 1,088 patients), a validation set (called tuning set in 
the paper) (120 exams, 111 patients), and a hidden test set (called validation set in the paper) 
(120 exams, 113 patients). To form the validation and tuning sets, stratified random sampling was used to ensure that 
at least 50 positive examples of each label (abnormal, ACL tear, and meniscal tear) were present in each set. 
All exams from each patient were put in the same split.
"""


class Mrnet(tfds.core.GeneratorBasedBuilder):
  """TODO(mrnet): MRI knee axial images with classification labels."""
  MANUAL_DOWNLOAD_INSTRUCTIONS = "Have a directory with MRNet train and test npy in it"
  # TODO(mrnet): Set up version.
  VERSION = tfds.core.Version('0.1.0')
  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Tensor(shape=(256, 256, 1), dtype=tf.uint8),
            'label': tfds.features.ClassLabel(names=["abnormal", "ACL", "Meniscus", "normal", "Both_ACL_Meniscus"]),
        }),
        supervised_keys=('image', 'label'),
        # Homepage of the dataset for documentation
        homepage='https://stanfordmlgroup.github.io/competitions/mrnet/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    data_dir = dl_manager.manual_dir
    if not tf.io.gfile.exists(data_dir):
      msg = "You must download the dataset files manually and place them in: "
      msg += dl_manager.manual_dir
      msg += " as train, valid folders and a series of csv files."
      msg += " See testing/test_data/fake_examples/mrnet."
      raise AssertionError(msg)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'archive': os.path.join(data_dir, "train"),
                'label_path': os.path.join(data_dir, "train_labels.csv"),
                'data_dir': data_dir,
                'process': 'train'

            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'archive': os.path.join(data_dir, "valid"),
                'label_path': os.path.join(data_dir, "valid_labels.csv"),
                'data_dir': data_dir,
                'process': 'test'
            }),
    ]

  def _generate_examples(self, data_dir=None, archive=None, label_path=None, process=None):
    """Generate MRNet examples as dicts.
    Args:
      data_dir (str): The path of the downloaded and generated data.
      archive (str): Path to the image data files
      label_path (str): Path to the csv label files
      process (str): Flag to decide the splits

    Yields:
      Generator yielding the next examples
    """
    if process == 'train':
        abnormal_train = pd.read_csv(os.path.join(data_dir, "train-abnormal.csv"), names=["Patient_Number", "abnormal"])
        ACL_train = pd.read_csv(os.path.join(data_dir, "train-acl.csv"), names=["Patient_Number", "ACL"])
        meniscus_train = pd.read_csv(os.path.join(data_dir, "train-meniscus.csv"), names=["Patient_Number", "meniscus"])
        abnormal_acl_train = abnormal_train.merge(ACL_train, on="Patient_Number")
        ab_acl_meni_train = abnormal_acl_train.merge(meniscus_train, on="Patient_Number")
    else:
        abnormal_test = pd.read_csv(os.path.join(data_dir, "valid-abnormal.csv"), names=["Patient_Number", "abnormal"])
        ACL_test = pd.read_csv(os.path.join(data_dir, "valid-acl.csv"), names=["Patient_Number", "ACL"])
        meniscus_test = pd.read_csv(os.path.join(data_dir, "valid-meniscus.csv"), names=["Patient_Number", "meniscus"])
        abnormal_acl_test = abnormal_test.merge(ACL_test, on="Patient_Number")
        ab_acl_meni_test = abnormal_acl_test.merge(meniscus_test, on="Patient_Number")

    def sumup(row):
        if (row['abnormal'] == 1) & (row["ACL"] == 1) & (row["meniscus"] == 1):
            val = "Both_ACL_Meniscus"
        elif (row['abnormal'] == 1) & (row["ACL"] == 1) & (row["meniscus"] == 0):
            val = "ACL"
        elif (row['abnormal'] == 1) & (row["ACL"] == 0) & (row["meniscus"] == 1):
            val = "Meniscus"
        elif (row['abnormal'] == 1) & (row["ACL"] == 0) & (row["meniscus"] == 0):
            val = "abnormal"
        elif row['abnormal'] == 0:
            val = "normal"
        return val
    if process == 'train':
        ab_acl_meni_train['sumup'] = ab_acl_meni_train.apply(sumup, axis=1)
        ab_acl_meni_train[['Patient_Number', "sumup"]].to_csv(os.path.join(data_dir, "train_labels.csv"), header=False)
    else:
        ab_acl_meni_test['sumup'] = ab_acl_meni_test.apply(sumup, axis=1)
        ab_acl_meni_test[['Patient_Number', "sumup"]].to_csv(os.path.join(data_dir, "valid_labels.csv"), header=False)

    all_labels = pd.read_csv(label_path, names=["Patient_Number", "label"])

    count = 0
    archive_list = [os.path.join(archive, "axial"), os.path.join(archive, "coronal"), os.path.join(archive, "sagittal")]
    for direction in archive_list:
        files = []
        for r, d, f in tf.io.gfile.walk(direction):
            for file in f:
                if '.npy' in file:
                    files.append(os.path.join(r, file))
        sorted_files = sorted(files)

        for path_cube in sorted_files:
            cube = np.load(tf.io.gfile.GFile(path_cube, mode='rb'))
            for picture in cube:
                example_image = picture[..., np.newaxis]
                example_label = (all_labels.loc[all_labels['Patient_Number'] ==
                                                int(os.path.splitext(os.path.basename(path_cube))[0][:4]),
                                                'label'].iloc[0])
                count += 1
                yield count, {
                        'image': example_image,
                        'label': example_label,
                       }
