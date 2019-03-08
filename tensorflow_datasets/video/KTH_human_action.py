import tensorflow_datasets.public_api as tfds
DESCRIPTION="""\
The current video database containing six types of human actions (walking, jogging, running, boxing, hand waving and hand clapping) performed several times by 25 subjects in four different scenarios: outdoors s1, outdoors with scale variation s2, outdoors with different clothes s3 and indoors s4 as illustrated below. Currently the database contains 2391 sequences. All sequences were taken over homogeneous backgrounds with a static camera with 25fps frame rate. The sequences were downsampled to the spatial resolution of 160x120 pixels and have a length of four seconds in average.
"""
DATA_URL=(" http://www.nada.kth.se/cvap/actions/walking.zip","http://www.nada.kth.se/cvap/actions/jogging.zip","http://www.nada.kth.se/cvap/actions/running.zip",
            "http://www.nada.kth.se/cvap/actions/boxing.zip","http://www.nada.kth.se/cvap/actions/handwaving.zip","http://www.nada.kth.se/cvap/actions/handclapping.zip")
FRAMES_PER_SEC= 25
IMG_SHAPE=(160,120)
CITATION ="""Schuldt, Laptev and Caputo, Proc. ICPR'04, Cambridge, UK """
class KTH_human_action(tfds.core.GeneratorBasedBuilder):
    """  KTH human action video data set"""

    VERSION = tfds.core.Version('0.1.0')

    features = tfds.features.FeaturesDict({
        "video":tfds.features.Video( shape=(None,160,120,1)),
        "label":tfds.features.ClassLabel(num_classes=6),

    })

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            name='KTH_human_action',
            description=DESCRIPTION,
            urls=["http://www.nada.kth.se/cvap/actions/"],
            features=features,
            citation=CITATION,
            supervised_keys=("video","label"),
        )
    def _split_generators(self,dl_manager):
        extracted_path=[]
        for data_url in DATA_URL:
            extracted_path.append(dl_manager.download_and_extract(DATA_URL))
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=8,
                gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "train"),
                    "labels": os.path.join(extracted_path, "train_labels.csv"),
        }),


            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=8,
                gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "validation"),
                "labels": os.path.join(extracted_path, "validation_labels.csv"),
               }),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=9,
                gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "test"),
                "labels": os.path.join(extracted_path, "test_labels.csv"),
        })

        ]
    def _generator_examples(self,filedir):
        with tf.io.gfile.GFile(data_path, "rb") as fp:
            images = np.load(fp)
        images = np.transpose(images, (1, 0, 2, 3))
        images = np.expand_dims(images, axis=-1)
        for sequence in images:
            yield dict(image_sequence=sequence)
