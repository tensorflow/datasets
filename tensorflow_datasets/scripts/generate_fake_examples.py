from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags

from tensorflow_datasets.core import holder

r"""Generate dataset fake examples and tests.

python -m tensorflow_datasets.scripts.generate_fake.examples \
  --dataset_name dataset_name \
  --file_path /Users/user1/Desktop/test.zip \
  --dataset_type dataset_type

"""

FLAGS = flags.FLAGS

_DATASET_TYPE = ['image', 'video', 'audio', 'text', 'structured', 'translate']

flags.DEFINE_string('dataset_name', None, 'Dataset name')
flags.DEFINE_string('file_path', None, 'File to generated examples.')
flags.DEFINE_enum('dataset_type', 'image', _DATASET_TYPE, 'Dataset type')


def main(_):
	print(FLAGS.dataset_name)
	holder.Generator(dataset_name=FLAGS.dataset_name,
									 dataset_path=FLAGS.file_path,
									 dataset_type=FLAGS.dataset_type).generator()


if __name__ == '__main__':
	app.run(main)
