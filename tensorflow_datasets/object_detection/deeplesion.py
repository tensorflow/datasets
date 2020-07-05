# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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
"""DeepLesion dataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets as tfds
import tensorflow as tf
from tensorflow_datasets.core import utils
import numpy as np
import os
import io
from zipfile import ZipFile
import random
import math

# info of deeplesion dataset
_URL = ("https://nihcc.app.box.com/v/DeepLesion")

_DESCRIPTION = """\
The DeepLesion dataset contains 32,120 axial computed tomography (CT) slices 
from 10,594 CT scans (studies) of 4,427 unique patients. There are 1–3 lesions 
in each image with accompanying bounding  boxes  and  size  measurements,  
adding  up  to  32,735  lesions  altogether.  The  lesion annotations were 
mined from NIH’s picture archiving and communication system (PACS).
"""

_CITATION = """\
@article{DBLP:journals/corr/abs-1710-01766,
  author    = {Ke Yan and
               Xiaosong Wang and
               Le Lu and
               Ronald M. Summers},
  title     = {DeepLesion: Automated Deep Mining, Categorization and Detection
               of Significant Radiology Image Findings using Large-Scale
               Clinical Lesion Annotations},
  journal   = {CoRR},
  volume    = {abs/1710.01766},
  year      = {2017},
  url       = {http://arxiv.org/abs/1710.01766},
  archivePrefix = {arXiv},
  eprint    = {1710.01766},
  timestamp = {Mon, 13 Aug 2018 16:48:13 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-01766},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

@misc{zisheng_liang_2020_3749392,
  author    = {Zisheng Liang and Ouwen Huang},
  title     = {TensorFlow Datasets DeepLesion: Tools for Processing NIH DeepLesion Dataset},
  year      = {2020}
  doi       = {10.5281/zenodo.3749392}
}
"""


class DeeplesionConfig(tfds.core.BuilderConfig):
  """BuilderConfig for DeeplesionConfig."""
  def __init__(self,
               name=None,
               thickness=None,
               **kwargs):
    super(DeeplesionConfig,
          self).__init__(name=name,
                         version=tfds.core.Version('1.0.0'),
                         **kwargs)
    self.thickness = thickness


class Deeplesion(tfds.core.GeneratorBasedBuilder):
  """DeepLesion dataset builder."""
  BUILDER_CONFIGS = [
    DeeplesionConfig(
      name='abnormal',
      description=_DESCRIPTION,
    ),
    DeeplesionConfig(
      name='normal',
      description=_DESCRIPTION,
    ),
    DeeplesionConfig(
      name='volume',
      description=_DESCRIPTION,
      thickness=5
    ),
  ]

  def _info(self):
    if self.builder_config.name == 'abnormal':
      features = tfds.features.FeaturesDict({
          "image/name":
          tfds.features.Text(),
          "image":
          tfds.features.Image(shape=(None, None, 1),
                              dtype=tf.uint16,
                              encoding_format='png'),
          "bboxs":
          tfds.features.Sequence(tfds.features.BBoxFeature()),
      })
    elif self.builder_config.name == 'normal':
      features = tfds.features.FeaturesDict({
          "image/name":
          tfds.features.Text(),
          "image":
          tfds.features.Image(shape=(None, None, 1),
                              dtype=tf.uint16,
                              encoding_format='png'),
      })
    elif self.builder_config.name == 'volume':
      features = tfds.features.FeaturesDict({
          "key_image/name":
          tfds.features.Text(),
          "images":
          tfds.features.Sequence(
              tfds.features.Image(shape=(None, None, 1),
                                  dtype=tf.uint16,
                                  encoding_format='png')),
          "bboxs":
          tfds.features.Sequence(tfds.features.BBoxFeature()),
          "key_index":
          tfds.features.Tensor(shape=(), dtype=tf.int32),
          "measurement_coord":
          tfds.features.Sequence(
              tfds.features.Tensor(shape=(8, ), dtype=tf.float32)),
          "lesion_diameters_pixel":
          tfds.features.Sequence(
              tfds.features.Tensor(shape=(2, ), dtype=tf.float32)),
          "normalized_lesion_loc":
          tfds.features.Sequence(
              tfds.features.Tensor(shape=(3, ), dtype=tf.float32)),
          "possibly_noisy":
          tfds.features.Tensor(shape=(), dtype=tf.int32),
          "slice_range":
          tfds.features.Tensor(shape=(2, ), dtype=tf.int32),
          "slice_range_trunc":
          tfds.features.Tensor(shape=(2, ), dtype=tf.int32),
          "spacing_mm_px":
          tfds.features.Tensor(shape=(3, ), dtype=tf.float32),
          "image_size":
          tfds.features.Tensor(shape=(2, ), dtype=tf.int32),
          "dicom_windows":
          tfds.features.Sequence(
              tfds.features.Tensor(shape=(2, ), dtype=tf.int32)),
          "patient_gender":
          tfds.features.Tensor(shape=(), dtype=tf.int32),
          "patient_age":
          tfds.features.Tensor(shape=(), dtype=tf.int32),
      })
    else:
      raise AssertionError('No builder_config found!')

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=features,
        homepage=_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    resources = {
        'zipfile01':
        'https://nihcc.box.com/shared/static/sp5y2k799v4x1x77f7w1aqp26uyfq7qz.zip',
        'zipfile02':
        'https://nihcc.box.com/shared/static/l9e1ys5e48qq8s409ua3uv6uwuko0y5c.zip',
        'zipfile03':
        'https://nihcc.box.com/shared/static/48jotosvbrw0rlke4u88tzadmabcp72r.zip',
        'zipfile04':
        'https://nihcc.box.com/shared/static/xa3rjr6nzej6yfgzj9z6hf97ljpq1wkm.zip',
        'zipfile05':
        'https://nihcc.box.com/shared/static/58ix4lxaadjxvjzq4am5ehpzhdvzl7os.zip',
        'zipfile06':
        'https://nihcc.box.com/shared/static/cfouy1al16n0linxqt504n3macomhdj8.zip',
        'zipfile07':
        'https://nihcc.box.com/shared/static/z84jjstqfrhhlr7jikwsvcdutl7jnk78.zip',
        'zipfile08':
        'https://nihcc.box.com/shared/static/6viu9bqirhjjz34xhd1nttcqurez8654.zip',
        'zipfile09':
        'https://nihcc.box.com/shared/static/9ii2xb6z7869khz9xxrwcx1393a05610.zip',
        'zipfile10':
        'https://nihcc.box.com/shared/static/2c7y53eees3a3vdls5preayjaf0mc3bn.zip',
        'zipfile11':
        'https://nihcc.box.com/shared/static/2zsqpzru46wsp0f99eaag5yiad42iezz.zip',
        'zipfile12':
        'https://nihcc.box.com/shared/static/8v8kfhgyngceiu6cr4sq1o8yftu8162m.zip',
        'zipfile13':
        'https://nihcc.box.com/shared/static/jl8ic5cq84e1ijy6z8h52mhnzfqj36q6.zip',
        'zipfile14':
        'https://nihcc.box.com/shared/static/un990ghdh14hp0k7zm8m4qkqrbc0qfu5.zip',
        'zipfile15':
        'https://nihcc.box.com/shared/static/kxvbvri827o1ssl7l4ji1fngfe0pbt4p.zip',
        'zipfile16':
        'https://nihcc.box.com/shared/static/h1jhw1bee3c08pgk537j02q6ue2brxmb.zip',
        'zipfile17':
        'https://nihcc.box.com/shared/static/78hamrdfzjzevrxqfr95h1jqzdqndi19.zip',
        'zipfile18':
        'https://nihcc.box.com/shared/static/kca6qlkgejyxtsgjgvyoku3z745wbgkc.zip',
        'zipfile19':
        'https://nihcc.box.com/shared/static/e8yrtq31g0d8yhjrl6kjplffbsxoc5aw.zip',
        'zipfile20':
        'https://nihcc.box.com/shared/static/vomu8feie1qembrsfy2yaq36cimvymj8.zip',
        'zipfile21':
        'https://nihcc.box.com/shared/static/ecwyyx47p2jd621wt5c5tc92dselz9nx.zip',
        'zipfile22':
        'https://nihcc.box.com/shared/static/fbnafa8rj00y0b5tq05wld0vbgvxnbpe.zip',
        'zipfile23':
        'https://nihcc.box.com/shared/static/50v75duviqrhaj1h7a1v3gm6iv9d58en.zip',
        'zipfile24':
        'https://nihcc.box.com/shared/static/oylbi4bmcnr2o65id2v9rfnqp16l3hp0.zip',
        'zipfile25':
        'https://nihcc.box.com/shared/static/mw15sn09vriv3f1lrlnh3plz7pxt4hoo.zip',
        'zipfile26':
        'https://nihcc.box.com/shared/static/zi68hd5o6dajgimnw5fiu7sh63kah5sd.zip',
        'zipfile27':
        'https://nihcc.box.com/shared/static/3yiszde3vlklv4xoj1m7k0syqo3yy5ec.zip',
        'zipfile28':
        'https://nihcc.box.com/shared/static/w2v86eshepbix9u3813m70d8zqe735xq.zip',
        'zipfile29':
        'https://nihcc.box.com/shared/static/0cf5w11yvecfq34sd09qol5atzk1a4ql.zip',
        'zipfile30':
        'https://nihcc.box.com/shared/static/275en88yybbvzf7hhsbl6d7kghfxfshi.zip',
        'zipfile31':
        'https://nihcc.box.com/shared/static/l52tpmmkgjlfa065ow8czhivhu5vx27n.zip',
        'zipfile32':
        'https://nihcc.box.com/shared/static/p89awvi7nj0yov1l2o9hzi5l3q183lqe.zip',
        'zipfile33':
        'https://nihcc.box.com/shared/static/or9m7tqbrayvtuppsm4epwsl9rog94o8.zip',
        'zipfile34':
        'https://nihcc.box.com/shared/static/vuac680472w3r7i859b0ng7fcxf71wev.zip',
        'zipfile35':
        'https://nihcc.box.com/shared/static/pllix2czjvoykgbd8syzq9gq5wkofps6.zip',
        'zipfile36':
        'https://nihcc.box.com/shared/static/2dn2kipkkya5zuusll4jlyil3cqzboyk.zip',
        'zipfile37':
        'https://nihcc.box.com/shared/static/peva7rpx9lww6zgpd0n8olpo3b2n05ft.zip',
        'zipfile38':
        'https://nihcc.box.com/shared/static/2fda8akx3r3mhkts4v6mg3si7dipr7rg.zip',
        'zipfile39':
        'https://nihcc.box.com/shared/static/ijd3kwljgpgynfwj0vhj5j5aurzjpwxp.zip',
        'zipfile40':
        'https://nihcc.box.com/shared/static/nc6rwjixplkc5cx983mng9mwe99j8oa2.zip',
        'zipfile41':
        'https://nihcc.box.com/shared/static/rhnfkwctdcb6y92gn7u98pept6qjfaud.zip',
        'zipfile42':
        'https://nihcc.box.com/shared/static/7315e79xqm72osa4869oqkb2o0wayz6k.zip',
        'zipfile43':
        'https://nihcc.box.com/shared/static/4nbwf4j9ejhm2ozv8mz3x9jcji6knhhk.zip',
        'zipfile44':
        'https://nihcc.box.com/shared/static/1lhhx2uc7w14bt70de0bzcja199k62vn.zip',
        'zipfile45':
        'https://nihcc.box.com/shared/static/guho09wmfnlpmg64npz78m4jg5oxqnbo.zip',
        'zipfile46':
        'https://nihcc.box.com/shared/static/epu016ga5dh01s9ynlbioyjbi2dua02x.zip',
        'zipfile47':
        'https://nihcc.box.com/shared/static/b4ebv95vpr55jqghf6bthg92vktocdkg.zip',
        'zipfile48':
        'https://nihcc.box.com/shared/static/byl9pk2y727wpvk0pju4ls4oomz9du6t.zip',
        'zipfile49':
        'https://nihcc.box.com/shared/static/kisfbpualo24dhby243nuyfr8bszkqg1.zip',
        'zipfile50':
        'https://nihcc.box.com/shared/static/rs1s5ouk4l3icu1n6vyf63r2uhmnv6wz.zip',
        'zipfile51':
        'https://nihcc.box.com/shared/static/7tvrneuqt4eq4q1d7lj0fnafn15hu9oj.zip',
        'zipfile52':
        'https://nihcc.box.com/shared/static/gjo530t0dgeci3hizcfdvubr2n3mzmtu.zip',
        'zipfile53':
        'https://nihcc.box.com/shared/static/7x4pvrdu0lhazj83sdee7nr0zj0s1t0v.zip',
        'zipfile54':
        'https://nihcc.box.com/shared/static/z7s2zzdtxe696rlo16cqf5pxahpl8dup.zip',
        'zipfile55':
        'https://nihcc.box.com/shared/static/shr998yp51gf2y5jj7jqxz2ht8lcbril.zip',
        'zipfile56':
        'https://nihcc.box.com/shared/static/kqg4peb9j53ljhrxe3l3zrj4ac6xogif.zip',
        'ann_file':
        'https://raw.githubusercontent.com/anir16293/Deep-Lesion/master/DL_info.csv'
    }

    # download all resources
    archive_paths = dl_manager.download(resources)

    # get ann_file
    ann_path = archive_paths['ann_file']
    del archive_paths['ann_file']

    # create two helper instances:
    # `archiveUtils` to read images from archives
    # `annParser` to parse the annotation file `DL_info.csv`
    archiveUtils = ArchiveUtils(archive_paths)
    annParser = AnnParser(ann_path, config=self.builder_config)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": archiveUtils,
                "split": annParser.ann['train'],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "archive": archiveUtils,
                "split": annParser.ann['validation'],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": archiveUtils,
                "split": annParser.ann['test'],
            },
        ),
    ]

  def _generate_examples(self, archive, split):
    """Returns examples

    Args:
      archive: `ArchiveUtils`, read image(s) from archives using filename(s)
      split: `pandas.DataFrame`, each row contains an annotation of an image

    Yields:
      example key and data
    """
    if self.builder_config.name in ['abnormal', 'normal']:
      for idx, value in enumerate(split.values):
        # collect annotations
        file_name, bboxs, im_size, _, _, _, _, _, _, _, _, _, _, _ = value

        # build example
        record = {
            "image/name": file_name,
            "image": archive.extract_image(file_name),
        }
        if self.builder_config.name == 'abnormal':
          record.update(bboxs = _format_bboxs(bboxs, im_size))
        yield idx, record

    elif self.builder_config.name == 'volume':
      for idx, value in enumerate(split.values):
        # collect annotations
        file_name, bboxs, size, ks_idx, m_coords, diameters, n_loc, p_noisy, slice_range, spacing, dicom_windows, p_gender, p_age, sp = value

        # generate name list and cutoff indices for tructated series
        fileNameUtil = FileNameUtils(file_name)
        startIdx, endIdx = [int(x) for x in slice_range.split(',')]
        fname_list = fileNameUtil.get_fname_list(startIdx, endIdx)
        t_startIdx, t_endIdx = _cal_cutoff_position(
            len(fname_list), self.builder_config.thickness, ks_idx - startIdx)

        # build example
        record = {
            "key_image/name":
            file_name,
            "images":
            archive.extract_images(fname_list[t_startIdx:t_endIdx + 1]),
            "bboxs":
            _format_bboxs(bboxs, size),
            "key_index":
            ks_idx - startIdx - t_startIdx,
            "measurement_coord":
            _format_values(m_coords, 8, float),
            "lesion_diameters_pixel":
            _format_values(diameters, 2, float),
            "normalized_lesion_loc":
            _format_values(n_loc, 3, float),
            "possibly_noisy":
            int(p_noisy),
            "slice_range": [startIdx, endIdx],
            "slice_range_trunc":
            [t_startIdx + startIdx, t_endIdx + startIdx],
            "spacing_mm_px": [float(x) for x in spacing.split(',')],
            "image_size": [int(x) for x in size.split(',')],
            "dicom_windows":
            _format_values(dicom_windows, 2, int),
            "patient_gender":
            int(p_gender),
            "patient_age":
            int(p_age),
        }
        yield idx, record

    else:
      raise AssertionError('No builder_config found!')


class ArchiveUtils():
  """Helper class to read image(s) from archives

  Attributes:
    path: `dict`, paths of archives
    lookup_table: `dict`, hash table to lookup file path in archives
  """
  def __init__(self, path):
    """Inits ArchiveUtils with paths of archives"""
    self.path = path

  @utils.memoized_property
  def lookup_table(self):
    return self._build_lut()

  def extract_image(self, fileName):
    """Returns a file object according to the fileName

    Args:
      fileName: `str`, a fileName from the annotation file

    Returns:
      a file object of the fileName
    """
    fileNameUtil = FileNameUtils(fileName)
    archive = tf.io.gfile.GFile(self.lookup_table[fileNameUtil.seriesFolder], 'rb')
    with ZipFile(archive, 'r') as zipfile:
      fpath = os.path.join('Images_png', fileNameUtil.filePath)
      fObj = io.BytesIO(zipfile.read(fpath))
    return fObj

  def extract_images(self, fileNames):
    """Returns a list of file objects according to the list of fileName
    """
    fObj = []
    for fname in fileNames:
      fObj.append(self.extract_image(fname))
    return [self.extract_image(fname) for fname in fileNames]

  @utils.memoize()
  def _build_lut(self):
    """Returns a hash table to lookup path of an archive using seriesFolder.
    """
    lut = {}
    for k, v in self.path.items():  # k:v, <zipfile#>:<path of the zipfile>
      archive = tf.io.gfile.GFile(v, 'rb')
      with ZipFile(archive, 'r') as zipfile:
        for name in zipfile.namelist():  
          # name has a format as "Image_pngs/<seriesFolder>/<xxx>.png"
          seriesFolder = name.split('/')[1]
          lut[seriesFolder] = v
    return lut


class FileNameUtils():
  """Helper class to parse fileName from the annotation file

  Attributes:
    fileName: `str`, "<seriesFolder>_<%03d>.png"
    seriesFolder: `str`, "<seriesFolder>"
    sliceIdx: `int`, d
    sliceFileName: `str`, "<%03d>.png"
    filePath: `str`, "<seriesFolder>/<%03d>.png"
  """
  def __init__(self, fileName):
    """Inits with a fileName"""
    self.fileName = fileName

  @utils.memoized_property
  def seriesFolder(self):
    return '_'.join(self.fileName.split('_')[:-1])

  @utils.memoized_property
  def sliceIdx(self):
    return int(self.fileName.split('_')[-1][:-4])

  @utils.memoized_property
  def sliceFileName(self):
    return '%03d.png' % self.sliceIdx

  @utils.memoized_property
  def filePath(self):
    return os.path.join(self.seriesFolder, self.sliceFileName)


  def get_fname(self, sliceIdx):
    """Returns a fileName in annotated format

    Args:
      sliceIdx: `int`, index of a slice (the index should in valid slice_range)

    Returns:
      a `str` in "<seriesFolder>_<%03d>.png" format
    """
    return '_'.join([self.seriesFolder, '%03d.png' % sliceIdx])

  def get_fname_list(self, start, end):
    """Returns a list of names contructed by continuous indices

    Args:
      start: `int`, start point of continuous indices
      end: `int`, end point of continuous indices (inclusive)

    Returns:
      a list of `str`
    """
    return [self.get_fname(s) for s in range(start, end + 1)]


class AnnParser():
  """Deeplesion Annotation Parser

  Attributes:
    ann_path: `str`, path of the annotation file
    config: `tfds.core.BuilderConfig`, builder_config
    ann: `dict`, <split>:`pandas.Dataframe`, parsed annotation
  """
  def __init__(self, ann_path, config=None):
    """Inits with path of the annotation file
    """
    self.ann_path = ann_path
    self.config = config
  
  @utils.memoized_property
  def ann(self):
    _ann = self._ann_parser()
    if self.config.name == 'normal':
      _ann = {'train': self._create_ann_for_normals(_ann['train']),
              'validation': self._create_ann_for_normals(_ann['validation']),
              'test': self._create_ann_for_normals(_ann['test']),
             }
    return _ann

  def _ann_parser(self):
    """Returns annotions of three splits

      cleanup the annotations,
      group the annotations by File_name,
      split the annotations by Train_Val_Test
    """
    pd = tfds.core.lazy_imports.pandas
    with tf.io.gfile.GFile(self.ann_path) as csv_f:
        # read file
      df = pd.read_csv(csv_f)

      # select columns
      df_t = df[['File_name', 'Bounding_boxes', 'Image_size',
                'Key_slice_index', 'Measurement_coordinates', 'Lesion_diameters_Pixel_',
                'Normalized_lesion_location', 'Possibly_noisy', 'Slice_range',
                'Spacing_mm_px_', 'DICOM_windows', 'Patient_gender',
                'Patient_age', 'Train_Val_Test']]
      df_t = df_t.copy()

      # clean data
      df_t.fillna(-1, inplace=True)
      df_t.Patient_gender.replace(['M', 'F'], [1, 0], inplace=True)

      mask = df_t.apply(
          lambda x: x['Image_size'].split(", ")[0] == '512', axis=1)
      df_t = df_t[mask]  # filter out Image_size != 512
      df_t = df_t[df_t.Possibly_noisy ==
                  0]  # filter out possibly noisy image
      df_t = df_t[df_t.Spacing_mm_px_ >
                  "0.6"]  # filter out spacing mm/pixel < 0.6
      space = df_t.Spacing_mm_px_.apply(
          lambda x: float(x.split(", ")[2]))
      df_t['z_space'] = space
      df_t = df_t[(df_t.z_space <= 6) & (df_t.z_space >= 1)]
      df_t.drop(columns=['z_space'], inplace=True)

      # group and aggregate
      def concat(a): return ", ".join(a)  # rules for aggregation
      d = {
          'Bounding_boxes': concat,
          'Image_size': 'first',
          'Key_slice_index': 'first',
          'Measurement_coordinates': concat,
          'Lesion_diameters_Pixel_': concat,
          'Normalized_lesion_location': concat,
          'Possibly_noisy': 'first',
          'Slice_range': 'first',
          'Spacing_mm_px_': 'first',
          'DICOM_windows': concat,
          'Patient_gender': 'first',
          'Patient_age': 'first',
          'Train_Val_Test': 'first',
      }
      df_new = df_t.groupby(
          'File_name',
          as_index=False).aggregate(d).reindex(columns=df_t.columns)

      df_new = df_new.drop_duplicates("File_name")

      # split
      return {'train': df_new[df_new['Train_Val_Test'] == 1],
              'validation': df_new[df_new['Train_Val_Test'] == 2],
              'test': df_new[df_new['Train_Val_Test'] == 3]
             }

  def _create_ann_for_normals(self, ann):
    """Returns new created dataframe of normal scans

    To calulate the length of abnormal area in z direction
    known: spacing (mm per pixel) in z direction, and the length
      of long axis of lesion(pixels)
    assumption: assume lesions are enclosed in a ball-shape area,
      and the long axis is the longest axis in all direction.
    1. convert length of long axis from pixels into mm using
      spacing (mm per pixel) in x-y plane
    2. take this length as the abnormal range in z direction, convert
      it into num of slice 

    Args:
      ann: `pandas.Dataframe`, annotations of abnormal scans

    Returns:
      a `pandas.Dataframe`, columns align with ann
    """
    normal_scans_ann = []  # list of dicts to initiate a new dataframe
    for idx, value in enumerate(ann.values):
      # collect info from each row
      file_name, bboxs, size, ks_idx, m_coords, diameters, n_loc, p_noisy, slice_range, spacing, dicom_windows, p_gender, p_age, sp = value

      # calculate (approximately) offset of normal area from key slice 
      # spacing in x, y, z direction, (float, float, float)
      spacing_xy_mm_px = float(spacing.split(',')[0])  
      spacing_z_mm_interval = float(spacing.split(',')[2])
      longest_px = max([
          float(x) for x in diameters.split(',')
      ])  # the first one is always the longest, list of (float, float)
      longest_mm = longest_px * spacing_xy_mm_px
      offset_z = math.ceil(longest_mm / spacing_z_mm_interval)

      # randomly pick out a normal scan
      s_range = [int(x) for x in slice_range.split(',')]
      slice_idxs = [
          x for x in range(s_range[0], s_range[1] + 1)
      ]  # collect all valid idxs within the boundaries (includsively)
      key_idx = int(ks_idx)
      valid_idxs_pool = list(
          filter(
              lambda x: True
              if abs(x - key_idx) > offset_z else False, slice_idxs))

      # create a record for the normal scan
      for normal_idx in valid_idxs_pool:
        normal = {
            'File_name':
            FileNameUtils(file_name).get_fname(normal_idx),
            'Bounding_boxes': None,
            'Image_size': size,
            'Key_slice_index': ks_idx,
            'Measurement_coordinates': None,
            'Lesion_diameters_Pixel_': None,
            'Normalized_lesion_location': None,
            'Possibly_noisy': p_noisy,
            'Slice_range': slice_range,
            'Spacing_mm_px_': spacing,
            'DICOM_windows': dicom_windows,
            'Patient_gender': p_gender,
            'Patient_age': p_age,
            'Train_Val_Test': sp,
        }
        normal_scans_ann.append(normal)

    # create a new Dataframe of normals
    pd = tfds.core.lazy_imports.pandas
    normal_ann = pd.DataFrame(
        normal_scans_ann,
        columns=[
            'File_name', 'Bounding_boxes', 'Image_size', 'Key_slice_index',
            'Measurement_coordinates', 'Lesion_diameters_Pixel_',
            'Normalized_lesion_location', 'Possibly_noisy', 'Slice_range',
            'Spacing_mm_px_', 'DICOM_windows', 'Patient_gender',
            'Patient_age', 'Train_Val_Test',
        ])
    normal_ann = normal_ann.drop_duplicates("File_name")
    mask = normal_ann["File_name"].isin(ann["File_name"])
    normal_ann = normal_ann[~mask]

    return normal_ann.sample(n=len(ann), random_state=42)


def _cal_cutoff_position(length, thickness, keyIdx):
  """Returns cutoff indices of keyIdx-centred truncated list

  Args:
    length: `int`, length of a list
    thickness: `int`, cutoff thickness - number of slices
    keyIdx: `int`, index of the key slice

  Returns:
    a tuple of two `int`
  """
  left_block = (thickness - 1) // 2
  right_block = thickness - 1 - left_block

  start = max(0, keyIdx - left_block)
  end = min(length - 1, keyIdx + right_block)
  return start, end


def _format_bboxs(bboxs, size):
  """Returns bbox feature

  Args:
    bboxs: `str`, "xmin,ymin,xmax,ymax"
    size: `str`, "height,width", height is assumed to be equal with width.

  Returns:
    tfds.features.BBox
  """
  size = [float(x) for x in size.split(',')]
  if len(size) != 2 or size[0] != size[1]:
    raise AssertionError(
        'height should be equal with width for this dataset')
  coords = np.clip([float(x) for x in bboxs.split(',')], 0.0, size[0])

  cnt = int((len(coords)) / 4)

  bbox_list = []
  for i in range(cnt):
    ymin = coords[i * 4 + 1] / size[1]
    xmin = coords[i * 4] / size[0]
    ymax = coords[i * 4 + 3] / size[1]
    xmax = coords[i * 4 + 2] / size[0]
    bbox_list.append(
        tfds.features.BBox(ymin=ymin, xmin=xmin, ymax=ymax, xmax=xmax))

  return bbox_list


def _format_values(val, n, e_type):
  """Returns a feature formated value

  Args:
    val: `str`, "num1,num2,num3,...", value to format
    n: `int`, number of elememts within tuples
    e_type: `str`, the type of each elements within tuples

  Returns
    a list of tuples of e_type values
  """
  lst = [e_type(float(x)) for x in val.split(',')]
  return [lst[i:i+n] for i in range(0, len(lst), n)]
