# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""Add HuggingFace Datasets."""

import argparse
import os
import re
from typing import Optional

from absl import app
from absl.flags import argparse_flags

# TODO(adiagarwal) : Add an import for logging
# from logging import getLogger

TO_CONVERT = [
    # (pattern, replacement)
    # Order is important here for some replacements
    (r"import\slogging", r"from absl import logging\n"),
    (r"with\sopen", r"with tf.io.gfile.GFile"),
    (r"nlp\.Value\(\"string\"\)", r"tfds.features.Text()"),
    (r"nlp\.Value\(\"string\"\),", r"tfds.features.Text("),
    (r"nlp\.Value\(\"([\w\d]+)\"\)", r"tf.\1"),
    (r"nlp\.features", "tfds.features"),
    (r"features\s*=\s*nlp\.Features\(",
     r"features=tfds.features.FeaturesDict("),
    (r"dict\(", r"tfds.features.FeaturesDict("),
    (r"nlp.SplitGenerator", r"tfds.core.SplitGenerator"),
    (r"self\.config\.data_dir", r"dl_manager.manual_dir"),
    (r"self\.config", r"self.builder_config"),
    (r"nlp\.Split", r"tfds.Split"),
    (r"nlp", r"tfds.core"),
]


def _parse_flags(_) -> argparse.Namespace:
  """Command line flags."""
  parser = argparse_flags.ArgumentParser(
      prog="convert_dataset",
      description="Tool to add hugging face datasets",
  )
  parser.add_argument(
      "--hugging_face_path",
      help="Path of hugging face.",
  )
  parser.add_argument(
      "--tfds_path",
      help="Path of tensorflow",
  )
  return parser.parse_args()


def main(args: argparse.Namespace):

  convert_dataset(
      hugging_face_path=args.hugging_face_path, tfds_path=args.tfds_path)


def convert_dataset(hugging_face_path: Optional[str] = None,
                    tfds_path: Optional[str] = None) -> None:
  """Conver Hugging Face Datasets."""
  output_file = tfds_path
  file_name = [hugging_face_path]

  for fname in file_name:
    # TODO(adiagarwal) : Uncomment after adding logging
    # if not os.path.isfile(fname) or "__init__" in fname or "_test" in fname or ".py" not in fname:
    # self._logger.info("Skipping file")
    # continue

    with open(fname, "r") as f:
      lines = f.readlines()

      out_lines = []
      is_builder = False
      # needs_manual_update = False
      # nlp_imports = []
      for line in lines:
        out_line = line

        if "import nlp" in out_line:
          out_line = ""
          out_lines.append("import tensorflow as tf\n")
          out_lines.append("import tensorflow_datasets:public_api as tfds\n")

        elif out_line.startswith("def"):
          continue
        elif "from __future" in out_line:
          out_line = ""
        elif "return nlp.DatasetInfo(" in out_line:
          out_lines.append("\t\treturn tfds.core.DatasetInfo(\n")
          out_lines.append("\t\t\tbuilder=self,\n")
          out_line = ""
        elif "import logging" in out_line:
          out_line = "from absl import logging\n"
        else:
          for pattern, replacement in TO_CONVERT:
            out_line = re.sub(pattern, replacement, out_line)

        assert ("nlp" not in out_line), f"Error converting {out_line.strip()}"

        if "GeneratorBasedBuilder" in out_line or "BeamBasedBuilder" in out_line:
          is_builder = True
        out_lines.append(out_line)

        with open(output_file, "w") as f:
          f.writelines(out_line)


if __name__ == "__main__":
  app.run(main, flags_parser=_parse_flags)
