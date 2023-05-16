# roman_urdu_hate_speech

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/roman_urdu_hate_speech)
*   [Huggingface](https://huggingface.co/datasets/roman_urdu_hate_speech)


## Coarse_Grained


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:roman_urdu_hate_speech/Coarse_Grained')
```

*   **Description**:

```
The Roman Urdu Hate-Speech and Offensive Language Detection (RUHSOLD) dataset is a  Roman Urdu dataset of tweets annotated by experts in the relevant language.  The authors develop the gold-standard for two sub-tasks.  First sub-task is based on binary labels of Hate-Offensive content and Normal content (i.e., inoffensive language).  These labels are self-explanatory.  The authors refer to this sub-task as coarse-grained classification.  Second sub-task defines Hate-Offensive content with  four labels at a granular level.  These labels are the most relevant for the demographic of users who converse in RU and  are defined in related literature. The authors refer to this sub-task as fine-grained classification.  The objective behind creating two gold-standards is to enable the researchers to evaluate the hate speech detection  approaches on both easier (coarse-grained) and challenging (fine-grained) scenarios.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2002
`'train'` | 7208
`'validation'` | 800

*   **Features**:

```json
{
    "tweet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "Abusive/Offensive",
            "Normal"
        ],
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## Fine_Grained


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:roman_urdu_hate_speech/Fine_Grained')
```

*   **Description**:

```
The Roman Urdu Hate-Speech and Offensive Language Detection (RUHSOLD) dataset is a  Roman Urdu dataset of tweets annotated by experts in the relevant language.  The authors develop the gold-standard for two sub-tasks.  First sub-task is based on binary labels of Hate-Offensive content and Normal content (i.e., inoffensive language).  These labels are self-explanatory.  The authors refer to this sub-task as coarse-grained classification.  Second sub-task defines Hate-Offensive content with  four labels at a granular level.  These labels are the most relevant for the demographic of users who converse in RU and  are defined in related literature. The authors refer to this sub-task as fine-grained classification.  The objective behind creating two gold-standards is to enable the researchers to evaluate the hate speech detection  approaches on both easier (coarse-grained) and challenging (fine-grained) scenarios.
```

*   **License**: MIT License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2002
`'train'` | 7208
`'validation'` | 7208

*   **Features**:

```json
{
    "tweet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 5,
        "names": [
            "Abusive/Offensive",
            "Normal",
            "Religious Hate",
            "Sexism",
            "Profane/Untargeted"
        ],
        "id": null,
        "_type": "ClassLabel"
    }
}
```


