import os
import zipfile
import shutil
from PIL import Image
import tensorflow as tf


# TODO add tar.gz support
# TODO check types with python-magic

class Holder:

	def __init__(self, name, file_type, path, output_path=None):
		self.name = name  # image
		self.typ = file_type  # png
		self.path = path  # /folder/image.png
		self.output_path = output_path  # /target_folder/image.png


class ImageHolder(Holder):

	def __init__(self, zip_file=None, *args, **kwargs):
		super(ImageHolder, self).__init__(*args, **kwargs)
		self.zip_file = zip_file

	def image_size(self):
		try:
			if self.zip_file:
				infile = self.path
				file = self.zip_file.open(infile,	'r')
			else:
				file = self.path
			im = Image.open(file)
			return im.size
		except OSError:
			return 10, 10

	def create_fakes(self):
		basedir = os.path.dirname(self.output_path)
		if not tf.io.gfile.exists(basedir):
			tf.io.gfile.makedirs(basedir)
		print('created, ', self.path, ', size: ', self.image_size())
		img = Image.new('RGB', self.image_size(), (255, 255, 255))
		img.save(self.output_path)


class PlainTextHolder(Holder):

	def __init__(self, *args, **kwargs):
		super(PlainTextHolder, self).__init__(*args, **kwargs)

	def create_fakes(self):
		out = tf.io.gfile.GFile(self.output_path, mode='w')
		with tf.io.gfile.GFile(self.path, mode='r') as inf:
			count = 0
			breaker = 0
			while count < 5 and breaker < 30:  # write 5 non empty line
				line = inf.readline()
				out.write(line)
				print(line)
				if not line.rstrip():
					count += 1
				breaker += 1

		out.close()


class ZipHolder(Holder):
	def __init__(self, *args, **kwargs):
		super(ZipHolder, self).__init__(*args, **kwargs)

	def create_fakes(self):
		zip_file = zipfile.ZipFile(self.path)
		files = zip_file.infolist()
		for file in files:
			name = os.path.basename(file.filename)
			typ = os.path.splitext(file.filename)[1]
			target_path = os.path.join(os.path.splitext(self.output_path)[0],
																 file.filename)

			hold = HolderFactory(zip_file, name, typ, file.filename,
													 target_path).generate_holder()
			hold.create_fakes()

		print('out = ', self.output_path)
		print('file2 = ', os.path.join(os.path.splitext(self.path)[0]))
		print('file type2 = ', type(os.path.join(os.path.splitext(self.path)[0])))
		folder_path = os.path.join(os.path.splitext(self.output_path)[0])
		shutil.make_archive(os.path.splitext(self.output_path)[0], 'zip',
												folder_path)
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
			return PlainTextHolder(self.name, self.typ, self.path, self.output_path)


class Generator:
	def __init__(self, inpath):
		self.inpath = inpath
		self.outpath = os.path.join('/Users/syny/PycharmProjects/tensorflow'
																'/datasets/tensorflow_datasets/testing'
																'/test_data/fake_examples',
																os.path.basename(inpath) + 'hey')

	def generator(self):  # hepsini tariyor bu bunu bi duzelt bea

		for dirpath, dirnames, filenames in tf.io.gfile.walk(self.inpath):
			print('dirpath = ', dirpath, '\ndirnames = ', dirnames, '\n filenames = ',
						filenames)
			# check the folder is created
			if os.path.relpath(dirpath, self.inpath) == '.':
				if not tf.io.gfile.isdir(self.outpath):
					tf.io.gfile.mkdir(self.outpath)

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