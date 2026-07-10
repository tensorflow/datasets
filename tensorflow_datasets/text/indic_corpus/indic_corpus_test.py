"""indic_corpus dataset."""

import tensorflow_datasets as tfds
from . import indic_corpus


class IndicCorpusTest(tfds.testing.DatasetBuilderTestCase):
    """Tests for indic_corpus dataset."""

    # TODO(indic_corpus):
    DATASET_CLASS = indic_corpus.IndicCorpus
	BUILDER_CONFIG_NAMES_TO_TEST = ['indic_corpus']
	for config in indic_corpus.IndicCorpus.BUILDER_CONFIGS:
		if config.name == "indic_corpus":
			config.languages = ["as"]
    SPLITS = {
        "as": 3,
		"as-validation": 2

    }


if __name__ == "__main__":
    tfds.testing.test_main()
