"""tensorflow/datasets is a library of datasets ready to use with TensorFlow.

tensorflow/datasets is a library of public datasets ready to use with
TensorFlow. Each dataset definition contains the logic necessary to download and
prepare the dataset, as well as to read it into a model using the
`tf.data.Dataset` API.

Usage outside of TensorFlow is also supported.

See the README on GitHub for further documentation.
"""

import datetime
import itertools
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
    'attrs>=18.1.0',
    'dill',  # TODO(tfds): move to TESTS_REQUIRE.
    'future',
    'numpy',
    'promise',
    'protobuf>=3.6.1',
    'requests>=2.19.0',
    'six',
    'tensorflow-metadata',
    'termcolor',
    'tqdm',
    'wrapt',
    # Python 2 backports
    'bz2file;python_version<"3"',
    'functools32;python_version<"3"',
    'futures;python_version<"3"',
    # shutil.disk_usage was introduced in Python 3.3, use psutil instead.
    'psutil;python_version<"3.3"',
    # enum introduced in Python 3.4
    'enum34;python_version<"3.4"'
]

TESTS_REQUIRE = [
    'apache-beam',
    'jupyter',
    'mako',
    'pytest',
    'pytest-xdist',
    # Python 2 backports
    'mock;python_version<"3"',
    # TODO(b/142892342): Re-enable
    # 'tensorflow-docs @ git+https://github.com/tensorflow/docs#egg=tensorflow-docs',  # pylint: disable=line-too-long
]

# Static files needed by datasets.
DATASET_FILES = [
    'image/caltech101_labels.txt',
    'image/categories_places365.txt',
    'image/cbis_ddsm_calc_distributions.txt',
    'image/cbis_ddsm_calc_types.txt',
    'image/cbis_ddsm_mass_margins.txt',
    'image/cbis_ddsm_mass_shapes.txt',
    'image/cbis_ddsm_patch_labels.txt',
    'image/dtd_key_attributes.txt',
    'image/food-101_classes.txt',
    'image/imagenet_resized_labels.txt',
    'image/imagenet2012_labels.txt',
    'image/imagenet2012_validation_labels.txt',
    'image/imagenette_labels.txt',
    'image/inaturalist_labels.txt',
    'image/inaturalist_supercategories.txt',
    'image/open_images_classes_all.txt',
    'image/open_images_classes_boxable.txt',
    'image/open_images_classes_trainable.txt',
    'image/plant_leaves_urls.txt',
    'image/plantae_k_urls.txt',
    'image/quickdraw_labels.txt',
    'image/sun397_labels.txt',
    'image/sun397_tfds_te.txt',
    'image/sun397_tfds_tr.txt',
    'image/sun397_tfds_va.txt',
    'url_checksums/*',
    'video/ucf101_labels.txt',
]

# Extra dependencies required by specific datasets
DATASET_EXTRAS = {
    # In alphabetical order
    'aflw2k3d': ['scipy'],
    'c4': ['apache_beam', 'langdetect', 'nltk', 'tldextract'],
    'cats_vs_dogs': ['matplotlib'],
    'colorectal_histology': ['Pillow'],
    'eurosat': ['scikit-image',],
    'groove': ['pretty_midi', 'pydub'],
    'imagenet2012_corrupted': [
        # This includes pre-built source; you may need to use an alternative
        # route to install OpenCV
        'opencv-python==3.4.0.14',
        'scikit-image',
        'scipy'
    ],
    'librispeech': ['pydub'],  # and ffmpeg installed
    # sklearn version required to avoid conflict with librosa from
    # https://github.com/scikit-learn/scikit-learn/issues/14485
    'nsynth': ['crepe>=0.0.9', 'librosa', 'scikit-learn==0.20.3'],
    'pet_finder': ['pandas'],
    'svhn': ['scipy'],
    'the300w_lp': ['scipy'],
    'duke_ultrasound': ['scipy'],
    'wider_face': ['Pillow'],
    'wikipedia': ['mwparserfromhell', 'apache_beam'],
}


# Extra dataset deps are required for the tests
all_dataset_extras = list(itertools.chain.from_iterable(
    deps for ds_name, deps in DATASET_EXTRAS.items() if ds_name != 'nsynth'))


EXTRAS_REQUIRE = {
    'apache-beam': ['apache-beam'],
    'matplotlib': ['matplotlib'],
    'tensorflow': ['tensorflow>=1.15.0'],
    'tensorflow_gpu': ['tensorflow-gpu>=1.15.0'],
    # Tests dependencies are installed in ./oss_scripts/oss_pip_install.sh
    # and run in ./oss_scripts/oss_tests.sh
    'tests': TESTS_REQUIRE + all_dataset_extras,
    # Nsynth is run in isolation, installed and run in
    # ./oss_scripts/oss_tests.sh.
    'tests_nsynth': TESTS_REQUIRE + DATASET_EXTRAS['nsynth'],
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
        'tensorflow_datasets': DATASET_FILES + [
            'scripts/templates/*',
        ],
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
