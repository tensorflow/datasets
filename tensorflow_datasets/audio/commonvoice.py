"""
Mozilla Common Voice Dataset
"""
import os
import csv
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
_DOWNLOAD_LINKS = {
    "en": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/en.tar.gz",
    "de": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/de.tar.gz",
    "fr": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/fr.tar.gz",
    "cy": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/cy.tar.gz",
    "br": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/br.tar.gz",
    "cv": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/cv.tar.gz",
    "tr": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/tr.tar.gz",
    "tt": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/tt.tar.gz",
    "ky": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/ky.tar.gz",
    "ga-IE": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/ga-IE.tar.gz",
    "kab": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/kab.tar.gz",
    "ca": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/ca.tar.gz",
    "zh-TW": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/zh-TW.tar.gz",
    "sl": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/sl.tar.gz",
    "it": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/it.tar.gz",
    "nl": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/nl.tar.gz",
    "cnh": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/cnh.tar.gz",
    "eo": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/eo.tar.gz"}
_SPLITS = {
    tfds.Split.TRAIN: "train",
    tfds.Split.TEST: "test",
    tfds.Split.VALIDATION: "validated"}


class CommonVoiceConfig(tfds.core.BuilderConfig):
    """
        Configuration Class for Mozilla CommonVoice Dataset
    """
    @tfds.core.api_utils.disallow_positional_args
    def __init__(self, language="en", **kwargs):
        if language not in _DOWNLOAD_LINKS.keys():
            raise ValueError(
                "language must be one of %s" %
                _DOWNLOAD_LINKS.keys())
        self._language = language
        name = kwargs.get("name", None)
        name = "%s_%s" % ("common_voice" if name is None else name, language)
        kwargs["name"] = name
        description = kwargs.get("description", None)
        description = "Language Code: %s" % language if description is None else description
        kwargs["description"] = description
        super(CommonVoiceConfig, self).__init__(**kwargs)

    @property
    def download_urls(self):
        """
            Property returning Download URL based on Language Specified
        """
        return _DOWNLOAD_LINKS[self._language]


def _generate_builder_configs():
    """
        Generates Builder Configs
    """
    configs = []
    version = "1.0.0"
    for k in _DOWNLOAD_LINKS.keys():
        config = CommonVoiceConfig(version=version, language=k)
        configs.append(config)
    return configs


class CommonVoice(tfds.core.GeneratorBasedBuilder):
    """
    Mozilla Common Voice Dataset
    """
    BUILDER_CONFIGS = _generate_builder_configs()
    VERSION = tfds.core.Version("1.0.0")

    def _info(self):
        return tfds.core.DatasetInfo(
            description=("Mozilla Common Voice Dataset"),
            builder=self,
            features=tfds.features.FeaturesDict({
                "client_id": tfds.features.Text(),
                "upvotes": tf.int32,
                "downvotes": tf.int32,
                "age": tfds.features.Text(),
                "gender": tfds.features.Text(),
                "accent": tfds.features.Text(),
                "sentence": tfds.features.Text(),
                "voice": tfds.features.Audio()
            }),
            urls=[u"https://voice.mozilla.org/en/datasets"]
        )

    def _split_generators(self, dl_manager):
        dl_path = dl_manager.extract(
            dl_manager.download(
                self.builder_config.download_urls))
        # Need to Check for replacement
        clip_folder = os.path.join(dl_path, "clips")
        return [tfds.core.SplitGenerator(
            name=k,
            num_shards=40,
            gen_kwargs={
                "audio_path": clip_folder,
                "label_path": os.path.join(dl_path, "%s.tsv" % v)
            }) for k, v in _SPLITS.items()]

    def _generate_examples(self, audio_path, label_path):
        """
            Generate Voice Samples and Statements Given the Path to the Shared Audio Folder
            and Path to the Train/Test/Validation File (.tsv)
        """
        with tf.io.gfile.GFile(label_path) as file_:
            dataset = csv.DictReader(file_, delimiter="\t")
            for row in dataset:
                yield {
                    "client_id": row["client_id"],
                    "voice": os.path.join(audio_path, "%s.mp3" % row["path"]),
                    "sentence": row["sentence"],
                    "upvotes": int(row["up_votes"]) if len(row["up_votes"]) > 0 else 0,
                    "downvotes": int(row["down_votes"]) if len(row["down_votes"]) > 0 else 0,
                    "age": row["age"],
                    "gender": row["gender"],
                    "accent": row["accent"]}
