import tensorflow as tf
import numpy as np
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_PATH = {"en":"https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/en.tar.gz"}
class commonvoice(tfds.core.GeneratorBasedBuilder):
    def _info(self):
       return tfds.core.DatasetInfo(
       name = "commonvoice",
       version = "1.0.0",
       description = "Mozilla Common Voice Dataset (English)",
       builder = self,
       urls = [u"https://voice.mozilla.org/en/datasets"]
       )
    def _split_generators(self,dl_manager):
        dl_path = dl_manager.download_and_extract(_DOWNLOAD_PATH)
        clip_folder = os.path.join(dl_path,"clips") # Need to Check for replacement

        pass
    def _generate_examples(self):
        pass

