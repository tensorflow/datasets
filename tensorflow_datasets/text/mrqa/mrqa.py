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

"""mrqa datasets."""

# pylint: disable=g-complex-comprehension, anomalous-backslash-in-string

from __future__ import annotations

import json
import textwrap

from etils import epath
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The MRQA 2019 Shared Task focuses on generalization in question answering. An
effective question answering system should do more than merely interpolate from
the training set to answer test examples drawn from the same distribution: it
should also be able to extrapolate to out-of-distribution examples — a
significantly harder challenge.

MRQA adapts and unifies multiple distinct question answering datasets (carefully
selected subsets of existing datasets) into the same format (SQuAD format).
Among them, six datasets were made available for training, and six datasets were
made available for testing. Small portions of the training datasets
were held-out as in-domain data that may be used for development. The testing
datasets only contain out-of-domain data. This benchmark is released as part of
the MRQA 2019 Shared Task.

More information can be found at: `https://mrqa.github.io/2019/shared.html`.
"""

_HOMEPAGE = 'https://mrqa.github.io/2019/shared.html'

_CITATION = """@inproceedings{fisch-etal-2019-mrqa,
    title = "{MRQA} 2019 Shared Task: Evaluating Generalization in Reading Comprehension",
    author = "Fisch, Adam  and
      Talmor, Alon  and
      Jia, Robin  and
      Seo, Minjoon  and
      Choi, Eunsol  and
      Chen, Danqi",
    booktitle = "Proceedings of the 2nd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5801",
    doi = "10.18653/v1/D19-5801",
    pages = "1--13",
}

Note that each MRQA dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
"""

_URL_BASE = 'https://s3.us-east-2.amazonaws.com/mrqa/release/v2'
_URLs = {
    # Train sub-datasets
    'train+SQuAD':
        f'{_URL_BASE}/train/SQuAD.jsonl.gz',
    'train+NewsQA':
        f'{_URL_BASE}/train/NewsQA.jsonl.gz',
    'train+TriviaQA':
        f'{_URL_BASE}/train/TriviaQA-web.jsonl.gz',
    'train+SearchQA':
        f'{_URL_BASE}/train/SearchQA.jsonl.gz',
    'train+HotpotQA':
        f'{_URL_BASE}/train/HotpotQA.jsonl.gz',
    'train+NaturalQuestions':
        f'{_URL_BASE}/train/NaturalQuestionsShort.jsonl.gz',
    # Validation sub-datasets
    'validation+SQuAD':
        f'{_URL_BASE}/dev/SQuAD.jsonl.gz',
    'validation+NewsQA':
        f'{_URL_BASE}/dev/NewsQA.jsonl.gz',
    'validation+TriviaQA':
        f'{_URL_BASE}/dev/TriviaQA-web.jsonl.gz',
    'validation+SearchQA':
        f'{_URL_BASE}/dev/SearchQA.jsonl.gz',
    'validation+HotpotQA':
        f'{_URL_BASE}/dev/HotpotQA.jsonl.gz',
    'validation+NaturalQuestions':
        f'{_URL_BASE}/dev/NaturalQuestionsShort.jsonl.gz',
    # Test sub-datasets
    'test+BioASQ':
        'http://participants-area.bioasq.org/MRQA2019/',  # BioASQ.jsonl.gz
    'test+DROP':
        f'{_URL_BASE}/dev/DROP.jsonl.gz',
    'test+DuoRC':
        f'{_URL_BASE}/dev/DuoRC.ParaphraseRC.jsonl.gz',
    'test+RACE':
        f'{_URL_BASE}/dev/RACE.jsonl.gz',
    'test+RelationExtraction':
        f'{_URL_BASE}/dev/RelationExtraction.jsonl.gz',
    'test+TextbookQA':
        f'{_URL_BASE}/dev/TextbookQA.jsonl.gz',
}


class MRQAConfig(tfds.core.BuilderConfig):
  """BuilderConfig for MRQA."""

  def __init__(self, *, features, data_urls, citation, **kwargs):
    """BuilderConfig for MRQA.

    Args:
      features: `tfds.features.FeaturesDict`, specific feature dict for the
        dataset.
      data_urls: `dict`, urls to download the files from
      citation: `string`, citation for the data set
      **kwargs: keyword arguments forwarded to super.
    """
    super(MRQAConfig, self).__init__(**kwargs)
    self.features = features
    self.data_urls = data_urls
    self.citation = citation


class MRQA(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for mrqa dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  DEFAULT_FEATURES = tfds.features.FeaturesDict({
      'subset':
          tf.string,
      'context':
          tf.string,
      'context_tokens':
          tfds.features.Sequence({
              'tokens': tf.string,
              'offsets': tf.int32,
          }),
      'qid':
          tf.string,
      'question':
          tf.string,
      'question_tokens':
          tfds.features.Sequence({
              'tokens': tf.string,
              'offsets': tf.int32,
          }),
      'detected_answers':
          tfds.features.Sequence({
              'text':
                  tf.string,
              'char_spans':
                  tfds.features.Sequence({
                      'start': tf.int32,
                      'end': tf.int32,
                  }),
              'token_spans':
                  tfds.features.Sequence({
                      'start': tf.int32,
                      'end': tf.int32,
                  }),
          }),
      'answers':
          tfds.features.Sequence(tf.string),
  })
  BUILDER_CONFIGS = [
      MRQAConfig(
          name='squad',
          description=textwrap.dedent("""\
          The SQuAD (Stanford Question Answering Dataset) dataset is used as the
          basis for the shared task format. Crowdworkers are shown paragraphs
          from Wikipedia and are asked to write questions with extractive
          answers.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': _URLs['train+SQuAD'],
              'validation': _URLs['validation+SQuAD'],
          },
          citation=textwrap.dedent("""\
          @inproceedings{rajpurkar-etal-2016-squad,
              title = "{SQ}u{AD}: 100,000+ Questions for Machine Comprehension of Text",
              author = "Rajpurkar, Pranav  and
                Zhang, Jian  and
                Lopyrev, Konstantin  and
                Liang, Percy",
              booktitle = "Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing",
              month = nov,
              year = "2016",
              address = "Austin, Texas",
              publisher = "Association for Computational Linguistics",
              url = "https://aclanthology.org/D16-1264",
              doi = "10.18653/v1/D16-1264",
              pages = "2383--2392",
          }
          """)),
      MRQAConfig(
          name='news_qa',
          description=textwrap.dedent("""\
          Two sets of crowdworkers ask and answer questions based on CNN news
          articles. The “questioners” see only the article’s headline and
          summary while the “answerers” see the full article. Questions that
          have no answer or are flagged in the dataset to be without annotator
          agreement are discarded.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': _URLs['train+NewsQA'],
              'validation': _URLs['validation+NewsQA'],
          },
          citation=textwrap.dedent("""\
          @inproceedings{trischler-etal-2017-newsqa,
              title = "{N}ews{QA}: A Machine Comprehension Dataset",
              author = "Trischler, Adam  and
                Wang, Tong  and
                Yuan, Xingdi  and
                Harris, Justin  and
                Sordoni, Alessandro  and
                Bachman, Philip  and
                Suleman, Kaheer",
              booktitle = "Proceedings of the 2nd Workshop on Representation Learning for {NLP}",
              month = aug,
              year = "2017",
              address = "Vancouver, Canada",
              publisher = "Association for Computational Linguistics",
              url = "https://aclanthology.org/W17-2623",
              doi = "10.18653/v1/W17-2623",
              pages = "191--200",
          }
      #     """)),
      MRQAConfig(
          name='trivia_qa',
          description=textwrap.dedent("""\
          Question and answer pairs are sourced from trivia and quiz-league
          websites. The web version of TriviaQA, where the contexts are
          retrieved from the results of a Bing search query, is used.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': _URLs['train+TriviaQA'],
              'validation': _URLs['validation+TriviaQA'],
          },
          citation=textwrap.dedent("""\
          @inproceedings{joshi-etal-2017-triviaqa,
              title = "{T}rivia{QA}: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension",
              author = "Joshi, Mandar  and
                Choi, Eunsol  and
                Weld, Daniel  and
                Zettlemoyer, Luke",
              booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
              month = jul,
              year = "2017",
              address = "Vancouver, Canada",
              publisher = "Association for Computational Linguistics",
              url = "https://aclanthology.org/P17-1147",
              doi = "10.18653/v1/P17-1147",
              pages = "1601--1611",
          }
          """)),
      MRQAConfig(
          name='search_qa',
          description=textwrap.dedent("""\
          Question and answer pairs are sourced from the Jeopardy! TV show. The
          contexts are composed of retrieved snippets from a Google search
          query.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': _URLs['train+SearchQA'],
              'validation': _URLs['validation+SearchQA'],
          },
          citation=textwrap.dedent("""\
          @article{dunn2017searchqa,
              title={Searchqa: A new q\&a dataset augmented with context from a search engine},
              author={Dunn, Matthew and Sagun, Levent and Higgins, Mike and Guney, V Ugur and Cirik, Volkan and Cho, Kyunghyun},
              journal={arXiv preprint arXiv:1704.05179},
              year={2017}
          }
          """)),
      MRQAConfig(
          name='hotpot_qa',
          description=textwrap.dedent("""\
          Crowdworkers are shown two entity-linked paragraphs from Wikipedia and
          are asked to write and answer questions that require multi-hop
          reasoning to solve. In the original setting, these paragraphs are
          mixed with additional distractor paragraphs to make inference harder.
          Here, the distractor paragraphs are not included.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': _URLs['train+HotpotQA'],
              'validation': _URLs['validation+HotpotQA'],
          },
          citation=textwrap.dedent("""\
          @inproceedings{yang-etal-2018-hotpotqa,
              title = "{H}otpot{QA}: A Dataset for Diverse, Explainable Multi-hop Question Answering",
              author = "Yang, Zhilin  and
                Qi, Peng  and
                Zhang, Saizheng  and
                Bengio, Yoshua  and
                Cohen, William  and
                Salakhutdinov, Ruslan  and
                Manning, Christopher D.",
              booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
              month = oct # "-" # nov,
              year = "2018",
              address = "Brussels, Belgium",
              publisher = "Association for Computational Linguistics",
              url = "https://aclanthology.org/D18-1259",
              doi = "10.18653/v1/D18-1259",
              pages = "2369--2380",
          }
          """)),
      MRQAConfig(
          name='natural_questions',
          description=textwrap.dedent("""\
          Questions are collected from information-seeking queries to the Google
          search engine by real users under natural conditions. Answers to the
          questions are annotated in a retrieved Wikipedia page by crowdworkers.
          Two types of annotations are collected: 1) the HTML bounding box
          containing enough information to completely infer the answer to the
          question (Long Answer), and 2) the subspan or sub-spans within the
          bounding box that comprise the actual answer (Short Answer). Only the
          examples that have short answers are used, and the long answer is used
          as the context.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'train': _URLs['train+NaturalQuestions'],
              'validation': _URLs['validation+NaturalQuestions'],
          },
          citation=textwrap.dedent("""\
          @article{kwiatkowski-etal-2019-natural,
              title = "Natural Questions: A Benchmark for Question Answering Research",
              author = "Kwiatkowski, Tom  and
                Palomaki, Jennimaria  and
                Redfield, Olivia  and
                Collins, Michael  and
                Parikh, Ankur  and
                Alberti, Chris  and
                Epstein, Danielle  and
                Polosukhin, Illia  and
                Devlin, Jacob  and
                Lee, Kenton  and
                Toutanova, Kristina  and
                Jones, Llion  and
                Kelcey, Matthew  and
                Chang, Ming-Wei  and
                Dai, Andrew M.  and
                Uszkoreit, Jakob  and
                Le, Quoc  and
                Petrov, Slav",
              journal = "Transactions of the Association for Computational Linguistics",
              volume = "7",
              year = "2019",
              address = "Cambridge, MA",
              publisher = "MIT Press",
              url = "https://aclanthology.org/Q19-1026",
              doi = "10.1162/tacl_a_00276",
              pages = "452--466",
          }
          """)),
      MRQAConfig(
          name='bio_asq',
          description=textwrap.dedent("""\
          BioASQ, a challenge on large-scale biomedical semantic indexing and
          question answering, contains question and answer pairs that are
          created by domain experts. They are then manually linked to multiple
          related science (PubMed) articles. The full abstract of each of the
          linked articles is downloaded and used as individual contexts (e.g., a
          single question can be linked to multiple, independent articles to
          create multiple QA-context pairs). Abstracts that do not exactly
          contain the answer are discarded.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'test': _URLs['test+BioASQ'],
          },
          citation=textwrap.dedent("""\
          @article{tsatsaronis2015overview,
              title={An overview of the BIOASQ large-scale biomedical semantic indexing and question answering competition},
              author={Tsatsaronis, George and Balikas, Georgios and Malakasiotis, Prodromos and Partalas, Ioannis and Zschunke, Matthias and Alvers, Michael R and Weissenborn, Dirk and Krithara, Anastasia and Petridis, Sergios and Polychronopoulos, Dimitris and others},
              journal={BMC bioinformatics},
              volume={16},
              number={1},
              pages={1--28},
              year={2015},
              publisher={Springer}
          }
          """)),
      MRQAConfig(
          name='drop',
          description=textwrap.dedent("""\
          DROP (Discrete Reasoning Over the content of Paragraphs) examples were
          collected similarly to SQuAD, where crowdworkers are asked to create
          question-answer pairs from Wikipedia paragraphs. The questions focus
          on quantitative reasoning, and the original dataset contains
          non-extractive numeric answers as well as extractive text answers. The
          set of questions that are extractive is used.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'test': _URLs['test+DROP'],
          },
          citation=textwrap.dedent("""\
          @inproceedings{dua-etal-2019-drop,
              title = "{DROP}: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs",
              author = "Dua, Dheeru  and
                Wang, Yizhong  and
                Dasigi, Pradeep  and
                Stanovsky, Gabriel  and
                Singh, Sameer  and
                Gardner, Matt",
              booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
              month = jun,
              year = "2019",
              address = "Minneapolis, Minnesota",
              publisher = "Association for Computational Linguistics",
              url = "https://aclanthology.org/N19-1246",
              doi = "10.18653/v1/N19-1246",
              pages = "2368--2378",
          }
          """)),
      MRQAConfig(
          name='duo_rc',
          description=textwrap.dedent("""\
          The ParaphraseRC split of the DuoRC dataset is used. In this setting,
          two different plot summaries of the same movie are collected—one from
          Wikipedia and the other from IMDb. Two different sets of crowdworkers
          ask and answer questions about the movie plot, where the “questioners”
          are shown only the Wikipedia page, and the “answerers” are shown only
          the IMDb page. Questions that are marked as unanswerable are
          discarded.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'test': _URLs['test+DuoRC'],
          },
          citation=textwrap.dedent("""\
          @inproceedings{saha-etal-2018-duorc,
              title = "{D}uo{RC}: Towards Complex Language Understanding with Paraphrased Reading Comprehension",
              author = "Saha, Amrita  and
                Aralikatte, Rahul  and
                Khapra, Mitesh M.  and
                Sankaranarayanan, Karthik",
              booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
              month = jul,
              year = "2018",
              address = "Melbourne, Australia",
              publisher = "Association for Computational Linguistics",
              url = "https://aclanthology.org/P18-1156",
              doi = "10.18653/v1/P18-1156",
              pages = "1683--1693",
          }
          """)),
      MRQAConfig(
          name='race',
          description=textwrap.dedent("""\
          ReAding Comprehension Dataset From Examinations (RACE) is collected
          from English reading comprehension exams for middle and high school
          Chinese students. The high school split (which is more challenging)
          is used and also the implicit “fill in the blank” style questions
          (which are unnatural for this task) are filtered out.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'test': _URLs['test+RACE'],
          },
          citation=textwrap.dedent("""\
          @inproceedings{lai-etal-2017-race,
              title = "{RACE}: Large-scale {R}e{A}ding Comprehension Dataset From Examinations",
              author = "Lai, Guokun  and
                Xie, Qizhe  and
                Liu, Hanxiao  and
                Yang, Yiming  and
                Hovy, Eduard",
              booktitle = "Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing",
              month = sep,
              year = "2017",
              address = "Copenhagen, Denmark",
              publisher = "Association for Computational Linguistics",
              url = "https://aclanthology.org/D17-1082",
              doi = "10.18653/v1/D17-1082",
              pages = "785--794",
          }
          """)),
      MRQAConfig(
          name='relation_extraction',
          description=textwrap.dedent("""\
          Given a slot-filling dataset, relations among entities are
          systematically transformed into questionanswer pairs using templates.
          For example, the educated_at(x, y) relationship between two entities x
          and y appearing in a sentence can be expressed as “Where was x
          educated at?” with answer y. Multiple templates for each type of
          relation are collected. The dataset’s zeroshot benchmark split
          (generalization to unseen relations) is used, and only the positive
          examples are kept.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'test': _URLs['test+RelationExtraction'],
          },
          citation=textwrap.dedent("""\
          @inproceedings{levy-etal-2017-zero,
              title = "Zero-Shot Relation Extraction via Reading Comprehension",
              author = "Levy, Omer  and
                Seo, Minjoon  and
                Choi, Eunsol  and
                Zettlemoyer, Luke",
              booktitle = "Proceedings of the 21st Conference on Computational Natural Language Learning ({C}o{NLL} 2017)",
              month = aug,
              year = "2017",
              address = "Vancouver, Canada",
              publisher = "Association for Computational Linguistics",
              url = "https://aclanthology.org/K17-1034",
              doi = "10.18653/v1/K17-1034",
              pages = "333--342",
          }
          """)),
      MRQAConfig(
          name='textbook_qa',
          description=textwrap.dedent("""\
          TextbookQA is collected from lessons from middle school Life Science,
          Earth Science, and Physical Science textbooks. Questions that are
          accompanied with a diagram, or that are “True or False” questions are
          not included.
          """),
          features=DEFAULT_FEATURES,
          data_urls={
              'test': _URLs['test+TextbookQA'],
          },
          citation=textwrap.dedent("""\
          @inproceedings{kembhavi2017you,
              title={Are you smarter than a sixth grader? textbook question answering for multimodal machine comprehension},
              author={Kembhavi, Aniruddha and Seo, Minjoon and Schwenk, Dustin and Choi, Jonghyun and Farhadi, Ali and Hajishirzi, Hannaneh},
              booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern recognition},
              pages={4999--5007},
              year={2017}
          }
          """)),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(self.builder_config.features),
        supervised_keys=None,
        homepage=_HOMEPAGE,
        citation=self.builder_config.citation + '\n' + _CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    data_dir = dl_manager.download_and_extract(self.builder_config.data_urls)
    split_generators = {}

    if 'train' in self.builder_config.data_urls:
      split_generators.update({
          tfds.Split.TRAIN:
              self._generate_examples(path=data_dir['train'], split='train'),
      })

    if 'validation' in self.builder_config.data_urls:
      split_generators.update({
          tfds.Split.VALIDATION:
              self._generate_examples(
                  path=data_dir['validation'], split='validation'),
      })

    if 'test' in self.builder_config.data_urls:
      split_generators.update({
          tfds.Split.TEST:
              self._generate_examples(path=data_dir['test'], split='test'),
      })
    return split_generators

  def _generate_examples(self, path, split):
    """Yields examples."""
    with epath.Path(path).open() as f:
      header = next(f)
      subset = json.loads(header)['header']['dataset']

      for row in f:
        paragraph = json.loads(row)
        context = paragraph['context'].strip()
        context_tokens = [{
            'tokens': t[0],
            'offsets': t[1]
        } for t in paragraph['context_tokens']]
        for qa in paragraph['qas']:
          qid = qa['qid']
          question = qa['question'].strip()
          question_tokens = [{
              'tokens': t[0],
              'offsets': t[1]
          } for t in qa['question_tokens']]
          detected_answers = []
          for detect_ans in qa['detected_answers']:
            detected_answers.append({
                'text':
                    detect_ans['text'].strip(),
                'char_spans': [{
                    'start': t[0],
                    'end': t[1]
                } for t in detect_ans['char_spans']],
                'token_spans': [{
                    'start': t[0],
                    'end': t[1]
                } for t in detect_ans['token_spans']],
            })
          answers = qa['answers']
          yield f'{split}+{subset}_{qid}', {
              'subset': subset,
              'context': context,
              'context_tokens': context_tokens,
              'qid': qid,
              'question': question,
              'question_tokens': question_tokens,
              'detected_answers': detected_answers,
              'answers': answers,
          }
