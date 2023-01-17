Clean-up text for 40+ Wikipedia languages editions of pages correspond to
entities. The datasets have train/dev/test splits per language. The dataset is
cleaned up by page filtering to remove disambiguation pages, redirect pages,
deleted pages, and non-entity pages. Each example contains the wikidata id of
the entity, and the full Wikipedia article after page processing that removes
non-content sections and structured objects. The language models trained on this
corpus - including 41 monolingual models, and 2 multilingual models - can be
found at https://tfhub.dev/google/collections/wiki40b-lm/1.
