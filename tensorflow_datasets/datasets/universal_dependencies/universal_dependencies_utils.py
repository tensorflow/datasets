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

"""Utils for the Universal Dependencies dataset.

This file contains details about the different configs of the Universal
Dependencies dataset, such as the description of the configs and their urls.
"""
import os
from typing import List, Union

from etils import epath

DESCRIPTIONS = {
    "af_afribooms":
        "UD Afrikaans-AfriBooms is a conversion of the AfriBooms Dependency "
        "Treebank, originally annotated with a simplified PoS set and "
        "dependency relations according to a subset of the Stanford tag set. "
        "The corpus consists of public government documents. The dataset was "
        "proposed in 'AfriBooms: An Online Treebank for Afrikaans' by "
        "Augustinus et al. (2016); "
        "https://www.aclweb.org/anthology/L16-1107.pdf.",
    "akk_pisandub":
        "A small set of sentences from Babylonian royal inscriptions.",
    "akk_riao":
        "UD_Akkadian-RIAO is a small treebank which consists of 22 277 words "
        "and 1845 sentences. This represents an intact subset of a total of "
        "2211 sentences from the early Neo-Assyrian royal inscriptions  of the"
        " tenth and ninth centuries BCE. These royal inscriptions were "
        "extracted from Oracc (Open Richly Annotated Cuneiform Corpus; "
        "http://oracc.museum.upenn.edu/riao/), where all Neo-Assyrian royal "
        "inscriptions are lemmatized word-for-word. The language of the corpus"
        " is Standard Babylonian, with occasional Assyrianisms, whereas "
        "“Akkadian” is the umbrella term for both Assyrian and Babylonian. The"
        " treebank was manually annotated following the UD annotation "
        "guidelines.",
    "aqz_tudet":
        "UD_Akuntsu-TuDeT is a collection of annotated texts in Akuntsú. "
        "Together with UD_Tupinamba-TuDeT and UD_Munduruku-TuDeT, "
        "UD_Akuntsu-TuDeT is part of the TuLaR project.  The sentences are "
        "being annotated by Carolina Aragon and Fabrício Ferraz Gerardi.",
    "sq_tsa":
        "The UD Treebank for Standard Albanian (TSA) is a small treebank that "
        "consists of 60 sentences corresponding to 922 tokens. The data was "
        "collected from different Wikipedia entries. This treebank was created"
        " mainly manually following the Universal Dependencies guidelines. The"
        " lemmatization was performed using the lemmatizer "
        "https://bitbucket.org/timarkh/uniparser-albanian-grammar/src/master/ "
        "developed by the Albanian National Corpus team (Maria Morozova, "
        "Alexander Rusakov, Timofey Arkhangelskiy). Tagging and Morphological "
        "Analysis were semi-automated through python scripts and corrected "
        "manually, whereas Dependency relations were assigned fully manually. "
        "We encourage any initiatives to increase the size and/or improve the "
        "overall quality of the Treebank.",
    "am_att":
        "UD_Amharic-ATT is a manually annotated Treebanks. It is annotated for"
        " POS tag, morphological information and dependency relations. Since "
        "Amharic is a morphologically-rich, pro-drop, and languages having a "
        "feature of clitic doubling, clitics have been segmented manually.",
    "grc_perseus":
        "This Universal Dependencies Ancient Greek Treebank consists of an "
        "automatic conversion of a selection of passages from the Ancient "
        "Greek and Latin Dependency Treebank 2.1",
    "grc_proiel":
        "The Ancient Greek PROIEL treebank is based on the Ancient Greek data "
        "from the PROIEL treebank, which is maintained at the Department of "
        "Philosophy, Classics, History of Arts and Ideas at the University of "
        "Oslo. The conversion is based on the 20180408 release of the PROIEL "
        "treebank available from "
        "https://github.com/proiel/proiel-treebank/releases. The original "
        "annotators are acknowledged in the files available there. The "
        "conversion code is available in the Rubygem proiel-cli, "
        "https://github.com/proiel/proiel-cli.",
    "apu_ufpa":
        "The initial release contains 70 annotated sentences. This is the "
        "first treebank in a language from the Arawak family. The original "
        "interlinear glosses are included in the tree bank, and their "
        "conversion into a full UD annotation is an ongoing process. The "
        "sent_id values (e.g.: FernandaM2017:Texto-6-19) are representative of"
        " the collector, year of publication, text identifier and the number "
        "of the sentence in order from the original text.",
    "hbo_ptnk":
        "UD Ancient Hebrew PTNK contains portions of the Biblia Hebraic "
        "Stuttgartensia with morphological annotations from ETCBC.",
    "ar_nyuad":
        "The treebank consists of 19,738 sentences (738889 tokens), and its "
        "domain is mainly newswire. The annotation is licensed under the terms"
        " of CC BY-SA 4.0, and the original PATB can be obtained from the "
        "LDC’s official website.",
    "ar_padt":
        "The Arabic-PADT UD treebank is based on the Prague Arabic Dependency "
        "Treebank (PADT), created at the Charles University in Prague.",
    "ar_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "aii_as":
        "The Uppsala Assyrian Treebank is a small treebank for Modern Standard"
        " Assyrian. The corpus is collected and annotated manually. The data "
        "was randomly collected from different textbooks and a short "
        "translation of The Merchant of Venice.",
    "bm_crb":
        "The UD Bambara treebank is a section of the Corpus Référence du "
        "Bambara annotated natively with Universal Dependencies.",
    "eu_bdt":
        "The Basque UD treebank is based on a automatic conversion from part "
        "of the Basque Dependency Treebank (BDT), created at the University of"
        " of the Basque Country by the IXA NLP research group. The treebank "
        "consists of 8.993 sentences (121.443 tokens) and covers mainly "
        "literary and journalistic texts.",
    "bej_nsc":
        "A Universal Dependencies corpus for Beja, North-Cushitic branch of "
        "the Afro-Asiatic phylum mainly spoken in Sudan, Egypt and Eritrea.",
    "be_hse":
        "The Belarusian UD treebank is based on a sample of the news texts "
        "included in the Belarusian-Russian parallel subcorpus of the Russian "
        "National Corpus, online search available at: "
        "http://ruscorpora.ru/search-para-be.html.",
    "bn_bru":
        "The BRU Bengali treebank has been created at Begum Rokeya University,"
        " Rangpur, by the members of Semantics Lab.",
    "bho_bhtb":
        "The Bhojpuri UD Treebank (BHTB) v2.6 consists of 6,664 tokens(357 "
        "sentences). This Treebank is a part of the Universal Dependency "
        "treebank project. Initially, it was initiated by me (Atul) at "
        "Jawaharlal Nehru University, New Delhi during the doctoral research "
        "work. BHTB data contains syntactic annotation according to "
        "dependency-constituency schema, as well as morphological tags and "
        "lemmas. In this data, XPOS is annotated  according to Bureau of "
        "Indian Standards (BIS) Part Of Speech (POS) tagset.",
    "br_keb":
        "UD Breton-KEB is a treebank of Breton that has been manually "
        "annotated according to the Universal Dependencies guidelines. The "
        "tokenisation guidelines and morphological annotation comes from a "
        "finite-state morphological analyser of Breton released as part of the"
        " Apertium project.",
    "bg_btb":
        "UD_Bulgarian-BTB is based on the HPSG-based BulTreeBank, created at "
        "the Institute of Information and Communication Technologies, "
        "Bulgarian Academy of Sciences. The original consists of 215,000 "
        "tokens (over 15,000 sentences).",
    "bxr_bdt":
        "The UD Buryat treebank was annotated manually natively in UD and "
        "contains grammar book sentences, along with news and some fiction.",
    "yue_hk":
        "A Cantonese treebank (in Traditional Chinese characters) of film "
        "subtitles and of legislative proceedings of Hong Kong, parallel with "
        "the Chinese-HK treebank.",
    "ca_ancora":
        "Catalan data from the AnCora corpus.",
    "ceb_gja":
        "UD_Cebuano_GJA is a collection of annotated Cebuano sample sentences "
        "randomly taken from three different sources: community-contributed "
        "samples from the website Tatoeba, a Cebuano grammar book by Bunye & "
        "Yap (1971) and Tanangkinsing's reference grammar on Cebuano (2011). "
        "This project is currently work in progress.",
    "zh_cfl":
        "The Chinese-CFL UD treebank is manually annotated by Keying Li with "
        "minor manual revisions by Herman Leung and John Lee at City "
        "University of Hong Kong, based on essays written by learners of "
        "Mandarin Chinese as a foreign language. The data is in Simplified "
        "Chinese.",
    "zh_gsd":
        "Traditional Chinese Universal Dependencies Treebank annotated and "
        "converted by Google.",
    "zh_gsdsimp":
        "Simplified Chinese Universal Dependencies dataset converted from the "
        "GSD (traditional) dataset with manual corrections.",
    "zh_hk":
        "A Traditional Chinese treebank of film subtitles and of legislative "
        "proceedings of Hong Kong, parallel with the Cantonese-HK treebank.",
    "zh_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "ckt_hse":
        "This data is a manual annotation of the corpus from multimedia "
        "annotated corpus of the Chuklang project, a dialectal corpus of the "
        "Amguema variant of Chukchi.",
    "lzh_kyoto":
        "Classical Chinese Universal Dependencies Treebank annotated and "
        "converted by Institute for Research in Humanities, Kyoto University.",
    "cop_scriptorium":
        "UD Coptic contains manually annotated Sahidic Coptic texts, including"
        " Biblical texts, sermons, letters, and hagiography.",
    "hr_set":
        "The Croatian UD treebank is based on the extension of the SETimes-HR "
        "corpus, the hr500k corpus.",
    "cs_cac":
        "The UD_Czech-CAC treebank is based on the Czech Academic Corpus 2.0 "
        "(CAC; Český akademický korpus; ČAK), created at Charles University in"
        " Prague.",
    "cs_cltt":
        "The UD_Czech-CLTT treebank is based on the Czech Legal Text Treebank "
        "1.0, created at Charles University in Prague.",
    "cs_fictree":
        "FicTree is a treebank of Czech fiction, automatically converted into "
        "the UD format. The treebank was built at Charles University in "
        "Prague.",
    "cs_pdt":
        "The Czech-PDT UD treebank is based on the Prague Dependency Treebank "
        "3.0 (PDT), created at the Charles University in Prague.",
    "cs_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "da_ddt":
        "The Danish UD treebank is a conversion of the Danish Dependency "
        "Treebank.",
    "nl_alpino":
        "This corpus consists of samples from various treebanks annotated at "
        "the University of Groningen using the Alpino annotation tools and "
        "guidelines.",
    "nl_lassysmall":
        "This corpus contains sentences from the Wikipedia section of the "
        "Lassy Small Treebank. Universal Dependency annotation was generated "
        "automatically from the original annotation in Lassy.",
    "en_esl":
        "UD English-ESL / Treebank of Learner English (TLE) contains manual "
        "POS tag and dependency annotations for 5,124 English as a Second "
        "Language (ESL) sentences drawn from the Cambridge Learner Corpus "
        "First Certificate in English (FCE) dataset.",
    "en_ewt":
        "A Gold Standard Universal Dependencies Corpus for English, built over"
        " the source material of the English Web Treebank LDC2012T13 "
        "(https://catalog.ldc.upenn.edu/LDC2012T13).",
    "en_gum":
        "Universal Dependencies syntax annotations from the GUM corpus "
        "(https://corpling.uis.georgetown.edu/gum/).",
    "en_gumreddit":
        "Universal Dependencies syntax annotations from the Reddit portion of "
        "the GUM corpus (https://corpling.uis.georgetown.edu/gum/) ",
    "en_lines":
        "UD English_LinES is the English half of the LinES Parallel Treebank "
        "with the original dependency annotation first automatically converted"
        " into Universal Dependencies and then partially reviewed. Its "
        "contents cover literature, an online manual and Europarl data.",
    "en_atis":
        "UD Atis Treebank is a manually annotated treebank consisting of the "
        "sentences in the Atis (Airline Travel Informations) dataset which "
        "includes the human speech transcriptions of people asking for flight "
        "information on the automated inquiry systems.",
    "en_partut":
        "UD_English-ParTUT is a conversion of a multilingual parallel treebank"
        " developed at the University of Turin, and consisting of a variety of"
        " text genres, including talks, legal texts and Wikipedia articles, "
        "among others.",
    "en_pronouns":
        "UD English-Pronouns is dataset created to make pronoun identification"
        " more accurate and with a more balanced distribution across genders. "
        "The dataset is initially targeting the Independent Genitive pronouns,"
        " 'hers', (independent) 'his', (singular) 'theirs', 'mine', and "
        "(singular) 'yours'.",
    "en_pud":
        "This is the English portion of the Parallel Universal Dependencies "
        "(PUD) treebanks created for the CoNLL 2017 shared task on "
        "Multilingual Parsing from Raw Text to Universal Dependencies "
        "(http://universaldependencies.org/conll17/).",
    "myv_jr":
        "UD Erzya is the original annotation (CoNLL-U) for texts in the Erzya "
        "language, it originally consists of a sample from a number of fiction"
        " authors writing originals in Erzya.",
    "et_edt":
        "UD Estonian is a converted version of the Estonian Dependency "
        "Treebank (EDT), originally annotated in the Constraint Grammar (CG) "
        "annotation scheme, and consisting of genres of fiction, newspaper "
        "texts and scientific texts. The treebank contains 30,972 trees, "
        "437,769 tokens.",
    "et_ewt":
        "UD EWT treebank consists of different genres of new media. The "
        "treebank contains 4,493 trees, 56,399 tokens.",
    "fo_farpahc":
        "UD_Icelandic-FarPaHC is a conversion of the Faroese Parsed Historical"
        " Corpus (FarPaHC) to the Universal Dependencies scheme. The "
        "conversion was done using UDConverter.",
    "fo_oft":
        "This is a treebank of Faroese based on the Faroese Wikipedia.",
    "fi_ftb":
        "FinnTreeBank 1 consists of manually annotated grammatical examples "
        "from VISK. The UD version of FinnTreeBank 1 was converted from a "
        "native annotation model with a script and later manually revised.",
    "fi_ood":
        "Finnish-OOD is an external out-of-domain test set for Finnish-TDT "
        "annotated natively into UD scheme.",
    "fi_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "fi_tdt":
        "UD_Finnish-TDT is based on the Turku Dependency Treebank (TDT), a "
        "broad-coverage dependency treebank of general Finnish covering "
        "numerous genres. The conversion to UD was followed by extensive "
        "manual checks and corrections, and the treebank closely adheres to "
        "the UD guidelines.",
    "fr_fqb":
        "The corpus **UD_French-FQB** is an automatic conversion of the French"
        " QuestionBank v1, a corpus entirely made of questions.",
    "fr_ftb":
        "The Universal Dependency version of the French Treebank (Abeillé et "
        "al., 2003), hereafter UD_French-FTB, is a treebank of sentences from "
        "the newspaper Le Monde, initially manually annotated with "
        "morphological information and phrase-structure and then converted to "
        "the Universal Dependencies annotation scheme.",
    "fr_gsd":
        "The **UD_French-GSD** was converted in 2015 from the content head "
        "version of the universal dependency treebank v2.0 "
        "(https://github.com/ryanmcd/uni-dep-tb). It is updated since 2015 "
        "independently from the previous source.",
    "fr_partut":
        "UD_French-ParTUT is a conversion of a multilingual parallel treebank "
        "developed at the University of Turin, and consisting of a variety of "
        "text genres, including talks, legal texts and Wikipedia articles, "
        "among others.",
    "fr_rhapsodie":
        "A Universal Dependencies corpus for spoken French.",
    "fr_parisstories":
        "Paris Stories is a corpus of oral French collected and transcribed by"
        " Linguistics students from Sorbonne Nouvelle and corrected by "
        "students from the Plurital Master's Degree of Computational "
        "Linguistics ( Inalco, Paris Nanterre, Sorbonne Nouvelle) between 2017"
        " and 2021. It contains monologues and dialogues from speakers living "
        "in the Parisian region.",
    "fr_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "fr_sequoia":
        "UD_French-Sequoia is an automatic conversion of the Sequoia Treebank "
        "corpus French Sequoia corpus.",
    "gl_ctg":
        "The Galician UD treebank is based on the automatic parsing of the "
        "Galician Technical Corpus (http://sli.uvigo.gal/CTG) created at the "
        "University of Vigo by the the TALG NLP research group.",
    "gl_treegal":
        "The Galician-TreeGal is a treebank for Galician developed at LyS "
        "Group (Universidade da Coruña).",
    "de_gsd":
        "The German UD is converted from the content head version of the "
        "universal dependency treebank v2.0 (legacy).",
    "de_hdt":
        "UD German-HDT is a conversion of the Hamburg Dependency Treebank, "
        "created at the University of Hamburg through manual annotation in "
        "conjunction with a standard for morphologically and syntactically "
        "annotating sentences as well as a constraint-based parser.",
    "de_lit":
        "This treebank aims at gathering texts of the German literary history."
        " Currently, it hosts Fragments of the early Romanticism, i.e. "
        "aphorism-like texts mainly dealing with philosophical issues "
        "concerning art, beauty and related topics.",
    "de_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "got_proiel":
        "The UD Gothic treebank is based on the Gothic data from the PROIEL "
        "treebank, and consists of Wulfila's Bible translation.",
    "el_gdt":
        "The Greek UD treebank (UD_Greek-GDT) is derived from the Greek "
        "Dependency Treebank (http://gdt.ilsp.gr), a resource developed and "
        "maintained by researchers at the Institute for Language and Speech "
        "Processing/Athena R.C. (http://www.ilsp.gr).",
    "gub_tudet":
        "UD_Guajajara-TuDeT is a collection of annotated sentences in "
        "Guajajara. Sentences stem from multiple sources such as descriptions "
        "of the language, short stories, dictionaries and translations from "
        "the New Testament. Sentence annotation and documentation by Lorena "
        "Martín Rodríguez and Fabrício Ferraz Gerardi.",
    "gn_oldtudet":
        "UD_Guarani-OldTuDeT is a collection of annotated texts in Old "
        "Guaraní. All known sources in this language are being annotated: "
        "cathesisms, grammars (seventeenth and eighteenth century), sentences "
        "from dictionaries, and other texts. Sentence annotation and "
        "documentation by Fabrício Ferraz Gerardi and Lorena Martín Rodríguez.",
    "he_htb":
        "A Universal Dependencies Corpus for Hebrew.",
    "he_iahltwiki":
        "Publicly available subset of the IAHLT UD Hebrew Treebank's Wikipedia"
        " section (https://www.iahlt.org/)",
    "qfn_fame":
        "UD_Frisian_Dutch-Fame is a selection of 400 sentences from the FAME! "
        "speech corpus by Yilmaz et al. (2016a, 2016b). The treebank is "
        "manually annotated using the UD scheme.",
    "qhe_hiencs":
        "The Hindi-English Code-switching treebank is based on code-switching "
        "tweets of Hindi and English multilingual speakers (mostly Indian) on "
        "Twitter. The treebank is manually annotated using UD sceheme. The "
        "training and evaluations sets were seperately annotated by different "
        "annotators using UD v2 and v1 guidelines respectively. The evaluation"
        " sets are automatically converted from UD v1 to v2.",
    "hi_hdtb":
        "The Hindi UD treebank is based on the Hindi Dependency Treebank "
        "(HDTB), created at IIIT Hyderabad, India.",
    "hi_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "hu_szeged":
        "The Hungarian UD treebank is derived from the Szeged Dependency "
        "Treebank (Vincze et al. 2010).",
    "is_modern":
        "UD_Icelandic-Modern is a conversion of the modern additions to the "
        "Icelandic Parsed Historical Corpus (IcePaHC) to the Universal "
        "Dependencies scheme.",
    "is_icepahc":
        "UD_Icelandic-IcePaHC is a conversion of the Icelandic Parsed "
        "Historical Corpus (IcePaHC) to the Universal Dependencies scheme. The"
        " conversion was done using UDConverter.",
    "is_pud":
        "Icelandic-PUD is the Icelandic part of the Parallel Universal "
        "Dependencies (PUD) treebanks.",
    "id_csui":
        "UD Indonesian-CSUI is a conversion from an Indonesian constituency "
        "treebank in the Penn Treebank format named Kethu that was also a "
        "conversion from a constituency treebank built by Dinakaramani et al. "
        "(2015). We named this treebank Indonesian-CSUI, since all the three "
        "versions of the treebanks were built at Faculty of Computer Science, "
        "Universitas Indonesia.",
    "id_gsd":
        "The Indonesian UD is converted from the content head version of the "
        "universal dependency treebank v2.0 (legacy).",
    "id_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "ga_idt":
        "A Universal Dependencies 4910-sentence treebank for modern Irish.",
    "ga_twittirish":
        "A Universal Dependencies treebank of 866 tweets in modern Irish.",
    "it_isdt":
        "The Italian corpus annotated according to the UD annotation scheme "
        "was obtained by conversion from ISDT (Italian Stanford Dependency "
        "Treebank), released for the dependency parsing shared task of "
        "Evalita-2014 (Bosco et al. 2014).",
    "it_partut":
        "UD_Italian-ParTUT is a conversion of a multilingual parallel treebank"
        " developed at the University of Turin, and consisting of a variety of"
        " text genres, including talks, legal texts and Wikipedia articles, "
        "among others.",
    "it_postwita":
        "PoSTWITA-UD is a collection of Italian tweets annotated in Universal "
        "Dependencies that can be exploited for the training of NLP systems to"
        " enhance their performance on social media texts.",
    "it_markit":
        "It is MarkIT That is New: An Italian Treebank of Marked "
        "Constructions. Teresa Paccosi, Alessio Palmero Aprosio and Sara "
        "Tonelli, To appear in Proceedings of the Eighth Italian Conference on"
        " Computational Linguistics 2022 (CLIC-it 2021)",
    "it_valico":
        "Manually corrected Treebank of Learner Italian drawn from the Valico "
        "corpus and correspondent corrected sentences.",
    "it_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "it_twittiro":
        "TWITTIRÒ-UD is a collection of ironic Italian tweets annotated in "
        "Universal Dependencies. The treebank can be exploited for the "
        "training of NLP systems to enhance their performance on social media "
        "texts, and in particular, for irony detection purposes.",
    "it_vit":
        "The UD_Italian-VIT corpus was obtained by conversion from VIT (Venice"
        " Italian Treebank), developed at the Laboratory of Computational "
        "Linguistics of the Università Ca' Foscari in Venice (Delmonte et al. "
        "2007; Delmonte 2009; "
        "http://rondelmo.it/resource/VIT/Browser-VIT/index.htm).",
    "ja_pudluw":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "ja_bccwjluw":
        "This Universal Dependencies (UD) Japanese treebank is based on the "
        "definition of UD Japanese convention described in the UD "
        "documentation. The original sentences are from `Balanced Corpus of "
        "Contemporary Written Japanese'(BCCWJ).",
    "ja_gsdluw":
        "This Universal Dependencies (UD) Japanese treebank is based on the "
        "definition of UD Japanese convention described in the UD "
        "documentation. The original sentences are from Google UDT 2.0.",
    "ja_bccwj":
        "This Universal Dependencies (UD) Japanese treebank is based on the "
        "definition of UD Japanese convention described in the UD "
        "documentation. The original sentences are from `Balanced Corpus of "
        "Contemporary Written Japanese'(BCCWJ).",
    "ja_gsd":
        "This Universal Dependencies (UD) Japanese treebank is based on the "
        "definition of UD Japanese convention described in the UD "
        "documentation.  The original sentences are from Google UDT 2.0.",
    "ja_modern":
        "This Universal Dependencies (UD) Japanese treebank is based on the "
        "definition of UD Japanese convention described in the UD "
        "documentation. The original sentences are from `Corpus of Historical "
        "Japanese' (CHJ).",
    "ja_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the [CoNLL 2017 shared task on Multilingual Parsing from"
        " Raw Text to Universal "
        "Dependencies](http://universaldependencies.org/conll17/).",
    "jv_csui":
        "UD Javanese-CSUI is a dependency treebank in Javanese, a regional "
        "language in Indonesia with more than 60 million users. The original "
        "sentences were taken from OPUS, especially from the WikiMatrix v1 "
        "corpus. We revised the sentences that contained more Indonesian words"
        " than Javanese words and manually annotated them.",
    "urb_tudet":
        "UD_Kaapor-TuDeT is a collection of annotated sentences in Ka'apor. "
        "The project is a work in progress and the treebank is being updated "
        "on a regular basis.",
    "xnr_kdtb":
        "The Kangri UD Treebank (KDTB) is a part of the Universal Dependency "
        "treebank project.",
    "krl_kkpp":
        "UD Karelian-KKPP is a manually annotated new corpus of Karelian made "
        "in Universal dependencies annotation scheme. The data is collected "
        "from VepKar corpora and consists of mostly modern news texts but also"
        " some stories and educational texts.",
    "kk_ktb":
        "The UD Kazakh treebank is a combination of text from various sources "
        "including Wikipedia, some folk tales, sentences from the UDHR, news "
        "and phrasebook sentences. Sentences IDs include partial document "
        "identifiers.",
    "arr_tudet":
        "UD_Karo-TuDeT is a collection of annotated sentences in Karo. The "
        "sentences stem from the only grammatical description of the language "
        "(Gabas, 1999) and from the sentences in the dictionary by the same "
        "author (Gabas, 2007). Sentence annotation and documentation by "
        "Fabrício Ferraz Gerardi.",
    "kfm_aha":
        "The AHA Khunsari Treebank is a small treebank for contemporary "
        "Khunsari. Its corpus is collected and annotated manually. We have "
        "prepared this treebank based on interviews with Khunsari speakers.",
    "quc_iu":
        "UD Kʼicheʼ-IU is a treebank consisting of sentences from a variety of"
        " text domains but principally dictionary example sentences and "
        "linguistic examples.",
    "koi_uh":
        "This is a Komi-Permyak literary language treebank consisting of "
        "original and translated texts.",
    "kpv_ikdp":
        "This treebank consists of dialectal transcriptions of spoken "
        "Komi-Zyrian. The current texts are short recorded segments from "
        "different areas where the Iźva dialect of Komi language is spoken.",
    "kpv_lattice":
        "UD Komi-Zyrian Lattice is a treebank of written standard Komi-Zyrian.",
    "ko_gsd":
        "The Google Korean Universal Dependency Treebank is first converted "
        "from the Universal Dependency Treebank v2.0 (legacy), and then "
        "enhanced by Chun et al., 2018.",
    "ko_kaist":
        "The KAIST Korean Universal Dependency Treebank is generated by Chun "
        "et al., 2018 from the constituency trees in the KAIST Tree-Tagging "
        "Corpus.",
    "ko_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "kmr_mg":
        "The UD Kurmanji corpus is a corpus of Kurmanji Kurdish. It contains "
        "fiction and encyclopaedic texts in roughly equal measure. It has been"
        " annotated natively in accordance with the UD annotation scheme.",
    "la_ittb":
        "Latin data from the _Index Thomisticus_ Treebank. Data are taken from"
        " the _Index Thomisticus_ corpus by Roberto Busa SJ, which contains "
        "the complete work by Thomas Aquinas (1225–1274; Medieval Latin) and "
        "by 61 other authors related to Thomas.",
    "la_udante":
        "The UDante treebank is based on the Latin texts of Dante Alighieri, "
        "taken from the DanteSearch corpus, originally created at the "
        "University of Pisa, Italy. It is a treebank of Latin language, more "
        "precisely of literary Medieval Latin (XIVth century).",
    "la_llct":
        "This Universal Dependencies version of the LLCT (Late Latin Charter "
        "Treebank) consists of an automated conversion of the LLCT2 treebank "
        "from the Latin Dependency Treebank (LDT) format into the Universal "
        "Dependencies standard.",
    "la_perseus":
        "This Universal Dependencies Latin Treebank consists of an automatic "
        "conversion of a selection of passages from the Ancient Greek and "
        "Latin Dependency Treebank 2.1",
    "la_proiel":
        "The Latin PROIEL treebank is based on the Latin data from the PROIEL "
        "treebank, and contains most of the Vulgate New Testament translations"
        " plus selections from Caesar's Gallic War, Cicero's Letters to "
        "Atticus, Palladius' Opus Agriculturae and the first book of Cicero's "
        "De officiis.",
    "lv_lvtb":
        "Latvian UD Treebank is based on Latvian Treebank (LVTB), being "
        "created at University of Latvia, Institute of Mathematics and "
        "Computer Science, Artificial Intelligence Laboratory.",
    "lij_glt":
        "The Genoese Ligurian Treebank is a small, manually annotated "
        "collection of contemporary Ligurian prose. The focus of the treebank "
        "is written Genoese, the koiné variety of Ligurian which is associated"
        " with today's literary, journalistic and academic ligurophone sphere.",
    "lt_alksnis":
        "The Lithuanian dependency treebank ALKSNIS v3.0 (Vytautas Magnus "
        "University).",
    "lt_hse":
        "Lithuanian treebank annotated manually (dependencies) using the "
        "Morphological Annotator by CCL, Vytautas Magnus University "
        "(http://tekstynas.vdu.lt/) and manual disambiguation. A pilot version"
        " which includes news and an essay by Tomas Venclova is available "
        "here.",
    "olo_kkpp":
        "UD Livvi-KKPP is a manually annotated new corpus of Livvi-Karelian "
        "made directly in the Universal dependencies annotation scheme. The "
        "data is collected from VepKar corpora and consists of mostly modern "
        "news texts but also some stories and educational texts.",
    "nds_lsdc":
        "The UD Low Saxon LSDC dataset consists of sentences in 18 Low Saxon "
        "dialects from both Germany and the Netherlands. These sentences are "
        "(or are to become) part of the LSDC dataset and represent the "
        "language from the 19th and early 20th century in genres such as short"
        " stories, novels, speeches, letters and fairytales.",
    "mt_mudt":
        "MUDT (Maltese Universal Dependencies Treebank) is a manually "
        "annotated treebank of Maltese, a Semitic language of Malta descended "
        "from North African Arabic with a significant amount of Italo-Romance "
        "influence. MUDT was designed as a balanced corpus with four major "
        "genres (see Splitting below) represented roughly equally.",
    "gv_cadhan":
        "This is the Cadhan Aonair UD treebank for Manx Gaelic, created by "
        "Kevin Scannell.",
    "mr_ufal":
        "UD Marathi is a manually annotated treebank consisting primarily of "
        "stories from Wikisource, and parts of an article on Wikipedia.",
    "gun_dooley":
        "UD Mbya_Guarani-Dooley is a corpus of narratives written in Mbyá "
        "Guaraní (Tupian) in Brazil, and collected by Robert Dooley. Due to "
        "copyright restrictions, the corpus that is distributed as part of UD "
        "only contains the annotation (tags, features, relations) while the "
        "FORM and LEMMA columns are empty.",
    "gun_thomas":
        "UD Mbya_Guarani-Thomas is a corpus of Mbyá Guaraní (Tupian) texts "
        "collected by Guillaume Thomas. The current version of the corpus "
        "consists of three speeches by Paulina Kerechu Núñez Romero, a Mbyá "
        "Guaraní speaker from Ytu, Caazapá Department, Paraguay.",
    "mdf_jr":
        "Erme Universal Dependencies annotated texts Moksha are the origin of "
        "UD_Moksha-JR with annotation (CoNLL-U) for texts in the Moksha "
        "language, it originally consists of a sample from a number of fiction"
        " authors writing originals in Moksha.",
    "myu_tudet":
        "UD_Munduruku-TuDeT is a collection of annotated sentences in "
        "Mundurukú. Together with UD_Akuntsu-TuDeT and UD_Tupinamba-TuDeT, "
        "UD_Munduruku-TuDeT is part of the TuLaR project.",
    "pcm_nsc":
        "A Universal Dependencies corpus for spoken Naija (Nigerian Pidgin).",
    "nyq_aha":
        "The AHA Nayini Treebank is a small treebank for contemporary Nayini. "
        "Its corpus is collected and annotated manually. We have prepared this"
        " treebank based on interviews with Nayini speakers.",
    "sme_giella":
        "This is a North Sámi treebank based on a manually disambiguated and "
        "function-labelled gold-standard corpus of North Sámi produced by the "
        "Giellatekno team at UiT Norgga árktalaš universitehta.",
    "no_bokmaal":
        "The Norwegian UD treebank is based on the Bokmål section of the "
        "Norwegian Dependency Treebank (NDT), which is a syntactic treebank of"
        " Norwegian. NDT has been automatically converted to the UD scheme by "
        "Lilja Øvrelid at the University of Oslo.",
    "no_nynorsk":
        "The Norwegian UD treebank is based on the Nynorsk section of the "
        "Norwegian Dependency Treebank (NDT), which is a syntactic treebank of"
        " Norwegian.  NDT has been automatically converted to the UD scheme by"
        " Lilja Øvrelid at the University of Oslo.",
    "no_nynorsklia":
        "This Norwegian treebank is based on the LIA treebank of transcribed "
        "spoken Norwegian dialects. The treebank has been automatically "
        "converted to the UD scheme by Lilja Øvrelid at the University of "
        "Oslo.",
    "cu_proiel":
        "The Old Church Slavonic (OCS) UD treebank is based on the Old Church "
        "Slavonic data from the PROIEL treebank and contains the text of the "
        "Codex Marianus New Testament translation.",
    "fro_srcmf":
        "UD_Old_French-SRCMF is a conversion of (part of) the SRCMF corpus "
        "(Syntactic Reference Corpus of Medieval French srcmf.org).",
    "orv_birchbark":
        "UD Old_East_Slavic-Birchbark is based on the RNC Corpus of Birchbark "
        "Letters and includes documents written in 1025-1500 in an East Slavic"
        " vernacular (letters, household and business records, records for "
        "church services, spell against diseases, and other short "
        "inscriptions). The treebank is manually syntactically annotated in "
        "the UD 2.0 scheme, morphological and lexical annotation is a "
        "conversion of the original RNC annotation.",
    "orv_rnc":
        "`UD_Old_Russian-RNC` is a sample of the Middle Russian corpus "
        "(1300-1700), a part of the Russian National Corpus. The data were "
        "originally annotated according to the RNC and extended UD-Russian "
        "morphological schemas and UD 2.4 dependency schema.",
    "orv_torot":
        "UD_Old_Russian-TOROT is a conversion of a selection of the Old East "
        "Slavonic and Middle Russian data in the Tromsø Old Russian and OCS "
        "Treebank (TOROT), which was originally annotated in PROIEL dependency"
        " format.",
    "otk_tonqq":
        "`UD_Old_Turkish-Tonqq` is an Old Turkish treebank built upon Turkic "
        "script texts or sentences that are trivially convertible.",
    "fa_perdt":
        "The Persian Universal Dependency Treebank (PerUDT) is the result of "
        "automatic coversion of Persian Dependency Treebank (PerDT) with "
        "extensive manual corrections. Please refer to the follwoing work, if "
        "you use this data: Mohammad Sadegh Rasooli, Pegah Safari, Amirsaeid "
        "Moloodi, and Alireza Nourian. 'The Persian Dependency Treebank Made "
        "Universal'. 2020 (to appear).",
    "fa_seraji":
        "The Persian Universal Dependency Treebank (Persian UD) is based on "
        "Uppsala Persian Dependency Treebank (UPDT). The conversion of the "
        "UPDT to the Universal Dependencies was performed semi-automatically "
        "with extensive manual checks and corrections.",
    "pl_lfg":
        "The LFG Enhanced UD treebank of Polish is based on a corpus of LFG "
        "(Lexical Functional Grammar) syntactic structures generated by an LFG"
        " grammar of Polish, POLFIE, and manually disambiguated by human "
        "annotators.",
    "pl_pdb":
        "The Polish PDB-UD treebank is based on the Polish Dependency Bank 2.0"
        " (PDB 2.0), created at the Institute of Computer Science, Polish "
        "Academy of Sciences in Warsaw. The PDB-UD treebank is an extended and"
        " corrected version of the Polish SZ-UD treebank (the release 1.2 to "
        "2.3).",
    "pl_pud":
        "This is the Polish portion of the Parallel Universal Dependencies "
        "(PUD) treebanks, created at the Institute of Computer Science, Polish"
        " Academy of Sciences in Warsaw.Re",
    "pt_bosque":
        "This Universal Dependencies (UD) Portuguese treebank is based on the "
        "Constraint Grammar converted version of the Bosque, which is part of "
        "the Floresta Sintá(c)tica treebank. It contains both European "
        "(CETEMPúblico) and Brazilian (CETENFolha) variants.",
    "pt_gsd":
        "The Brazilian Portuguese UD is converted from the Google Universal "
        "Dependency Treebank v2.0 (legacy).",
    "pt_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "ro_art":
        "The UD treebank ArT is a treebank of the Aromanian dialect of the "
        "Romanian language in UD format.",
    "ro_nonstandard":
        "The Romanian Non-standard UD treebank (called UAIC-RoDia) is based on"
        " UAIC-RoDia Treebank. UAIC-RoDia = ISLRN 156-635-615-024-0",
    "ro_rrt":
        "The Romanian UD treebank (called RoRefTrees) (Barbu Mititelu et al., "
        "2016) is the reference treebank in UD format for standard Romanian.",
    "ro_simonero":
        "SiMoNERo is a medical corpus of contemporary Romanian.",
    "ru_gsd":
        "Russian Universal Dependencies Treebank annotated and converted by "
        "Google.",
    "ru_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "ru_syntagrus":
        "Russian data from the SynTagRus corpus.",
    "ru_taiga":
        "Universal Dependencies treebank is based on data samples extracted "
        "from Taiga Corpus and MorphoRuEval-2017 and GramEval-2020 shared "
        "tasks collections.",
    "sa_ufal":
        "A small Sanskrit treebank of sentences from Pañcatantra, an ancient "
        "Indian collection of interrelated fables by Vishnu Sharma.",
    "sa_vedic":
        "The Treebank of Vedic Sanskrit contains 4,000 sentences with 27,000 "
        "words chosen from metrical and prose passages of the Ṛgveda (RV), the"
        " Śaunaka recension of the Atharvaveda (ŚS), the Maitrāyaṇīsaṃhitā "
        "(MS), and the Aitareya- (AB) and Śatapatha-Brāhmaṇas (ŚB). Lexical "
        "and morpho-syntactic information has been generated using a tagging "
        "software and manually validated. POS tags have been induced "
        "automatically from the morpho-sytactic information of each word.",
    "gd_arcosg":
        "A treebank of Scottish Gaelic based on the Annotated Reference Corpus"
        " Of Scottish Gaelic (ARCOSG).",
    "sr_set":
        "The Serbian UD treebank is based on the "
        "[SETimes-SR](http://hdl.handle.net/11356/1200) corpus and additional "
        "news documents from the Serbian web.",
    "sms_giellagas":
        "The UD Skolt Sami Giellagas treebank is based almost entirely on "
        "spoken Skolt Sami corpora.",
    "sk_snk":
        "The Slovak UD treebank is based on data originally annotated as part "
        "of the Slovak National Corpus, following the annotation style of the "
        "Prague Dependency Treebank.",
    "sl_ssj":
        "The Slovenian UD Treebank is a rule-based conversion of the ssj500k "
        "treebank, the largest collection of manually syntactically annotated "
        "data in Slovenian, originally annotated in the JOS annotation scheme.",
    "sl_sst":
        "The Spoken Slovenian UD Treebank (SST) is the first syntactically "
        "annotated corpus of spoken Slovenian, based on a sample of the "
        "reference GOS corpus, a collection of transcribed audio recordings of"
        " monologic, dialogic and multi-party spontaneous speech in different "
        "everyday situations.",
    "soj_aha":
        "The AHA Soi Treebank is a small treebank for contemporary Soi. Its "
        "corpus is collected and annotated manually. We have prepared this "
        "treebank based on interviews with Soi speakers.",
    "ajp_madar":
        "The South_Levantine_Arabic-MADAR treebank consists of 100 "
        "manually-annotated sentences taken from the "
        "[MADAR](https://camel.abudhabi.nyu.edu/madar/) (Multi-Arabic Dialect "
        "Applications and Resources) project. ",
    "es_ancora":
        "Spanish data from the AnCora corpus.",
    "es_gsd":
        "The Spanish UD is converted from the content head version of the "
        "universal dependency treebank v2.0 (legacy).",
    "es_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the [CoNLL 2017 shared task on Multilingual Parsing from"
        " Raw Text to Universal "
        "Dependencies](http://universaldependencies.org/conll17/).",
    "swl_sslc":
        "The Universal Dependencies treebank for Swedish Sign Language (ISO "
        "639-3: swl) is derived from the Swedish Sign Language Corpus (SSLC) "
        "from the department of linguistics, Stockholm University.",
    "sv_lines":
        "UD Swedish_LinES is the Swedish half of the LinES Parallel Treebank "
        "with UD annotations. All segments are translations from English and "
        "the sources cover literary genres, online manuals and Europarl data.",
    "sv_pud":
        "Swedish-PUD is the Swedish part of the Parallel Universal "
        "Dependencies (PUD) treebanks.",
    "sv_talbanken":
        "The Swedish-Talbanken treebank is based on Talbanken, a treebank "
        "developed at Lund University in the 1970s.",
    "gsw_uzh":
        "_UD_Swiss_German-UZH_ is a tiny manually annotated treebank of 100 "
        "sentences in different Swiss German dialects and a variety of text "
        "genres.",
    "tl_trg":
        "UD_Tagalog-TRG is a UD treebank manually annotated using sentences "
        "from a grammar book.",
    "tl_ugnayan":
        "Ugnayan is a manually annotated Tagalog treebank currently composed "
        "of educational fiction and nonfiction text. The treebank is under "
        "development at the University of the Philippines.",
    "ta_mwtt":
        "MWTT - Modern Written Tamil Treebank has sentences taken primarily "
        "from a text called 'A Grammar of Modern Tamil' by Thomas Lehmann "
        "(1993). This initial release has 536 sentences of various lengths, "
        "and all of these are added as the test set.",
    "ta_ttb":
        "The UD Tamil treebank is based on the Tamil Dependency Treebank "
        "created at the Charles University in Prague by Loganathan Ramasamy.",
    "te_mtg":
        "The Telugu UD treebank is created in UD based on manual annotations "
        "of sentences from a grammar book.",
    "th_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "tpn_tudet":
        "UD_Tupinamba-TuDeT is a collection of annotated texts in Tupi(nambá)."
        " Together with UD_Akuntsu-TuDeT and UD_Munduruku-TuDeT, "
        "UD_Tupinamba-TuDeT is part of the TuLaR. The treebank is ongoing work"
        " and is constantly being updated.",
    "qtd_sagt":
        "UD Turkish-German SAGT is a Turkish-German code-switching treebank "
        "that is developed as part of the SAGT project.",
    "tr_atis":
        "This treebank is a translation of English ATIS (Airline Travel "
        "Information System) corpus (see References). It consists of 5432 "
        "sentences.",
    "tr_tourism":
        "Turkish Tourism is a domain specific treebank consisting of 19,750 "
        "manually annotated sentences and 92,200 tokens. These sentences were "
        "taken from the original customer reviews of a tourism company.",
    "tr_kenet":
        "Turkish-Kenet UD Treebank is the biggest treebank of Turkish. It "
        "consists of 18,700 manually annotated sentences and 178,700 tokens. "
        "Its corpus consists of dictionary examples.",
    "tr_penn":
        "Turkish version of the Penn Treebank. It consists of a total of 9,560"
        " manually annotated sentences and 87,367 tokens. (It only includes "
        "sentences up to 15 words long.)",
    "tr_framenet":
        "Turkish FrameNet consists of 2,700 manually annotated example "
        "sentences and 19,221 tokens. Its data consists of the sentences taken"
        " from the Turkish FrameNet Project. The annotated sentences can be "
        "filtered according to the semantic frame category of the root of the "
        "sentence.",
    "tr_boun":
        "The largest Turkish dependency treebank annotated in UD style. "
        "Created by the members of "
        "[TABILAB](http://http://tabilab.cmpe.boun.edu.tr/) from Boğaziçi "
        "University.",
    "tr_gb":
        "This is a treebank annotating example sentences from a comprehensive "
        "grammar book of Turkish.",
    "tr_imst":
        "The UD Turkish Treebank, also called the IMST-UD Treebank, is a "
        "semi-automatic conversion of the IMST Treebank (Sulubacak et al., "
        "2016).",
    "tr_pud":
        "This is a part of the Parallel Universal Dependencies (PUD) treebanks"
        " created for the CoNLL 2017 shared task on Multilingual Parsing from "
        "Raw Text to Universal Dependencies.",
    "uk_iu":
        "Gold standard Universal Dependencies corpus for Ukrainian, developed "
        "for UD originally, by Institute for Ukrainian, NGO. [українською]",
    "hsb_ufal":
        "A small treebank of Upper Sorbian based mostly on Wikipedia.",
    "ur_udtb":
        "The Urdu Universal Dependency Treebank was automatically converted "
        "from Urdu Dependency Treebank (UDTB) which is part of an ongoing "
        "effort of creating multi-layered treebanks for Hindi and Urdu.",
    "ug_udt":
        "The Uyghur UD treebank is based on the Uyghur Dependency Treebank "
        "(UDT), created at the Xinjiang University in Ürümqi, China.",
    "vi_vtb":
        "The Vietnamese UD treebank is a conversion of the constituent "
        "treebank created in the VLSP project (https://vlsp.hpda.vn/).",
    "wbp_ufal":
        "A small treebank of grammatical examples in Warlpiri, taken from "
        "linguistic literature.",
    "cy_ccg":
        "UD Welsh-CCG (Corpws Cystrawennol y Gymraeg) is a treebank of Welsh, "
        "annotated according to the Universal Dependencies guidelines.",
    "hy_armtdp":
        "A Universal Dependencies treebank for Eastern Armenian developed for "
        "UD originally by the ArmTDP team led by Marat M. Yavrumyan at the "
        "Yerevan State University.",
    "wo_wtb":
        "UD_Wolof-WTB is a natively manual developed treebank for Wolof. "
        "Sentences were collected from encyclopedic, fictional, biographical, "
        "religious texts and news.",
    "sjo_xdt":
        "The UD Xibe Treebank is a corpus of the Xibe language (ISO "
        "639-3: sjo) containing manually annotated syntactic trees under the "
        "Universal Dependencies. Sentences come from three sources: grammar "
        "book examples, newspaper (Cabcal News) and Xibe textbooks.",
    "sah_yktdt":
        "UD_Yakut-YKTDT is a collection Yakut ([Sakha]) sentences "
        "(https://glottolog.org/resource/languoid/id/yaku1245). The project is "
        "work-in-progress and the treebank is being updated on a regular basis",
    "yo_ytb":
        "Parts of the Yoruba Bible and of the Yoruba edition of Wikipedia, "
        "hand-annotated natively in Universal Dependencies.",
    "ess_sli":
        "UD_Yupik-SLI is a treebank of St. Lawrence Island Yupik (ISO 639-3: "
        "ess) that has been manually annotated at the morpheme level, based on "
        "a finite-state morphological analyzer by Chen et al., 2020. The "
        "word-level annotation, merging multiword expressions, is provided in "
        "not-to-release/ess_sli-ud-test.merged.conllu. More information about "
        "the treebank can be found in our publication (AmericasNLP, 2021).",
}

UD_FILEPATHS = {
    "af_afribooms": {
        "train": "UD_Afrikaans-AfriBooms/r2.10/af_afribooms-ud-train.conllu",
        "dev": "UD_Afrikaans-AfriBooms/r2.10/af_afribooms-ud-dev.conllu",
        "test": "UD_Afrikaans-AfriBooms/r2.10/af_afribooms-ud-test.conllu",
    },
    "akk_pisandub": {
        "test": "UD_Akkadian-PISANDUB/r2.10/akk_pisandub-ud-test.conllu",
    },
    "akk_riao": {
        "test": "UD_Akkadian-RIAO/r2.10/akk_riao-ud-test.conllu",
    },
    "aqz_tudet": {
        "test": "UD_Akuntsu-TuDeT/r2.10/aqz_tudet-ud-test.conllu",
    },
    "sq_tsa": {
        "test": "UD_Albanian-TSA/r2.10/sq_tsa-ud-test.conllu",
    },
    "am_att": {
        "test": "UD_Amharic-ATT/r2.10/am_att-ud-test.conllu",
    },
    "grc_perseus": {
        "train": "UD_Ancient_Greek-Perseus/r2.10/grc_perseus-ud-train.conllu",
        "dev": "UD_Ancient_Greek-Perseus/r2.10/grc_perseus-ud-dev.conllu",
        "test": "UD_Ancient_Greek-Perseus/r2.10/grc_perseus-ud-test.conllu",
    },
    "grc_proiel": {
        "train": "UD_Ancient_Greek-PROIEL/r2.10/grc_proiel-ud-train.conllu",
        "dev": "UD_Ancient_Greek-PROIEL/r2.10/grc_proiel-ud-dev.conllu",
        "test": "UD_Ancient_Greek-PROIEL/r2.10/grc_proiel-ud-test.conllu",
    },
    "apu_ufpa": {
        "test": "UD_Apurina-UFPA/r2.10/apu_ufpa-ud-test.conllu",
    },
    "ar_nyuad": {
        "train": "UD_Arabic-NYUAD/r2.10/ar_nyuad-ud-train.conllu",
        "dev": "UD_Arabic-NYUAD/r2.10/ar_nyuad-ud-dev.conllu",
        "test": "UD_Arabic-NYUAD/r2.10/ar_nyuad-ud-test.conllu",
    },
    "hbo_ptnk": {
        "train": "UD_Ancient_Hebrew-PTNK/r2.10/hbo_ptnk-ud-train.conllu",
        "dev": "UD_Ancient_Hebrew-PTNK/r2.10/hbo_ptnk-ud-dev.conllu",
        "test": "UD_Ancient_Hebrew-PTNK/r2.10/hbo_ptnk-ud-test.conllu",
    },
    "ar_padt": {
        "train": "UD_Arabic-PADT/r2.10/ar_padt-ud-train.conllu",
        "dev": "UD_Arabic-PADT/r2.10/ar_padt-ud-dev.conllu",
        "test": "UD_Arabic-PADT/r2.10/ar_padt-ud-test.conllu",
    },
    # TODO(tfds) Add Armenian BSUT splits when it will be officially released.
    "ar_pud": {
        "test": "UD_Arabic-PUD/r2.10/ar_pud-ud-test.conllu",
    },
    "hy_armtdp": {
        "train": "UD_Armenian-ArmTDP/r2.10/hy_armtdp-ud-train.conllu",
        "dev": "UD_Armenian-ArmTDP/r2.10/hy_armtdp-ud-dev.conllu",
        "test": "UD_Armenian-ArmTDP/r2.10/hy_armtdp-ud-test.conllu",
    },
    "aii_as": {
        "test": "UD_Assyrian-AS/r2.10/aii_as-ud-test.conllu",
    },
    "bm_crb": {
        "test": "UD_Bambara-CRB/r2.10/bm_crb-ud-test.conllu",
    },
    "eu_bdt": {
        "train": "UD_Basque-BDT/r2.10/eu_bdt-ud-train.conllu",
        "dev": "UD_Basque-BDT/r2.10/eu_bdt-ud-dev.conllu",
        "test": "UD_Basque-BDT/r2.10/eu_bdt-ud-test.conllu",
    },
    "bej_nsc": {
        "test": "UD_Beja-NSC/r2.10/bej_nsc-ud-test.conllu",
    },
    "be_hse": {
        "train": "UD_Belarusian-HSE/r2.10/be_hse-ud-train.conllu",
        "dev": "UD_Belarusian-HSE/r2.10/be_hse-ud-dev.conllu",
        "test": "UD_Belarusian-HSE/r2.10/be_hse-ud-test.conllu",
    },
    "bn_bru": {
        "test": "UD_Bengali-BRU/r2.10/bn_bru-ud-test.conllu",
    },
    "bho_bhtb": {
        "test": "UD_Bhojpuri-BHTB/r2.10/bho_bhtb-ud-test.conllu",
    },
    "br_keb": {
        "test": "UD_Breton-KEB/r2.10/br_keb-ud-test.conllu",
    },
    "bg_btb": {
        "train": "UD_Bulgarian-BTB/r2.10/bg_btb-ud-train.conllu",
        "dev": "UD_Bulgarian-BTB/r2.10/bg_btb-ud-dev.conllu",
        "test": "UD_Bulgarian-BTB/r2.10/bg_btb-ud-test.conllu",
    },
    "bxr_bdt": {
        "train": "UD_Buryat-BDT/r2.10/bxr_bdt-ud-train.conllu",
        "test": "UD_Buryat-BDT/r2.10/bxr_bdt-ud-test.conllu",
    },
    "yue_hk": {
        "test": "UD_Cantonese-HK/r2.10/yue_hk-ud-test.conllu",
    },
    "ca_ancora": {
        "train": "UD_Catalan-AnCora/r2.10/ca_ancora-ud-train.conllu",
        "dev": "UD_Catalan-AnCora/r2.10/ca_ancora-ud-dev.conllu",
        "test": "UD_Catalan-AnCora/r2.10/ca_ancora-ud-test.conllu",
    },
    "ceb_gja": {
        "test": "UD_Cebuano-GJA/r2.10/ceb_gja-ud-test.conllu",
    },
    "zh_cfl": {
        "test": "UD_Chinese-CFL/r2.10/zh_cfl-ud-test.conllu",
    },
    "zh_gsd": {
        "train": "UD_Chinese-GSD/r2.10/zh_gsd-ud-train.conllu",
        "dev": "UD_Chinese-GSD/r2.10/zh_gsd-ud-dev.conllu",
        "test": "UD_Chinese-GSD/r2.10/zh_gsd-ud-test.conllu",
    },
    "zh_gsdsimp": {
        "train": "UD_Chinese-GSDSimp/r2.10/zh_gsdsimp-ud-train.conllu",
        "dev": "UD_Chinese-GSDSimp/r2.10/zh_gsdsimp-ud-dev.conllu",
        "test": "UD_Chinese-GSDSimp/r2.10/zh_gsdsimp-ud-test.conllu",
    },
    "zh_hk": {
        "test": "UD_Chinese-HK/r2.10/zh_hk-ud-test.conllu",
    },
    "zh_pud": {
        "test": "UD_Chinese-PUD/r2.10/zh_pud-ud-test.conllu",
    },
    "ckt_hse": {
        "test": "UD_Chukchi-HSE/r2.10/ckt_hse-ud-test.conllu",
    },
    "lzh_kyoto": {
        "train": "UD_Classical_Chinese-Kyoto/r2.10/lzh_kyoto-ud-train.conllu",
        "dev": "UD_Classical_Chinese-Kyoto/r2.10/lzh_kyoto-ud-dev.conllu",
        "test": "UD_Classical_Chinese-Kyoto/r2.10/lzh_kyoto-ud-test.conllu",
    },
    "cop_scriptorium": {
        "train": "UD_Coptic-Scriptorium/r2.10/cop_scriptorium-ud-train.conllu",
        "dev": "UD_Coptic-Scriptorium/r2.10/cop_scriptorium-ud-dev.conllu",
        "test": "UD_Coptic-Scriptorium/r2.10/cop_scriptorium-ud-test.conllu",
    },
    "hr_set": {
        "train": "UD_Croatian-SET/r2.10/hr_set-ud-train.conllu",
        "dev": "UD_Croatian-SET/r2.10/hr_set-ud-dev.conllu",
        "test": "UD_Croatian-SET/r2.10/hr_set-ud-test.conllu",
    },
    "cs_cac": {
        "train": "UD_Czech-CAC/r2.10/cs_cac-ud-train.conllu",
        "dev": "UD_Czech-CAC/r2.10/cs_cac-ud-dev.conllu",
        "test": "UD_Czech-CAC/r2.10/cs_cac-ud-test.conllu",
    },
    "cs_cltt": {
        "train": "UD_Czech-CLTT/r2.10/cs_cltt-ud-train.conllu",
        "dev": "UD_Czech-CLTT/r2.10/cs_cltt-ud-dev.conllu",
        "test": "UD_Czech-CLTT/r2.10/cs_cltt-ud-test.conllu",
    },
    "cs_fictree": {
        "train": "UD_Czech-FicTree/r2.10/cs_fictree-ud-train.conllu",
        "dev": "UD_Czech-FicTree/r2.10/cs_fictree-ud-dev.conllu",
        "test": "UD_Czech-FicTree/r2.10/cs_fictree-ud-test.conllu",
    },
    "cs_pdt": {
        "train": [
            "UD_Czech-PDT/r2.10/cs_pdt-ud-train-l.conllu",
            "UD_Czech-PDT/r2.10/cs_pdt-ud-train-m.conllu",
            "UD_Czech-PDT/r2.10/cs_pdt-ud-train-c.conllu",
            "UD_Czech-PDT/r2.10/cs_pdt-ud-train-v.conllu",
        ],
        "dev": "UD_Czech-PDT/r2.10/cs_pdt-ud-dev.conllu",
        "test": "UD_Czech-PDT/r2.10/cs_pdt-ud-test.conllu",
    },
    "cs_pud": {
        "test": "UD_Czech-PUD/r2.10/cs_pud-ud-test.conllu",
    },
    "da_ddt": {
        "train": "UD_Danish-DDT/r2.10/da_ddt-ud-train.conllu",
        "dev": "UD_Danish-DDT/r2.10/da_ddt-ud-dev.conllu",
        "test": "UD_Danish-DDT/r2.10/da_ddt-ud-test.conllu",
    },
    "nl_alpino": {
        "train": "UD_Dutch-Alpino/r2.10/nl_alpino-ud-train.conllu",
        "dev": "UD_Dutch-Alpino/r2.10/nl_alpino-ud-dev.conllu",
        "test": "UD_Dutch-Alpino/r2.10/nl_alpino-ud-test.conllu",
    },
    "nl_lassysmall": {
        "train": "UD_Dutch-LassySmall/r2.10/nl_lassysmall-ud-train.conllu",
        "dev": "UD_Dutch-LassySmall/r2.10/nl_lassysmall-ud-dev.conllu",
        "test": "UD_Dutch-LassySmall/r2.10/nl_lassysmall-ud-test.conllu",
    },
    "en_atis": {
        "train": "UD_English-Atis/r2.10/en_atis-ud-train.conllu",
        "dev": "UD_English-Atis/r2.10/en_atis-ud-dev.conllu",
        "test": "UD_English-Atis/r2.10/en_atis-ud-test.conllu",
    },
    "en_esl": {
        "train": "UD_English-ESL/r2.10/en_esl-ud-train.conllu",
        "dev": "UD_English-ESL/r2.10/en_esl-ud-dev.conllu",
        "test": "UD_English-ESL/r2.10/en_esl-ud-test.conllu",
    },
    "en_ewt": {
        "train": "UD_English-EWT/r2.10/en_ewt-ud-train.conllu",
        "dev": "UD_English-EWT/r2.10/en_ewt-ud-dev.conllu",
        "test": "UD_English-EWT/r2.10/en_ewt-ud-test.conllu",
    },
    "en_gum": {
        "train": "UD_English-GUM/r2.10/en_gum-ud-train.conllu",
        "dev": "UD_English-GUM/r2.10/en_gum-ud-dev.conllu",
        "test": "UD_English-GUM/r2.10/en_gum-ud-test.conllu",
    },
    "en_gumreddit": {
        "train": "UD_English-GUMReddit/r2.10/en_gumreddit-ud-train.conllu",
        "dev": "UD_English-GUMReddit/r2.10/en_gumreddit-ud-dev.conllu",
        "test": "UD_English-GUMReddit/r2.10/en_gumreddit-ud-test.conllu",
    },
    "en_lines": {
        "train": "UD_English-LinES/r2.10/en_lines-ud-train.conllu",
        "dev": "UD_English-LinES/r2.10/en_lines-ud-dev.conllu",
        "test": "UD_English-LinES/r2.10/en_lines-ud-test.conllu",
    },
    "en_partut": {
        "train": "UD_English-ParTUT/r2.10/en_partut-ud-train.conllu",
        "dev": "UD_English-ParTUT/r2.10/en_partut-ud-dev.conllu",
        "test": "UD_English-ParTUT/r2.10/en_partut-ud-test.conllu",
    },
    "en_pronouns": {
        "test": "UD_English-Pronouns/r2.10/en_pronouns-ud-test.conllu",
    },
    "en_pud": {
        "test": "UD_English-PUD/r2.10/en_pud-ud-test.conllu",
    },
    "myv_jr": {
        "test": "UD_Erzya-JR/r2.10/myv_jr-ud-test.conllu",
    },
    "et_edt": {
        "train": "UD_Estonian-EDT/r2.10/et_edt-ud-train.conllu",
        "dev": "UD_Estonian-EDT/r2.10/et_edt-ud-dev.conllu",
        "test": "UD_Estonian-EDT/r2.10/et_edt-ud-test.conllu",
    },
    "et_ewt": {
        "train": "UD_Estonian-EWT/r2.10/et_ewt-ud-train.conllu",
        "dev": "UD_Estonian-EWT/r2.10/et_ewt-ud-dev.conllu",
        "test": "UD_Estonian-EWT/r2.10/et_ewt-ud-test.conllu",
    },
    "fo_farpahc": {
        "train": "UD_Faroese-FarPaHC/r2.10/fo_farpahc-ud-train.conllu",
        "dev": "UD_Faroese-FarPaHC/r2.10/fo_farpahc-ud-dev.conllu",
        "test": "UD_Faroese-FarPaHC/r2.10/fo_farpahc-ud-test.conllu",
    },
    "fo_oft": {
        "test": "UD_Faroese-OFT/r2.10/fo_oft-ud-test.conllu",
    },
    "fi_ftb": {
        "train": "UD_Finnish-FTB/r2.10/fi_ftb-ud-train.conllu",
        "dev": "UD_Finnish-FTB/r2.10/fi_ftb-ud-dev.conllu",
        "test": "UD_Finnish-FTB/r2.10/fi_ftb-ud-test.conllu",
    },
    "fi_ood": {
        "test": "UD_Finnish-OOD/r2.10/fi_ood-ud-test.conllu",
    },
    "fi_pud": {
        "test": "UD_Finnish-PUD/r2.10/fi_pud-ud-test.conllu",
    },
    "fi_tdt": {
        "train": "UD_Finnish-TDT/r2.10/fi_tdt-ud-train.conllu",
        "dev": "UD_Finnish-TDT/r2.10/fi_tdt-ud-dev.conllu",
        "test": "UD_Finnish-TDT/r2.10/fi_tdt-ud-test.conllu",
    },
    "fr_parisstories": {
        "train": "UD_French-ParisStories/r2.10/fr_parisstories-ud-train.conllu",
        "test": "UD_French-ParisStories/r2.10/fr_parisstories-ud-test.conllu",
    },
    "fr_fqb": {
        "test": "UD_French-FQB/r2.10/fr_fqb-ud-test.conllu",
    },
    "fr_rhapsodie": {
        "train": "UD_French-Rhapsodie/r2.10/fr_rhapsodie-ud-train.conllu",
        "dev": "UD_French-Rhapsodie/r2.10/fr_rhapsodie-ud-dev.conllu",
        "test": "UD_French-Rhapsodie/r2.10/fr_rhapsodie-ud-test.conllu",
    },
    "fr_ftb": {
        "train": "UD_French-FTB/r2.10/fr_ftb-ud-train.conllu",
        "dev": "UD_French-FTB/r2.10/fr_ftb-ud-dev.conllu",
        "test": "UD_French-FTB/r2.10/fr_ftb-ud-test.conllu",
    },
    "fr_gsd": {
        "train": "UD_French-GSD/r2.10/fr_gsd-ud-train.conllu",
        "dev": "UD_French-GSD/r2.10/fr_gsd-ud-dev.conllu",
        "test": "UD_French-GSD/r2.10/fr_gsd-ud-test.conllu",
    },
    "fr_partut": {
        "train": "UD_French-ParTUT/r2.10/fr_partut-ud-train.conllu",
        "dev": "UD_French-ParTUT/r2.10/fr_partut-ud-dev.conllu",
        "test": "UD_French-ParTUT/r2.10/fr_partut-ud-test.conllu",
    },
    "fr_pud": {
        "test": "UD_French-PUD/r2.10/fr_pud-ud-test.conllu",
    },
    "fr_sequoia": {
        "train": "UD_French-Sequoia/r2.10/fr_sequoia-ud-train.conllu",
        "dev": "UD_French-Sequoia/r2.10/fr_sequoia-ud-dev.conllu",
        "test": "UD_French-Sequoia/r2.10/fr_sequoia-ud-test.conllu",
    },
    "qfn_fame": {
        "test": "UD_Frisian_Dutch-Fame/r2.10/qfn_fame-ud-test.conllu",
    },
    "gl_ctg": {
        "train": "UD_Galician-CTG/r2.10/gl_ctg-ud-train.conllu",
        "dev": "UD_Galician-CTG/r2.10/gl_ctg-ud-dev.conllu",
        "test": "UD_Galician-CTG/r2.10/gl_ctg-ud-test.conllu",
    },
    "gl_treegal": {
        "train": "UD_Galician-TreeGal/r2.10/gl_treegal-ud-train.conllu",
        "test": "UD_Galician-TreeGal/r2.10/gl_treegal-ud-test.conllu",
    },
    "de_gsd": {
        "train": "UD_German-GSD/r2.10/de_gsd-ud-train.conllu",
        "dev": "UD_German-GSD/r2.10/de_gsd-ud-dev.conllu",
        "test": "UD_German-GSD/r2.10/de_gsd-ud-test.conllu",
    },
    "de_hdt": {
        "train": [
            "UD_German-HDT/r2.10/de_hdt-ud-train-a-1.conllu",
            "UD_German-HDT/r2.10/de_hdt-ud-train-a-2.conllu",
            "UD_German-HDT/r2.10/de_hdt-ud-train-b-1.conllu",
            "UD_German-HDT/r2.10/de_hdt-ud-train-b-2.conllu",
        ],
        "dev": "UD_German-HDT/r2.10/de_hdt-ud-dev.conllu",
        "test": "UD_German-HDT/r2.10/de_hdt-ud-test.conllu",
    },
    "de_lit": {
        "test": "UD_German-LIT/r2.10/de_lit-ud-test.conllu",
    },
    "de_pud": {
        "test": "UD_German-PUD/r2.10/de_pud-ud-test.conllu",
    },
    "got_proiel": {
        "train": "UD_Gothic-PROIEL/r2.10/got_proiel-ud-train.conllu",
        "dev": "UD_Gothic-PROIEL/r2.10/got_proiel-ud-dev.conllu",
        "test": "UD_Gothic-PROIEL/r2.10/got_proiel-ud-test.conllu",
    },
    "el_gdt": {
        "train": "UD_Greek-GDT/r2.10/el_gdt-ud-train.conllu",
        "dev": "UD_Greek-GDT/r2.10/el_gdt-ud-dev.conllu",
        "test": "UD_Greek-GDT/r2.10/el_gdt-ud-test.conllu",
    },
    "gub_tudet": {
        "test": "UD_Guajajara-TuDeT/r2.10/gub_tudet-ud-test.conllu",
    },
    "gn_oldtudet": {
        "test": "UD_Guarani-OldTuDeT/r2.10/gn_oldtudet-ud-test.conllu",
    },
    "he_iahltwiki": {
        "train": "UD_Hebrew-IAHLTwiki/r2.10/he_iahltwiki-ud-train.conllu",
        "dev": "UD_Hebrew-IAHLTwiki/r2.10/he_iahltwiki-ud-dev.conllu",
        "test": "UD_Hebrew-IAHLTwiki/r2.10/he_iahltwiki-ud-test.conllu",
    },
    "he_htb": {
        "train": "UD_Hebrew-HTB/r2.10/he_htb-ud-train.conllu",
        "dev": "UD_Hebrew-HTB/r2.10/he_htb-ud-dev.conllu",
        "test": "UD_Hebrew-HTB/r2.10/he_htb-ud-test.conllu",
    },
    "qhe_hiencs": {
        "train": "UD_Hindi_English-HIENCS/r2.10/qhe_hiencs-ud-train.conllu",
        "dev": "UD_Hindi_English-HIENCS/r2.10/qhe_hiencs-ud-dev.conllu",
        "test": "UD_Hindi_English-HIENCS/r2.10/qhe_hiencs-ud-test.conllu",
    },
    "hi_hdtb": {
        "train": "UD_Hindi-HDTB/r2.10/hi_hdtb-ud-train.conllu",
        "dev": "UD_Hindi-HDTB/r2.10/hi_hdtb-ud-dev.conllu",
        "test": "UD_Hindi-HDTB/r2.10/hi_hdtb-ud-test.conllu",
    },
    "hi_pud": {
        "test": "UD_Hindi-PUD/r2.10/hi_pud-ud-test.conllu",
    },
    "hu_szeged": {
        "train": "UD_Hungarian-Szeged/r2.10/hu_szeged-ud-train.conllu",
        "dev": "UD_Hungarian-Szeged/r2.10/hu_szeged-ud-dev.conllu",
        "test": "UD_Hungarian-Szeged/r2.10/hu_szeged-ud-test.conllu",
    },
    "is_modern": {
        "train": "UD_Icelandic-Modern/r2.10/is_modern-ud-train.conllu",
        "dev": "UD_Icelandic-Modern/r2.10/is_modern-ud-dev.conllu",
        "test": "UD_Icelandic-Modern/r2.10/is_modern-ud-test.conllu",
    },
    "is_icepahc": {
        "train": "UD_Icelandic-IcePaHC/r2.10/is_icepahc-ud-train.conllu",
        "dev": "UD_Icelandic-IcePaHC/r2.10/is_icepahc-ud-dev.conllu",
        "test": "UD_Icelandic-IcePaHC/r2.10/is_icepahc-ud-test.conllu",
    },
    "is_pud": {
        "test": "UD_Icelandic-PUD/r2.10/is_pud-ud-test.conllu",
    },
    "id_csui": {
        "train": "UD_Indonesian-CSUI/r2.10/id_csui-ud-train.conllu",
        "test": "UD_Indonesian-CSUI/r2.10/id_csui-ud-test.conllu",
    },
    "id_gsd": {
        "train": "UD_Indonesian-GSD/r2.10/id_gsd-ud-train.conllu",
        "dev": "UD_Indonesian-GSD/r2.10/id_gsd-ud-dev.conllu",
        "test": "UD_Indonesian-GSD/r2.10/id_gsd-ud-test.conllu",
    },
    "id_pud": {
        "test": "UD_Indonesian-PUD/r2.10/id_pud-ud-test.conllu",
    },
    "ga_twittirish": {
        "test": "UD_Irish-TwittIrish/r2.10/ga_twittirish-ud-test.conllu",
    },
    "ga_idt": {
        "train": "UD_Irish-IDT/r2.10/ga_idt-ud-train.conllu",
        "dev": "UD_Irish-IDT/r2.10/ga_idt-ud-dev.conllu",
        "test": "UD_Irish-IDT/r2.10/ga_idt-ud-test.conllu",
    },
    "it_valico": {
        "test": "UD_Italian-Valico/r2.10/it_valico-ud-test.conllu",
    },
    "it_markit": {
        "train": "UD_Italian-MarkIT/r2.10/it_markit-ud-train.conllu",
        "dev": "UD_Italian-MarkIT/r2.10/it_markit-ud-dev.conllu",
        "test": "UD_Italian-MarkIT/r2.10/it_markit-ud-test.conllu",
    },
    "it_isdt": {
        "train": "UD_Italian-ISDT/r2.10/it_isdt-ud-train.conllu",
        "dev": "UD_Italian-ISDT/r2.10/it_isdt-ud-dev.conllu",
        "test": "UD_Italian-ISDT/r2.10/it_isdt-ud-test.conllu",
    },
    "it_partut": {
        "train": "UD_Italian-ParTUT/r2.10/it_partut-ud-train.conllu",
        "dev": "UD_Italian-ParTUT/r2.10/it_partut-ud-dev.conllu",
        "test": "UD_Italian-ParTUT/r2.10/it_partut-ud-test.conllu",
    },
    "it_postwita": {
        "train": "UD_Italian-PoSTWITA/r2.10/it_postwita-ud-train.conllu",
        "dev": "UD_Italian-PoSTWITA/r2.10/it_postwita-ud-dev.conllu",
        "test": "UD_Italian-PoSTWITA/r2.10/it_postwita-ud-test.conllu",
    },
    "it_pud": {
        "test": "UD_Italian-PUD/r2.10/it_pud-ud-test.conllu",
    },
    "it_twittiro": {
        "train": "UD_Italian-TWITTIRO/r2.10/it_twittiro-ud-train.conllu",
        "dev": "UD_Italian-TWITTIRO/r2.10/it_twittiro-ud-dev.conllu",
        "test": "UD_Italian-TWITTIRO/r2.10/it_twittiro-ud-test.conllu",
    },
    "it_vit": {
        "train": "UD_Italian-VIT/r2.10/it_vit-ud-train.conllu",
        "dev": "UD_Italian-VIT/r2.10/it_vit-ud-dev.conllu",
        "test": "UD_Italian-VIT/r2.10/it_vit-ud-test.conllu",
    },
    "ja_gsdluw": {
        "train": "UD_Japanese-GSDLUW/r2.10/ja_gsdluw-ud-train.conllu",
        "dev": "UD_Japanese-GSDLUW/r2.10/ja_gsdluw-ud-dev.conllu",
        "test": "UD_Japanese-GSDLUW/r2.10/ja_gsdluw-ud-test.conllu",
    },
    "ja_pudluw": {
        "test": "UD_Japanese-PUDLUW/r2.10/ja_pudluw-ud-test.conllu",
    },
    "ja_bccwjluw": {
        "train": "UD_Japanese-BCCWJLUW/r2.10/ja_bccwjluw-ud-train.conllu",
        "dev": "UD_Japanese-BCCWJLUW/r2.10/ja_bccwjluw-ud-dev.conllu",
        "test": "UD_Japanese-BCCWJLUW/r2.10/ja_bccwjluw-ud-test.conllu",
    },
    "ja_bccwj": {
        "train": "UD_Japanese-BCCWJ/r2.10/ja_bccwj-ud-train.conllu",
        "dev": "UD_Japanese-BCCWJ/r2.10/ja_bccwj-ud-dev.conllu",
        "test": "UD_Japanese-BCCWJ/r2.10/ja_bccwj-ud-test.conllu",
    },
    "ja_gsd": {
        "train": "UD_Japanese-GSD/r2.10/ja_gsd-ud-train.conllu",
        "dev": "UD_Japanese-GSD/r2.10/ja_gsd-ud-dev.conllu",
        "test": "UD_Japanese-GSD/r2.10/ja_gsd-ud-test.conllu",
    },
    "ja_modern": {
        "test": "UD_Japanese-Modern/r2.10/ja_modern-ud-test.conllu",
    },
    "ja_pud": {
        "test": "UD_Japanese-PUD/r2.10/ja_pud-ud-test.conllu",
    },
    "jv_csui": {
        "test": "UD_Javanese-CSUI/r2.10/jv_csui-ud-test.conllu",
    },
    "urb_tudet": {
        "test": "UD_Kaapor-TuDeT/r2.10/urb_tudet-ud-test.conllu",
    },
    "xnr_kdtb": {
        "test": "UD_Kangri-KDTB/r2.10/xnr_kdtb-ud-test.conllu",
    },
    "krl_kkpp": {
        "test": "UD_Karelian-KKPP/r2.10/krl_kkpp-ud-test.conllu",
    },
    "arr_tudet": {
        "test": "UD_Karo-TuDeT/r2.10/arr_tudet-ud-test.conllu",
    },
    "kk_ktb": {
        "train": "UD_Kazakh-KTB/r2.10/kk_ktb-ud-train.conllu",
        "test": "UD_Kazakh-KTB/r2.10/kk_ktb-ud-test.conllu",
    },
    "kfm_aha": {
        "test": "UD_Khunsari-AHA/r2.10/kfm_aha-ud-test.conllu",
    },
    "quc_iu": {
        "test": "UD_Kiche-IU/r2.10/quc_iu-ud-test.conllu",
    },
    "koi_uh": {
        "test": "UD_Komi_Permyak-UH/r2.10/koi_uh-ud-test.conllu",
    },
    "kpv_ikdp": {
        "test": "UD_Komi_Zyrian-IKDP/r2.10/kpv_ikdp-ud-test.conllu",
    },
    "kpv_lattice": {
        "test": "UD_Komi_Zyrian-Lattice/r2.10/kpv_lattice-ud-test.conllu",
    },
    "ko_gsd": {
        "train": "UD_Korean-GSD/r2.10/ko_gsd-ud-train.conllu",
        "dev": "UD_Korean-GSD/r2.10/ko_gsd-ud-dev.conllu",
        "test": "UD_Korean-GSD/r2.10/ko_gsd-ud-test.conllu",
    },
    "ko_kaist": {
        "train": "UD_Korean-Kaist/r2.10/ko_kaist-ud-train.conllu",
        "dev": "UD_Korean-Kaist/r2.10/ko_kaist-ud-dev.conllu",
        "test": "UD_Korean-Kaist/r2.10/ko_kaist-ud-test.conllu",
    },
    "ko_pud": {
        "test": "UD_Korean-PUD/r2.10/ko_pud-ud-test.conllu",
    },
    "kmr_mg": {
        "train": "UD_Kurmanji-MG/r2.10/kmr_mg-ud-train.conllu",
        "test": "UD_Kurmanji-MG/r2.10/kmr_mg-ud-test.conllu",
    },
    "la_udante": {
        "train": "UD_Latin-UDante/r2.10/la_udante-ud-train.conllu",
        "dev": "UD_Latin-UDante/r2.10/la_udante-ud-dev.conllu",
        "test": "UD_Latin-UDante/r2.10/la_udante-ud-test.conllu",
    },
    "la_ittb": {
        "train": "UD_Latin-ITTB/r2.10/la_ittb-ud-train.conllu",
        "dev": "UD_Latin-ITTB/r2.10/la_ittb-ud-dev.conllu",
        "test": "UD_Latin-ITTB/r2.10/la_ittb-ud-test.conllu",
    },
    "la_llct": {
        "train": "UD_Latin-LLCT/r2.10/la_llct-ud-train.conllu",
        "dev": "UD_Latin-LLCT/r2.10/la_llct-ud-dev.conllu",
        "test": "UD_Latin-LLCT/r2.10/la_llct-ud-test.conllu",
    },
    "la_perseus": {
        "train": "UD_Latin-Perseus/r2.10/la_perseus-ud-train.conllu",
        "test": "UD_Latin-Perseus/r2.10/la_perseus-ud-test.conllu",
    },
    "la_proiel": {
        "train": "UD_Latin-PROIEL/r2.10/la_proiel-ud-train.conllu",
        "dev": "UD_Latin-PROIEL/r2.10/la_proiel-ud-dev.conllu",
        "test": "UD_Latin-PROIEL/r2.10/la_proiel-ud-test.conllu",
    },
    "lv_lvtb": {
        "train": "UD_Latvian-LVTB/r2.10/lv_lvtb-ud-train.conllu",
        "dev": "UD_Latvian-LVTB/r2.10/lv_lvtb-ud-dev.conllu",
        "test": "UD_Latvian-LVTB/r2.10/lv_lvtb-ud-test.conllu",
    },
    "lij_glt": {
        "train": "UD_Ligurian-GLT/r2.10/lij_glt-ud-train.conllu",
        "test": "UD_Ligurian-GLT/r2.10/lij_glt-ud-test.conllu",
    },
    "lt_alksnis": {
        "train": "UD_Lithuanian-ALKSNIS/r2.10/lt_alksnis-ud-train.conllu",
        "dev": "UD_Lithuanian-ALKSNIS/r2.10/lt_alksnis-ud-dev.conllu",
        "test": "UD_Lithuanian-ALKSNIS/r2.10/lt_alksnis-ud-test.conllu",
    },
    "lt_hse": {
        "train": "UD_Lithuanian-HSE/r2.10/lt_hse-ud-train.conllu",
        "dev": "UD_Lithuanian-HSE/r2.10/lt_hse-ud-train.conllu",
        "test": "UD_Lithuanian-HSE/r2.10/lt_hse-ud-train.conllu",
    },
    "olo_kkpp": {
        "train": "UD_Livvi-KKPP/r2.10/olo_kkpp-ud-train.conllu",
        "test": "UD_Livvi-KKPP/r2.10/olo_kkpp-ud-test.conllu",
    },
    "nds_lsdc": {
        "test": "UD_Low_Saxon-LSDC/r2.10/nds_lsdc-ud-test.conllu",
    },
    # TODO(tfds) Add Madi Jarawara splits when it will be officially released.
    # TODO(tfds) Add Makurap TuDeT splits when it will be officially released.
    "mt_mudt": {
        "train": "UD_Maltese-MUDT/r2.10/mt_mudt-ud-train.conllu",
        "dev": "UD_Maltese-MUDT/r2.10/mt_mudt-ud-dev.conllu",
        "test": "UD_Maltese-MUDT/r2.10/mt_mudt-ud-test.conllu",
    },
    "gv_cadhan": {
        "test": "UD_Manx-Cadhan/r2.10/gv_cadhan-ud-test.conllu",
    },
    "mr_ufal": {
        "train": "UD_Marathi-UFAL/r2.10/mr_ufal-ud-train.conllu",
        "dev": "UD_Marathi-UFAL/r2.10/mr_ufal-ud-dev.conllu",
        "test": "UD_Marathi-UFAL/r2.10/mr_ufal-ud-test.conllu",
    },
    "gun_dooley": {
        "test": "UD_Mbya_Guarani-Dooley/r2.10/gun_dooley-ud-test.conllu",
    },
    "gun_thomas": {
        "test": "UD_Mbya_Guarani-Thomas/r2.10/gun_thomas-ud-test.conllu",
    },
    "mdf_jr": {
        "test": "UD_Moksha-JR/r2.10/mdf_jr-ud-test.conllu",
    },
    "myu_tudet": {
        "test": "UD_Munduruku-TuDeT/r2.10/myu_tudet-ud-test.conllu",
    },
    "pcm_nsc": {
        "train": "UD_Naija-NSC/r2.10/pcm_nsc-ud-train.conllu",
        "dev": "UD_Naija-NSC/r2.10/pcm_nsc-ud-dev.conllu",
        "test": "UD_Naija-NSC/r2.10/pcm_nsc-ud-test.conllu",
    },
    "nyq_aha": {
        "test": "UD_Nayini-AHA/r2.10/nyq_aha-ud-test.conllu",
    },
    # TODO(tfds) Add Neapolitan RB splits when it will be officially released.
    "sme_giella": {
        "train": "UD_North_Sami-Giella/r2.10/sme_giella-ud-train.conllu",
        "test": "UD_North_Sami-Giella/r2.10/sme_giella-ud-test.conllu",
    },
    "no_bokmaal": {
        "train": "UD_Norwegian-Bokmaal/r2.10/no_bokmaal-ud-train.conllu",
        "dev": "UD_Norwegian-Bokmaal/r2.10/no_bokmaal-ud-dev.conllu",
        "test": "UD_Norwegian-Bokmaal/r2.10/no_bokmaal-ud-test.conllu",
    },
    "no_nynorsk": {
        "train": "UD_Norwegian-Nynorsk/r2.10/no_nynorsk-ud-train.conllu",
        "dev": "UD_Norwegian-Nynorsk/r2.10/no_nynorsk-ud-dev.conllu",
        "test": "UD_Norwegian-Nynorsk/r2.10/no_nynorsk-ud-test.conllu",
    },
    "no_nynorsklia": {
        "train": "UD_Norwegian-NynorskLIA/r2.10/no_nynorsklia-ud-train.conllu",
        "dev": "UD_Norwegian-NynorskLIA/r2.10/no_nynorsklia-ud-dev.conllu",
        "test": "UD_Norwegian-NynorskLIA/r2.10/no_nynorsklia-ud-test.conllu",
    },
    "cu_proiel": {
        "train":
            "UD_Old_Church_Slavonic-PROIEL/r2.10/cu_proiel-ud-train.conllu",
        "dev":
            "UD_Old_Church_Slavonic-PROIEL/r2.10/cu_proiel-ud-dev.conllu",
        "test":
            "UD_Old_Church_Slavonic-PROIEL/r2.10/cu_proiel-ud-test.conllu",
    },
    "fro_srcmf": {
        "train": "UD_Old_French-SRCMF/r2.10/fro_srcmf-ud-train.conllu",
        "dev": "UD_Old_French-SRCMF/r2.10/fro_srcmf-ud-dev.conllu",
        "test": "UD_Old_French-SRCMF/r2.10/fro_srcmf-ud-test.conllu",
    },
    "orv_birchbark": {
        "train":
            "UD_Old_East_Slavic-Birchbark/r2.10/orv_birchbark-ud-train.conllu",
        "dev":
            "UD_Old_East_Slavic-Birchbark/r2.10/orv_birchbark-ud-dev.conllu",
        "test":
            "UD_Old_East_Slavic-Birchbark/r2.10/orv_birchbark-ud-test.conllu",
    },
    "orv_rnc": {
        "train": "UD_Old_Russian-RNC/r2.10/orv_rnc-ud-train.conllu",
        "test": "UD_Old_Russian-RNC/r2.10/orv_rnc-ud-test.conllu",
    },
    "orv_torot": {
        "train": "UD_Old_Russian-TOROT/r2.10/orv_torot-ud-train.conllu",
        "dev": "UD_Old_Russian-TOROT/r2.10/orv_torot-ud-dev.conllu",
        "test": "UD_Old_Russian-TOROT/r2.10/orv_torot-ud-test.conllu",
    },
    "otk_tonqq": {
        "test": "UD_Old_Turkish-Tonqq/r2.10/otk_tonqq-ud-test.conllu",
    },
    "fa_perdt": {
        "train": "UD_Persian-PerDT/r2.10/fa_perdt-ud-train.conllu",
        "dev": "UD_Persian-PerDT/r2.10/fa_perdt-ud-dev.conllu",
        "test": "UD_Persian-PerDT/r2.10/fa_perdt-ud-test.conllu",
    },
    "fa_seraji": {
        "train": "UD_Persian-Seraji/r2.10/fa_seraji-ud-train.conllu",
        "dev": "UD_Persian-Seraji/r2.10/fa_seraji-ud-dev.conllu",
        "test": "UD_Persian-Seraji/r2.10/fa_seraji-ud-test.conllu",
    },
    "pl_lfg": {
        "train": "UD_Polish-LFG/r2.10/pl_lfg-ud-train.conllu",
        "dev": "UD_Polish-LFG/r2.10/pl_lfg-ud-dev.conllu",
        "test": "UD_Polish-LFG/r2.10/pl_lfg-ud-test.conllu",
    },
    "pl_pdb": {
        "train": "UD_Polish-PDB/r2.10/pl_pdb-ud-train.conllu",
        "dev": "UD_Polish-PDB/r2.10/pl_pdb-ud-dev.conllu",
        "test": "UD_Polish-PDB/r2.10/pl_pdb-ud-test.conllu",
    },
    "pl_pud": {
        "test": "UD_Polish-PUD/r2.10/pl_pud-ud-test.conllu",
    },
    "pt_bosque": {
        "train": "UD_Portuguese-Bosque/r2.10/pt_bosque-ud-train.conllu",
        "dev": "UD_Portuguese-Bosque/r2.10/pt_bosque-ud-dev.conllu",
        "test": "UD_Portuguese-Bosque/r2.10/pt_bosque-ud-test.conllu",
    },
    "pt_gsd": {
        "train": "UD_Portuguese-GSD/r2.10/pt_gsd-ud-train.conllu",
        "dev": "UD_Portuguese-GSD/r2.10/pt_gsd-ud-dev.conllu",
        "test": "UD_Portuguese-GSD/r2.10/pt_gsd-ud-test.conllu",
    },
    "pt_pud": {
        "test": "UD_Portuguese-PUD/r2.10/pt_pud-ud-test.conllu",
    },
    "ro_art": {
        "test": "UD_Romanian-ArT/r2.10/ro_art-ud-test.conllu",
    },
    "ro_nonstandard": {
        "train": "UD_Romanian-Nonstandard/r2.10/ro_nonstandard-ud-train.conllu",
        "dev": "UD_Romanian-Nonstandard/r2.10/ro_nonstandard-ud-dev.conllu",
        "test": "UD_Romanian-Nonstandard/r2.10/ro_nonstandard-ud-test.conllu",
    },
    "ro_rrt": {
        "train": "UD_Romanian-RRT/r2.10/ro_rrt-ud-train.conllu",
        "dev": "UD_Romanian-RRT/r2.10/ro_rrt-ud-dev.conllu",
        "test": "UD_Romanian-RRT/r2.10/ro_rrt-ud-test.conllu",
    },
    "ro_simonero": {
        "train": "UD_Romanian-SiMoNERo/r2.10/ro_simonero-ud-train.conllu",
        "dev": "UD_Romanian-SiMoNERo/r2.10/ro_simonero-ud-dev.conllu",
        "test": "UD_Romanian-SiMoNERo/r2.10/ro_simonero-ud-test.conllu",
    },
    "ru_gsd": {
        "train": "UD_Russian-GSD/r2.10/ru_gsd-ud-train.conllu",
        "dev": "UD_Russian-GSD/r2.10/ru_gsd-ud-dev.conllu",
        "test": "UD_Russian-GSD/r2.10/ru_gsd-ud-test.conllu",
    },
    "ru_pud": {
        "test": "UD_Russian-PUD/r2.10/ru_pud-ud-test.conllu",
    },
    "ru_syntagrus": {
        "train": "UD_Russian-SynTagRus/r2.7/ru_syntagrus-ud-train.conllu",
        "dev": "UD_Russian-SynTagRus/r2.7/ru_syntagrus-ud-dev.conllu",
        "test": "UD_Russian-SynTagRus/r2.7/ru_syntagrus-ud-test.conllu",
    },
    "ru_taiga": {
        "train": "UD_Russian-Taiga/r2.10/ru_taiga-ud-train.conllu",
        "dev": "UD_Russian-Taiga/r2.10/ru_taiga-ud-dev.conllu",
        "test": "UD_Russian-Taiga/r2.10/ru_taiga-ud-test.conllu",
    },
    "sa_ufal": {
        "test": "UD_Sanskrit-UFAL/r2.10/sa_ufal-ud-test.conllu",
    },
    "sa_vedic": {
        "train": "UD_Sanskrit-Vedic/r2.10/sa_vedic-ud-train.conllu",
        "test": "UD_Sanskrit-Vedic/r2.10/sa_vedic-ud-test.conllu",
    },
    "gd_arcosg": {
        "train": "UD_Scottish_Gaelic-ARCOSG/r2.10/gd_arcosg-ud-train.conllu",
        "dev": "UD_Scottish_Gaelic-ARCOSG/r2.10/gd_arcosg-ud-dev.conllu",
        "test": "UD_Scottish_Gaelic-ARCOSG/r2.10/gd_arcosg-ud-test.conllu",
    },
    "sr_set": {
        "train": "UD_Serbian-SET/r2.10/sr_set-ud-train.conllu",
        "dev": "UD_Serbian-SET/r2.10/sr_set-ud-dev.conllu",
        "test": "UD_Serbian-SET/r2.10/sr_set-ud-test.conllu",
    },
    "sms_giellagas": {
        "test": "UD_Skolt_Sami-Giellagas/r2.10/sms_giellagas-ud-test.conllu",
    },
    "sk_snk": {
        "train": "UD_Slovak-SNK/r2.10/sk_snk-ud-train.conllu",
        "dev": "UD_Slovak-SNK/r2.10/sk_snk-ud-dev.conllu",
        "test": "UD_Slovak-SNK/r2.10/sk_snk-ud-test.conllu",
    },
    "sl_ssj": {
        "train": "UD_Slovenian-SSJ/r2.10/sl_ssj-ud-train.conllu",
        "dev": "UD_Slovenian-SSJ/r2.10/sl_ssj-ud-dev.conllu",
        "test": "UD_Slovenian-SSJ/r2.10/sl_ssj-ud-test.conllu",
    },
    "sl_sst": {
        "train": "UD_Slovenian-SST/r2.10/sl_sst-ud-train.conllu",
        "test": "UD_Slovenian-SST/r2.10/sl_sst-ud-test.conllu",
    },
    "soj_aha": {
        "test": "UD_Soi-AHA/r2.10/soj_aha-ud-test.conllu",
    },
    "ajp_madar": {
        "test":
            "UD_South_Levantine_Arabic-MADAR/r2.10/ajp_madar-ud-test.conllu",
    },
    "es_ancora": {
        "train": "UD_Spanish-AnCora/r2.10/es_ancora-ud-train.conllu",
        "dev": "UD_Spanish-AnCora/r2.10/es_ancora-ud-dev.conllu",
        "test": "UD_Spanish-AnCora/r2.10/es_ancora-ud-test.conllu",
    },
    "es_gsd": {
        "train": "UD_Spanish-GSD/r2.10/es_gsd-ud-train.conllu",
        "dev": "UD_Spanish-GSD/r2.10/es_gsd-ud-dev.conllu",
        "test": "UD_Spanish-GSD/r2.10/es_gsd-ud-test.conllu",
    },
    "es_pud": {
        "test": "UD_Spanish-PUD/r2.10/es_pud-ud-test.conllu",
    },
    "swl_sslc": {
        "train": "UD_Swedish_Sign_Language-SSLC/r2.10/swl_sslc-ud-train.conllu",
        "dev": "UD_Swedish_Sign_Language-SSLC/r2.10/swl_sslc-ud-dev.conllu",
        "test": "UD_Swedish_Sign_Language-SSLC/r2.10/swl_sslc-ud-test.conllu",
    },
    "sv_lines": {
        "train": "UD_Swedish-LinES/r2.10/sv_lines-ud-train.conllu",
        "dev": "UD_Swedish-LinES/r2.10/sv_lines-ud-dev.conllu",
        "test": "UD_Swedish-LinES/r2.10/sv_lines-ud-test.conllu",
    },
    "sv_pud": {
        "test": "UD_Swedish-PUD/r2.10/sv_pud-ud-test.conllu",
    },
    "sv_talbanken": {
        "train": "UD_Swedish-Talbanken/r2.10/sv_talbanken-ud-train.conllu",
        "dev": "UD_Swedish-Talbanken/r2.10/sv_talbanken-ud-dev.conllu",
        "test": "UD_Swedish-Talbanken/r2.10/sv_talbanken-ud-test.conllu",
    },
    "gsw_uzh": {
        "test": "UD_Swiss_German-UZH/r2.10/gsw_uzh-ud-test.conllu",
    },
    "tl_trg": {
        "test": "UD_Tagalog-TRG/r2.10/tl_trg-ud-test.conllu",
    },
    "tl_ugnayan": {
        "test": "UD_Tagalog-Ugnayan/r2.10/tl_ugnayan-ud-test.conllu",
    },
    "ta_mwtt": {
        "test": "UD_Tamil-MWTT/r2.10/ta_mwtt-ud-test.conllu",
    },
    "ta_ttb": {
        "train": "UD_Tamil-TTB/r2.10/ta_ttb-ud-train.conllu",
        "dev": "UD_Tamil-TTB/r2.10/ta_ttb-ud-dev.conllu",
        "test": "UD_Tamil-TTB/r2.10/ta_ttb-ud-test.conllu",
    },
    "te_mtg": {
        "train": "UD_Telugu-MTG/r2.10/te_mtg-ud-train.conllu",
        "dev": "UD_Telugu-MTG/r2.10/te_mtg-ud-dev.conllu",
        "test": "UD_Telugu-MTG/r2.10/te_mtg-ud-test.conllu",
    },
    "th_pud": {
        "test": "UD_Thai-PUD/r2.10/th_pud-ud-test.conllu",
    },
    "tpn_tudet": {
        "test": "UD_Tupinamba-TuDeT/r2.10/tpn_tudet-ud-test.conllu",
    },
    "qtd_sagt": {
        "train": "UD_Turkish_German-SAGT/r2.10/qtd_sagt-ud-train.conllu",
        "dev": "UD_Turkish_German-SAGT/r2.10/qtd_sagt-ud-dev.conllu",
        "test": "UD_Turkish_German-SAGT/r2.10/qtd_sagt-ud-test.conllu",
    },
    "tr_kenet": {
        "train": "UD_Turkish-Kenet/r2.10/tr_kenet-ud-train.conllu",
        "dev": "UD_Turkish-Kenet/r2.10/tr_kenet-ud-dev.conllu",
        "test": "UD_Turkish-Kenet/r2.10/tr_kenet-ud-test.conllu",
    },
    "tr_atis": {
        "train": "UD_Turkish-Atis/r2.10/tr_atis-ud-train.conllu",
        "dev": "UD_Turkish-Atis/r2.10/tr_atis-ud-dev.conllu",
        "test": "UD_Turkish-Atis/r2.10/tr_atis-ud-test.conllu",
    },
    "tr_penn": {
        "train": "UD_Turkish-Penn/r2.10/tr_penn-ud-train.conllu",
        "dev": "UD_Turkish-Penn/r2.10/tr_penn-ud-dev.conllu",
        "test": "UD_Turkish-Penn/r2.10/tr_penn-ud-test.conllu",
    },
    "tr_tourism": {
        "train": "UD_Turkish-Tourism/r2.10/tr_tourism-ud-train.conllu",
        "dev": "UD_Turkish-Tourism/r2.10/tr_tourism-ud-dev.conllu",
        "test": "UD_Turkish-Tourism/r2.10/tr_tourism-ud-test.conllu",
    },
    "tr_framenet": {
        "train": "UD_Turkish-FrameNet/r2.10/tr_framenet-ud-train.conllu",
        "dev": "UD_Turkish-FrameNet/r2.10/tr_framenet-ud-dev.conllu",
        "test": "UD_Turkish-FrameNet/r2.10/tr_framenet-ud-test.conllu",
    },
    "tr_boun": {
        "train": "UD_Turkish-BOUN/r2.10/tr_boun-ud-train.conllu",
        "dev": "UD_Turkish-BOUN/r2.10/tr_boun-ud-dev.conllu",
        "test": "UD_Turkish-BOUN/r2.10/tr_boun-ud-test.conllu",
    },
    "tr_gb": {
        "test": "UD_Turkish-GB/r2.10/tr_gb-ud-test.conllu",
    },
    "tr_imst": {
        "train": "UD_Turkish-IMST/r2.10/tr_imst-ud-train.conllu",
        "dev": "UD_Turkish-IMST/r2.10/tr_imst-ud-dev.conllu",
        "test": "UD_Turkish-IMST/r2.10/tr_imst-ud-test.conllu",
    },
    "tr_pud": {
        "test": "UD_Turkish-PUD/r2.10/tr_pud-ud-test.conllu",
    },
    "uk_iu": {
        "train": "UD_Ukrainian-IU/r2.10/uk_iu-ud-train.conllu",
        "dev": "UD_Ukrainian-IU/r2.10/uk_iu-ud-dev.conllu",
        "test": "UD_Ukrainian-IU/r2.10/uk_iu-ud-test.conllu",
    },
    # TODO(tfds) Add Umbrian Ikuvina split when it will be officially released.
    "hsb_ufal": {
        "train": "UD_Upper_Sorbian-UFAL/r2.10/hsb_ufal-ud-train.conllu",
        "test": "UD_Upper_Sorbian-UFAL/r2.10/hsb_ufal-ud-test.conllu",
    },
    "ur_udtb": {
        "train": "UD_Urdu-UDTB/r2.10/ur_udtb-ud-train.conllu",
        "dev": "UD_Urdu-UDTB/r2.10/ur_udtb-ud-dev.conllu",
        "test": "UD_Urdu-UDTB/r2.10/ur_udtb-ud-test.conllu",
    },
    "ug_udt": {
        "train": "UD_Uyghur-UDT/r2.10/ug_udt-ud-train.conllu",
        "dev": "UD_Uyghur-UDT/r2.10/ug_udt-ud-dev.conllu",
        "test": "UD_Uyghur-UDT/r2.10/ug_udt-ud-test.conllu",
    },
    "vi_vtb": {
        "train": "UD_Vietnamese-VTB/r2.10/vi_vtb-ud-train.conllu",
        "dev": "UD_Vietnamese-VTB/r2.10/vi_vtb-ud-dev.conllu",
        "test": "UD_Vietnamese-VTB/r2.10/vi_vtb-ud-test.conllu",
    },
    "wbp_ufal": {
        "test": "UD_Warlpiri-UFAL/r2.10/wbp_ufal-ud-test.conllu",
    },
    "cy_ccg": {
        "train": "UD_Welsh-CCG/r2.10/cy_ccg-ud-train.conllu",
        "test": "UD_Welsh-CCG/r2.10/cy_ccg-ud-test.conllu",
    },
    "wo_wtb": {
        "train": "UD_Wolof-WTB/r2.10/wo_wtb-ud-train.conllu",
        "dev": "UD_Wolof-WTB/r2.10/wo_wtb-ud-dev.conllu",
        "test": "UD_Wolof-WTB/r2.10/wo_wtb-ud-test.conllu",
    },
    "sjo_xdt": {
        "test": "UD_Xibe-XDT/r2.10/sjo_xdt-ud-test.conllu",
    },
    "sah_yktdt": {
        "test": "UD_Yakut-YKTDT/r2.10/sah_yktdt-ud-test.conllu",
    },
    "yo_ytb": {
        "test": "UD_Yoruba-YTB/r2.10/yo_ytb-ud-test.conllu",
    },
    "ess_sli": {
        "test": "UD_Yupik-SLI/r2.10/ess_sli-ud-test.conllu",
    },
}

LANGS = DESCRIPTIONS.keys()


def prepare_ud_filepaths(
    path_prefix: epath.PathLike,
    filepaths: Union[epath.PathLike,
                     List[epath.PathLike]]) -> List[epath.PathLike]:
  """Prepends a path prefix to a (list of) filepaths.

  Args:
    path_prefix: A path which will be prepended to all paths in filepaths.
    filepaths: The filepaths to be prepared. Could be a list of paths for
      multiple files, or a single path.

  Returns:
    A list with the resulting filepath(s). In case a single path was given as
    `filepath`, it will returns a one-item list containing the resulting path.
  """
  paths = filepaths if isinstance(filepaths, list) else [filepaths]
  return [os.path.join(path_prefix, filepath) for filepath in paths]
