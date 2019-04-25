"""tensorflow/datasets is a library of datasets ready to use with TensorFlow.

tensorflow/datasets is a library of public datasets ready to use with
TensorFlow. Each dataset definition contains the logic necessary to download and
prepare the dataset, as well as to read it into a model using the
`tf.data.Dataset` API.

Usage outside of TensorFlow is also supported.

See the README on GitHub for further documentation.
"""

import datetime
import os
import sys

from setuptools import find_packages
from setuptools import setup

nightly = False
if '--nightly' in sys.argv:
  nightly = True
  sys.argv.remove('--nightly')

project_name = 'tensorflow-datasets'

# To enable importing version.py directly, we add its path to sys.path.
version_path = os.path.join(
    os.path.dirname(__file__), 'tensorflow_datasets')
sys.path.append(version_path)
from version import __version__  # pylint: disable=g-import-not-at-top

if nightly:
  project_name = 'tfds-nightly'
  datestring = (os.environ.get('TFDS_NIGHTLY_TIMESTAMP') or
                datetime.datetime.now().strftime('%Y%m%d%H%M'))
  __version__ += 'dev%s' % datestring

DOCLINES = __doc__.split('\n')

REQUIRED_PKGS = [
    'absl-py',
    'future',
    'numpy',
    'promise',
    'protobuf>=3.6.1',
    'psutil',
    'requests',
    'six',
    'tensorflow-metadata',
    'termcolor',
    'tqdm',
    'wrapt',
]

TESTS_REQUIRE = [
    'jupyter',
    'pytest',
    'apache-beam',
]

if sys.version_info.major == 3:
  # Packages only for Python 3
  pass
else:
  # Packages only for Python 2
  TESTS_REQUIRE.append('mock')
  REQUIRED_PKGS.append('bz2file')
  REQUIRED_PKGS.append('functools32')
  REQUIRED_PKGS.append('futures')  # concurrent.futures

if sys.version_info < (3, 4):
  # enum introduced in Python 3.4
  REQUIRED_PKGS.append('enum34')

# Static files needed by datasets.
DATASET_FILES = [
    'image/imagenet2012_labels.txt',
    'image/imagenet2012_validation_labels.txt',
    'image/quickdraw_labels.txt',
    'url_checksums/*',
]

DATASET_EXTRAS = {
    # In alphabetical order
    'cats_vs_dogs': ['matplotlib'],
    'colorectal_histology': ['Pillow'],
    'imagenet2012_corrupted': [
        # This includes pre-built source; you may need to use an alternative
        # route to install OpenCV
        'opencv-python==3.4.0.14',
        'scikit-image',
        'scipy'
    ],
    'librispeech': ['pydub'],  # and ffmpeg installed
    'svhn': ['scipy'],
    'wikipedia': ['mwparserfromhell', 'apache_beam'],
}

all_dataset_extras = []
for deps in DATASET_EXTRAS.values():
  all_dataset_extras.extend(deps)

EXTRAS_REQUIRE = {
    'apache-beam': ['apache-beam'],
    'tensorflow': ['tensorflow>=1.12.0'],
    'tensorflow_gpu': ['tensorflow-gpu>=1.12.0'],
    'tests': TESTS_REQUIRE + all_dataset_extras,
}
EXTRAS_REQUIRE.update(DATASET_EXTRAS)

setup(
    name=project_name,
    version=__version__,
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    author='Google Inc.',
    author_email='packages@tensorflow.org',
    url='http://github.com/tensorflow/datasets',
    download_url='https://github.com/tensorflow/datasets/tags',
    license='Apache 2.0',
    packages=find_packages(),
    package_data={
        'tensorflow_datasets': DATASET_FILES,
    },
    scripts=[],
    install_requires=REQUIRED_PKGS,
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='tensorflow machine learning datasets',
)
