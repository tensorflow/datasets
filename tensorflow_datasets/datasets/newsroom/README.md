NEWSROOM is a large dataset for training and evaluating summarization systems.
It contains 1.3 million articles and summaries written by authors and editors in
the newsrooms of 38 major publications.

Dataset features includes:

- text: Input news text.
- summary: Summary for the news.

And additional features:

- title: news title.
- url: url of the news.
- date: date of the article.
- density: extractive density.
- coverage: extractive coverage.
- compression: compression ratio.
- density_bin: low, medium, high.
- coverage_bin: extractive, abstractive.
- compression_bin: low, medium, high.

This dataset can be downloaded upon requests. Unzip all the contents
"train.jsonl, dev.jsonl, test.jsonl" to the tfds folder.
