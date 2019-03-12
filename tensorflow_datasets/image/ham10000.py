"""HAM10000 Dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import csv
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = ("https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000/"
"downloads/skin-cancer-mnist-ham10000.zip/2")

_DESCRIPTION = ("The dataset consists of 10015 dermatoscopic images which"
"can serve as a training set for academic machine learning purposes."
"Cases include a representative collection of all important diagnostic "
"categories in the realm of pigmented lesions: Actinic keratoses and " 
"intraepithelial carcinoma / Bowen's disease (akiec), basal cell carcinoma (bcc), "
"benign keratosis-like lesions (solar lentigines / seborrheic "
"keratoses and lichen-planus like keratoses, bkl), dermatofibroma (df), "
"melanoma (mel), melanocytic nevi (nv) and vascular lesions "
"(angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc)")

_IMAGE_SHAPE = (450, 600, 3)

_NAMES = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc'] 

_CITATION = """\
@data{DVN/DBW86T_2018,
author = {Tschandl, Philipp},
publisher = {Harvard Dataverse},
title = "{The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions}",
UNF = {UNF:6:IQTf5Cb+3EzwZ95U5r0hnQ==},
year = {2018},
version = {V1},
doi = {10.7910/DVN/DBW86T},
url = {https://doi.org/10.7910/DVN/DBW86T}
}
"""

class Ham10000(tfds.core.GeneratorBasedBuilder):
    """HAM10000 Dermatoscopic images"""

    VERSION = tfds.core.Version('1.0.0')


    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
    
            description=(_DESCRIPTION),
            
            features=tfds.features.FeaturesDict({
                "image":tfds.features.Image(shape=_IMAGE_SHAPE),
                "label": tfds.features.ClassLabel(names=_NAMES),
            }),

            supervised_keys=("image", "label"),
            
            urls=[_URL],
            
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        """Function to split the images into training set as no other set is specified"""
        
        path = dl_manager.manual_dir
        return [
            tfds.core.SplitGenerator(
                name="train",
                num_shards=10,
                gen_kwargs={
                    "images_dir_path": path,
                    "labels_dir_path":os.path.join(path, "HAM10000_metadata.csv")
                },
            )
        
        ]

    def _generate_examples(self, images_dir_path, labels_dir_path):
        """ Function to extract images and labels"""

        csv_list = readCsv(labels_dir_path)
        
        data_folder_list = [os.path.join(images_dir_path, 'HAM10000_images_part_1'), os.path.join(images_dir_path, 'HAM10000_images_part_2')]
        for data_folder in data_folder_list:
            for image_file in tf.io.gfile.listdir(data_folder):
                        
                
                image_path = os.path.join(data_folder, image_file)
                label = return_label(image_file.split(".")[0], csv_list)
                print(label)
                
                yield {
                
                    "label": label,
                    "image": image_path
                    }


def readCsv(labels_dir_path):
    """Function to read labels.csv file and store in memory"""

    readCSV = csv.DictReader(tf.io.gfile.GFile(labels_dir_path))
    #Covert csv to list to iterate without saving the state of the generator
    return list(readCSV) 

def return_label(image_name, csv_list):
    """Function to return the corresponding label from filename"""

    for row in range(len(csv_list)):
        if csv_list[row]['image_id'] == image_name:
            return csv_list[row]['dx']
                