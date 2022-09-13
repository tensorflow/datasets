# offenseval_dravidian

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/offenseval_dravidian)
*   [Huggingface](https://huggingface.co/datasets/offenseval_dravidian)


## tamil


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:offenseval_dravidian/tamil')
```

*   **Description**:

```
Offensive language identification in dravidian lanaguages dataset. The goal of this task is to identify offensive language content of the code-mixed dataset of comments/posts in Dravidian Languages ( (Tamil-English, Malayalam-English, and Kannada-English)) collected from social media.
```

*   **License**: Creative Commons Attribution 4.0 International Licence
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 35139
`'validation'` | 4388

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 6,
        "names": [
            "Not_offensive",
            "Offensive_Untargetede",
            "Offensive_Targeted_Insult_Individual",
            "Offensive_Targeted_Insult_Group",
            "Offensive_Targeted_Insult_Other",
            "not-Tamil"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## malayalam


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:offenseval_dravidian/malayalam')
```

*   **Description**:

```
Offensive language identification in dravidian lanaguages dataset. The goal of this task is to identify offensive language content of the code-mixed dataset of comments/posts in Dravidian Languages ( (Tamil-English, Malayalam-English, and Kannada-English)) collected from social media.
```

*   **License**: Creative Commons Attribution 4.0 International Licence
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 16010
`'validation'` | 1999

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 6,
        "names": [
            "Not_offensive",
            "Offensive_Untargetede",
            "Offensive_Targeted_Insult_Individual",
            "Offensive_Targeted_Insult_Group",
            "Offensive_Targeted_Insult_Other",
            "not-malayalam"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## kannada


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:offenseval_dravidian/kannada')
```

*   **Description**:

```
Offensive language identification in dravidian lanaguages dataset. The goal of this task is to identify offensive language content of the code-mixed dataset of comments/posts in Dravidian Languages ( (Tamil-English, Malayalam-English, and Kannada-English)) collected from social media.
```

*   **License**: Creative Commons Attribution 4.0 International Licence
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 6217
`'validation'` | 777

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 6,
        "names": [
            "Not_offensive",
            "Offensive_Untargetede",
            "Offensive_Targeted_Insult_Individual",
            "Offensive_Targeted_Insult_Group",
            "Offensive_Targeted_Insult_Other",
            "not-Kannada"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


