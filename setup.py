# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""tensorflow/datasets is a library of datasets ready to use with TensorFlow.

tensorflow/datasets is a library of public datasets ready to use with
TensorFlow. Each dataset definition contains the logic necessary to download and
prepare the dataset, as well as to read it into a model using the
`tf.data.Dataset` API.

Usage outside of TensorFlow is also supported.

See the README on GitHub for further documentation.
"""

import itertools
import os
import sys

import pkg_resources
import setuptools

# To enable importing version.py directly, we add its path to sys.path.
version_path = os.path.join(os.path.dirname(__file__), 'tensorflow_datasets')
sys.path.append(version_path)
from version import __version__  # pytype: disable=import-error  # pylint: disable=g-import-not-at-top

if datestring := os.environ.get('TFDS_NIGHTLY_TIMESTAMP'):
  project_name = 'tfds-nightly'
  # Version as `X.Y.Z.dev199912312459`
  curr_version = pkg_resources.parse_version(__version__)
  __version__ = f'{curr_version.base_version}.dev{datestring}'
else:
  project_name = 'tensorflow-datasets'

DOCLINES = __doc__.split('\n')

REQUIRED_PKGS = [
    'absl-py',
    # Min version of 0.5.0 as old array_record wheel are bugged on all
    # platform except 'x86_64'. See
    # https://github.com/google/array_record/issues/71
    'array_record>=0.5.0;platform_system=="Linux"',
    'dm-tree',
    'etils[edc,enp,epath,epy,etree]>=1.6.0;python_version<"3.11"',
    'etils[edc,enp,epath,epy,etree]>=1.9.1;python_version>="3.11"',
    'immutabledict',
    'numpy',
    'promise',
    'protobuf>=3.20',
    'psutil',
    'pyarrow',
    'requests>=2.19.0',
    'simple_parsing',
    'tensorflow-metadata',
    'termcolor',
    'toml',
    'tqdm',
    'wrapt',
    # Standard library backports
    'importlib_resources;python_version<"3.9"',
]

TESTS_DEPENDENCIES = [
    'dill',
    'jax[cpu]==0.4.28',
    'jupyter',
    'pytest',
    'pytest-shard',
    'pytest-xdist',
    # Lazy-deps required by core
    'apache-beam',
    'conllu',
    'mlcroissant>=1.0.9',
    'pandas',
    'pydub',
    # Required by scripts/documentation/
    'pyyaml',
    'tensorflow-io[tensorflow];python_version<"3.12"',
]

# Additional deps for formatting
DEV_DEPENDENCIES = [
    'pylint>=2.6.0',
    'yapf',
]

# Static files needed by datasets.
DATASET_FILES = [
    'datasets/imagenet2012/labels.txt',
    'datasets/imagenet2012/validation_labels.txt',
    'datasets/lvis/classes.txt',
    'datasets/ogbg_molpcba/tasks.txt',
    'datasets/quickdraw/labels.txt',
    'datasets/smartwatch_gestures/labels.txt',
    'image_classification/caltech101_labels.txt',
    'image_classification/categories_places365.txt',
    'image_classification/cbis_ddsm_calc_distributions.txt',
    'image_classification/cbis_ddsm_calc_types.txt',
    'image_classification/cbis_ddsm_mass_margins.txt',
    'image_classification/cbis_ddsm_mass_shapes.txt',
    'image_classification/cbis_ddsm_patch_labels.txt',
    'image_classification/dtd_key_attributes.txt',
    'image_classification/food-101_classes.txt',
    'image_classification/i_naturalist2018/inaturalist2018_labels.txt',
    'image_classification/i_naturalist2018/inaturalist2018_supercategories.txt',
    'image_classification/i_naturalist2021/i_naturalist2021_labels.txt',
    'image_classification/i_naturalist2021/i_naturalist2021_supercategories.txt',
    'image_classification/imagenet_resized_labels.txt',
    'image_classification/imagenette_labels.txt',
    'image_classification/imagewang_labels.txt',
    'image_classification/inaturalist_labels.txt',
    'image_classification/inaturalist_supercategories.txt',
    'image_classification/placesfull/categories_placesfull.txt',
    'image_classification/plantae_k_urls.txt',
    'image_classification/sun397_labels.txt',
    'image_classification/sun397_tfds_te.txt',
    'image_classification/sun397_tfds_tr.txt',
    'image_classification/sun397_tfds_va.txt',
    'object_detection/open_images_classes_all.txt',
    'object_detection/open_images_classes_boxable.txt',
    'object_detection/open_images_classes_trainable.txt',
    'video/tao/labels.txt',
    'video/ucf101_labels.txt',
    'video/youtube_vis/labels.txt',
]

# Extra dependencies required by specific datasets
DATASET_EXTRAS = {
    # In alphabetical order
    'aflw2k3d': ['scipy'],
    'beir': ['apache-beam'],
    'ble_wind_field': ['gcsfs', 'zarr'],
    'c4': [
        'apache-beam',
        'gcld3',
        'langdetect',
        # nltk==3.8.2 is broken: https://github.com/nltk/nltk/issues/3293
        'nltk==3.8.1',
        'tldextract',
    ],
    'c4_wsrs': ['apache-beam'],
    'cats_vs_dogs': ['matplotlib'],
    'colorectal_histology': ['Pillow'],
    'common_voice': ['pydub'],  # and ffmpeg installed
    'duke_ultrasound': ['scipy'],
    'eurosat': ['scikit-image', 'tifffile', 'imagecodecs'],
    'groove': ['pretty_midi', 'pydub'],
    'gtzan': ['pydub'],
    'imagenet2012_corrupted': [
        # This includes pre-built source; you may need to use an alternative
        # route to install OpenCV
        'opencv-python',
        'scikit-image',
        'scipy',
    ],
    'librispeech': ['pydub'],  # and ffmpeg installed
    'lsun': ['tensorflow-io[tensorflow]'],
    # sklearn version required to avoid conflict with librosa from
    # https://github.com/scikit-learn/scikit-learn/issues/14485
    # See https://github.com/librosa/librosa/issues/1160
    'nsynth': ['crepe>=0.0.11', 'librosa', 'scikit-learn==0.20.3'],
    'ogbg_molpcba': ['pandas', 'networkx'],
    'pet_finder': ['pandas'],
    'qm9': ['pandas'],
    'robonet': ['h5py'],  # and ffmpeg installed
    # envlogger is not available for Python versions >= 3.11 or non Linux
    # platforms: https://pypi.org/project/envlogger/#files
    'locomotion': ['envlogger;python_version<"3.11" and sys_platform=="linux"'],
    'robosuite_panda_pick_place_can': [
        'envlogger;python_version<"3.11" and sys_platform=="linux"'
    ],
    'smartwatch_gestures': ['pandas'],
    'svhn': ['scipy'],
    'the300w_lp': ['scipy'],
    'wake_vision': ['pandas'],
    'wider_face': ['Pillow'],
    'wiki_dialog': ['apache-beam'],
    'wikipedia': ['apache-beam', 'mwparserfromhell', 'mwxml'],
    'wsc273': ['bs4', 'lxml'],
    'youtube_vis': ['pycocotools'],
}

# Those datasets have dependencies which conflict with the rest of TFDS, so
# running them in an isolated environments.
ISOLATED_DATASETS = ('nsynth', 'lsun')

# Extra dataset deps are required for the tests
all_dataset_dependencies = list(
    itertools.chain.from_iterable(
        deps
        for ds_name, deps in DATASET_EXTRAS.items()
        if ds_name not in ISOLATED_DATASETS
    )
)

TESTS_ALL_DEPENDENCIES = TESTS_DEPENDENCIES + all_dataset_dependencies
# `datasets` needs to be installed separately in Python >= 3.10 due to
# conflicts between `multiprocess` and `apache-beam` libraries. See
# https://github.com/uqfoundation/multiprocess/issues/125
HUGGINGFACE_ALL_DEPENDENCIES = [
    dep for dep in TESTS_ALL_DEPENDENCIES if not dep.startswith('apache-beam')
] + ['datasets']

EXTRAS = {
    'matplotlib': ['matplotlib'],
    'tensorflow': ['tensorflow>=2.1'],
    'tf-nightly': ['tf-nightly'],
    'tensorflow-data-validation': ['tensorflow-data-validation'],
    'tests-all': TESTS_ALL_DEPENDENCIES,
    'dev': TESTS_DEPENDENCIES + DEV_DEPENDENCIES,
    'huggingface': HUGGINGFACE_ALL_DEPENDENCIES,
}
EXTRAS.update(DATASET_EXTRAS)

setuptools.setup(
    name=project_name,
    version=__version__,
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    author='Google Inc.',
    author_email='packages@tensorflow.org',
    url='https://github.com/tensorflow/datasets',
    download_url='https://github.com/tensorflow/datasets/tags',
    license='Apache 2.0',
    packages=setuptools.find_packages(),
    package_data={
        'tensorflow_datasets': DATASET_FILES + [
            # Bundle `datasets/` folder in PyPI releases
            'datasets/*/*',
            'core/utils/colormap.csv',
            'scripts/documentation/templates/*',
            'url_checksums/*',
            'checksums.tsv',
            'community-datasets.toml',
            'dataset_collections/*/*.md',
            'dataset_collections/*/*.bib',
            'core/valid_tags.txt',
        ],
    },
    exclude_package_data={
        'tensorflow_datasets': [
            'dummy_data/*',
        ],
    },
    scripts=[],
    install_requires=REQUIRED_PKGS,
    python_requires='>=3.10',
    extras_require=EXTRAS,
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
    # Include_package_data is required for setup.py to recognize the MANIFEST.in
    #   https://python-packaging.readthedocs.io/en/latest/non-code-files.html
    include_package_data=True,
)
