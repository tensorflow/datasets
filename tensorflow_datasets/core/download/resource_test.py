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

from absl.testing import parameterized
from tensorflow_datasets import testing
from tensorflow_datasets.core.download import resource


class ResourceTest(parameterized.TestCase, testing.TestCase):

  @parameterized.parameters(
      ('bar.tar.gz', resource.ExtractMethod.TAR_GZ),
      ('bar.gz', resource.ExtractMethod.GZIP),
      ('bar.tar.zip', resource.ExtractMethod.ZIP),
      ('bar.gz.strange', resource.ExtractMethod.NO_EXTRACT),
      ('bar.tar', resource.ExtractMethod.TAR),
      ('bar.tar.bz2', resource.ExtractMethod.TAR),
      ('bar.bz2', resource.ExtractMethod.BZIP2),
  )
  def test_guess_extract_method(self, fname, expected_extract_method):
    extract_method = resource.guess_extract_method(fname)
    self.assertEqual(
        extract_method,
        expected_extract_method,
        '(%s)->%s instead of %s'
        % (fname, extract_method, expected_extract_method),
    )

  @parameterized.parameters(
      (
          'http://data.statmt.org/wmt17/translation-task/dev.tgz',
          'data.statmt.org_wmt17_translation-task_devDjZ11PU9sKPPvF2sZTAzTsV7Pi3IYHaPDMOoeEuby2E.tgz',
      ),
      (
          'http://data.statmt.org/wmt18/translation-task/training-parallel-nc-v13.tgz',
          'data.stat.org_wmt1_tran-task_trai-para-nc-6LWgxBgzCHdv_LtotNmnXjpCH6OhzkF8D3v10aRrznA.tgz',
      ),
      (
          'http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz',
          'fashion-mnist_train-images-idx3-ubytepR2BibiiUp2twRbpoktblvl2KbaPDel0VUV9KrXm91Y.gz',
      ),
      (
          'http://ufldl.stanford.edu/housenumbers/test_32x32.mat',
          'ufldl.stanford.edu_housenumbers_test_32x32kIzM03CdHZsHqtImuAxFCXPGHhEH4JT7Owsqi_QawO4.mat',
      ),
      (
          'http://www.statmt.org/lm-benchmark/1-billion-word-language-modeling-benchmark-r13output.tar.gz',
          'stat.org_lm-benc_1-bill-word-lang-mode-fPxXes4bTZ_y2eAI2mGRqBKUvUJm1CS1Idm0DH98KN8.tar.gz',
      ),
      (
          'http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz',
          'statmt.org_wmt13_traini-parall-europa-v71cKcs9sx8w9ctm8xHloEI83SJqzD7piDNK3xUXpQIB4.tgz',
      ),
      (
          'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz',
          'yann.lecu.com_exdb_mnis_trai-imag-idx3-ubyt5m0Lc_VeEzGZ1PUycLKoWNyYkH_vWEKNi0mu7m4Hmbk.gz',
      ),
      (
          'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz',
          'yann.lecu.com_exdb_mnis_trai-labe-idx1-ubyt7cc_IeM51G_ngIY2ORleKjMjLVCXd-TCUHlYvEiRiKI.gz',
      ),
      (
          'https://drive.google.com/uc?export=download&id=0B7EVK8r0v71pd0FJY3Blby1HUTQ',
          'ucexport_download_id_0B7EVK8r0v71pd0FJY3Blby1HbdQ1eXJPJLYv0yq8hL1lCD5T2aOraaQwvj25ndmE7pg',
      ),
      (
          'https://github.com/brendenlake/omniglot/raw/master/python/images_background_small2.zip',
          'bren_omni_raw_mast_pyth_imag_back_smalUSA8LkdUW89lgXr31txDoVFbI9BtQhxvtZWYTIdAJAg.zip',
      ),
      (
          'https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json',
          'rajpurkar_SQuAD-explorer_train-v1.1uLsZc14btZFRCgHMAy9Mn5abwO6wga4bMozTBvOyQAg.json',
      ),
      (
          'https://storage.googleapis.com/scv_dataset/data/Brawl_64x64_png/valid-00000-of-00001.tfrecords',
          'scv_Brawl_64x64_png_valid-0_1Ez3yPwN0QDCxBd0xHeLb2DfUERJjkqFd2dyL5Z7-ULg.tfrecords',
      ),
      (
          'https://storage.googleapis.com/scv_dataset/data/CollectMineralShards_128x128_png/train-00005-of-00010.tfrecords',
          'scv_CollectMi_128x128_png_train-5_10kiunW_2RTDhXuPrxCVkUZKCoWpADYBUWE8DpraC8zAA.tfrecords',
      ),
      (
          'https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz',
          'cs.toronto.edu_kriz_cifar-100-pythonJDFhDchdt5UW8GUAkvf_-H_r_LnFs6sHlOrqTidrpSI.tar.gz',
      ),
  )
  def test_get_dl_fname(self, url, expected_dl_fname):
    dl_fname = resource.get_dl_fname(url)
    self.assertEqual(dl_fname, expected_dl_fname)


if __name__ == '__main__':
  testing.test_main()
