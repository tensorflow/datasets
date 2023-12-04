# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Streamlit components for the editor."""

import enum

from tensorflow_datasets.core.utils.lazy_imports_utils import streamlit as st


class Tab(enum.Enum):
  """Lists tabs in the editor."""

  OVERVIEW = "Overview"
  METADATA = "Metadata"
  RESOURCES = "Resources"
  RECORDSETS = "RecordSets"


def render_editor():
  """Renders the Croissant editor with its 4 tabs to build the dataset."""
  tab1, tab2, tab3, tab4 = st.tabs(
      [Tab.OVERVIEW, Tab.METADATA, Tab.RESOURCES, Tab.RECORDSETS]
  )

  with tab1:
    st.write(Tab.OVERVIEW.value)

  with tab2:
    st.write(Tab.METADATA.value)

  with tab3:
    st.write(Tab.RESOURCES.value)

  with tab4:
    st.write(Tab.RECORDSETS.value)
