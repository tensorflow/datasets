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

"""Text datasets."""

from tensorflow_datasets.text.ag_news_subset import AGNewsSubset
from tensorflow_datasets.text.anli import Anli
from tensorflow_datasets.text.assin2 import Assin2
from tensorflow_datasets.text.beir import Beir
from tensorflow_datasets.text.blimp import Blimp
from tensorflow_datasets.text.bool_q import BoolQ
from tensorflow_datasets.text.c4 import C4
from tensorflow_datasets.text.cfq import CFQ
from tensorflow_datasets.text.cfq import CFQConfig
from tensorflow_datasets.text.civil_comments import CivilComments
from tensorflow_datasets.text.clinc_oos import ClincOOS
from tensorflow_datasets.text.cos_e import CosE
from tensorflow_datasets.text.definite_pronoun_resolution import DefinitePronounResolution
from tensorflow_datasets.text.docnli import DocNLI
from tensorflow_datasets.text.dolphin_number_word import DolphinNumberWord
from tensorflow_datasets.text.drop import Drop
from tensorflow_datasets.text.eraser_multi_rc import EraserMultiRc
from tensorflow_datasets.text.esnli import Esnli
from tensorflow_datasets.text.gap import Gap
from tensorflow_datasets.text.gem import Gem
from tensorflow_datasets.text.glue import Glue
from tensorflow_datasets.text.goemotions import Goemotions
from tensorflow_datasets.text.gpt3 import Gpt3
from tensorflow_datasets.text.gsm8k import Gsm8k
from tensorflow_datasets.text.hellaswag import Hellaswag
from tensorflow_datasets.text.imdb import IMDBReviews
from tensorflow_datasets.text.irc_disentanglement import IrcDisentanglement
from tensorflow_datasets.text.lambada import Lambada
from tensorflow_datasets.text.librispeech_lm import LibrispeechLm
from tensorflow_datasets.text.lm1b import Lm1b
from tensorflow_datasets.text.math_dataset import MathDataset
from tensorflow_datasets.text.math_qa import MathQa
from tensorflow_datasets.text.movie_rationales import MovieRationales
from tensorflow_datasets.text.mrqa import MRQA
from tensorflow_datasets.text.multi_nli import MultiNLI
from tensorflow_datasets.text.multi_nli_mismatch import MultiNLIMismatch
from tensorflow_datasets.text.openbookqa import Openbookqa
from tensorflow_datasets.text.paws_wiki import PawsWiki
from tensorflow_datasets.text.paws_x_wiki import PawsXWiki
from tensorflow_datasets.text.pg19 import Pg19
from tensorflow_datasets.text.piqa import PIQA
from tensorflow_datasets.text.qa4mre import Qa4mre
from tensorflow_datasets.text.quac import Quac
from tensorflow_datasets.text.quality import Quality
from tensorflow_datasets.text.race import Race
from tensorflow_datasets.text.reddit_disentanglement import RedditDisentanglement
from tensorflow_datasets.text.salient_span_wikipedia import SalientSpanWikipedia
from tensorflow_datasets.text.salient_span_wikipedia import SalientSpanWikipediaConfig
from tensorflow_datasets.text.scan import Scan
from tensorflow_datasets.text.scan import ScanConfig
from tensorflow_datasets.text.schema_guided_dialogue import SchemaGuidedDialogue
from tensorflow_datasets.text.scicite import Scicite
from tensorflow_datasets.text.scitail import SciTail
from tensorflow_datasets.text.scrolls import Scrolls
from tensorflow_datasets.text.sentiment140 import Sentiment140
from tensorflow_datasets.text.snli import Snli
from tensorflow_datasets.text.squad_question_generation import SquadQuestionGeneration
from tensorflow_datasets.text.star_cfq import StarCFQ
from tensorflow_datasets.text.story_cloze import StoryCloze
from tensorflow_datasets.text.super_glue import SuperGlue
from tensorflow_datasets.text.tiny_shakespeare import TinyShakespeare
from tensorflow_datasets.text.trec import Trec
from tensorflow_datasets.text.unifiedqa import UnifiedQA
from tensorflow_datasets.text.wiki40b import Wiki40b
from tensorflow_datasets.text.wikiann import Wikiann
from tensorflow_datasets.text.wikipedia import Wikipedia
from tensorflow_datasets.text.wikipedia_toxicity_subtypes import WikipediaToxicitySubtypes
from tensorflow_datasets.text.winogrande import Winogrande
from tensorflow_datasets.text.wordnet import Wordnet
from tensorflow_datasets.text.wsc273 import Wsc273
from tensorflow_datasets.text.xnli import Xnli
from tensorflow_datasets.text.xtreme_pawsx import XtremePawsx
from tensorflow_datasets.text.xtreme_xnli import XtremeXnli
from tensorflow_datasets.text.yelp_polarity import YelpPolarityReviews
