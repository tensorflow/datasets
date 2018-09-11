"""Install tensorflow_datasets."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='tensorflow_datasets',
    version='0.0.1',
    description='tensorflow/datasets',
    author='Google Inc.',
    author_email='no-reply@google.com',
    url='http://github.com/tensorflow/datasets',
    license='Apache 2.0',
    packages=find_packages(),
    package_data={},
    scripts=[],
    install_requires=[
        'future',
        'six',
    ],
    extras_require={
        'tensorflow': ['tensorflow>=1.9.0'],
        'tensorflow_gpu': ['tensorflow-gpu>=1.9.0'],
        'tests': [
            'pytest',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='tensorflow machine learning datasets',
)
