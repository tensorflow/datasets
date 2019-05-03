from pathlib import Path

import kaggle
import pandas as pd
import tensorflow as tf
import tensorflow_datasets as tfds

_TAGS = [
    'Child_speech_and_kid_speaking', 'Cutlery_and_silverware',
    'Marimba_and_xylophone', 'Hi-hat', 'Slam', 'Stream', 'Shatter',
    'Mechanical_fan', 'Cupboard_open_or_close',
    'Traffic_noise_and_roadway_noise', 'Sink_(filling_or_washing)',
    'Female_singing', 'Raindrop', 'Zipper_(clothing)', 'Printer', 'Writing',
    'Chewing_and_mastication', 'Bass_drum', 'Sigh', 'Trickle_and_dribble',
    'Walk_and_footsteps', 'Church_bell', 'Buzz', 'Cricket',
    'Computer_keyboard', 'Tick-tock', 'Male_singing',
    'Female_speech_and_woman_speaking', 'Bass_guitar', 'Applause',
    'Water_tap_and_faucet', 'Clapping', 'Microwave_oven',
    'Drawer_open_or_close', 'Yell', 'Chirp_and_tweet', 'Tap', 'Cheering',
    'Squeak', 'Screaming', 'Whispering', 'Harmonica', 'Finger_snapping',
    'Crowd', 'Frying_(food)', 'Purr', 'Acoustic_guitar', 'Chink_and_clink',
    'Glockenspiel', 'Run', 'Bus', 'Motorcycle', 'Hiss', 'Toilet_flush',
    'Strum', 'Scissors', 'Male_speech_and_man_speaking', 'Gurgling',
    'Dishes_and_pots_and_pans', 'Fart', 'Race_car_and_auto_racing',
    'Waves_and_surf', 'Drip', 'Gong', 'Gasp',
    'Accelerating_and_revving_and_vroom', 'Burping_and_eructation',
    'Keys_jangling', 'Skateboard', 'Crackle', 'Electric_guitar',
    'Bicycle_bell', 'Sneeze', 'Knock', 'Meow', 'Bark',
    'Bathtub_(filling_or_washing)', 'Accordion', 'Fill_(with_liquid)',
    'Car_passing_by'
]

# TODO
_CITATION = '''\

'''

# TODO
_DESCRIPTION = '''\
The main research question addressed in this competition is how to adequately exploit a small amount of reliable, manually-labeled data, and a larger quantity of noisy web audio data in a multi-label audio tagging task with a large vocabulary setting. In addition, since the data comes from different sources, the task encourages domain adaptation approaches to deal with a potential domain mismatch.

# Train set

The train set is meant to be for system development. The idea is to limit the supervision provided (i.e., the manually-labeled data), thus promoting approaches to deal with label noise. The train set is composed of two subsets as follows:

##Curated subset

The curated subset is a small set of manually-labeled data from FSD.

    Number of clips/class: 75 except in a few cases (where there are less)
    Total number of clips: 4970
    Avge number of labels/clip: 1.2
    Total duration: 10.5 hours

The duration of the audio clips ranges from 0.3 to 30s due to the diversity of the sound categories and the preferences of Freesound users when recording/uploading sounds. It can happen that a few of these audio clips present additional acoustic material beyond the provided ground truth label(s).

## Noisy subset

The noisy subset is a larger set of noisy web audio data from Flickr videos taken from the YFCC dataset.

    Number of clips/class: 300
    Total number of clips: 19815
    Avge number of labels/clip: 1.2
    Total duration: ~80 hours

The duration of the audio clips ranges from 1s to 15s, with the vast majority lasting 15s.

Considering the numbers above, per-class data distribution available for training is, for most of the classes, 300 clips from the noisy subset and 75 clips from the curated subset, which means 80% noisy - 20% curated at the clip level (not at the audio duration level, considering the variable-length clips).
'''

_URLS = [
    'http://dcase.community/challenge2019/task-audio-tagging',
    'https://www.kaggle.com/c/freesound-audio-tagging-2019/',
]


class FreesoundAudioTagging2019Config(tfds.core.BuilderConfig):
    def __init__(self, concatenate_sources=False, **kwargs):
        self.concatenate_sources = concatenate_sources
        super(FreesoundAudioTagging2019Config, self).__init__(**kwargs)


class FreesoundAudioTagging2019(tfds.core.GeneratorBasedBuilder):

    # TODO Is there an official semver version for the dataset?
    VERSION = tfds.core.Version('1.0.0')

    def _info(self):
        audio = tfds.features.Text()
        tags = tfds.features.FeaturesDict({name: tf.bool for name in _TAGS})
        dataset_info = tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                'audio': audio,
                'tags': tags
            }),
            supervised_keys=('audio', 'tags'),
            urls=_URLS,
            citation=_CITATION,
        )
        return dataset_info

    def _split_generators(self, dl_manager):
        download_dir = Path(dl_manager._download_dir)

        csvs = {
            tfds.Split.TRAIN: download_dir / 'train_noisy.csv',
            tfds.Split.VALIDATION: download_dir / 'train_curated.csv',
            tfds.Split.TEST: download_dir / 'sample_submission.csv',
        }

        zips = {
            tfds.Split.TRAIN: download_dir / 'train_noisy.zip',
            tfds.Split.VALIDATION: download_dir / 'train_curated.zip',
            tfds.Split.TEST: download_dir / 'test.zip',
        }

        kaggle.api.authenticate()
        for resource in list(csvs.values()) + list(zips.values()):
            if not resource.is_file():
                kaggle.api.competition_download_file(
                    competition='freesound-audio-tagging-2019',
                    file_name=resource.name,
                    path=download_dir,
                    quiet=False,
                )

        zips = {k: v.as_posix() for k, v in zips.items()}
        dirs = dl_manager.extract(zips)

        splits = [tfds.Split.TRAIN, tfds.Split.VALIDATION, tfds.Split.TEST]
        split_generators = [
            tfds.core.SplitGenerator(
                name=tfds.Split,
                gen_kwargs={
                    'csv_path': csvs[tfds.Split],
                    'data_path': dirs[tfds.Split]
                },
            ) for tfds.Split in splits
        ]
        return split_generators

    def _generate_examples(self, csv_path, data_path):
        data_path = Path(data_path)
        df = pd.read_csv(csv_path)
        if 'labels' in df.columns:
            df = df.join(df.labels.str.get_dummies(','))
        for i, row in df.iterrows():
            audio = (data_path / row['fname']).as_posix()
            tags = {tag: row[tag] for tag in _TAGS}
            yield {'audio': audio, 'tags': tags}
