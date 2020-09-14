"""pathVQA dataset."""

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import json
import os

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
***TBD***
"""


class Pathvqa(tfds.core.GeneratorBasedBuilder):
  """TODO(pathVQA): Short description of my dataset."""

  # TODO(pathVQA): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(pathVQA): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Tensor(shape = (None, None, 3), dtype = tf.uint8), 
            "question": tfds.features.Text(),
            "answer": tfds.features.Text(),
        }),
#         supervised_keys=('image', 'question', 'answer'),
        supervised_keys=None,
        homepage='https://github.com/UCSD-AI4H/PathVQA',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
#     extracted_path = dl_manager.download_and_extract('https://storage.googleapis.com/bme590/roujia/pathVQARW')
#     extracted_path = dl_manager.download_and_extract('www.dukelibraryrepo.com/bme590/roujia/pathVQARW.tar.gz')
    extracted_path = 'gs://bme590/roujia/pathVQARW'
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'images_dir': os.path.join(extracted_path, "train/", "pic"),
                'labels_dir': os.path.join(extracted_path, "train/", "labels.json")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'images_dir': os.path.join(extracted_path, "test/", "pic"),
                'labels_dir': os.path.join(extracted_path, "test/", "labels.json")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'images_dir': os.path.join(extracted_path, "val/", "pic"),
                'labels_dir': os.path.join(extracted_path, "val/", "labels.json")
                       },
        ),
#         tfds.core.SplitGenerator(
#             name=tfds.Split.HOLDOUT,
#             gen_kwargs={
#                 'images_dir': os.path.join(extracted_path, "hold-out/", "pic"),
#                 'labels_dir': os.path.join(extracted_path, "hold-out/", "labels.json")
#             },
#         ),
    ]

  def _generate_examples(self, images_dir = None, labels_dir = None):
    # tf.io.gfile.Open('gs://bme590/roujia/pathVQARW/train/labels.json')
    # open('./labels.json')
    my_files = tf.io.gfile.listdir(images_dir)
    for file in my_files:
        print(file)
        questions = []
        answers = []
        with tf.io.gfile.GFile(labels_dir, 'r') as f:
            for line in f:
                str = line[:-2]
                try:
                    x = json.loads(str)
                    if file == x['Images']: 
                        questions.append(x['Questions'])
                        answers.append(x['Answers'])
                    else:
                        continue
                except: 
                    continue
        image = tf.io.read_file(os.path.join(images_dir, file)) 
        imageTensor = tf.io.decode_jpeg(image)
        questionTensor = questions
        answerTensor = answers
    yield 'key', {
        'image': imageTensor,
        'question': questionTensor,
        'answer': answerTensor, 
    }