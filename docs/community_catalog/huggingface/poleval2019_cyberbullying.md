# poleval2019_cyberbullying

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/poleval2019_cyberbullying)
*   [Huggingface](https://huggingface.co/datasets/poleval2019_cyberbullying)


## task01


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:poleval2019_cyberbullying/task01')
```

*   **Description**:

```
In Task 6-1, the participants are to distinguish between normal/non-harmful tweets (class: 0) and tweets
    that contain any kind of harmful information (class: 1). This includes cyberbullying, hate speech and
    related phenomena.

    In Task 6-2, the participants shall distinguish between three classes of tweets: 0 (non-harmful),
    1 (cyberbullying), 2 (hate-speech). There are various definitions of both cyberbullying and hate-speech,
    some of them even putting those two phenomena in the same group. The specific conditions on which we based
    our annotations for both cyberbullying and hate-speech, which have been worked out during ten years of research
    will be summarized in an introductory paper for the task, however, the main and definitive condition to 1
    distinguish the two is whether the harmful action is addressed towards a private person(s) (cyberbullying),
    or a public person/entity/large group (hate-speech).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10041

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
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## task02


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:poleval2019_cyberbullying/task02')
```

*   **Description**:

```
In Task 6-1, the participants are to distinguish between normal/non-harmful tweets (class: 0) and tweets
    that contain any kind of harmful information (class: 1). This includes cyberbullying, hate speech and
    related phenomena.

    In Task 6-2, the participants shall distinguish between three classes of tweets: 0 (non-harmful),
    1 (cyberbullying), 2 (hate-speech). There are various definitions of both cyberbullying and hate-speech,
    some of them even putting those two phenomena in the same group. The specific conditions on which we based
    our annotations for both cyberbullying and hate-speech, which have been worked out during ten years of research
    will be summarized in an introductory paper for the task, however, the main and definitive condition to 1
    distinguish the two is whether the harmful action is addressed towards a private person(s) (cyberbullying),
    or a public person/entity/large group (hate-speech).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 10041

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
            "0",
            "1",
            "2"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


