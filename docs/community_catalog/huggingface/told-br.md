# told-br

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/told-br)
*   [Huggingface](https://huggingface.co/datasets/told-br)


## multilabel


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:told-br/multilabel')
```

*   **Description**:

```
ToLD-Br is the biggest dataset for toxic tweets in Brazilian Portuguese, crowdsourced
by 42 annotators selected from a pool of 129 volunteers. Annotators were selected aiming
to create a plural group in terms of demographics (ethnicity, sexual orientation, age, gender).
Each tweet was labeled by three annotators in 6 possible categories:
LGBTQ+phobia,Xenophobia, Obscene, Insult, Misogyny and Racism.
```

*   **License**: https://github.com/JAugusto97/ToLD-Br/blob/main/LICENSE_ToLD-Br.txt 
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 21000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "homophobia": {
        "num_classes": 4,
        "names": [
            "zero_votes",
            "one_vote",
            "two_votes",
            "three_votes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "obscene": {
        "num_classes": 4,
        "names": [
            "zero_votes",
            "one_vote",
            "two_votes",
            "three_votes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "insult": {
        "num_classes": 4,
        "names": [
            "zero_votes",
            "one_vote",
            "two_votes",
            "three_votes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "racism": {
        "num_classes": 4,
        "names": [
            "zero_votes",
            "one_vote",
            "two_votes",
            "three_votes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "misogyny": {
        "num_classes": 4,
        "names": [
            "zero_votes",
            "one_vote",
            "two_votes",
            "three_votes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "xenophobia": {
        "num_classes": 4,
        "names": [
            "zero_votes",
            "one_vote",
            "two_votes",
            "three_votes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## binary


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:told-br/binary')
```

*   **Description**:

```
ToLD-Br is the biggest dataset for toxic tweets in Brazilian Portuguese, crowdsourced
by 42 annotators selected from a pool of 129 volunteers. Annotators were selected aiming
to create a plural group in terms of demographics (ethnicity, sexual orientation, age, gender).
Each tweet was labeled by three annotators in 6 possible categories:
LGBTQ+phobia,Xenophobia, Obscene, Insult, Misogyny and Racism.
```

*   **License**: https://github.com/JAugusto97/ToLD-Br/blob/main/LICENSE_ToLD-Br.txt 
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2100
`'train'` | 16800
`'validation'` | 2100

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
            "not-toxic",
            "toxic"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


