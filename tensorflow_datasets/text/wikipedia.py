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

"""Wikipedia dataset containing cleaned articles of all languages."""

import bz2
import dataclasses
import json
import re

from absl import flags  # pylint:disable=g-bad-import-order,g-import-not-at-top
from absl import logging
from etils import epath
import tensorflow_datasets.public_api as tfds

FLAGS = flags.FLAGS

_CITATION = """\
@ONLINE {wikidump,
    author = "Wikimedia Foundation",
    title  = "Wikimedia Downloads",
    url    = "https://dumps.wikimedia.org"
}
"""

_DESCRIPTION = """\
Wikipedia dataset containing cleaned articles of all languages.
The datasets are built from the Wikipedia dump
(https://dumps.wikimedia.org/) with one split per language. Each example
contains the content of one full Wikipedia article with cleaning to strip
markdown and unwanted sections (references, etc.).
"""

_LICENSE = (
    "This work is licensed under the Creative Commons Attribution-ShareAlike "
    "3.0 Unported License. To view a copy of this license, visit "
    "http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to "
    "Creative Commons, PO Box 1866, Mountain View, CA 94042, USA."
)

# Source: https://en.wikipedia.org/wiki/List_of_Wikipedias (accessed 3/1/2019)
# Removed because no articles: hz.
WIKIPEDIA_LANGUAGES = [
    "aa",
    "ab",
    "ace",
    "ady",
    "af",
    "ak",
    "als",
    "am",
    "an",
    "ang",
    "ar",
    "arc",
    "arz",
    "as",
    "ast",
    "atj",
    "av",
    "ay",
    "az",
    "azb",
    "ba",
    "bar",
    "bat-smg",
    "bcl",
    "be",
    "be-x-old",
    "bg",
    "bh",
    "bi",
    "bjn",
    "bm",
    "bn",
    "bo",
    "bpy",
    "br",
    "bs",
    "bug",
    "bxr",
    "ca",
    "cbk-zam",
    "cdo",
    "ce",
    "ceb",
    "ch",
    "cho",
    "chr",
    "chy",
    "ckb",
    "co",
    "cr",
    "crh",
    "cs",
    "csb",
    "cu",
    "cv",
    "cy",
    "da",
    "de",
    "din",
    "diq",
    "dsb",
    "dty",
    "dv",
    "dz",
    "ee",
    "el",
    "eml",
    "en",
    "eo",
    "es",
    "et",
    "eu",
    "ext",
    "fa",
    "ff",
    "fi",
    "fiu-vro",
    "fj",
    "fo",
    "fr",
    "frp",
    "frr",
    "fur",
    "fy",
    "ga",
    "gag",
    "gan",
    "gd",
    "gl",
    "glk",
    "gn",
    "gom",
    "gor",
    "got",
    "gu",
    "gv",
    "ha",
    "hak",
    "haw",
    "he",
    "hi",
    "hif",
    "ho",
    "hr",
    "hsb",
    "ht",
    "hu",
    "hy",
    "ia",
    "id",
    "ie",
    "ig",
    "ii",
    "ik",
    "ilo",
    "inh",
    "io",
    "is",
    "it",
    "iu",
    "ja",
    "jam",
    "jbo",
    "jv",
    "ka",
    "kaa",
    "kab",
    "kbd",
    "kbp",
    "kg",
    "ki",
    "kj",
    "kk",
    "kl",
    "km",
    "kn",
    "ko",
    "koi",
    "krc",
    "ks",
    "ksh",
    "ku",
    "kv",
    "kw",
    "ky",
    "la",
    "lad",
    "lb",
    "lbe",
    "lez",
    "lfn",
    "lg",
    "li",
    "lij",
    "lmo",
    "ln",
    "lo",
    "lrc",
    "lt",
    "ltg",
    "lv",
    "mai",
    "map-bms",
    "mdf",
    "mg",
    "mh",
    "mhr",
    "mi",
    "min",
    "mk",
    "ml",
    "mn",
    "mr",
    "mrj",
    "ms",
    "mt",
    "mus",
    "mwl",
    "my",
    "myv",
    "mzn",
    "na",
    "nah",
    "nap",
    "nds",
    "nds-nl",
    "ne",
    "new",
    "ng",
    "nl",
    "nn",
    "no",
    "nov",
    "nrm",
    "nso",
    "nv",
    "ny",
    "oc",
    "olo",
    "om",
    "or",
    "os",
    "pa",
    "pag",
    "pam",
    "pap",
    "pcd",
    "pdc",
    "pfl",
    "pi",
    "pih",
    "pl",
    "pms",
    "pnb",
    "pnt",
    "ps",
    "pt",
    "qu",
    "rm",
    "rmy",
    "rn",
    "ro",
    "roa-rup",
    "roa-tara",
    "ru",
    "rue",
    "rw",
    "sa",
    "sah",
    "sat",
    "sc",
    "scn",
    "sco",
    "sd",
    "se",
    "sg",
    "sh",
    "si",
    "simple",
    "sk",
    "sl",
    "sm",
    "sn",
    "so",
    "sq",
    "sr",
    "srn",
    "ss",
    "st",
    "stq",
    "su",
    "sv",
    "sw",
    "szl",
    "ta",
    "tcy",
    "te",
    "tet",
    "tg",
    "th",
    "ti",
    "tk",
    "tl",
    "tn",
    "to",
    "tpi",
    "tr",
    "ts",
    "tt",
    "tum",
    "tw",
    "ty",
    "tyv",
    "udm",
    "ug",
    "uk",
    "ur",
    "uz",
    "ve",
    "vec",
    "vep",
    "vi",
    "vls",
    "vo",
    "wa",
    "war",
    "wo",
    "wuu",
    "xal",
    "xh",
    "xmf",
    "yi",
    "yo",
    "za",
    "zea",
    "zh",
    "zh-classical",
    "zh-min-nan",
    "zh-yue",
    "zu",
]


_EMPTY_LANGUAGES = {"20230601": {"aa", "na"}}


# Use mirror to avoid download caps.
_BASE_URL_TMPL = (
    "https://mirror.accum.se/mirror/wikimedia.org/dumps/{lang}wiki/{date}/"
)
_BASE_URL_TMPL_OLD = "https://dumps.wikimedia.your.org/{lang}wiki/{date}/"
_INFO_FILE = "dumpstatus.json"


class WikipediaConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Wikipedia."""

  def __init__(self, *, language=None, date=None, **kwargs):
    """BuilderConfig for Wikipedia.

    Args:
      language: string, the language code for the Wikipedia dump to use.
      date: string, date of the Wikipedia dump in YYYYMMDD format. A list of
        available dates can be found at https://dumps.wikimedia.org/enwiki/.
      **kwargs: keyword arguments forwarded to super.
    """
    super(WikipediaConfig, self).__init__(
        name=f"{date}.{language}",
        description=(
            f"Wikipedia dataset for {language}, parsed from {date} dump."
        ),
        **kwargs,
    )
    self.date = date
    self.language = language


@dataclasses.dataclass(frozen=True)
class WikiPage:
  id: int
  title: str
  text: str


def _builder_configs_for(snapshot: str):
  # We put English as the first language so that it's the default.
  configs = [WikipediaConfig(language="en", date=snapshot)]
  for lang in WIKIPEDIA_LANGUAGES:
    if lang == "en" or "-" in lang:
      continue
    if snapshot in _EMPTY_LANGUAGES and lang in _EMPTY_LANGUAGES[snapshot]:
      continue
    configs.append(WikipediaConfig(language=lang, date=snapshot))
  return configs


class Wikipedia(tfds.core.BeamBasedBuilder):
  """Wikipedia dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  BUILDER_CONFIGS = (
      _builder_configs_for("20230601")
      # Old versions files do not exists anymore but config are kept as
      # previously generated datasets can still be read.
      + _builder_configs_for("20230201")
      + _builder_configs_for("20220620")
      + _builder_configs_for("20201201")
      + _builder_configs_for("20200301")
      + _builder_configs_for("20190301")
  )

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "title": tfds.features.Text(),
            "text": tfds.features.Text(),
        }),
        # No default supervised_keys.
        supervised_keys=None,
        homepage="https://dumps.wikimedia.org",
        citation=_CITATION,
        license=_LICENSE,
    )

  def _split_generators(self, dl_manager):
    def _base_url(lang):
      tmpl = _BASE_URL_TMPL
      if self.builder_config.date <= "20220620":
        tmpl = _BASE_URL_TMPL_OLD
      return tmpl.format(
          lang=lang.replace("-", "_"), date=self._builder_config.date
      )

    lang = self._builder_config.language

    info_url = _base_url(lang) + _INFO_FILE
    # Use dictionary since testing mock always returns the same result.
    downloaded_files = dl_manager.download_and_extract({"info": info_url})

    xml_urls = []
    total_bytes = 0
    info_path = epath.Path(downloaded_files["info"])
    dump_info = json.loads(info_path.read_text("utf-8"))
    multistream_dump_info = dump_info["jobs"]["articlesmultistreamdump"]
    assert (
        multistream_dump_info["status"] == "done"
    ), "Specified dump (%s) multistream status is not 'done': %s" % (
        _base_url(lang),
        multistream_dump_info["status"],
    )

    for fname, info in multistream_dump_info["files"].items():
      if ".xml" not in fname:
        continue
      total_bytes += info["size"]
      xml_urls.append(_base_url(lang) + fname)

    # Use dictionary since testing mock always returns the same result.
    downloaded_files = dl_manager.download({"xml": xml_urls})

    return {
        tfds.Split.TRAIN: self._generate_examples(downloaded_files["xml"], lang)
    }

  def _generate_examples(self, filepaths, language):
    """Build PCollection of examples in the raw (text) form."""
    beam = tfds.core.lazy_imports.apache_beam
    mwparserfromhell = tfds.core.lazy_imports.mwparserfromhell
    mwxml = tfds.core.lazy_imports.mwxml

    def _extract_content(filepath):
      """Extracts article content from a single WikiMedia XML file."""
      filepath = epath.Path(filepath)
      logging.info("generating examples from = %s", filepath)
      with filepath.open("rb") as f:
        f = bz2.BZ2File(filename=f)
        dump = mwxml.Dump.from_file(f)
        for page in dump:
          beam.metrics.Metrics.counter(language, "pages-read").inc()
          if page is None:
            continue
          # Filter pages that are not in the "main" namespace.
          if page.namespace != 0:
            continue
          beam.metrics.Metrics.counter(language, "pages-in-main-read").inc()

          try:
            revision = next(iter(page))  # A single revision in dumps.
          except (TypeError, StopIteration):
            beam.metrics.Metrics.counter(language, "no-revision-error").inc()
            continue

          if not revision.text:
            beam.metrics.Metrics.counter(language, "empty-revision-error").inc()
            continue

          if revision.text[:9].lower().startswith("#redirect"):
            beam.metrics.Metrics.counter(language, "filtered-redirects").inc()
            continue

          yield WikiPage(id=page.id, title=page.title, text=revision.text)

    # Filters for references, tables, and file/image links.
    re_rm_wikilink = re.compile(
        "^(?:File|Image|Media):", flags=re.IGNORECASE | re.UNICODE
    )

    def _parse_and_clean_wikicode(raw_content):
      """Strips formatting and unwanted sections from raw page content."""
      wikicode = mwparserfromhell.parse(raw_content)

      def rm_wikilink(obj):
        return bool(re_rm_wikilink.match(str(obj.title)))  # pytype: disable=wrong-arg-types

      def rm_tag(obj):
        return str(obj.tag) in {"ref", "table"}

      def rm_template(obj):
        return obj.name.lower() in {
            "reflist",
            "notelist",
            "notelist-ua",
            "notelist-lr",
            "notelist-ur",
            "notelist-lg",
        }

      def try_remove_obj(obj, section):
        try:
          section.remove(obj)
        except ValueError:
          # For unknown reasons, objects are sometimes not found.
          pass

      section_text = []
      # Filter individual sections to clean.
      for section in wikicode.get_sections(
          flat=True, include_lead=True, include_headings=True
      ):
        for obj in section.ifilter_wikilinks(
            matches=rm_wikilink, recursive=True
        ):
          try_remove_obj(obj, section)
        for obj in section.ifilter_templates(
            matches=rm_template, recursive=True
        ):
          try_remove_obj(obj, section)
        for obj in section.ifilter_tags(matches=rm_tag, recursive=True):
          try_remove_obj(obj, section)

        section_text.append(section.strip_code().strip())
      return "\n\n".join(section_text)

    def _parse_page(page: WikiPage):
      beam.metrics.Metrics.counter(language, "extracted-examples").inc()
      try:
        text = _parse_and_clean_wikicode(page.text)
      except tfds.core.lazy_imports.mwparserfromhell.parser.ParserError as e:
        beam.metrics.Metrics.counter(language, "parser-error").inc()
        logging.error("mwparserfromhell ParseError: %s", e)
        return

      if not text:
        beam.metrics.Metrics.counter(language, "empty-clean-examples").inc()
        return

      beam.metrics.Metrics.counter(language, "cleaned-examples").inc()

      yield page.id, {
          "title": page.title.replace("_", " "),
          "text": text,
      }

    return (
        beam.Create(filepaths)
        | beam.FlatMap(_extract_content)
        | beam.Reshuffle()
        | beam.FlatMap(_parse_page)
    )
