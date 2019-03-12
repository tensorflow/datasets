import csv
import os
import tensorflow_datasets.public_api as tfds
_DOWNLOAD_LINK = {
    "folder_path": "ftp://cs.stanford.edu/cs/cvgl/Stanford_Online_Products.zip"}
_SPLITS = {
        tfds.Split.TRAIN: "Ebay_train",
        tfds.Split.TEST: "Ebay_test"}


class StanfordOnlineProducts(tfds.core.GeneratorBasedBuilder):
  VERSION = tfds.core.Version("1.0.0")

  def_info(self):
    return tfds.core.DatasetInfo(
    description=("Stanford Online Products Dataset"),
    builder=self,
    urls=["http://cvgl.stanford.edu/projects/lifted_struct/"],
    features=tfds.features.FeatureDict({

    })
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract(_DOWNLOAD_LINK)
    path = os.path.join(path["folder_path"], "Stanford_Online_Products")
    return [tfds.core.SplitGenerator(name=k, num_shards=40, gen_kwargs={"file_path": os.path.join(path, v)} for k, v in _SPLITS.items()]
