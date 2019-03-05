"""
Mozilla Common Voice Dataset (English)
"""
import os
import csv
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
_DOWNLOAD_LINK = {
    "en": "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-1/en.tar.gz"}
_SPLITS = {
    tfds.Split.TRAIN: "train",
    tfds.Split.TEST: "test",
    tfds.Split.VALIDATION: "validated"}


class CommonVoice(tfds.core.GeneratorBasedBuilder):
    """
    Mozilla Common Voice Dataset (English)
    """
    VERSION = tfds.core.Version("1.0.0")

    def _info(self):
        return tfds.core.DatasetInfo(
            description=("Mozilla Common Voice Dataset (English)"),
            builder=self,
            features=tfds.features.FeaturesDict({
                "client_id": tfds.features.Text(),
                "upvotes": tf.int32,
                "downvotes": tf.int32,
                "age": tfds.features.Text(),
                "gender": tfds.features.Text(),
                "accent": tfds.features.Text(),
                "sentence": tfds.features.Text(),
                "voice": tfds.features.Tensor(shape=(None,), dtype=tf.float32)
            }),
            urls=[u"https://voice.mozilla.org/en/datasets"]
        )

    def _split_generators(self, dl_manager):
        dl_path = dl_manager.extract(dl_manager.download(_DOWNLOAD_LINK))
        # Need to Check for replacement
        clip_folder = os.path.join(dl_path["en"], "clips")
        return [tfds.core.SplitGenerator(
            name=k,
            num_shards=40,
            gen_kwargs={
                "audio_path": clip_folder,
                "label_path": os.path.join(dl_path["en"], "%s.tsv" % v)
            }) for k, v in _SPLITS.items()]

    def _generate_examples(self, audio_path, label_path):
        """
            Generate Voice Samples and Statements Given the Path to the Shared Audio Folder
            and Path to the Train/Test/Validation File (.tsv)
        """
        with tf.gfile.GFile(label_path) as file_:
            dataset = csv.DictReader(file_, delimiter="\t")
            ffmpeg = tfds.features.Audio(file_format="mp3")
            for row in dataset:
                wave = ffmpeg.encode_example(
                    os.path.join(
                        audio_path, "%s.mp3" % row["path"]))
                yield {
                    "client_id": row["client_id"],
                    "voice": wave,
                    "sentence": row["sentence"],
                    "upvotes": int(row["up_votes"]) if len(row["up_votes"]) > 0 else 0,
                    "downvotes": int(row["down_votes"]) if len(row["down_votes"]) > 0 else 0,
                    "age": row["age"],
                    "gender": row["gender"],
                    "accent": row["accent"]}
