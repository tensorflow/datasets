import os
import re

import tensorflow as tf
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core import lazy_imports

import json
import shutil
import zipfile


# TODO add tar.gz support
# TODO check types with python-magic
# TODO check archive or extracted
# TODO count created example for test file
# TODO folder limit 2

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
		img = lazy_imports.PIL_Image.new('RGB', self.image_size(), (255, 255, 255))
		img.save(self.output_path)
		print('created, ', self.output_path, ', size: ', self.image_size())


class PlainTextHolder(Holder):

	def __init__(self, zip_file=None, *args, **kwargs):
		super(PlainTextHolder, self).__init__(*args, **kwargs)
		self.zip_file = zip_file

	def create_fakes(self):
		out = tf.io.gfile.GFile(self.output_path, mode='w')
		if self.zip_file:
			inf = self.zip_file.open(self.path, 'r')
		else:
			inf = tf.io.gfile.GFile(self.path, mode='r')
		count = 0
		breaker = 0
		while count < 5 and breaker < 30:  # write 5 non empty line
			line = inf.readline()
			out.write(line)
			if not line.rstrip():
				count += 1
			breaker += 1
		out.close()
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

	def __init__(self, dataset_name, dataset_path=None):
		"""
		Args:
			dataset_name: dataset name of generated
			dataset_path: path of downloaded file, default is None. It's search path
			on the `~/tensorflow_datasets/downloads` and return downloaded file path.
		"""
		self.dataset_name = dataset_name
		self.inpath = dataset_path if dataset_path else dataset_folder_finder(dataset_name)
		self.outpath = os.path.join(py_utils.tfds_dir(), 'testing',
																						 'test_data', 'fake_examples',
																						 os.path.basename(
																							 self.inpath))

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
		if self.inpath.endswith('.zip'):
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


def dataset_folder_finder(dataset_name, home_path=None):
	home = home_path if home_path else os.path.expanduser('~')
	path = os.path.join(home, 'tensorflow_datasets', 'downloads')

	for r, d, f in tf.io.gfile.walk(path):
		for file in f:
			if file.endswith(".INFO"):
				info_file = os.path.join(r, file)
				filename = os.path.splitext(info_file)[0]
				with tf.io.gfile.GFile(info_file) as data_file:
					data_item = json.load(data_file)
					if dataset_name in data_item['dataset_names']:
						return filename
	raise FileNotFoundError(
		'Dataset not found in `{}`. Please be sure the dataset is downloaded!'.format(
			path))