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

"""Main entrypoint for the Streamlit web application."""

from tensorflow_datasets.core.utils.lazy_imports_utils import streamlit as st
from tensorflow_datasets.editor.views import st_editor

st.set_page_config(page_title="Croissant Editor", page_icon="🥐", layout="wide")
st.header("Croissant Editor")
st_editor.render_editor()
