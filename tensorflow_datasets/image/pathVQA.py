"""pathVQA dataset."""

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import json
import os
import random

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
"""

class Pathvqa(tfds.core.GeneratorBasedBuilder):
  """pathVQA dataset"""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Tensor(shape = (None,), dtype = tf.uint8), 
            'shape': tfds.features.Tensor(shape = (None,),  dtype=tf.int8), 
            'question':  tfds.features.Tensor(shape=(None,), dtype=tf.string),
            'answer': tfds.features.Tensor(shape=(None,), dtype=tf.string),
        }),
        supervised_keys=None,
        homepage='https://github.com/UCSD-AI4H/PathVQA',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    extracted_path = 'gs://bme590/roujia/pathVQARW'
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'images_dir': os.path.join(extracted_path, "train/", "pic"),
                'labels_dir': os.path.join(extracted_path, "train/", "label.json")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'images_dir': os.path.join(extracted_path, "test/", "pic"),
                'labels_dir': os.path.join(extracted_path, "test/", "label.json")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'images_dir': os.path.join(extracted_path, "val/", "pic"),
                'labels_dir': os.path.join(extracted_path, "val/", "label.json")
                       },
        ),
    ]

  def _generate_examples(self, images_dir = None, labels_dir = None):
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
                x = json.loads(string)
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
            imageTensor = tf.io.decode_jpeg(image)
            shapeTensor = imageTensor.get_shape().as_list()
            imageTensor = tf.reshape(imageTensor, [-1])
            qa_dict = new_dict.get(file)
            questionTensor = qa_dict.get('Questions')
            answerTensor = qa_dict.get('Answers')
            key = file + str(random.randint(0,100))
            yield key, {
                'image': imageTensor,
                'shape': tf.stack(shapeTensor),
                'question': tf.stack(questionTensor),
                'answer': tf.stack(answerTensor), 
            }
        else: 
            continue