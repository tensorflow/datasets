"""Raw rf ultrasound data of breast tumors, with segmentation masks and classifiers."""

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article {MP:MP12538,
  author = {Piotrzkowska-Wróblewska, Hanna
            and Dobruch-Sobczak, Katarzyna
            and Byra, Michał
            and Nowicki, Andrzej},
  title = {Open access database of raw ultrasonic signals acquired
           from malignant and benign breast lesions},
  journal = {Medical Physics},
  issn = {2473-4209},
  url = {http://dx.doi.org/10.1002/mp.12538},
  doi = {10.1002/mp.12538},
  pages = {6105--6109},
  keywords = {Ultrasonography, ultrasonic signals, breast lesions, dataset},
}
"""

_DESCRIPTION = """\
The Open Access Series of Breast Ultrasonic Data contains 200 ultrasound scans
(2 orthogonal scans each) of 52 malignant and 48 benign breast tumors, collected
by the Department of Ultrasound at The Institute of Fundamental Technological Research
of the Polish Academy of Sciences from patients at the Institute of Oncology (Warsaw).
The scans are stored as rf data, and each scan includes a same-size mask that denotes
the region-of-interest for the tumor. The 100 tumors were ranked on the BI-RADS scale,
which describes the probability of lesion malignancy, and classified as malignant or benign.
"""

_DATA_URL = """https://zenodo.org/record/545928/files/OASBUD.mat?download=1"""

_INFO_URL = """https://zenodo.org/record/545928#.X1nR0WhKg2z"""


class Oasbud(tfds.core.GeneratorBasedBuilder):
  """Raw rf ultrasound data of breast tumors, with segmentation masks and classifiers."""

  VERSION = tfds.core.Version('0.1.0')
  
  # Heavy configurations for dataset - raw rf and processed b-mode options
  BUILDER_CONFIGS = [
    tfds.core.BuilderConfig(
        version=VERSION,
        name="raw_rf",
        description="Raw rf data from transducer."
    ),
    tfds.core.BuilderConfig(
        version=VERSION,
        name="b_mode",
        description="Processed B mode image."
    )
  ]

  def _info(self):
    # Create FeaturesDict according to builder config
    # Each patient has two scans, two masks, BIRAD id, and malignant classifier
    if self.builder_config.name is "b_mode":
        config_features = tfds.features.FeaturesDict({
            "image_1": tfds.features.Tensor(shape=(None, 510), dtype=tf.float32),
            "mask_1": tfds.features.Tensor(shape=(None, 510), dtype=tf.int16),
            "image_2": tfds.features.Tensor(shape=(None, 510), dtype=tf.float32),
            "mask_2": tfds.features.Tensor(shape=(None, 510), dtype=tf.int16),
            "bi-rads": tfds.features.Tensor(shape=(), dtype=tf.string),
            "label": tfds.features.Tensor(shape=(), dtype=tf.int8)
        })
    else:
        config_features = tfds.features.FeaturesDict({
            "scan_1": tfds.features.Tensor(shape=(None, 510), dtype=tf.int16),
            "mask_1": tfds.features.Tensor(shape=(None, 510), dtype=tf.int16),
            "scan_2": tfds.features.Tensor(shape=(None, 510), dtype=tf.int16),
            "mask_2": tfds.features.Tensor(shape=(None, 510), dtype=tf.int16),
            "bi-rads": tfds.features.Tensor(shape=(), dtype=tf.string),
            "label": tfds.features.Tensor(shape=(), dtype=tf.int8)
        })

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=config_features,
        # no inclusion of supervised keys because of two scans per label/patient ID
        homepage=_INFO_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Downloads the data, defines train split (all data)
    extracted_path = dl_manager.download_and_extract(_DATA_URL)
    
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "data_path": extracted_path
            }
        )
    ]

  def _generate_examples(self, data_path):
    """Yields examples."""
    with tf.io.gfile.GFile(data_path, "r") as f:
        data = tfds.core.lazy_imports.scipy.io.loadmat(f)["data"][0]
        for row in data:
            key = row[0][0]
            if self.builder_config.name is "b_mode":
                example_dict = {
                    "image_1": process_b_mode(row[1]),
                    "mask_1": row[3],
                    "image_2": process_b_mode(row[2]),
                    "mask_2": row[4],
                    "bi-rads": row[5],
                    "label": row[6][0],
                }
            else:
                example_dict = {
                    "scan_1": row[1],
                    "mask_1": row[3],
                    "scan_2": row[2],
                    "mask_2": row[4],
                    "bi-rads": row[5],
                    "label": row[6][0],
                }
            yield key, example_dict
            
    def process_b_mode(scan):
        envelope_image = np.abs(tfds.core.lazy_import.scipy.signal.hilbert(scan))
        return 20 * np.log10(envelope_image/np.max(envelope_image))

