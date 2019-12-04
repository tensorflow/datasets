"""Fine-Grained Visual Classification of Aircraft (FGVC-Aircraft) is a benchmark fgvc-aircraft-2013b/dataset for the fine grained visual categorization of aircraft."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import PIL

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """@techreport{maji13fine-grained,
   title = {Fine-Grained Visual Classification of Aircraft},
   author = {S. Maji and J. Kannala and E. Rahtu and M. Blaschko and A. Vedaldi},
   year = {2013},
   archivePrefix = {arXiv},
   eprint = {1306.5151},
   primaryClass = "cs-cv",
}
"""

_DESCRIPTION = """
Fine-Grained Visual Classification of Aircraft (FGVC-Aircraft) is a benchmark fgvc-aircraft-2013b/dataset for the fine grained visual categorization of aircraft.
"""

_URL = "http://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/archives/fgvc-aircraft-2013b.tar.gz"

class FgvcAircraft(tfds.core.GeneratorBasedBuilder):
  """FGVC-Aircraft fgvc-aircraft-2013b/dataset."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "variant": tfds.features.Text(),
            "family": tfds.features.Text(),
            "manufacturer": tfds.features.Text(),
            "bbox": tfds.features.BBoxFeature(),
        }),
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Get splits from file."""
    extract_path = dl_manager.download_and_extract(_URL)

    train_path = os.path.join(extract_path,
                              "fgvc-aircraft-2013b/data/images_train.txt")
    with tf.io.gfile.GFile(train_path) as f:
      train_list = [line.strip() for line in f.readlines()]
    val_path = os.path.join(extract_path,
                            "fgvc-aircraft-2013b/data/images_val.txt")
    with tf.io.gfile.GFile(val_path) as f:
      val_list = [line.strip() for line in f.readlines()]
    test_path = os.path.join(extract_path,
                             "fgvc-aircraft-2013b/data/images_test.txt")
    with tf.io.gfile.GFile(test_path) as f:
      test_list = [line.strip() for line in f.readlines()]

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "file_names": train_list,
                "data_path": extract_path
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "file_names": val_list,
                "data_path": extract_path
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "file_names": test_list,
                "data_path": extract_path
            },
        ),
    ]

  def _generate_examples(self, file_names, data_path):
    """Yields examples."""
    def get_data(data_path, data_dict, train, trainval, test):
      t_paths = [os.path.join(data_path, t_path)
                 for t_path in [train, trainval, test]]
      for t_path in t_paths:
        with tf.io.gfile.GFile(t_path) as f:
          t_data = [(line.split()[0],
                     " ".join(line.split()[1:])) for line in f.readlines()]
          for image, t_type in t_data:
            data_dict[image] = t_type

    variants = dict()
    v_train = "fgvc-aircraft-2013b/data/images_variant_train.txt"
    v_val = "fgvc-aircraft-2013b/data/images_variant_val.txt"
    v_test = "fgvc-aircraft-2013b/data/images_variant_test.txt"
    get_data(data_path, variants, v_train, v_val, v_test)

    families = dict()
    f_train = "fgvc-aircraft-2013b/data/images_family_train.txt"
    f_val = "fgvc-aircraft-2013b/data/images_family_val.txt"
    f_test = "fgvc-aircraft-2013b/data/images_family_test.txt"
    get_data(data_path, families, f_train, f_val, f_test)

    manufacturers = dict()
    m_train = "fgvc-aircraft-2013b/data/images_manufacturer_train.txt"
    m_val = "fgvc-aircraft-2013b/data/images_manufacturer_val.txt"
    m_test = "fgvc-aircraft-2013b/data/images_manufacturer_test.txt"
    get_data(data_path, manufacturers, m_train, m_val, m_test)

    bboxes = dict()
    bbox_path = os.path.join(data_path,
                             "fgvc-aircraft-2013b/data/images_box.txt")

    image_dir_path = "fgvc-aircraft-2013b/data/images"

    def normalize_bbox(bbox_side, image_side):
      return min(bbox_side / image_side, 1.0)

    with tf.io.gfile.GFile(bbox_path) as f:
      bbox_data = [line.split() for line in f.readlines()]
      for file_name, xmin, ymin, xmax, ymax in bbox_data:
        #width and height are not provided, find with pillow library
        open_file = PIL.Image.open(os.path.join(data_path,
                                                image_dir_path,
                                                file_name+".jpg"))
        width, height = open_file.size
        bboxes[file_name] = (normalize_bbox(float(xmin), width),
                             normalize_bbox(float(ymin), height),
                             normalize_bbox(float(xmax), width),
                             normalize_bbox(float(ymax), height))

    for file_name in file_names:
      image_path = os.path.join(data_path,
                                image_dir_path, file_name+".jpg")
      yield file_name, {"image": image_path,
                        "variant": variants[file_name],
                        "family": families[file_name],
                        "manufacturer": manufacturers[file_name],
                        "bbox":
                        tfds.features.BBox(
                            bboxes[file_name][0], bboxes[file_name][1],
                            bboxes[file_name][2], bboxes[file_name][3])}
