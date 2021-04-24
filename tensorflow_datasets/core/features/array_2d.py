# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Array2D feature for raising error (Not implemented currently). """

class Array2D:
    """Array2D feature is used in only two datasets in the community
    HuggingFace datasests.

    Since, both datasets are present in TFDS locally as well, this feature
    is not currently implemented.

    This is a dummy class to be used in the HF wrapper to map the HF function
    to this as:

    ```
    Array2D = features.Array2D
    ```
    It raises a custom error for the user whenever `Array2D` is used and also,
    prompts the user to check TFDS datasets if the dataset is available locally

    Example:

    * In this HUggingFace dataset script:

    ```
    features=datasets.Features(
        {
            "image": datasets.Array2D(shape=(28, 28), dtype="uint8"),
            "label": datasets.features.ClassLabel(names=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]),
        }
    ```

    * During dataset generation, output:


    """

    def __init__(self, **args):
        """ Raise an error message whenever `Array2D()` is called

        Args:
        Any or no arguments that the HF Array2D supports

        Raises:
        AttributeError: In all conditions currently.
        """
        #Raising custom error message
        exception_msg = "Array2D not supported in TFDS"
        suffix = """ \nYou can have a look at TFDS datasets if the dataset is available locally.
        """
        raise AttributeError(f'{exception_msg}{suffix}')
