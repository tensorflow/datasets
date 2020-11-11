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

import pkg_resources
from setuptools import find_packages
from setuptools import setup

if '--nightly' in sys.argv:
  nightly = True
  sys.argv.remove('--nightly')
else:
  nightly = False

project_name = 'tensorflow-datasets'

# To enable importing version.py directly, we add its path to sys.path.
version_path = os.path.join(
    os.path.dirname(__file__), 'tensorflow_datasets')
sys.path.append(version_path)
from version import __version__  # pytype: disable=import-error  # pylint: disable=g-import-not-at-top

if nightly:
  project_name = 'tfds-nightly'
  # Version as `X.Y.Z.dev199912312459`
  datestring = (os.environ.get('TFDS_NIGHTLY_TIMESTAMP') or
                datetime.datetime.now().strftime('%Y%m%d%H%M'))
  curr_version = pkg_resources.parse_version(__version__)
  __version__ = f'{curr_version.base_version}.dev{datestring}'


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
    # Standard library backports
    'dataclasses;python_version<"3.7"',
    'typing_extensions;python_version<"3.8"',
    'importlib_resources;python_version<"3.9"',
]

TESTS_REQUIRE = [
    'jupyter',
    'mako',
    'pytest',
    'pytest-xdist',
    # Lazy-deps required by core
    'pandas',
    'pydub',
    'apache_beam',
    # TFDV is only available for Python 3.6
    'tensorflow-data-validation;python_version<"3.7"',
    # TODO(b/142892342): Re-enable
    # 'tensorflow-docs @ git+https://github.com/tensorflow/docs#egg=tensorflow-docs',  # pylint: disable=line-too-long
]

# Additional deps for formatting
DEV_REQUIRE = [
    'pylint>=2.6.0',
    'yapf',
]

# Static files needed by datasets.
DATASET_FILES = [
    'image_classification/caltech101_labels.txt',
    'image_classification/categories_places365.txt',
    'image_classification/cbis_ddsm_calc_distributions.txt',
    'image_classification/cbis_ddsm_calc_types.txt',
    'image_classification/cbis_ddsm_mass_margins.txt',
    'image_classification/cbis_ddsm_mass_shapes.txt',
    'image_classification/cbis_ddsm_patch_labels.txt',
    'image_classification/dtd_key_attributes.txt',
    'image_classification/food-101_classes.txt',
    'image_classification/imagenet_resized_labels.txt',
    'image_classification/imagenet2012_labels.txt',
    'image_classification/imagenet2012_validation_labels.txt',
    'image_classification/imagenette_labels.txt',
    'image_classification/imagewang_labels.txt',
    'image_classification/inaturalist_labels.txt',
    'image_classification/inaturalist_supercategories.txt',
    'image_classification/plant_leaves_urls.txt',
    'image_classification/plantae_k_urls.txt',
    'image_classification/quickdraw_labels.txt',
    'image_classification/sun397_labels.txt',
    'image_classification/sun397_tfds_te.txt',
    'image_classification/sun397_tfds_tr.txt',
    'image_classification/sun397_tfds_va.txt',
    'image_classification/vgg_face2_labels.txt',
    'object_detection/open_images_classes_all.txt',
    'object_detection/open_images_classes_boxable.txt',
    'object_detection/open_images_classes_trainable.txt',
    'video/ucf101_labels.txt',
]

# Extra dependencies required by specific datasets
DATASET_EXTRAS = {
    # In alphabetical order
    'aflw2k3d': ['scipy'],
    'c4': ['apache_beam', 'gcld3', 'langdetect', 'nltk', 'tldextract'],
    'cats_vs_dogs': ['matplotlib'],
    'colorectal_histology': ['Pillow'],
    'common_voice': ['pydub'],  # and ffmpeg installed
    'eurosat': ['scikit-image', 'tifffile', 'imagecodecs'],
    'groove': ['pretty_midi', 'pydub'],
    'imagenet2012_corrupted': [
        # This includes pre-built source; you may need to use an alternative
        # route to install OpenCV
        'opencv-python',
        'scikit-image',
        'scipy'
    ],
    'librispeech': ['pydub'],  # and ffmpeg installed
    # sklearn version required to avoid conflict with librosa from
    # https://github.com/scikit-learn/scikit-learn/issues/14485
    # See https://github.com/librosa/librosa/issues/1160
    'nsynth': ['crepe>=0.0.11', 'librosa', 'scikit-learn==0.20.3'],
    'pet_finder': ['pandas'],
    'robonet': ['h5py'],  # and ffmpeg installed
    'svhn': ['scipy'],
    'the300w_lp': ['scipy'],
    'duke_ultrasound': ['scipy'],
    'wider_face': ['Pillow'],
    'wikipedia': ['mwparserfromhell', 'apache_beam'],
    'lsun': ['tensorflow-io'],
    'wsc273': ['bs4', 'lxml'],
}


# Those datasets have dependencies which conflict with the rest of TFDS, so
# running them in an isolated environments.
# See `./oss_scripts/oss_tests.sh` for the isolated test.
ISOLATED_DATASETS = ('nsynth', 'lsun')

# Extra dataset deps are required for the tests
all_dataset_extras = list(itertools.chain.from_iterable(
    deps for ds_name, deps in DATASET_EXTRAS.items()
    if ds_name not in ISOLATED_DATASETS
))


EXTRAS_REQUIRE = {
    'matplotlib': ['matplotlib'],
    'tensorflow': ['tensorflow>=2.1'],
    'tensorflow-data-validation': ['tensorflow-data-validation'],

    # Tests dependencies are installed in ./oss_scripts/oss_pip_install.sh
    # and run in ./oss_scripts/oss_tests.sh
    'tests-all': TESTS_REQUIRE + all_dataset_extras,
    'dev': TESTS_REQUIRE + DEV_REQUIRE,
}
EXTRAS_REQUIRE.update(DATASET_EXTRAS)

setup(
    name=project_name,
    version=__version__,
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    author='Google Inc.',
    author_email='packages@tensorflow.org',
    url='https://github.com/tensorflow/datasets',
    download_url='https://github.com/tensorflow/datasets/tags',
    license='Apache 2.0',
    packages=find_packages(),
    package_data={
        'tensorflow_datasets': DATASET_FILES + [
            'scripts/documentation/templates/*',
            'url_checksums/*',
            'checksums.tsv',
        ],
    },
    exclude_package_data={
        'tensorflow_datasets': [
            'dummy_data/*',
        ],
    },
    scripts=[],
    install_requires=REQUIRED_PKGS,
    python_requires='>=3.6',
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='tensorflow machine learning datasets',
    entry_points={
        'console_scripts': [
            'tfds = tensorflow_datasets.scripts.cli.main:launch_cli'
        ],
    },
)
