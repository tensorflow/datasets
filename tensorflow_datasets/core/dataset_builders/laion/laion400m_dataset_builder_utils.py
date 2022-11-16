# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Utils for Laion400mDatasetBuilder."""

HOMEPAGE = 'https://laion.ai/blog/laion-400-open-dataset/'
_MISSING_SIMILARITY_VALUE = -1.
_NSFW_MISSING_TAG = 'UNTAGGED'
_NSFW_TAGS = ('UNLIKELY', 'UNSURE', 'NSFW', _NSFW_MISSING_TAG)


def get_example_metadata(metadata_df_row):
  """Returns example metadata."""
  nsfw_tag = metadata_df_row['NSFW']
  if nsfw_tag not in _NSFW_TAGS:
    nsfw_tag = _NSFW_MISSING_TAG

  return {
      'caption': metadata_df_row['caption'],
      'nsfw': nsfw_tag,
      'similarity': metadata_df_row['similarity'] or _MISSING_SIMILARITY_VALUE,
      'license': metadata_df_row['LICENSE'] or '',
      'url': metadata_df_row['url'],
      'original_width': metadata_df_row['original_width'],
      'original_height': metadata_df_row['original_height'],
  }
