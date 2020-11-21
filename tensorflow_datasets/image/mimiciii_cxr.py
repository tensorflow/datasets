"""mimiciii_cxr dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import os

_CITATION = """
@article{Johnson2019,
abstract = {Chest radiography is an extremely powerful imaging modality, allowing for a detailed inspection of a patient's chest, but requires specialized training for proper interpretation. With the advent of high performance general purpose computer vision algorithms, the accurate automated analysis of chest radiographs is becoming increasingly of interest to researchers. Here we describe MIMIC-CXR, a large dataset of 227,835 imaging studies for 65,379 patients presenting to the Beth Israel Deaconess Medical Center Emergency Department between 2011-2016. Each imaging study can contain one or more images, usually a frontal view and a lateral view. A total of 377,110 images are available in the dataset. Studies are made available with a semi-structured free-text radiology report that describes the radiological findings of the images, written by a practicing radiologist contemporaneously during routine clinical care. All images and reports have been de-identified to protect patient privacy. The dataset is made freely available to facilitate and encourage a wide range of research in computer vision, natural language processing, and clinical data mining.},
author = {Johnson, Alistair E.W. and Pollard, Tom J. and Berkowitz, Seth J. and Greenbaum, Nathaniel R. and Lungren, Matthew P. and Deng, Chih Ying and Mark, Roger G. and Horng, Steven},
doi = {10.1038/s41597-019-0322-0},
file = {:Users/zl190/Downloads/s41597-019-0322-0.pdf:pdf},
issn = {20524463},
journal = {Scientific data},
number = {1},
pages = {317},
pmid = {31831740},
publisher = {Springer US},
title = {{MIMIC-CXR, a de-identified publicly available database of chest radiographs with free-text reports}},
url = {http://dx.doi.org/10.1038/s41597-019-0322-0},
volume = {6},
year = {2019}
}
"""

_DESCRIPTION = """
The MIMIC Chest X-ray (MIMIC-CXR) Database v2.0.0 is a large publicly available dataset of chest radiographs in DICOM format with free-text radiology reports. The dataset contains 377,110 images corresponding to 227,835 radiographic studies performed at the Beth Israel Deaconess Medical Center in Boston, MA. The dataset is de-identified to satisfy the US Health Insurance Portability and Accountability Act of 1996 (HIPAA) Safe Harbor requirements. Protected health information (PHI) has been removed. The dataset is intended to support a wide body of research in medicine including image understanding, natural language processing, and decision support.

The MIMIC-CXR dataset must be downloaded separately after reading and agreeing 
to a Research Use Agreement. To do so, please follow the instructions on the 
website, https://physionet.org/content/mimic-cxr/2.0.0/
"""

_LABELS = ({
    -1.0: "uncertain",
    1.0: "positive",
    0.0: "negative",
    99.0: "unmentioned",
})


class MimiciiiCxr(tfds.core.BeamBasedBuilder):
    '''
    DATASET_NAME=mimiciii_cxr
    GCP_PROJECT=seaworthy-project
    GCS_BUCKET=gs://tfds-nabla-us-central
    GCS_BUCKET_RAW=gs://nabla-public-data

    echo "git+https://github.com/ouwen/datasets@mimiciii" > /tmp/beam_requirements.txt
    echo "pydicom" >> /tmp/beam_requirements.txt

    python3 -m tensorflow_datasets.scripts.download_and_prepare \
      --datasets=$DATASET_NAME \
      --data_dir=$GCS_BUCKET \
      --manual_dir=$GCS_BUCKET_RAW/mimic-cxr-2.0.0 \
      --beam_pipeline_options=\
    "runner=DataflowRunner,project=$GCP_PROJECT,job_name=tfds-mimic-cxr-2-19-all,"\
    "staging_location=$GCS_BUCKET/binaries,temp_location=$GCS_BUCKET/temp,"\
    "requirements_file=/tmp/beam_requirements.txt,region=us-central1,"\
    "autoscaling_algorithm=THROUGHPUT_BASED,max_num_workers=100,"\
    "machine_type=n1-standard-2,experiments=shuffle_mode=service,enable_streaming_engine"
    '''
    
    VERSION = tfds.core.Version('0.2.0')
    SUPPORTED_VERSIONS = [ tfds.core.Version('0.1.0') ]
    
    BUILDER_CONFIGS = [
        tfds.core.BuilderConfig(
            name='512', version='0.2.0', supported_versions=None, description='512 image size.'
        ),
    ]
    MANUAL_DOWNLOAD_INSTRUCTIONS = """\
        You must register and agree to user agreement on the dataset page:
        https://physionet.org/content/mimic-cxr/2.0.0/
        Afterwards, you have to download and put the mimic-cxr-2.0.0 directory in the
        manual_dir. It should contain subdirectories: files/ with images
        and also mimic-cxr-2.0.0-split.csv, mimic-cxr-2.0.0-negbio.csv,
        mimic-cxr-2.0.0-chexpert.csv, and mimic-cxr-2.0.0-metadata.csv files.
        These four files can be downloaded from https://physionet.org/content/mimic-cxr-jpg/

        Once the csv files are ready, they must be pre-processed to combine metadata information
        with split information. This is performed via a group-by clause on study_id. Other fields
        are aggregated via pipe a ("|") delimiter.
    """
    
    def _info(self):
        image_size = 512 if self.builder_config.name is '512' else 2048
        
        return tfds.core.DatasetInfo(
                builder=self,
                description=_DESCRIPTION,
                features=tfds.features.FeaturesDict({
                     "subject_id": tfds.features.Text(),
                     "study_id": tfds.features.Text(),
                     "study_date": tfds.features.Text(),
                     "study_time": tfds.features.Text(),
                     "report": tfds.features.Text(),
                     "label_chexpert": tfds.features.Sequence(tfds.features.ClassLabel(names=list(_LABELS.values())), length=14),
                     "label_negbio": tfds.features.Sequence(tfds.features.ClassLabel(names=list(_LABELS.values())), length=14),
                     "image_sequence": tfds.features.Sequence({
                         "image": tfds.features.Image(shape=(image_size, image_size, 1), dtype=tf.uint16, encoding_format='png'),
                         "dicom_id": tfds.features.Text(),
                         "rows": tfds.features.Tensor(shape=(), dtype=tf.int32),
                         "columns": tfds.features.Tensor(shape=(), dtype=tf.int32),
                         "viewPosition": tfds.features.Text(),
                         "viewCodeSequence_CodeMeaning": tfds.features.Text(),
                         "patientOrientationCodeSequence_CodeMeaning": tfds.features.Text(),
                         "procedureCodeSequence_CodeMeaning": tfds.features.Text(),
                         "performedProcedureStepDescription": tfds.features.Text(),
                     })
                }),
                homepage='https://physionet.org/content/mimic-cxr/2.0.0/',
                citation=_CITATION)
           
    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={
                    'filepath': os.path.join(dl_manager.manual_dir, 'train-split.csv'),
                    'manual_dir': dl_manager.manual_dir
                },
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                gen_kwargs={
                    'filepath': os.path.join(dl_manager.manual_dir, 'val-split.csv'),
                    'manual_dir': dl_manager.manual_dir
                },
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={
                    'filepath': os.path.join(dl_manager.manual_dir, 'test-split.csv'),
                    'manual_dir': dl_manager.manual_dir
                }
            )
        ]

    def _build_pcollection(self, pipeline, filepath=None, manual_dir=None):
        beam = tfds.core.lazy_imports.apache_beam
        pydicom = tfds.core.lazy_imports.pydicom
        pd = tfds.core.lazy_imports.pandas
        image_size = 512 if self.builder_config.name is '512' else 2048
        
        def _right_size(row):
            data = row.split(",")
            return len(data)==11
        
        def _check_files(row):
            study_id, subject_id, split, dicom_id, performedProcedureStepDescription, ViewPosition, StudyDate, StudyTime, procedureCodeSequence_CodeMeaning, ViewCodeSequence_CodeMeaning, patientOrientationCodeSequence_CodeMeaning = row.split(",")
            basepath = '{}/files/p{}/p{}/s{}'.format(manual_dir, subject_id[0:2], subject_id, study_id)
            paths = ['{}/{}.dcm'.format(basepath, d) for d in dicom_id.split("|")]
            paths.append(basepath+'.txt')
            for path in paths:
                if not tf.io.gfile.exists(path): return False

            # Job Graph Too Large
            chexpert_df = pd.read_csv(tf.io.gfile.GFile(os.path.join(manual_dir, 'mimic-cxr-2.0.0-chexpert.csv'), 'r'))
            negbio_df = pd.read_csv(tf.io.gfile.GFile(os.path.join(manual_dir, 'mimic-cxr-2.0.0-negbio.csv'), 'r'))
            chexpert_df = chexpert_df.fillna(99.0)
            negbio_df = negbio_df.fillna(99.0)

            try:
                negbio_values = negbio_df[(negbio_df['subject_id']==int(subject_id)) & (negbio_df['study_id']==int(study_id))].values.tolist()[0][2:]
                chexpert_values = chexpert_df[(chexpert_df['subject_id']==int(subject_id)) & (chexpert_df['study_id']==int(study_id))].values.tolist()[0][2:]
                negbio_values = [_LABELS[v] for v in negbio_values]
                chexpert_values = [_LABELS[v] for v in chexpert_values]
            except Exception as e:
                print(subject_id)
                print(study_id)
                return False

            return True

        def _process_example(row):
            def fast_histogram_equalize(image):
                '''histogram for integer based images'''
                image = image - tf.reduce_min(image)
                image = tf.cast(image, tf.int32)
                histogram = tf.math.bincount(image)
                cdf = tf.cast(tf.math.cumsum(histogram), tf.float32)
                cdf = cdf/cdf[-1]
                return tf.gather(params=cdf, indices=image)
            study_id, subject_id, split, dicom_id, performedProcedureStepDescription, ViewPosition, StudyDate, StudyTime, procedureCodeSequence_CodeMeaning, ViewCodeSequence_CodeMeaning, patientOrientationCodeSequence_CodeMeaning = row.split(",")
            
            # Job Graph Too Large
            chexpert_df = pd.read_csv(tf.io.gfile.GFile(os.path.join(manual_dir, 'mimic-cxr-2.0.0-chexpert.csv'), 'r'))
            negbio_df = pd.read_csv(tf.io.gfile.GFile(os.path.join(manual_dir, 'mimic-cxr-2.0.0-negbio.csv'), 'r'))
            chexpert_df = chexpert_df.fillna(99.0)
            negbio_df = negbio_df.fillna(99.0)
            
            dicom_id = dicom_id.split("|")
            ViewPosition = ViewPosition.split("|")
            ViewCodeSequence_CodeMeaning = ViewCodeSequence_CodeMeaning.split("|")
            patientOrientationCodeSequence_CodeMeaning = patientOrientationCodeSequence_CodeMeaning.split("|")
            procedureCodeSequence_CodeMeaning = procedureCodeSequence_CodeMeaning.split("|")
            performedProcedureStepDescription = performedProcedureStepDescription.split("|")
            basepath = '{}/files/p{}/p{}/s{}'.format(manual_dir, subject_id[0:2], subject_id, study_id)
            
            dicom_paths = ['{}/{}.dcm'.format(basepath, d) for d in dicom_id]
            images = []
            rows = []
            columns = []
            for dicom_path in dicom_paths:
                with tf.io.gfile.GFile(dicom_path, 'rb') as d:
                    ds = pydicom.dcmread(d)
                    image = tf.squeeze(tf.constant(ds.pixel_array))[..., None]
                    row, col, channel = image.shape
                    image = fast_histogram_equalize(image)
                    images.append(tf.cast(tf.round(tf.image.resize_with_pad(image, image_size, image_size)), tf.uint16).numpy())
                    rows.append(row)
                    columns.append(col)

            negbio_values = negbio_df[(negbio_df['subject_id']==int(subject_id)) & (negbio_df['study_id']==int(study_id))].values.tolist()[0][2:]
            chexpert_values = chexpert_df[(chexpert_df['subject_id']==int(subject_id)) & (chexpert_df['study_id']==int(study_id))].values.tolist()[0][2:]
            negbio_values = [_LABELS[v] for v in negbio_values]
            chexpert_values = [_LABELS[v] for v in chexpert_values]
            
            return dicom_id, {
                "subject_id": subject_id,
                "study_id": study_id,
                "study_date": StudyDate.split("|")[0],
                "study_time": StudyTime.split("|")[0],
                "report": tf.io.read_file(basepath+'.txt'),
                "label_chexpert": chexpert_values,
                "label_negbio": negbio_values,
                "image_sequence":{
                     "image": images,
                     "rows": rows,
                     "columns": columns,
                     "dicom_id": dicom_id,
                     "viewPosition": ViewPosition,
                     "viewCodeSequence_CodeMeaning": ViewCodeSequence_CodeMeaning,
                     "patientOrientationCodeSequence_CodeMeaning": patientOrientationCodeSequence_CodeMeaning,
                     "procedureCodeSequence_CodeMeaning": procedureCodeSequence_CodeMeaning,
                     "performedProcedureStepDescription": performedProcedureStepDescription,
                }
            }
    
        return (
            pipeline
            | beam.io.ReadFromText(filepath, skip_header_lines=1)
            | beam.Filter(_right_size)
            | beam.Filter(_check_files)
            | beam.Map(_process_example)
        )
