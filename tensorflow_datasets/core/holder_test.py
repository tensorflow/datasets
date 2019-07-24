import os
import sys

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import holder
from tensorflow_datasets.core import lazy_imports
import shutil
import zipfile

if sys.version_info.major == 2:
	import mock  # pylint: disable=g-import-not-at-top,unused-import
	from itertools import \
		izip as zip  # pylint: disable=g-import-not-at-top,unused-import
else:
	from unittest import \
		mock  # pylint: disable=g-import-not-at-top,g-importing-member


class TestImageHolder(testing.TestCase):

	@classmethod
	def setUpClass(cls):
		super(TestImageHolder, cls).setUpClass()
		cls.TEST_DIR = testing.make_tmp_dir()
		cls._image_path = os.path.join(cls.TEST_DIR, 'test.png')
		cls._image_size = (11, 11)
		with mock.patch.object(holder.ImageHolder, 'image_size',
													 return_value=cls._image_size):
			image = holder.ImageHolder(None, 'test', 'png', None, cls._image_path)
			image.create_fakes()
		cls.im_size = lazy_imports.PIL_Image.open(cls._image_path).size

	def test_create_fakes(self):
		self.assertTrue(tf.io.gfile.exists(self._image_path))

	def test_image_size(self):
		self.assertEqual(self.im_size, self._image_size)

	@classmethod
	def tearDownClass(cls):
		testing.rm_tmp_dir(cls.TEST_DIR)


class TestPlainTextHolder(testing.TestCase):

	@classmethod
	def setUpClass(cls):
		super(TestPlainTextHolder, cls).setUpClass()
		cls.TEST_DIR = testing.make_tmp_dir()
		cls._target_file_path = os.path.join(cls.TEST_DIR, 'created.txt')
		cls._output_file_path = os.path.join(cls.TEST_DIR, 'test.txt')
		with tf.io.gfile.GFile(cls._target_file_path, 'w') as f:
			for i in range(10):
				f.write("This is line %d\r\n" % (i + 1))
		file = holder.PlainTextHolder(None, 'test', 'txt', cls._target_file_path,
																	cls._output_file_path)
		file.create_fakes()

	def test_create_fakes(self):
		with tf.io.gfile.GFile(self._target_file_path, 'r') as target_file, \
				tf.io.gfile.GFile(self._output_file_path, 'r') as fake_file:
			for x, y in zip(target_file, fake_file):
				self.assertEqual(x, y)

	@classmethod
	def tearDownClass(cls):
		testing.rm_tmp_dir(cls.TEST_DIR)


class TestZipHolder(tf.test.TestCase):

	@classmethod
	def setUpClass(cls):
		super(TestZipHolder, cls).setUpClass()
		cls.TEMP_DIR = testing.make_tmp_dir()
		cls.TEST_DIR = os.path.join(cls.TEMP_DIR, 'test_folder')
		# create fake image
		cls._image_folder = os.path.join(cls.TEST_DIR, 'image')
		tf.io.gfile.makedirs(cls._image_folder)
		cls.image_file_path = os.path.join(cls._image_folder, 'image.png')
		with mock.patch.object(holder.ImageHolder, 'image_size', return_value=(11, 11)):
			image = holder.ImageHolder(None, 'image', 'png', None, cls.image_file_path)
			image.create_fakes()
		# create fake text file
		cls.text_folder = os.path.join(cls.TEST_DIR, 'text')
		tf.io.gfile.makedirs(cls.text_folder)
		cls.text_file_path = os.path.join(cls.text_folder, 'test.txt')
		with tf.io.gfile.GFile(cls.text_file_path, 'w') as f:
			for i in range(10):
				f.write("This is line %d\r\n" % (i + 1))

		shutil.make_archive(cls.TEST_DIR, 'zip', cls.TEST_DIR)
		cls.zip_path = cls.TEST_DIR + '.zip'
		cls.out_zip_path = cls.TEST_DIR + '_auto_gen.zip'
		zip_gen = holder.ZipHolder('test_folder', 'zip', cls.zip_path, cls.out_zip_path)
		zip_gen.create_fakes()

	def test_create_fakes(self):
		original_zip_files = zipfile.ZipFile(self.zip_path).namelist()
		copied_zip_files = zipfile.ZipFile(self.out_zip_path).namelist()
		self.assertEqual(original_zip_files, copied_zip_files)

	@classmethod
	def tearDownClass(cls):
		testing.rm_tmp_dir(cls.TEMP_DIR)


if __name__ == '__main__':
	testing.test_main()
