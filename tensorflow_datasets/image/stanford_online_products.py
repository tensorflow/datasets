"""Stanford Online Products Dataset"""
import csv
import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
_DOWNLOAD_LINK = "ftp://cs.stanford.edu/cs/cvgl/Stanford_Online_Products.zip"
_SPLITS = {
  tfds.Split.TRAIN: "Ebay_train",
  tfds.Split.TEST: "Ebay_test"}

_SUPER_CLASSES = [
  'bicycle',
  'cabinet',
  'chair',
  'coffee_maker',
  'fan',
  'kettle',
  'lamp',
  'mug',
  'sofa',
  'stapler',
  'table',
  'toaster']
_CITATION = """\
@inproceedings{song2016deep,
 author    = {Song, Hyun Oh and Xiang, Yu and Jegelka, Stefanie and Savarese, Silvio},
 title     = {Deep Metric Learning via Lifted Structured Feature Embedding},
 booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
 year      = {2016}
}
"""


class StanfordOnlineProducts(tfds.core.GeneratorBasedBuilder):
  """Stanford Online Products Dataset"""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
      description=("Stanford Online Products Dataset"),
      builder=self,
      citation=_CITATION,
      urls=["http://cvgl.stanford.edu/projects/lifted_struct/"],
      features=tfds.features.FeaturesDict({
        "class_id": tfds.features.ClassLabel(num_classes=22364),
        "super_class_id/num": tfds.features.ClassLabel(num_classes=len(_SUPER_CLASSES)),
        "super_class_id": tfds.features.ClassLabel(names=_SUPER_CLASSES),
        "image": tfds.features.Image()
      })
    )

  def _split_generators(self, dl_manager):
    dl_path = dl_manager.download_and_extract(_DOWNLOAD_LINK)
    folder_path = os.path.join(
      dl_path,
      "Stanford_Online_Products")
    return [
      tfds.core.SplitGenerator(
        name=k,
        num_shards=4,
        gen_kwargs={
          "file_path": os.path.join(
            folder_path,
            "%s.txt" %
            v)}) for k,
      v in _SPLITS.items()]

  def _generate_examples(self, file_path):
    """
      Generate Image Samples and  Class IDs of Images of Product from the Data Directory

      Args:
        file_path: str, path to the Ebay_(train/test/info).txt file.
                    Having Columns ['class_id', 'super_class_id', 'path']
    """
    with tf.io.gfile.GFile(file_path, "r") as file_:
      dataset = csv.DictReader(file_, delimiter=" ")
      for row in dataset:
        yield{
          "class_id": int(row["class_id"]),
          "super_class_id/num": int(row["super_class_id"]),
          "super_class_id": _SUPER_CLASSES[int(row["super_class_id"]) - 1],
          "image": os.path.join(os.path.dirname(file_path), row["path"])}
