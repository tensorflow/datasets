A colossal, cleaned version of Common Crawl's web crawl corpus.

Based on Common Crawl dataset: https://commoncrawl.org

To generate this dataset, please follow
[the instructions from t5](https://github.com/google-research/text-to-text-transfer-transformer#c4).

Due to the overhead of cleaning the dataset, it is recommend you prepare it with
a distributed service like Cloud Dataflow. More info at
https://www.tensorflow.org/datasets/beam_datasets.
