# conceptual_captions

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/conceptual_captions)
*   [Huggingface](https://huggingface.co/datasets/conceptual_captions)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conceptual_captions')
```

*   **Description**:

```
Image captioning dataset
The resulting dataset (version 1.1) has been split into Training, Validation, and Test splits. The Training split consists of 3,318,333 image-URL/caption pairs, with a total number of 51,201 total token types in the captions (i.e., total vocabulary). The average number of tokens per captions is 10.3 (standard deviation of 4.5), while the median is 9.0 tokens per caption. The Validation split consists of 15,840 image-URL/caption pairs, with similar statistics.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3318333
`'validation'` | 15840

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "caption": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## unlabeled


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conceptual_captions/unlabeled')
```

*   **Description**:

```
Google's Conceptual Captions dataset has more than 3 million images, paired with natural-language captions.
In contrast with the curated style of the MS-COCO images, Conceptual Captions images and their raw descriptions are harvested from the web,
and therefore represent a wider variety of styles. The raw descriptions are harvested from the Alt-text HTML attribute associated with web images.
The authors developed an automatic pipeline that extracts, filters, and transforms candidate image/caption pairs, with the goal of achieving a balance of cleanliness,
informativeness, fluency, and learnability of the resulting captions.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of
Google LLC ("Google") as the data source would be appreciated. The dataset is
provided "AS IS" without any warranty, express or implied. Google disclaims all
liability for any damages, direct or indirect, resulting from the use of the
dataset.

*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3318333
`'validation'` | 15840

*   **Features**:

```json
{
    "image_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "caption": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## labeled


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conceptual_captions/labeled')
```

*   **Description**:

```
Google's Conceptual Captions dataset has more than 3 million images, paired with natural-language captions.
In contrast with the curated style of the MS-COCO images, Conceptual Captions images and their raw descriptions are harvested from the web,
and therefore represent a wider variety of styles. The raw descriptions are harvested from the Alt-text HTML attribute associated with web images.
The authors developed an automatic pipeline that extracts, filters, and transforms candidate image/caption pairs, with the goal of achieving a balance of cleanliness,
informativeness, fluency, and learnability of the resulting captions.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of
Google LLC ("Google") as the data source would be appreciated. The dataset is
provided "AS IS" without any warranty, express or implied. Google disclaims all
liability for any damages, direct or indirect, resulting from the use of the
dataset.

*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2007090

*   **Features**:

```json
{
    "image_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "caption": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "MIDs": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "confidence_scores": {
        "feature": {
            "dtype": "float64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


