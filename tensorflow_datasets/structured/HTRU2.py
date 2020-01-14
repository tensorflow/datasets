"""Dataset for Predicting a Pulsar Star"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
import tensorflow as tf

import os

_CITATION = """\
@article{10.1093/mnras/stw656,
    author = {Lyon, R. J. and Stappers, B. W. and Cooper, S. and Brooke, J. M. and Knowles, J. D.},
    title = "{Fifty years of pulsar candidate selection: from simple filters to a new principled real-time classification approach}",
    journal = {Monthly Notices of the Royal Astronomical Society},
    volume = {459},
    number = {1},
    pages = {1104-1123},
    year = {2016},
    month = {04},
    abstract = "{Improving survey specifications are causing an exponential rise in pulsar candidate numbers and data volumes. We study the candidate filters used to mitigate these problems during the past 50 years. We find that some existing methods such as applying constraints on the total number of candidates collected per observation, may have detrimental effects on the success of pulsar searches. Those methods immune to such effects are found to be ill-equipped to deal with the problems associated with increasing data volumes and candidate numbers, motivating the development of new approaches. We therefore present a new method designed for online operation. It selects promising candidates using a purpose-built tree-based machine learning classifier, the Gaussian Hellinger Very Fast Decision Tree, and a new set of features for describing candidates. The features have been chosen so as to (i) maximize the separation between candidates arising from noise and those of probable astrophysical origin, and (ii) be as survey-independent as possible. Using these features our new approach can process millions of candidates in seconds (∼1 million every 15 s), with high levels of pulsar recall (90 per cent+). This technique is therefore applicable to the large volumes of data expected to be produced by the Square Kilometre Array. Use of this approach has assisted in the discovery of 20 new pulsars in data obtained during the Low-Frequency Array Tied-Array All-Sky Survey.}",
    issn = {0035-8711},
    doi = {10.1093/mnras/stw656},
    url = {https://doi.org/10.1093/mnras/stw656},
    eprint = {http://oup.prod.sis.lan/mnras/article-pdf/459/1/1104/8115310/stw656.pdf},
}
"""

_DESCRIPTION = """\
HTRU2 is a data set which describes a sample of pulsar candidates collected during the High Time Resolution Universe Survey (South).
Pulsars are a rare type of Neutron star that produce radio emission detectable here on Earth. 
They are of considerable scientific interest as probes of space-time, the inter-stellar medium, and states of matter.
As pulsars rotate, their emission beam sweeps across the sky, and when this crosses our line of sight, produces a detectable pattern of broadband radio emission.
As pulsars rotate rapidly, this pattern repeats periodically. 
Thus, pulsar search involves looking for periodic radio signals with large radio telescopes.
Each pulsar produces a slightly different emission pattern, which varies slightly with each rotation.
Thus a potential signal detection known as a 'candidate', is averaged over many rotations of the pulsar, as determined by the length of an observation.
In the absence of additional info, each candidate could potentially describe a real pulsar.
However, in practice almost all detections are caused by radio frequency interference (RFI) and noise, making legitimate signals hard to find.
Machine learning tools are now being used to automatically label pulsar candidates to facilitate rapid analysis. 
Classification systems in particular are being widely adopted, which treat the candidate data sets as binary classification problems. 
Here the legitimate pulsar examples are a minority positive class, and spurious examples the majority negative class. 
At present multi-class labels are unavailable, given the costs associated with data annotation.
The data set shared here contains 16,259 spurious examples caused by RFI/noise, and 1,639 real pulsar examples. 
These examples have all been checked by human annotators.
"""

_URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/00372/HTRU2.zip"

class Htru2(tfds.core.GeneratorBasedBuilder):
  """Dataset for Predicting a Pulsar Star"""

  VERSION = tfds.core.Version('2.0.0',
                              experiments={tfds.core.Experiment.S3: False})

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
          "Features" : tfds.features.FeaturesDict({
            "Mean of the integrated profile" : tf.float64,
            "Standard deviation of the integrated profile" : tf.float64,
            "Excess kurtosis of the integrated profile" : tf.float64,
            "Skewness of the integrated profile" : tf.float64,
            "Mean of the DM-SNR curve" : tf.float64,
            "Standard deviation of the DM-SNR curve" : tf.float64,
            "Excess kurtosis of the DM-SNR curve" : tf.float64,
            "Skewness of the DM-SNR curve" : tf.float64,
          }),
          "Class" : tfds.features.ClassLabel(num_classes=2)
        }),
        supervised_keys=None,
        homepage="https://archive.ics.uci.edu/ml/datasets/HTRU2",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs={
                'file_path': path,
            }),
    ]

  def _generate_examples(self, file_path):
    """Yields examples."""
    with tf.io.gfile.GFile(os.path.join(file_path, "HTRU_2.csv"), "r") as csvfile:
      features = [
          "Mean of the integrated profile",
          "Standard deviation of the integrated profile",
          "Excess kurtosis of the integrated profile",
          "Skewness of the integrated profile",
          "Mean of the DM-SNR curve",
          "Standard deviation of the DM-SNR curve",
          "Excess kurtosis of the DM-SNR curve",
          "Skewness of the DM-SNR curve",
          "Class"  # 0 for noise, 1 for pulsar
      ]

      lines = csvfile.readlines()
      for i in lines:
        feature_lst = i.split(",")
        length_increase = 0
        for j in range(len(feature_lst)):
            if j % (len(features) - 1) == 0 and j != 0:
              temp = feature_lst[j + length_increase][0:]
              feature_lst[j + length_increase] = feature_lst[j + length_increase][0]
              feature_lst.insert(j + length_increase + 1, temp)
              length_increase += 1

        feature_dict = {}
        for j in range(len(feature_lst)):
          if j % len(features) == 0:
              feature_dict = {}
              feature_dict[features[j % len(features)]] = float(feature_lst[j])

          elif j % len(features) < len(features) - 1:
            feature_dict[features[j % len(features)]] = float(feature_lst[j])

          elif j % len(features) == len(features) - 1:
            yield j // len(features), {"Features" : feature_dict,
                                       "Class" : int(feature_lst[j])}
