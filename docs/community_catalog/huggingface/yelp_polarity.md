# yelp_polarity

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/yelp_polarity)
*   [Huggingface](https://huggingface.co/datasets/yelp_polarity)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:yelp_polarity/plain_text')
```

*   **Description**:

```
Large Yelp Review Dataset.
This is a dataset for binary sentiment classification. We provide a set of 560,000 highly polar yelp reviews for training, and 38,000 for testing. 
ORIGIN
The Yelp reviews dataset consists of reviews from Yelp. It is extracted
from the Yelp Dataset Challenge 2015 data. For more information, please
refer to http://www.yelp.com/dataset_challenge

The Yelp reviews polarity dataset is constructed by
Xiang Zhang (xiang.zhang@nyu.edu) from the above dataset.
It is first used as a text classification benchmark in the following paper:
Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks
for Text Classification. Advances in Neural Information Processing Systems 28
(NIPS 2015).


DESCRIPTION

The Yelp reviews polarity dataset is constructed by considering stars 1 and 2
negative, and 3 and 4 positive. For each polarity 280,000 training samples and
19,000 testing samples are take randomly. In total there are 560,000 trainig
samples and 38,000 testing samples. Negative polarity is class 1,
and positive class 2.

The files train.csv and test.csv contain all the training samples as
comma-sparated values. There are 2 columns in them, corresponding to class
index (1 and 2) and review text. The review texts are escaped using double
quotes ("), and any internal double quote is escaped by 2 double quotes ("").
New lines are escaped by a backslash followed with an "n" character,
that is "
".
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 38000
`'train'` | 560000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "1",
            "2"
        ],
        "id": null,
        "_type": "ClassLabel"
    }
}
```


