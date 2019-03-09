from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import os
import numpy as np
import csv



_URL = "https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000/downloads/skin-cancer-mnist-ham10000.zip/2"

_DESCRIPTION = ("The dataset consists of 10015 dermatoscopic images which can serve as a training set for academic machine learning purposes."
                "Cases include a representative collection of all important diagnostic categories in the realm of pigmented lesions: Actinic keratoses and " 
                "intraepithelial carcinoma / Bowen's disease (akiec), basal cell carcinoma (bcc), benign keratosis-like lesions (solar lentigines / seborrheic "
                "keratoses and lichen-planus like keratoses, bkl), dermatofibroma (df), melanoma (mel), melanocytic nevi (nv) and vascular lesions "
                "(angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc)")



_IMAGE_SHAPE = (600,450,3)

_NAMES = ['akiec','bcc','bkl','df','mel','nv','vasc'] 


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
            #"file_name": tfds.features.Text(),
            "label": tfds.features.ClassLabel(names = _NAMES),
        }),

       
        
        supervised_keys=("image", "label"),
        
        urls=[_URL],
        
        citation=_CITATION
     )

  def _split_generators(self, dl_manager):
    # TODO(pierrot): implement download using kaggle API.
    
    path = dl_manager.manual_dir
    return [
        tfds.core.SplitGenerator(
            name="train",
            num_shards=10,
            gen_kwargs={
                "images_dir_path": path,
                "labels_dir_path":os.path.join(path,"HAM10000_metadata.csv")
            },
        )
       
    ]

  def _generate_examples(self,images_dir_path,labels_dir_path):

     data_folder_list = [os.path.join(images_dir_path,'HAM10000_images_part_1'),os.path.join(images_dir_path,'HAM10000_images_part_2')]
     for data_folder in data_folder_list:
        for file in tf.io.gfile.listdir(data_folder):
                
        
                    image_path = os.path.join(data_folder,file)
                    label = return_label(images_dir_path,file.split(".")[0],labels_dir_path)
                   
                    yield {
                    
                            
                            "label": label,
                            "image": image_path
                        }

                      
def return_label(path,image_name,labels_dir_path):
    
    with tf.io.gfile.GFile(labels_dir_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[1] == image_name:
                return row[2]



