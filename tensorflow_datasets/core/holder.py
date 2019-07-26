import os
import re

import tensorflow as tf
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core import lazy_imports
from tensorflow_datasets.core import naming
from tensorflow_datasets.scripts import create_new_dataset
import json
import shutil
import zipfile


# TODO add tar.gz support
# TODO check types with python-magic (pip install python-magic-bin==0.4.14
# TODO check archive or extracted
# TODO count created example for test file
# TODO create auto test

NUMBER_OF_CREATED_FILE = 0

class Holder(object):

	def __init__(self, name, file_type, path, output_path=None):
		self.name = name  # image
		self.typ = file_type  # png
		self.path = path  # /folder/image.png
		self.output_path = output_path  # /target_folder/image.png
		self.create_basedir()

	def create_basedir(self):
		basedir = os.path.dirname(self.output_path)
		if not tf.io.gfile.exists(basedir):
			tf.io.gfile.makedirs(basedir)


class ImageHolder(Holder):

	def __init__(self, zip_file=None, *args, **kwargs):
		super(ImageHolder, self).__init__(*args, **kwargs)
		self.zip_file = zip_file

	def image_size(self):
		try:
			if self.zip_file:
				infile = self.path
				file = self.zip_file.open(infile, 'r')
			else:
				file = self.path
			im = lazy_imports.PIL_Image.open(file)
			return im.size
		except OSError:
			return 10, 10

	def create_fakes(self):
		global NUMBER_OF_CREATED_FILE
		img = lazy_imports.PIL_Image.new('RGB', self.image_size(), (255, 255, 255))
		img.save(self.output_path)
		NUMBER_OF_CREATED_FILE += 1
		print('created, ', self.output_path, ', size: ', self.image_size())


class PlainTextHolder(Holder):

	def __init__(self, zip_file=None, *args, **kwargs):
		super(PlainTextHolder, self).__init__(*args, **kwargs)
		self.zip_file = zip_file

	def create_fakes(self):
		global NUMBER_OF_CREATED_FILE
		out = tf.io.gfile.GFile(self.output_path, mode='w')
		if self.zip_file:
			inf = self.zip_file.open(self.path, 'r')
		else:
			inf = tf.io.gfile.GFile(self.path, mode='r')
		count = 0
		breaker = 0
		while count < 4 and breaker < 30:  # write 4 non empty line
			line = inf.readline()
			out.write(line)
			if not line.rstrip():
				count += 1
			breaker += 1
		out.close()
		NUMBER_OF_CREATED_FILE += 1
		print('created, ', self.output_path)


class ZipHolder(Holder):
	def __init__(self, *args, **kwargs):
		super(ZipHolder, self).__init__(*args, **kwargs)

	def create_fakes(self):
		zip_file = zipfile.ZipFile(self.path)
		f = zip_file.namelist()
		r = re.compile(".*/$")
		folders = list(filter(r.match, f))  # it's catch the folders names
		ex_files = []
		for prefix in folders[:2]:  # take 2 example from 2 folders
			ex_files += list(filter(lambda x: x.startswith(prefix), f))[1:3]
			ex_files += list(filter(lambda x: x.startswith(prefix)
																						and not x.endswith('/'), f))[1:3]
		ex_files = ex_files[:5] if len(ex_files) > 4 else ex_files
		for file in set(ex_files):
			name = os.path.basename(file)
			typ = os.path.splitext(file)[1]
			basedir = os.path.basename(os.path.splitext(self.output_path)[0])
			if basedir in file:
				rel_path = os.path.relpath(file, basedir)
			else:
				rel_path = file
			target_path = os.path.join(os.path.splitext(self.output_path)[0], rel_path)
			hold = HolderFactory(zip_file, name, typ, file,
													 target_path).generate_holder()
			if hold is not None:
				hold.create_fakes()
			else:
				continue
		zip_file.close()
		folder_path = os.path.splitext(self.output_path)[0]
		shutil.make_archive(folder_path, 'zip', folder_path)
		tf.io.gfile.rmtree(folder_path)  # delete created unzipped folder


class HolderFactory(Holder):
	def __init__(self, zip_file=None, *args, **kwargs):
		super(HolderFactory, self).__init__(*args, **kwargs)
		self.zip_file = zip_file

	def generate_holder(self):
		if self.path.endswith('.zip'):
			return ZipHolder(self.name, self.typ, self.path, self.output_path)
		elif self.path.endswith(('.jpg', '.jpeg', '.png', '.tiff')):
			return ImageHolder(self.zip_file, self.name, self.typ, self.path,
												 self.output_path)
		elif self.path.endswith(
				('.csv', '.txt', '.en', '.ne', '.si', '.data', '.md')):
			return PlainTextHolder(self.zip_file, self.name, self.typ, self.path, self.output_path)


class Generator(object):
	"""
	Generator of fake examples of dataset for testing.

	Example Usages:

		Just give an dataset_name when using
		default tfds download dir.(`~/tensorflow_datasets/downloads`)

		>> Generator('cats_vs_dogs').generator()

		Give a downloaded file or extracted folder path.
		>> Generator('cats_vs_dogs',
									dataset_path='~/tensorflow_datasets/downloads/kgyq21XHr2.zip')
									.generator()
	"""

	def __init__(self, dataset_name, dataset_path=None, dataset_type='image'):
		"""
		Args:
			dataset_name: dataset name of generated
			dataset_path: path of downloaded file, default is None. It's search path
			on the `~/tensorflow_datasets/downloads` and return downloaded file path.
			dataset_type: type of dataset for creating test file, default is image
		"""
		self.dataset_name = dataset_name
		self.dataset_type = dataset_type
		self.inpath = dataset_path if dataset_path else dataset_folder_finder(dataset_name)[0]
		self.outpath = os.path.join(py_utils.tfds_dir(), 'testing',
																						 'test_data', 'fake_examples',
																						 os.path.basename(
																							 self.inpath))
		self.is_extracted = (dataset_folder_finder(dataset_name)[1] == 'extracted')

	def zip_generator(self):
		self.outpath = os.path.join(py_utils.tfds_dir(), 'testing',
																						 'test_data', 'fake_examples',
																						 self.dataset_name,
																						 os.path.basename(
																							 self.inpath))
		hold = HolderFactory(None, self.dataset_name, 'zip', self.inpath, self.outpath)
		try:
			hold.generate_holder().create_fakes()
		except AttributeError:
			pass

	def generator(self):
		global NUMBER_OF_CREATED_FILE

		self.generator_of_tests()

		if not os.path.isdir(self.inpath):
			self.zip_generator()
		else:
			for dirpath, dirnames, filenames in tf.io.gfile.walk(self.inpath):
				structure = os.path.join(self.outpath,
																 os.path.relpath(dirpath, self.inpath))
				if not tf.io.gfile.isdir(structure):
					tf.io.gfile.mkdir(structure)
				else:
					print("Folder does already exits!")
				count = 0
				while count < 2:  # take just 2 files on one folder
					try:
						file = filenames[count]
					except IndexError:
						break
					file_path = os.path.join(dirpath, file)
					file_target_path = os.path.join(structure, file)
					name = os.path.basename(file_path)
					typ = os.path.splitext(file_path)[1]
					hold = HolderFactory(None, name, typ, file_path, file_target_path)
					try:
						hold.generate_holder().create_fakes()
					except AttributeError:
						pass
					count += 1
					if NUMBER_OF_CREATED_FILE > 4:
						break
		print(NUMBER_OF_CREATED_FILE)

	def generator_of_tests(self):
		data = dict(
			dataset_name=self.dataset_name,
			dataset_type=self.dataset_type,
			dataset_cls=naming.snake_to_camelcase(self.dataset_name),
			TODO='TODO({})'.format(self.dataset_name),
		)
		if not self.is_extracted:
			dl_extract_result = (
				"\n# It's created by automatically by auto fake generator. Check it path!\n"
				"  DL_EXTRACT_RESULT = {{\n"
				"  		\"train\": \"{path}\"\n"
				"  }}\n").format(path=os.path.basename(self.inpath))
		else:
			dl_extract_result = ''

		create_new_dataset.create_dataset_test_file(py_utils.tfds_dir(), data,
																								dl_extract_result)


def dataset_folder_finder(dataset_name, home_path=None):
	home = home_path if home_path else os.path.expanduser('~')
	download_path = os.path.join(home, 'tensorflow_datasets', 'downloads')
	extracted_path = os.path.join(download_path, 'extracted')

	for r, d, f in tf.io.gfile.walk(download_path):
		for file in f:
			if file.endswith(".INFO"):
				info_file = os.path.join(r, file)
				file_path = os.path.splitext(info_file)[0]
				filename = os.path.basename(file_path)
				with tf.io.gfile.GFile(info_file) as data_file:
					data_item = json.load(data_file)
					if dataset_name in data_item['dataset_names']:
						for x, y, z in tf.io.gfile.walk(extracted_path):
							for folder in y:
								if filename in folder:
									# it's a extracted
									return os.path.join(extracted_path, folder), 'extracted'
						return file_path, 'compressed'
	raise FileNotFoundError(
		'Dataset not found in `{}`. Please be sure the dataset is downloaded!'
		.format(download_path))