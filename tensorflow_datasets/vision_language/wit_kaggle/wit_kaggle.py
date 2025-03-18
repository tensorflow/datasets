# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Wikipedia-based Image Text (WIT) Dataset for the Kaggle competition."""
from __future__ import annotations

import base64
import csv
import functools
import gzip
import io
import sys
from typing import List, Optional

import numpy as np
from tensorflow_datasets.core.utils import bool_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Wikipedia - Image/Caption Matching Kaggle Competition.

This competition is organized by the
[Research team](https://research.wikimedia.org/) at the
[Wikimedia Foundation](https://wikimediafoundation.org/) in collaboration with
Google Research and a few external collaborators.
This competition is based on the
[WIT dataset](https://github.com/google-research-datasets/wit) published by
Google Research as detailed in this\
[SIGIR paper](https://dl.acm.org/doi/abs/10.1145/3404835.3463257).

In this competition, you’ll build a model that automatically retrieves the text
closest to an image. Specifically, you'll train your model to associate given
images with article titles or complex captions, in multiple languages.
The best models will account for the semantic granularity of Wikipedia images.
If successful, you'll be contributing to the accessibility of the largest
online encyclopedia. The millions of Wikipedia readers and edietors will be able
to more easily understand, search, and describe media at scale. As a result,
you’ll contribute to an open model to improve learning for all.
"""

_CITATION = """
@article{srinivasan2021wit,
  title={WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning},
  author={Srinivasan, Krishna and Raman, Karthik and Chen, Jiecao and Bendersky, Michael and Najork, Marc},
  journal={arXiv preprint arXiv:2103.01913},
  year={2021}
}
"""

_EMPTY_IMAGE_BYTES = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z/C/HgAGgwJ/lK3Q6wAAAABJRU5ErkJggg=="

_BEAM_NAMESPACE = "TFDS_WIT_KAGGLE"


class WitKaggleConfig(tfds.core.BuilderConfig):
  """BuilderConfig for WitKaggle."""

  def __init__(
      self,
      *,
      sample_files: Optional[List[str]] = None,
      image_folder: Optional[str] = None,
      split_specific_features: Optional[tfds.features.FeaturesDict] = None,
      resnet_embedding_shape: int = 2048,
      **kwargs,
  ):
    """BuilderConfig for WitKaggle.

    Args:
      sample_files: list of paths to the sample files.
      image_folder: path to the folder where image data lies.
      split_specific_features: tfds.features.FeaturesDict. The features for the
        specific WitKaggle split.
      resnet_embedding_shape: shape of resnet embeddings.
      **kwargs: keyword arguments forwarded to super.
    """
    super(WitKaggleConfig, self).__init__(**kwargs)
    self.sample_files = sample_files
    self.image_folder = image_folder

    # Features common to all configs.
    common_features = tfds.features.FeaturesDict({
        "caption_title_and_reference_description": (
            tfds.features.Text()
        ),  # Caption for the image_url (if existent, else '').
        "image_url": tfds.features.Text(),
        "image": (
            tfds.features.Image()
        ),  # Base64 encoded image bytes (if existent, else a blank image).
        "metadata_url": (
            tfds.features.Text()
        ),  # Url to the image's commons page (if existent, else '').
        "embedding": tfds.features.Tensor(
            shape=(resnet_embedding_shape,), dtype=np.float32
        ),  # A tensor of 2048 floats (if existent, else zeros).
    })
    self.features = tfds.features.FeaturesDict(
        {**common_features, **split_specific_features}
    )
    self.split_specific_features = split_specific_features
    self.resnet_embedding_shape = resnet_embedding_shape
    # For missing images, we use a zeroed vector of dimensionality (2048,) as
    # resnet embedding.
    self.empty_resnet_embedding = [0] * resnet_embedding_shape


class WitKaggle(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wit_kaggle dataset."""

  VERSION = tfds.core.Version("1.0.2")
  RELEASE_NOTES = {
      "1.0.2": "Fixes parsing of boolean fields.",
      "1.0.1": (
          "Optimize Beam pipeline to avoid strugglers, ignoring rows without "
          "an image URL. Also added more Beam counters."
      ),
      "1.0.0": """Initial release. It provides the train and test datasets from the
      Wikipedia - Image/Caption Matching Kaggle competition
      (https://www.kaggle.com/c/wikipedia-image-caption/data).

      The goal of the competition is to build a model that automatically
      retrieves the text closest to an image. Specifically, the model shuld be
      trained to associate given images with article titles or complex captions,
      in multiple languages. The best models will account for the semantic
      granularity of Wikipedia images.

      Note that this release doesn't provide the ground truth for the test set,
      as it hasn't been provided by the Kaggle competition yet.

      Note that not all of the training observations have corresponding image
      data. The released images exclude all images containing humans. For
      samples which are not associated with image data, the following image
      features are used: `image` is a byte-64 encoded blank image, `embedding`
      is a vector of 2048 zeros.

      The samples released for the competition can be loaded as:
      ```
      tfds.load("wit_kaggle/train_with_extended_features")
      tfds.load("wit_kaggle/test_without_gold")
      ```
      """,
  }

  # pytype: disable=wrong-keyword-args
  # In the Wikipedia - Image/Caption Matching competition, train samples are
  # associated with a rich set of metadata, while test samples only have a
  # sample_id and four image-related fields.
  BUILDER_CONFIGS = [
      WitKaggleConfig(
          name="train_with_extended_features",
          description=(
              "Training samples for the Wikipedia-Image/Caption Matching"
              " competition."
          ),
          sample_files=[
              f"train/train-0000{i}-of-00005.tsv.zip" for i in range(5)
          ],
          image_folder="train/image_data_train",
          split_specific_features=tfds.features.FeaturesDict({
              "language": tfds.features.Text(),
              "page_url": tfds.features.Text(),
              "image_url": tfds.features.Text(),
              "page_title": tfds.features.Text(),
              "section_title": tfds.features.Text(),
              "hierarchical_section_title": tfds.features.Text(),
              "caption_reference_description": tfds.features.Text(),
              "caption_attribution_description": tfds.features.Text(),
              "caption_alt_text_description": tfds.features.Text(),
              "mime_type": tfds.features.Text(),
              "original_height": np.int32,
              "original_width": np.int32,
              "is_main_image": np.bool_,
              "attribution_passes_lang_id": np.bool_,
              "page_changed_recently": np.bool_,
              "context_page_description": tfds.features.Text(),
              "context_section_description": tfds.features.Text(),
              "caption_title_and_reference_description": tfds.features.Text(),
          }),
      ),
      WitKaggleConfig(
          name="test_without_gold",
          description=(
              "Test samples (without gold answers) for the"
              " Wikipedia-Image/Caption Matching competition."
          ),
          sample_files=["test/test.tsv.zip"],
          image_folder="test/image_data_test",
          split_specific_features=tfds.features.FeaturesDict({
              "id": tfds.features.Text(),
              "image_url": tfds.features.Text(),
          }),
      ),
  ]
  # pytype: enable=wrong-keyword-args

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  Depending on the config called, manual_dir should contain some of the
  following subdirectories:
    * train
      - train-{0000x}-of-00005.tsv.zip
      - image_data_train/
        * image_pixels/
          - train_image_pixels_part-00{000-199}.csv.gz
        * resnet_embeddings/
          - train_resnet_embeddings_part-00{000-214}.csv.gz
    * test
      - test.tsv.zip
      - image_data_test/
        * image_pixels/
          - test_image_pixels_part-0000{0-4}.csv
        * resnet_embeddings/
          - test_resnet_embeddings_part-0000{0-9}.csv

  Registration at https://www.kaggle.com/c/wikipedia-image-caption/data
  is needed to get the links to download the dataset.
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=self.builder_config.features,
        supervised_keys=(
            "image_url",
            "caption_title_and_reference_description",
        ),
        homepage="https://www.kaggle.com/c/wikipedia-image-caption/code",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager, pipeline):
    """Returns SplitGenerators."""
    archive_path = {
        "samples": [
            tfds.download.Resource(  # pylint:disable=g-complex-comprehension
                path=dl_manager.manual_dir / filename,
                extract_method=tfds.download.ExtractMethod.ZIP,
            )
            for filename in self.builder_config.sample_files
        ],
        "images": tfds.download.Resource(
            path=dl_manager.manual_dir / self.builder_config.image_folder
        ),
    }

    extracted_paths = dl_manager.extract(archive_path)

    return {
        self.builder_config.name: self._generate_examples(
            pipeline=pipeline,
            samples_path=extracted_paths["samples"],
            image_pixels_path=extracted_paths["images"] / "image_pixels",
            image_resnet_path=extracted_paths["images"] / "resnet_embeddings",
        )
    }

  def _generate_examples(
      self, pipeline, samples_path, image_pixels_path, image_resnet_path
  ):
    """Processes the dataset and yields examples.

    Args:
      pipeline: the beam pipeline.
      samples_path: path to the split's sentences.
      image_pixels_path: path to the images' pixel representations.
      image_resnet_path: path to the images' pixel representations.

    Returns:
      Examples.
    """
    beam = tfds.core.lazy_imports.apache_beam
    counter = functools.partial(beam.metrics.Metrics.counter, _BEAM_NAMESPACE)

    def _get_csv_reader(filename):
      if filename.suffix == ".gz":
        counter("gz_csv_files").inc()
        g = tf.io.gfile.GFile(filename, "rb")
        f = gzip.open(g, "rt", newline="")
      else:
        counter("normal_csv_files").inc()
        f = tf.io.gfile.GFile(filename, "r")
      # Limit to 100 MB. Value must be smaller than the C long maximum value.
      csv.field_size_limit(sys.maxsize)
      return csv.reader(f, delimiter="\t")

    def _read_pixel_rows(filename):
      r"""Contains image_url \t image_pixel \t metadata_url."""
      reader = _get_csv_reader(filename)
      for row in reader:
        counter("pixel_rows").inc()
        image_url, image_representation, metadata_url = row
        if image_url:
          yield [image_url, (image_representation, metadata_url)]
        else:
          counter("pixel_rows_no_image_url").inc()

    def _read_resnet_rows(filename):
      r"""Contains image_url \t resnet_embedding."""
      reader = _get_csv_reader(filename)
      for row in reader:
        counter("resnet_rows").inc()
        image_url, image_representation = row
        if image_url:
          yield [image_url, image_representation]
        else:
          counter("resnet_rows_no_image_url").inc()

    def _read_samples_rows(folder_path):
      """Contains samples: train and test have different fields."""
      for filename in tf.io.gfile.listdir(folder_path):
        file_path = folder_path / filename
        f = tf.io.gfile.GFile(file_path, "r")
        # Limit to 100 MB. Value must be smaller than the C long maximum value.
        csv.field_size_limit(sys.maxsize)
        csv_reader = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_ALL)
        for row in csv_reader:
          counter("samples_rows").inc()
          sample = {
              feature_key: row[feature_key]
              for feature_key in self.builder_config.split_specific_features.keys()
          }
          image_url = row["image_url"]
          if image_url:
            yield [image_url, sample]
          else:
            counter("samples_rows_no_image_url").inc()

    def _process_examples(el):
      sample_url, sample_fields = el
      # Each image_url can be associated with multiple samples (e.g., multiple
      # languages).
      for i, sample_info in enumerate(sample_fields["sample_info"]):
        sample_id = f"{i}_{sample_url}"
        sample = {"image_url": sample_url}
        for feature_key in self.builder_config.split_specific_features.keys():
          sample[feature_key] = sample_info[feature_key]
          is_boolean_feature = (
              self.builder_config.split_specific_features[feature_key].np_dtype
              == np.bool_
          )
          if is_boolean_feature:
            sample[feature_key] = bool_utils.parse_bool(sample[feature_key])
        # Test samples don't have gold captions.
        if "caption_title_and_reference_description" not in sample_info:
          sample["caption_title_and_reference_description"] = ""

        # We output image data only if there is at least one image
        # representation per image_url.
        # Not all of the samples in the competition have corresponding image
        # data. In case multiple different image representations are associated
        # with the same image_url, we don't know which one is correct and don't
        # output any.
        if len(set(sample_fields["image_pixels"])) == 1:
          sample_image, sample_metadata = sample_fields["image_pixels"][0]
          sample["image"] = io.BytesIO(base64.b64decode(sample_image))
          sample["metadata_url"] = sample_metadata
        else:
          if len(set(sample_fields["image_pixels"])) > 1:
            counter("image_pixels_multiple").inc()
          else:
            counter("image_pixels_missing").inc()
            sample["image"] = io.BytesIO(base64.b64decode(_EMPTY_IMAGE_BYTES))
          sample["metadata_url"] = ""

        if len(set(sample_fields["image_resnet"])) == 1:
          image_resnet = [
              float(x) for x in sample_fields["image_resnet"][0].split(",")
          ]
          sample["embedding"] = image_resnet
        else:
          if len(set(sample_fields["image_resnet"])) > 1:
            counter("image_resnet_multiple").inc()
          else:
            counter("image_resnet_missing").inc()
          sample["embedding"] = self.builder_config.empty_resnet_embedding

        yield sample_id, sample

    # Read embeddings and bytes representations from (possibly compressed) csv.
    image_resnet_files = [
        image_resnet_path / f for f in tf.io.gfile.listdir(image_resnet_path)
    ]
    resnet_collection = (
        pipeline
        | "Collection from resnet files" >> beam.Create(image_resnet_files)
        | "Get embeddings per image" >> beam.FlatMap(_read_resnet_rows)
    )

    image_pixel_files = [
        image_pixels_path / f for f in tf.io.gfile.listdir(image_pixels_path)
    ]
    pixel_collection = (
        pipeline
        | "Collection from pixel files" >> beam.Create(image_pixel_files)
        | "Get pixels per image" >> beam.FlatMap(_read_pixel_rows)
    )

    # Read samples from tsv files.
    sample_collection = (
        pipeline
        | "Collection from sample files" >> beam.Create(samples_path)
        | "Get samples" >> beam.FlatMap(_read_samples_rows)
    )

    # Combine the features and yield examples.
    return (
        {
            "sample_info": sample_collection,
            "image_pixels": pixel_collection,
            "image_resnet": resnet_collection,
        }
        | "Group by image_url" >> beam.CoGroupByKey()
        | "Reshuffle" >> beam.Reshuffle()
        | "Process and yield examples" >> beam.FlatMap(_process_examples)
    )
