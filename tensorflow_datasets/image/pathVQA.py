"""pathVQA dataset."""

import os
# import json
# import random
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@misc{he2020pathvqa,
    title={PathVQA: 30000+ Questions for Medical Visual Question Answering},
    author={Xuehai He and Yichen Zhang and Luntian Mou and Eric Xing and Pengtao Xie},
    year={2020},
    eprint={2003.10286},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
"""

# TODO(pathVQA):
_DESCRIPTION = """\
The authors generated a pathology visual question answering (VQA) dataset by extracting images 
and captions from online pathology textbooks and online digital libraries. The dataset contains 
a total of 4,998 images and 32,799 question-answer pairs. 1670 images were generated from two 
pathology textbook Basic Pathology and Textbook of pathology, and the rest of images were 
generated from the PEIR digital library. About half of the images have a “yes/no” answer and 
the other half have a open-ended answer that include six types of information relevant to 
disease pathology: “what”, “where”, “when”, “whose”, “how”, and “how much/how many”. 

This dataset aims to help create an “AI” board-certificated pathologist in the United States. 
By providing the answer-pairs that are highly similar to the American Board Pathology (ABP) 
test, this dataset will lead to a better understanding about computer-aided clinical 
decision making and contribute to pathologist education. The construction of “AI” pathologists
could be a great potential for low-resource settings where medical training resources and 
medical professionals are scarcer than in the United States. 

The size of images is different case by case. The dataset will generate a 1D array of image
and original image shape. The user can utilize the reshape_image function to recover images
from 1D array. The questions and answers pair will be in format of lists. 
"""

class Pathvqa(tfds.core.GeneratorBasedBuilder):
  """pathVQA dataset"""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  Please set your manual_dir at 'gs://bme590/roujia/pathVQARW'
  in your tfds.download.DownloadConfig when using tfds.load
  """

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Tensor(shape = (None,),
                                          dtype = tf.uint8),
            'image_shape': tfds.features.Tensor(shape = (None,),
                                                dtype=tf.int32),
            'question': tfds.features.Tensor(shape=(None,),
                                             dtype=tf.string),
            'answer': tfds.features.Tensor(shape=(None,),
                                           dtype=tf.string),
        }),
        supervised_keys=None,
        homepage='https://github.com/UCSD-AI4H/PathVQA',
        citation=_CITATION,
    )

  def reshape_image(self, example):
    """Reshape the 1d images array based on image_shape
    Args:
      example: example generated from pathVQA, features dictionary
    Returns:
      updated image with orignal shape
    """
    image_array = example["image"]
    shape_array = example["image_shape"]
    image = tf.reshape(image_array, shape_array)
    return image

  def _split_generators(self, dl_manager):
    extracted_path = dl_manager.manual_dir
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'images_dir': os.path.join(extracted_path,
                                           "train/", "pic"),
                'labels_dir': os.path.join(extracted_path,
                                           "train/", "label.json")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'images_dir': os.path.join(extracted_path,
                                           "test/", "pic"),
                'labels_dir': os.path.join(extracted_path,
                                           "test/", "label.json")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'images_dir': os.path.join(extracted_path,
                                           "val/", "pic"),
                'labels_dir': os.path.join(extracted_path,
                                           "val/", "label.json")
            },
        ),
    ]

  def _generate_examples(self, images_dir = None, labels_dir = None):
    """Generate examples for TFDS pathVQA
    Args:
      images_dir: directory of images
      labels_dir: directory of labels
    Returns:
      a feature dictionary contains 1D image array, image shape,
      list of questions, list of answers
    """
    my_files = tf.io.gfile.listdir(images_dir)
    new_dict = {}
    with tf.io.gfile.GFile(labels_dir) as f:
      image_name = ''
      questions = []
      answers = []
      qa_dict = {}
      for line in f:
        string = line[:-2]
        try:
          x = tfds.core.lazy_imports.json.loads(string)
          temp_name = x.get('Images')
          if '.jpg' not in temp_name:
            temp_name = temp_name + '.jpg'
          if image_name == temp_name:
            questions.append(str(x.get('Questions')))
            answers.append(str(x.get('Answers')))
          else:
            qa_dict.update({'Questions' : questions})
            qa_dict.update({'Answers' : answers})
            new_dict.update({image_name : qa_dict})
            image_name = temp_name
            questions = []
            answers = []
            qa_dict = {}
        except:
          continue
    for file in my_files:
      if file in new_dict:
        image = tf.io.read_file(os.path.join(images_dir, file))
        image_tensor = tf.io.decode_jpeg(image)
        shape_tensor = tf.shape(image_tensor)
        image_tensor_flat = tf.reshape(image_tensor, [-1])
        qa_dict = new_dict.get(file)
        question_tensor = qa_dict.get('Questions')
        answer_tensor = qa_dict.get('Answers')
        key = file + str(tfds.core.lazy_imports.random.randint(0,100))
        yield key, {
            'image': image_tensor_flat,
            'image_shape': shape_tensor,
            'question': question_tensor,
            'answer': answer_tensor,
        }
      else:
        continue
        