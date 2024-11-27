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

"""C4 dataset based on Common Crawl."""

import collections
import functools
import json
import os
from typing import Optional, Sequence
import uuid

from absl import logging
from etils import epath
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text import c4_utils
import tree

PageFeatures = c4_utils.PageFeatures

_DESCRIPTION = """\
A colossal, cleaned version of Common Crawl's web crawl corpus.

Based on Common Crawl dataset: https://commoncrawl.org

To generate this dataset, please follow
[the instructions from t5](https://github.com/google-research/text-to-text-transfer-transformer#c4).

Due to the overhead of cleaning the dataset, it is recommend you prepare it with
a distributed service like Cloud Dataflow. More info at
https://www.tensorflow.org/datasets/beam_datasets.
"""
_CITATION = """
@article{2019t5,
  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
  journal = {arXiv e-prints},
  year = {2019},
  archivePrefix = {arXiv},
  eprint = {1910.10683},
}
"""
_VERSION = tfds.core.Version("3.1.0")

# TODO(adarob): Remove supported versions. Starting with 3.0.0, all generated
# datasets are automatically forward compatible. For example,
# tfds.load('c4:3.0.0') works even if the code is at 3.0.1.
_SUPPORTED_VERSIONS = [
    tfds.core.Version("2.3.1"),
    tfds.core.Version("2.3.0"),
    tfds.core.Version("2.2.1"),
    tfds.core.Version("2.2.0"),
]
RELEASE_NOTES = {
    "3.1.0": (
        "All: Select newest timestamp when deduping by URL (vs random); escape "
        "badword regexes."
        "Multilingual: Expand complete list of CC dumps (as of Aug 17, 2022); "
        "use soft badword filtering (99.9%); do not require spaces for "
        "Japanese when matching bad words (similar to Thai and Chinese); "
        "up minimum language detection threshold to 0.95 (from 0.7); allow "
        "badwords that filter >10% of documents for a given non-spaced "
        "language due to being common subwords."
    ),
    "3.0.1": "Remove mC4 languages with less than 10k pages.",
    "3.0.0": "Add multilingual version (mC4). Deterministic URL deduplication.",
    "2.3.1": "Hashing change.",
    "2.3.0": "Deduplicate lines within a page.",
    "2.2.1": "Update dataset_info.json",
}

_DOWNLOAD_HOST = "https://data.commoncrawl.org"
_WET_PATH_URL = (
    "https://data.commoncrawl.org/crawl-data/CC-MAIN-{cc_version}/wet.paths.gz"
)
_REALNEWS_DOMAINS_URL = "https://raw.githubusercontent.com/rowanz/grover/38f7184bd87237ae2d3bc330b99f1e2e246f6d51/realnews/domain_to_allowed_subdomains.json"
_OPENWEBTEXT_URLS_ZIP = "OpenWebText.zip"
_OPENWEBTEXT_URLS_URL = "https://mega.nz/#F!EZZD0YwJ!9_PlEQzdMVLaNdKv_ICNVQ"
_OPENWEBTEXT_URLS_FILE_PATTERN = "OpenWebText/Version 1/URLs/*.txt"
_EN_BADWORDS_URL = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/25e679f03d96baa721cde20db9944649e8d0a844/en"
_BADWORDS_URL = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/5faf2ba42d7b1c0977169ec3611df25a3c08eb13/{lang}"
_BADWORDS_LANGS = [
    "ar",
    "cs",
    "da",
    "de",
    "en",
    "eo",
    "es",
    "fa",
    "fi",
    "fil",
    "fr",
    "fr-CA-u-sd-caqc",
    "hi",
    "hu",
    "it",
    "ja",
    "kab",
    "ko",
    "nl",
    "no",
    "pl",
    "pt",
    "ru",
    "sv",
    "th",
    "tlh",
    "tr",
    "zh",
]
# Words that are allowed since they are common subwords in languages without
# spaces. These each filter >10% of documents of their language when disallowed.
_BADWORDS_ALLOWLIST = {"ja": {"sm", "グロ", "女の子"}, "zh": {"性"}}

DEFAULT_CC_VERSION = "2019-18"

OPENWEBTEXT_CC_VERSIONS = (  # August 2018 - July 2019
    "2019-18",  # Original default for single-crawl dataset (April 2019).
    "2019-30",
    "2019-26",
    "2019-22",
    "2019-13",
    "2019-09",
    "2019-04",
    "2018-51",
    "2018-47",
    "2018-43",
    "2018-39",
    "2018-34",
)

ALL_CC_VERSIONS = (  # as of August 1, 2022
    "2013-20",
    "2013-48",
    "2014-10",
    "2014-15",
    "2014-23",
    "2014-35",
    "2014-41",
    "2014-42",
    "2014-49",
    "2014-52",
    "2015-06",
    "2015-11",
    "2015-14",
    "2015-18",
    "2015-22",
    "2015-27",
    "2015-32",
    "2015-35",
    "2015-40",
    "2015-48",
    "2016-07",
    "2016-18",
    "2016-22",
    "2016-26",
    "2016-30",
    "2016-36",
    "2016-40",
    "2016-44",
    "2016-50",
    "2017-04",
    "2017-09",
    "2017-13",
    "2017-17",
    "2017-22",
    "2017-26",
    "2017-30",
    "2017-34",
    "2017-39",
    "2017-43",
    "2017-47",
    "2017-51",
    "2018-05",
    "2018-09",
    "2018-13",
    "2018-17",
    "2018-22",
    "2018-26",
    "2018-30",
    "2018-34",
    "2018-39",
    "2018-43",
    "2018-47",
    "2018-51",
    "2019-04",
    "2019-09",
    "2019-13",
    "2019-18",
    "2019-22",
    "2019-26",
    "2019-30",
    "2019-35",
    "2019-39",
    "2019-43",
    "2019-47",
    "2019-51",
    "2020-05",
    "2020-10",
    "2020-16",
    "2020-24",
    "2020-29",
    "2020-34",
    "2020-40",
    "2020-45",
    "2020-50",
    "2021-04",
    "2021-10",
    "2021-17",
    "2021-21",
    "2021-25",
    "2021-31",
    "2021-39",
    "2021-43",
    "2021-49",
    "2022-05",
    "2022-21",
    "2022-27",
)

_KNOWN_CORRUPT_WET_FILES = (  # as of August 12, 2022
    # files that raise UnicodeDecodeError
    "crawl-data/CC-MAIN-2017-13/segments/1490218203536.73/wet/CC-MAIN-20170322213003-00052-ip-10-233-31-227.ec2.internal.warc.wet.gz",
)

# Limited to languages in CLD3 that produce at least 10k pages when using the
# "multilingual" config below.
MC4_LANGUAGES = [
    "af",
    "am",
    "ar",
    "az",
    "be",
    "bg",
    "bg-Latn",
    "bn",
    "ca",
    "ceb",
    "co",
    "cs",
    "cy",
    "da",
    "de",
    "el",
    "el-Latn",
    "en",
    "eo",
    "es",
    "et",
    "eu",
    "fa",
    "fi",
    "fil",
    "fr",
    "fy",
    "ga",
    "gd",
    "gl",
    "gu",
    "ha",
    "haw",
    "hi",
    "hi-Latn",
    "hmn",
    "ht",
    "hu",
    "hy",
    "id",
    "ig",
    "is",
    "it",
    "iw",
    "ja",
    "ja-Latn",
    "jv",
    "ka",
    "kk",
    "km",
    "kn",
    "ko",
    "ku",
    "ky",
    "la",
    "lb",
    "lo",
    "lt",
    "lv",
    "mg",
    "mi",
    "mk",
    "ml",
    "mn",
    "mr",
    "ms",
    "mt",
    "my",
    "ne",
    "nl",
    "no",
    "ny",
    "pa",
    "pl",
    "ps",
    "pt",
    "ro",
    "ru",
    "ru-Latn",
    "sd",
    "si",
    "sk",
    "sl",
    "sm",
    "sn",
    "so",
    "sq",
    "sr",
    "st",
    "su",
    "sv",
    "sw",
    "ta",
    "te",
    "tg",
    "th",
    "tr",
    "uk",
    "ur",
    "uz",
    "vi",
    "xh",
    "yi",
    "yo",
    "zh",
    "zh-Latn",
    "zu",
]


class C4Config(tfds.core.BuilderConfig):
  """BuilderConfig for C4 dataset."""

  def __init__(
      self,
      name: str,
      languages: Sequence[str],
      cc_versions: Optional[Sequence[str]] = None,
      clean: bool = False,
      badwords_filter_fraction: float = 0.0,
      paragraph_filter: bool = False,
      dedupe: bool = True,
      realnewslike: bool = False,
      webtextlike: bool = False,
      **kwargs,
  ):
    """BuilderConfig for C4.

    Args:
      name: string, the name for the config.
      languages: list(string), the language code(s) to include.
      cc_versions: tuple(string), a collection of versions of Common Crawl to
        use as the raw source text. Set to None to use default.
      clean: bool, whether to heuristically filter out lines and pages
        considered low quality. Note: only expected to work reliably for English
        pages.
      badwords_filter_fraction: float, what fraction of pages to filter out that
        contain "bad words".
      paragraph_filter: bool, whether to filter out pages with too few or too
        short paragraphs.
      dedupe: bool, whether to deduplicate the dataset by paragraphs.
      realnewslike: bool, whether to limit to news domains as compiled by
        RealNews.
      webtextlike: bool, whether to limit to WebText-like URLs.
      **kwargs: keyword arguments forwarded to super.
    """
    super(C4Config, self).__init__(
        name=name,
        version=_VERSION,
        supported_versions=_SUPPORTED_VERSIONS,
        **kwargs,
    )

    if clean and tuple(languages) != ("en",):
      logging.warning(
          "C4 cleaning is only expected to work reliably for English pages."
      )

    if not 0.0 <= badwords_filter_fraction <= 1.0:
      raise ValueError(
          "`badwords_filter_fraction` must be between 0.0 and 1.0."
      )

    self.languages = languages
    self.cc_versions = cc_versions or (DEFAULT_CC_VERSION,)
    self.clean = clean
    self.badwords_filter_fraction = badwords_filter_fraction
    self.paragraph_filter = paragraph_filter
    self.dedupe = dedupe
    self.realnewslike = realnewslike
    self.webtextlike = webtextlike


class C4(tfds.core.BeamBasedBuilder):
  """C4 dataset based on Common Crawl."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = f"""
  You are using a C4 config that requires some files to be manually downloaded.
  For `c4/webtextlike`, download {_OPENWEBTEXT_URLS_ZIP} from
  {_OPENWEBTEXT_URLS_URL}.
  """

  BUILDER_CONFIGS = [
      C4Config(
          "en",
          languages=["en"],
          clean=True,
          dedupe=True,
          badwords_filter_fraction=1.0,
          description="English C4 dataset.",
      ),
      C4Config(
          "en.noclean",
          languages=["en"],
          clean=False,
          dedupe=False,
          badwords_filter_fraction=0.0,
          description=(
              "Disables all cleaning (deduplication, removal based on bad"
              " words, etc.)"
          ),
      ),
      C4Config(
          "realnewslike",
          languages=["en"],
          realnewslike=True,
          clean=True,
          dedupe=True,
          badwords_filter_fraction=1.0,
          description=(
              "Filters from the default config to only include content from the"
              " domains used in the 'RealNews' dataset (Zellers et al., 2019)."
          ),
      ),
      C4Config(
          "webtextlike",
          languages=["en"],
          cc_versions=OPENWEBTEXT_CC_VERSIONS,
          webtextlike=True,
          clean=True,
          dedupe=True,
          badwords_filter_fraction=1.0,
          description=(
              "Filters from the default config to only include content from the"
              " URLs in OpenWebText"
              " (https://github.com/jcpeterson/openwebtext)."
          ),
      ),
      C4Config(
          "multilingual",
          languages=MC4_LANGUAGES,
          cc_versions=ALL_CC_VERSIONS,
          clean=False,
          paragraph_filter=True,
          dedupe=True,
          badwords_filter_fraction=0.999,
          description=(
              "Multilingual C4 (mC4) has 101 languages and is generated from 86"
              " Common Crawl dumps."
          ),
      ),
  ]

  def _info(self):
    features = {
        "text": tfds.features.Text(),
        "url": tfds.features.Text(),
        "content-type": tfds.features.Text(),
        "content-length": tfds.features.Text(),
        "timestamp": tfds.features.Text(),
    }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        citation=_CITATION,
        homepage="https://github.com/google-research/text-to-text-transfer-transformer#datasets",
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager, pipeline
  ):
    # We will automatically download the first default CC version, but others
    # need to be manually downloaded.
    cc_versions = set(self.builder_config.cc_versions)
    files_to_download = {}
    files_to_download["wet_path_urls"] = [
        _WET_PATH_URL.format(cc_version=cc_version)
        for cc_version in cc_versions
    ]
    if self.builder_config.badwords_filter_fraction > 0.0:
      files_to_download["badwords"] = {
          lang: _BADWORDS_URL.format(lang=lang)
          for lang in _BADWORDS_LANGS
          if lang != "en"
      }
      # Use older "en" file for reproducibility of the original C4.
      files_to_download["badwords"]["en"] = _EN_BADWORDS_URL
    if self.builder_config.realnewslike:
      files_to_download["realnews_domains"] = _REALNEWS_DOMAINS_URL
    file_paths = dl_manager.download_and_extract(files_to_download)

    if self.builder_config.webtextlike:
      owt_path = dl_manager.manual_dir / _OPENWEBTEXT_URLS_ZIP
      if not owt_path.exists():
        raise AssertionError(
            "For the WebText-like config, you must manually download the "
            "following file from {0} and place it in {1}: {2}".format(
                _OPENWEBTEXT_URLS_URL,
                dl_manager.manual_dir,
                _OPENWEBTEXT_URLS_ZIP,
            )
        )
      file_paths["openwebtext_urls_zip"] = dl_manager.extract(owt_path)

    file_paths = tree.map_structure(os.fspath, file_paths)

    pages_pcollection = self._get_pages_pcollection(
        pipeline, file_paths, dl_manager
    )

    def _filter(page, lang, predicate_fn):
      return page.language == lang and c4_utils.get_hashed_url_filter_fn(
          predicate_fn
      )(page)

    train_predicate_fn = lambda x: x % 1000 != 0  # 99.9%
    validation_predicate_fn = lambda x: x % 1000 == 0  # 00.1%

    if len(self.builder_config.languages) == 1:
      # Single-language version.
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs=dict(
                  split="train",
                  pages=pages_pcollection,
                  split_filter_fn=c4_utils.get_hashed_url_filter_fn(
                      predicate_fn=train_predicate_fn
                  ),
              ),
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs=dict(
                  split="validation",
                  pages=pages_pcollection,
                  split_filter_fn=c4_utils.get_hashed_url_filter_fn(
                      predicate_fn=validation_predicate_fn
                  ),
              ),
          ),
      ]

    splits = []
    for lang in self.builder_config.languages + [c4_utils.UNKNOWN_LANGUAGE]:
      splits.extend([
          tfds.core.SplitGenerator(
              name=lang,
              gen_kwargs=dict(
                  split=lang,
                  pages=pages_pcollection,
                  split_filter_fn=functools.partial(
                      _filter, lang=lang, predicate_fn=train_predicate_fn
                  ),
              ),
          ),
          tfds.core.SplitGenerator(
              name=f"{lang}-validation",
              gen_kwargs=dict(
                  split=f"{lang}-validation",
                  pages=pages_pcollection,
                  split_filter_fn=functools.partial(
                      _filter,
                      lang=lang,
                      predicate_fn=validation_predicate_fn,
                  ),
              ),
          ),
      ])
    return splits

  def _get_pages_pcollection(self, pipeline, file_paths, dl_manager):
    """Build PCollection of un-split page content."""
    beam = tfds.core.lazy_imports.apache_beam

    def download_wet_file(path, dl_dir):
      url = f"{_DOWNLOAD_HOST}/{path}"
      out_path = epath.Path(dl_dir) / path

      if out_path.exists():
        c4_utils.get_counter_inc_fn("download_wet_url")("exists")
        return out_path

      tmp_dir = epath.Path(
          f"{os.fspath(out_path)}.incomplete{uuid.uuid4().hex}"
      )
      try:
        tmp_dir.mkdir(parents=True, exist_ok=True)
        downloader = tfds.download.download_manager.get_downloader()
        with downloader.tqdm():
          # TODO(slebedev): Investigate why pytype infers Promise[Future[...]].
          dl_path = downloader.download(url, tmp_dir).get().path  # type: ignore
          dl_path = epath.Path(dl_path)
        dl_path.rename(out_path)
      finally:
        tmp_dir.rmtree(missing_ok=True)
        c4_utils.get_counter_inc_fn("download_wet_url")("downloaded")
      return out_path

    wet_file_paths = (
        pipeline
        | "create_wet_path_urls" >> beam.Create(file_paths["wet_path_urls"])
        | beam.io.ReadAllFromText(
            compression_type=beam.io.filesystem.CompressionTypes.UNCOMPRESSED
        )
        # Increase parallelism.
        | beam.Reshuffle()
        | "filter_corrupt_wet_files"
        >> beam.Filter(lambda p: p not in _KNOWN_CORRUPT_WET_FILES)
        | beam.Map(
            download_wet_file,
            dl_dir=os.path.join(dl_manager.download_dir, "c4_wet_files"),
        )
    )

    # Parse WET files and filter by length.
    # Output: [PageFeatures]
    pages = (
        wet_file_paths
        | beam.FlatMap(c4_utils.split_wet_file)
        | beam.Filter(c4_utils.is_valid_length)
    )

    # Optionally filter for RealNews domains.
    # Output: [PageFeatures]
    if self.builder_config.realnewslike:
      with epath.Path(file_paths["realnews_domains"]).open() as f:
        realnews_domains = json.load(f)
      pages |= beam.Filter(c4_utils.is_realnews_domain, realnews_domains)

    # Normalize and deduplicate by URL.
    # Output: [PageFeatures]
    pages = (
        pages
        | "normalize_url" >> beam.Map(lambda p: (p.normalized_url, p))
        | "select_newest" >> beam.CombinePerKey(c4_utils.select_newest_page)
        | beam.Values()
    )

    # Optionally filter for WebText-like URLs.
    # Output: [PageFeatures]
    if self.builder_config.webtextlike:
      webtextlike_urls = (
          pipeline
          | "read_webtextlike_urls"
          >> beam.io.ReadFromText(
              os.path.join(
                  file_paths["openwebtext_urls_zip"],
                  _OPENWEBTEXT_URLS_FILE_PATTERN,
              )
          )
          | "add_dummy_page"
          >> beam.Map(lambda url: (c4_utils.normalize_url(url), PageFeatures()))
      )
      pages = (
          {
              "pages": pages | beam.Map(lambda p: (p.normalized_url, p)),
              "webtextlike_urls": webtextlike_urls,
          }
          | "group_webtextlike_urls" >> beam.CoGroupByKey()
          | beam.FlatMap(c4_utils.filter_by_webtextlike)
      )

    if self.builder_config.paragraph_filter:
      pages |= beam.Filter(c4_utils.paragraph_filter)

    if self.builder_config.clean:
      pages |= "clean_pages" >> beam.FlatMap(c4_utils.get_clean_page_fn())

    if self.builder_config.dedupe:
      pages = (
          # Also removes documents with too few sentences after deduplication.
          c4_utils.remove_duplicate_text(pages)  # pylint:disable=g-long-ternary
          if self.builder_config.clean
          else
          # If we are not cleaning, do not remove too-few-sentence documents.
          c4_utils.remove_duplicate_text(pages, min_num_sentences=0)
      )

    # Add detected language.
    if self.builder_config.languages == ["en"]:
      # Use langdetect for reproducibility of the original C4.
      pages |= beam.FlatMap(c4_utils.detect_english)
    else:
      pages = c4_utils.detect_languages(
          pages, valid_languages=self.builder_config.languages
      )

    if self.builder_config.badwords_filter_fraction > 0.0:
      # Create dictionary of badwords regex for each available language.
      badwords = collections.defaultdict(set)
      for lang, path in file_paths["badwords"].items():
        lang = lang.split("-")[0]  # remove suffix if present
        with epath.Path(path).open() as f:
          badwords[lang].update(l.strip() for l in f)

      for lang, allowlist in _BADWORDS_ALLOWLIST.items():
        badwords[lang] -= allowlist

      pages |= beam.Filter(
          c4_utils.get_badwords_filter_fn(
              badwords,
              filter_fraction=self.builder_config.badwords_filter_fraction,
          )
      )

    return pages

  def _build_pcollection(self, unused_pipeline, split, pages, split_filter_fn):
    beam = tfds.core.lazy_imports.apache_beam

    def _emit_examples(page: PageFeatures):
      c4_utils.get_counter_inc_fn(split)("examples")
      return page.url, {
          "url": page.url,
          "text": page.text,
          "content-type": page.content_type,
          "content-length": page.content_length,
          "timestamp": page.timestamp,
      }

    return pages | beam.Filter(split_filter_fn) | beam.Map(_emit_examples)
