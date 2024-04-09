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

"""Tests for croissant_builder."""

import json
import tempfile

from etils import epath
import numpy as np
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import FileFormat
from tensorflow_datasets.core.dataset_builders import croissant_builder
from tensorflow_datasets.core.features import image_feature
from tensorflow_datasets.core.features import text_feature
from tensorflow_datasets.core.utils.lazy_imports_utils import mlcroissant as mlc

DUMMY_ENTRIES = [{"index": i, "text": f"Dummy example {i}"} for i in range(2)]


def get_dummy_metadata():
  distribution = [
      mlc.FileObject(
          id="raw_data",
          description="File with the data.",
          encoding_format="application/jsonlines",
          content_url="data/raw_data.jsonl",
          sha256=(
              "ec6a2e5865be2c3ea2bf41817bf9ca78cbfcdd60bce0282721da8625a28fd10d"
          ),
      ),
  ]
  record_sets = [
      mlc.RecordSet(
          id="jsonl",
          description="Dummy record set.",
          fields=[
              mlc.Field(
                  name="index",
                  description="The sample index.",
                  data_types=mlc.DataType.INTEGER,
                  source=mlc.Source(
                      file_object="raw_data",
                      extract=mlc.Extract(column="index"),
                  ),
              ),
              mlc.Field(
                  name="text",
                  description="The dummy sample text.",
                  data_types=mlc.DataType.TEXT,
                  source=mlc.Source(
                      file_object="raw_data",
                      extract=mlc.Extract(column="text"),
                  ),
              ),
          ],
      )
  ]
  dummy_metadata = mlc.Metadata(
      name="DummyDataset",
      description="Dummy description.",
      cite_as=(
          "@article{dummyarticle, title={title}, author={author}, year={2020}}"
      ),
      url="https://dummy_url",
      distribution=distribution,
      record_sets=record_sets,
      version="1.2.0",
      license="Public",
  )
  return dummy_metadata


@pytest.mark.parametrize(
    ["field", "feature_type", "int_dtype", "float_dtype"],
    [
        (
            mlc.Field(
                data_types=mlc.DataType.INTEGER, description="Integer feature"
            ),
            np.int64,
            None,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.INTEGER, description="Integer feature"
            ),
            np.int8,
            np.int8,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.FLOAT, description="Float feature"
            ),
            np.float32,
            None,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.FLOAT, description="Float feature"
            ),
            np.float64,
            None,
            np.float64,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.BOOL, description="Boolean feature"
            ),
            np.bool_,
            None,
            None,
        ),
    ],
)
def test_simple_datatype_converter(field, feature_type, int_dtype, float_dtype):
  actual_feature = croissant_builder.datatype_converter(
      field,
      int_dtype=int_dtype if int_dtype else np.int64,
      float_dtype=float_dtype if float_dtype else np.float32,
  )
  assert actual_feature == feature_type


@pytest.mark.parametrize(
    ["field", "feature_type"],
    [
        (
            mlc.Field(data_types=mlc.DataType.TEXT, description="Text feature"),
            text_feature.Text,
        ),
        (
            mlc.Field(data_types=mlc.DataType.DATE, description="Date feature"),
            text_feature.Text,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.IMAGE_OBJECT,
                description="Image feature",
            ),
            image_feature.Image,
        ),
    ],
)
def test_complex_datatype_converter(field, feature_type):
  actual_feature = croissant_builder.datatype_converter(field)
  assert isinstance(actual_feature, feature_type)


class CroissantBuilderTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(CroissantBuilderTest, cls).setUpClass()

    # Write raw examples on tmp/data.
    data_dir = epath.Path(tempfile.gettempdir()) / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    raw_output_file = data_dir / "raw_data.jsonl"
    with open(raw_output_file, "w") as outfile:
      for entry in DUMMY_ENTRIES:
        json.dump(entry, outfile)
        outfile.write("\n")

    # Write Croissant JSON-LD on tmp.
    dummy_metadata = get_dummy_metadata()
    croissant_file = epath.Path(tempfile.gettempdir()) / "croissant.json"
    with open(croissant_file, "w") as f:
      f.write(json.dumps(dummy_metadata.to_json(), indent=2))
      f.write("\n")

    cls._tfds_tmp_dir = testing.make_tmp_dir()
    cls.builder = croissant_builder.CroissantBuilder(
        jsonld=croissant_file,
        file_format=FileFormat.ARRAY_RECORD,
        disable_shuffling=True,
        data_dir=cls._tfds_tmp_dir,
    )

  def test_dataset_info(self):
    assert self.builder.name == "DummyDataset"
    assert self.builder.version == "1.2.0"
    assert (
        self.builder._info().citation
        == "@article{dummyarticle, title={title}, author={author}, year={2020}}"
    )
    assert self.builder._info().description == "Dummy description."
    assert self.builder._info().homepage == "https://dummy_url"
    assert self.builder._info().redistribution_info.license == "Public"
    assert len(self.builder.metadata.record_sets) == 1
    assert self.builder.metadata.record_sets[0].id == "jsonl"
    assert (
        self.builder.metadata.ctx.conforms_to.value
        == "http://mlcommons.org/croissant/1.0"
    )

  def test_generated_samples(self):
    self.builder.download_and_prepare()
    for split_name in ["all", "default"]:
      data_source = self.builder.as_data_source(split=split_name)
      assert len(data_source) == 2
      for i in range(2):
        assert data_source[i]["index"] == DUMMY_ENTRIES[i]["index"]
        assert data_source[i]["text"].decode() == DUMMY_ENTRIES[i]["text"]
