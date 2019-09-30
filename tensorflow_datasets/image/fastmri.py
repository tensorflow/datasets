"""Main fastmri data loader script."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core import api_utils
import os
import matplotlib.pyplot as plt
import h5py
import numpy as np


_CITATION = """\
@article{DBLP:journals/corr/abs-1811-08839,
  author    = {Jure Zbontar and
               Florian Knoll and
               Anuroop Sriram and
               Matthew J. Muckley and
               Mary Bruno and
               Aaron Defazio and
               Marc Parente and
               Krzysztof J. Geras and
               Joe Katsnelson and
               Hersh Chandarana and
               Zizhao Zhang and
               Michal Drozdzal and
               Adriana Romero and
               Michael Rabbat and
               Pascal Vincent and
               James Pinkerton and
               Duo Wang and
               Nafissa Yakubova and
               Erich Owens and
               C. Lawrence Zitnick and
               Michael P. Recht and
               Daniel K. Sodickson and
               Yvonne W. Lui},
  title     = {fastMRI: An Open Dataset and Benchmarks for Accelerated {MRI}},
  journal   = {CoRR},
  volume    = {abs/1811.08839},
  year      = {2018},
  url       = {http://arxiv.org/abs/1811.08839},
  archivePrefix = {arXiv},
  eprint    = {1811.08839},
  timestamp = {Mon, 26 Nov 2018 12:52:45 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1811-08839},
  bibsource = {dblp computer science bibliography, https://dblp.org}
"""


_DESCRIPTION = """\
The anonymized imaging dataset provided by NYU Langone comprises raw k-space
data from more than 1,500 fully sampled knee MRIs obtained on 3 and 1.5 Tesla
magnets. Curation of these datasets are part of an IRB approved study.

The raw dataset includes coronal proton density-weighted images with and
without fat suppression. Raw data have been anonymized via conversion to the
vendor-neutral ISMRMD format and the RSNA clinical trial processor,
respectively.

Data used in the preparation of this article were obtained from the NYU fastMRI
Initiative database(fastmri.med.nyu.edu).[citation of arXiv paper:
https://arxiv.org/abs/1811.08839] As such, NYU fastMRI investigators provided
data but did not participate in analysis or writing of this report. A listing
of NYU fastMRI investigators,subject to updates, can be found at:
fastmri.med.nyu.edu.
The primary goal of fastMRI is to test whether machine learning can aid in the
reconstruction of medical images.
"""


def to_tensor(data):
    """
    Convert numpy array to tensor.
    Args:
    data (numpy.array): Input numpy array
    Returns:
    tf.Tensor: Tensorflow version of data
    """
    return tf.convert_to_tensor(data)


def data_stack(data):
    """
    Takes in complex arrays and real and imaginary parts
    are stacked along the last dimension.
    Args:
    data (numpy.array): Input numpy array
    Returns:
    data (numpy.array): Stacked output array
    """
    if np.iscomplexobj(data):
        data = np.stack((data.real, data.imag), axis=-1)
    return data


def apply_mask(data, mask_func, seed=None):
    """
    Subsample given k-space by multiplying with a mask.
    Args:
    data (numpy.array): The input k-space data. This should have at least 3
    dimensions, where dimensions -3 and -2 are the spatial dimensions, and
    the final dimension has size 2 (for complex values).
    mask_func (callable): A function that takes a shape (tuple of ints) and
    a random number seed and returns a mask.
    seed (int or 1-d array_like, optional): Seed for the random number
    generator.
    Returns:
    (tuple): tuple containing:
    masked data (numpy.array): Subsampled k-space data
    mask (numpy.array): The generated mask
    """
    shape = np.array(data.shape)
    shape[:-3] = 1
    mask = mask_func(shape, seed)
    return np.where(mask == 0, 0, data), mask


def fft2(data):
    """
    Apply centered 2 dimensional Fast Fourier Transform.
    Args:
    data (numpy.array): Complex valued input data containing at least 3
    dimensions: dimensions -3 & -2 are spatial dimensions and dimension -1
    has size 2. All other dimensions are assumed to be batch dimensions.
    Returns:
    numpy.array: The FFT of the input.
    """
    assert data.shape[-1] == 2
    data = np.fft.ifft2(data)
    data = np.fft.fftshift(data)
    return data


def ifft2(data):
    """
    Apply centered 2-dimensional Inverse Fast Fourier Transform.
    Args:
    data (numpy.array): Complex valued input data containing at least 3
    dimensions: dimensions-3 & -2 are spatial dimensions and dimension -1
    has size 2. All other dimensions are assumed to be batch dimensions.
    Returns:
    numpy.array: The IFFT of the input.
    """
    data = np.fft.ifft2(data)
    data = np.fft.fftshift(data)
    return data


def complex_abs(data):
    """
    Compute the absolute value of a complex valued stacked input array.
    Args:
    data (numpy.array): A complex valued array with real and
    imaginary parts stacked,where the size of the final dimension should be
    2.
    Returns:
    numpy.array: Absolute value of data
    """
    assert data.shape[-1] == 2
    return np.sqrt((data ** 2).sum(axis=-1))


def root_sum_of_squares(data, dim=0):
    """
    Compute the Root Sum of Squares (RSS) transform along a given dimension
    of an array.
    Args:
    data (numpy.array): The input array
    dim (int): The dimensions along which to apply the RSS transform
    Returns:
    rss (numpy.array): The RSS value
    """
    rss = np.sqrt((data ** 2).sum(axis=dim))
    return rss


def center_crop(data, shape):
    """
    Apply a center crop to the input real image or batch of real images.
    Args:
    data (numpy.array): The input array to be center cropped. It should
    have at least 2 dimensions and the cropping is applied along the last
    two dimensions.
    shape (int, int): The output shape. The shape should be smaller than
    the corresponding dimensions of data.
    Returns:
    np.array: The center cropped image
    """
    assert 0 < shape[0] <= data.shape[-2]
    assert 0 < shape[1] <= data.shape[-1]
    w_from = (data.shape[-2] - shape[0]) // 2
    h_from = (data.shape[-1] - shape[1]) // 2
    w_to = w_from + shape[0]
    h_to = h_from + shape[1]
    return data[..., w_from:w_to, h_from:h_to]


def complex_center_crop(data, shape):
    """
    Apply a center crop to the input image or batch of complex images.
    Args:
    data (numpy.array): The complex input tensor to be center cropped. It
    should have at least 3 dimensions and the cropping is applied along
    dimensions -3 and -2 and the last dimensions should have a size of 2.
    shape (int, int): The output shape. The shape should be smaller than
    the corresponding dimensions of data.
    Returns:
    numpy.array: The center cropped image
    """
    assert 0 < shape[0] <= data.shape[-3]
    assert 0 < shape[1] <= data.shape[-2]
    w_from = (data.shape[-3] - shape[0]) // 2
    h_from = (data.shape[-2] - shape[1]) // 2
    w_to = w_from + shape[0]
    h_to = h_from + shape[1]
    return data[..., w_from:w_to, h_from:h_to, :]


def normalize(data, mean, stddev, eps=0.):
    """
    Normalize the given array using:
    (data - mean) / (stddev + eps)
    Args:
    data (numpy.array): Input data to be normalized
    mean (float): Mean value
    stddev (float): Standard deviation
    eps (float): Added to stddev to prevent dividing by zero
    Returns:
    numpy.array: Normalized tensor
    """
    return (data - mean) / (stddev + eps)


def normalize_instance(data, eps=0.):
    """
    Normalize the given array using:
    (data - mean) / (stddev + eps)
    where mean and stddev are computed from the data itself.
    Args:
    data (numpy.array): Input data to be normalized
    eps (float): Added to stddev to prevent dividing by zero
    Returns:
    numpy.array: Normalized array
        """
    mean = data.mean()
    std = data.std()
    return normalize(data, mean, std, eps), mean, std


class MaskFunc:
    """
    MaskFunc creates a sub-sampling mask of a given shape.
    The mask selects a subset of columns from the input k-space data. If the
    k-space data has N columns, the mask picks out:
        1. N_low_freqs = (N * center_fraction) columns in the center
        corresponding to low-frequencies
        2. The other columns are selected uniformly at random with a
        probability equal to:
        prob = (N / acceleration - N_low_freqs) / (N - N_low_freqs).
    This ensures that the expected number of columns selected is equal to
    (N / acceleration)
    It is possible to use multiple center_fractions and accelerations, in which
    case one possible (center_fraction, acceleration) is chosen uniformly at
    random each time the MaskFunc object is called.
    For example, if accelerations = [4, 8] and center_fractions = [0.08, 0.04],
    then there is a 50% probability that 4-fold acceleration with 8% center
    fraction is selected and a 50% probability that 8-fold acceleration with 4%
    center fraction is selected.
    """
    def __init__(self, center_fractions, accelerations):
        """Args:
        center_fractions (List[float]): Fraction of low-frequency columns to be
        retained.
        If multiple values are provided, then one of these numbers is chosen
        uniformly each time.

        accelerations (List[int]): Amount of under-sampling. This should have
        the same length as center_fractions. If multiple values are provided,
        then one of these is chosen uniformly each time. An acceleration of 4
        retains 25% of the columns, but they may not be spaced evenly.
        """
        if len(center_fractions) != len(accelerations):
            raise ValueError('Center fractions should match accelerations')
        self.center_fractions = center_fractions
        self.accelerations = accelerations
        self.rng = np.random.RandomState()

    def __call__(self, shape, seed=None):
        """
        Args:
            shape (iterable[int]): The shape of the mask to be created. The
            shape should have at least 3 dimensions. Samples are drawn along
            the second last dimension.
            seed (int, optional): Seed for the random number generator. Setting
            the seed ensures the same mask is generated each time for the same
            shape.
        Returns:
            numpy.array: A mask of the specified shape.
        """
        if len(shape) < 3:
            raise ValueError('Shape should have 3 or more dimensions')
        self.rng.seed(seed)
        num_cols = shape[-2]
        choice = self.rng.randint(0, len(self.accelerations))
        center_fraction = self.center_fractions[choice]
        accel = self.accelerations[choice]
        # Create the mask
        num_low_freqs = int(round(num_cols * center_fraction))
        prob = (num_cols/acceleration-num_low_freqs)/(num_cols-num_low_freqs)
        mask = self.rng.uniform(size=num_cols) < prob
        pad = (num_cols - num_low_freqs + 1) // 2
        mask[pad:pad + num_low_freqs] = True
        # Reshape the mask
        mask_shape = [1 for _ in shape]
        mask_shape[-2] = num_cols
        mask = mask.reshape(*mask_shape).astype(np.float32)
        return mask

_CHALLENGES_TO_FILENAMES = {
    'singlecoil': ['singlecoil_train.tar.gz',
                   'singlecoil_test_v2.tar.gz'],
    'multicoil': ['multicoil_train.tar.gz',
                  'multicoil_test_v2.tar.gz']
}

_CHALLENGES, _FILENAMES = zip(*sorted(_CHALLENGES_TO_FILENAMES.items()))


class FastMRIConfig(tfds.core.BuilderConfig):
    """
    BuilderConfig for fastmri datasets.
    """
    @api_utils.disallow_positional_args
    def __init__(self, challenge_type, **kwargs):
        """Constructor.
        Args:
        challenge_type: string, must be one of the items in _CHALLENGES.
        **kwargs: keyword arguments forwarded to super.
        """
        super(FastMRIConfig, self).__init__(**kwargs)
        self.challenge = challenge_type


class FastMRI(tfds.core.GeneratorBasedBuilder):
    """Raw k-space MRI image data created from manual directory.

    The tar.gz files stored in the data directory should have the structure:
    ```
    path/to/manual_dir/<challenge>/fast_mri/<tar_file_train>, <tar_file_test>

    <challenge> should be either 'singlecoil' or 'multicoil'
    ```
    To use it:
    ```
    builder = tfds.image.ImageLabelFolder('<dataset_name>')
    dl_config = tfds.download.DownloadConfig(manual_dir='path/to/manual_dir/')
    builder.download_and_prepare(download_config=dl_config)
    print(builder.info)  # Splits, num examples,... automatically extracted
    ds = builder.as_dataset(split='split_name')
    ```
    ```
    """
    
    VERSION = tfds.core.Version('0.1.0')

    BUILDER_CONFIGS = [FastMRIConfig(
                            name='singlecoil',
                            version='0.0.1',
                            description='singlecoil dataset',
                            challenge_type='singlecoil'),
                       FastMRIConfig(
                            name='multicoil',
                            version='0.0.1',
                            description='multicoil dataset',
                            challenge_type='multicoil')
                       ]

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # tfds.features.FeatureConnectors
            features=tfds.features.FeaturesDict({
                "image_kspace": tfds.features.Image(shape=(None, None, 1)),
                "image_transformed": tfds.features.Image(shape=(None, None, 1))
            }),
            # If there's a common (input, target) tuple from the features,
            # specify them here. They'll be used if as_supervised=True in
            # builder.as_dataset.
            supervised_keys=None,
            # Homepage of the dataset for documentation
            urls=['https://fastmri.med.nyu.edu/'],
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        challenge = self.builder_config.challenge

        dl_paths = dl_manager.extract({
          'train': os.path.join(dl_manager.manual_dir,
                                _CHALLENGES_TO_FILENAMES[challenge][0]),
          'test': os.path.join(dl_manager.manual_dir,
                               _CHALLENGES_TO_FILENAMES[challenge][1])
        })

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    'images_dir_path': dl_paths['train'],
                    'split_type': 'train'
                },
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    'images_dir_path': dl_paths['test'],
                    'split_type': 'test'
                },
            ),
        ]

    def _generate_examples(self, images_dir_path=None, split_type=None):
        challenge = self.builder_config.challenge
        if challenge == 'singlecoil':
            if split_type == 'train':
                images_dir_path = images_dir_path + '/singlecoil_train/'
            else:
                images_dir_path = images_dir_path + '/singlecoil_test_v2/'
            for image_file in tf.io.gfile.listdir(images_dir_path):
                hf = h5py.File(images_dir_path + image_file, 'r')
                volume_kspace = hf['kspace'][()]
                slice_kspace = volume_kspace
                slice_kspace_3d = slice_kspace[0][:, :, None]
                kspace_output = np.uint8(np.log(np.abs(slice_kspace_3d)+1e-9))
                slice_image = ifft2(slice_kspace)
                slice_stack = data_stack(slice_image)
                slice_abs = complex_abs(slice_stack)
                slice_abs_3d = slice_abs[0][:, :, None]
                ab_output = np.uint8(np.log(np.abs(slice_abs_3d) + 1e-9))
                slice_tensor = to_tensor(slice_abs)
                yield image_file, {
                    "image_kspace": kspace_output,
                    "image_transformed": ab_output
                }
        else:
            if split_type == 'train':
                images_dir_path = images_dir_path + '/multicoil_train/'
            else:
                images_dir_path = images_dir_path + '/multicoil_test_v2/'
            for image_file in tf.io.gfile.listdir(images_dir_path):
                hf = h5py.File(images_dir_path + image_file, 'r')
                volume_kspace = hf['kspace'][()]
                slice_kspace = volume_kspace[20]
                slice_kspace_3d = slice_kspace[10][:, :, None]
                kspace_output = np.uint8(np.log(np.abs(slice_kspace_3d)+1e-9))
                slice_image = ifft2(slice_kspace)
                slice_stack = data_stack(slice_image)
                slice_abs = complex_abs(slice_stack)
                slice_tensor = to_tensor(slice_abs)
                slice_rss = root_sum_of_squares(slice_abs, dim=0)
                slice_rss_3d = slice_rss[:, :, None]
                rss_output = np.uint8(np.log(np.abs(slice_rss_3d) + 1e-9))
                yield image_file, {
                    "image_kspace": kspace_output,
                    "image_transformed": rss_output
                }
