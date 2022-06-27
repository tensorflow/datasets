# hebrew_sentiment

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hebrew_sentiment)
*   [Huggingface](https://huggingface.co/datasets/hebrew_sentiment)


## token


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hebrew_sentiment/token')
```

*   **Description**:

```
HebrewSentiment is a data set consists of 12,804 user comments to posts on the official Facebook page of Israel’s
president, Mr. Reuven Rivlin. In October 2015, we used the open software application Netvizz (Rieder,
2013) to scrape all the comments to all of the president’s posts in the period of June – August 2014,
the first three months of Rivlin’s presidency.2 While the president’s posts aimed at reconciling tensions
and called for tolerance and empathy, the sentiment expressed in the comments to the president’s posts
was polarized between citizens who warmly thanked the president, and citizens that fiercely critiqued his
policy. Of the 12,804 comments, 370 are neutral; 8,512 are positive, 3,922 negative.

Data Annotation: A trained researcher examined each comment and determined its sentiment value,
where comments with an overall positive sentiment were assigned the value 1, comments with an overall
negative sentiment were assigned the value -1, and comments that are off-topic to the post’s content
were assigned the value 0. We validated the coding scheme by asking a second trained researcher to
code the same data. There was substantial agreement between raters (N of agreements: 10623, N of
disagreements: 2105, Coehn’s Kappa = 0.697, p = 0).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2560
`'train'` | 10244

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "pos",
            "neg",
            "off-topic"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## morph


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hebrew_sentiment/morph')
```

*   **Description**:

```
HebrewSentiment is a data set consists of 12,804 user comments to posts on the official Facebook page of Israel’s
president, Mr. Reuven Rivlin. In October 2015, we used the open software application Netvizz (Rieder,
2013) to scrape all the comments to all of the president’s posts in the period of June – August 2014,
the first three months of Rivlin’s presidency.2 While the president’s posts aimed at reconciling tensions
and called for tolerance and empathy, the sentiment expressed in the comments to the president’s posts
was polarized between citizens who warmly thanked the president, and citizens that fiercely critiqued his
policy. Of the 12,804 comments, 370 are neutral; 8,512 are positive, 3,922 negative.

Data Annotation: A trained researcher examined each comment and determined its sentiment value,
where comments with an overall positive sentiment were assigned the value 1, comments with an overall
negative sentiment were assigned the value -1, and comments that are off-topic to the post’s content
were assigned the value 0. We validated the coding scheme by asking a second trained researcher to
code the same data. There was substantial agreement between raters (N of agreements: 10623, N of
disagreements: 2105, Coehn’s Kappa = 0.697, p = 0).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2555
`'train'` | 10221

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "pos",
            "neg",
            "off-topic"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


