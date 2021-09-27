"""PASS dataset."""

import tensorflow_datasets as tfds
import urllib.request
import tensorflow.compat.v2 as tf
pd = tfds.core.lazy_imports.pandas

_DESCRIPTION = """
PASS is a large-scale image dataset that does not include any humans,
human parts, or other personally identifiable information.
It that can be used for high-quality self-supervised pretraining while significantly reducing privacy concerns.

PASS contains 1.440.191 images without any labels sourced from YFCC-100M.

All images in this dataset are licenced under the CC-BY licence, as is the dataset itself.
For YFCC-100M see  http://www.multimediacommons.org/.
"""

_CITATION = """
@Article{asano21pass,
author = "Yuki M. Asano and Christian Rupprecht and Andrew Zisserman and Andrea Vedaldi",
title = "PASS: An ImageNet replacement for self-supervised pretraining without humans",
journal = "NeurIPS Track on Datasets and Benchmarks",
year = "2021"
}
"""

_URLS = {
    'train_images': [tfds.download.Resource(  # pylint:disable=g-complex-comprehension
        url='https://zenodo.org/record/5528345/files/PASS.%s.tar' % i_,
        extract_method=tfds.download.ExtractMethod.TAR)
        for i_ in '0123456789'],
    'meta_data':tfds.download.Resource(
        url='https://zenodo.org/record/5528345/files/pass_metadata.csv')
}

class PASS(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for pass dataset."""

    VERSION = tfds.core.Version('1.0.0')
    RELEASE_NOTES = {
        '1.0.0': 'Initial release.',
    }

    def _info(self):
        """Returns the dataset metadata."""
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                'image': tfds.features.Image(shape=(None, None, 3)),
                'image/creator_uname': tf.string,
            }),
            supervised_keys=None,
            homepage='https://www.robots.ox.ac.uk/~vgg/research/pass/',
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        paths = dl_manager.download(_URLS)
        with tf.io.gfile.GFile(paths['meta_data']) as f:
            meta = pd.read_csv(f)
        meta = {m[1]['hash']:m[1]['unickname'] for m in meta.iterrows()}
        return [tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                parts=paths['train_images'],
                meta=meta,
                dl_manager=dl_manager),
        )]


    def _generate_examples(self, dl_manager, parts, meta):
        """Yields examples."""
        _idx = 0
        for part in parts:
            for fname, fobj in dl_manager.iter_archive(part):
                _idx += 1
                record = {
                    "image": fobj,
                    "image/creator_uname": meta[fname.split('/')[-1].split('.')[0]]
                }
                yield _idx, record
