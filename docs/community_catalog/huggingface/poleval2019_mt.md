# poleval2019_mt

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/poleval2019_mt)
*   [Huggingface](https://huggingface.co/datasets/poleval2019_mt)


## ru-pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:poleval2019_mt/ru-pl')
```

*   **Description**:

```
PolEval is a SemEval-inspired evaluation campaign for natural language processing tools for Polish.Submitted solutions compete against one another within certain tasks selected by organizers, using available data and are evaluated according topre-established procedures. One of the tasks in PolEval-2019 was Machine Translation (Task-4).
The task is to train as good as possible machine translation system, using any technology,with limited textual resources.The competition will be done for 2 language pairs, more popular English-Polish (into Polish direction) and pair that can be called low resourcedRussian-Polish (in both directions).

Here, Polish-English is also made available to allow for training in both directions. However, the test data is ONLY available for English-Polish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2969
`'train'` | 20001
`'validation'` | 3001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "ru",
            "pl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## en-pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:poleval2019_mt/en-pl')
```

*   **Description**:

```
PolEval is a SemEval-inspired evaluation campaign for natural language processing tools for Polish.Submitted solutions compete against one another within certain tasks selected by organizers, using available data and are evaluated according topre-established procedures. One of the tasks in PolEval-2019 was Machine Translation (Task-4).
The task is to train as good as possible machine translation system, using any technology,with limited textual resources.The competition will be done for 2 language pairs, more popular English-Polish (into Polish direction) and pair that can be called low resourcedRussian-Polish (in both directions).

Here, Polish-English is also made available to allow for training in both directions. However, the test data is ONLY available for English-Polish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9845
`'train'` | 129255
`'validation'` | 10001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "pl"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## pl-ru


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:poleval2019_mt/pl-ru')
```

*   **Description**:

```
PolEval is a SemEval-inspired evaluation campaign for natural language processing tools for Polish.Submitted solutions compete against one another within certain tasks selected by organizers, using available data and are evaluated according topre-established procedures. One of the tasks in PolEval-2019 was Machine Translation (Task-4).
The task is to train as good as possible machine translation system, using any technology,with limited textual resources.The competition will be done for 2 language pairs, more popular English-Polish (into Polish direction) and pair that can be called low resourcedRussian-Polish (in both directions).

Here, Polish-English is also made available to allow for training in both directions. However, the test data is ONLY available for English-Polish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2967
`'train'` | 20001
`'validation'` | 3001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "pl",
            "ru"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## pl-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:poleval2019_mt/pl-en')
```

*   **Description**:

```
PolEval is a SemEval-inspired evaluation campaign for natural language processing tools for Polish.Submitted solutions compete against one another within certain tasks selected by organizers, using available data and are evaluated according topre-established procedures. One of the tasks in PolEval-2019 was Machine Translation (Task-4).
The task is to train as good as possible machine translation system, using any technology,with limited textual resources.The competition will be done for 2 language pairs, more popular English-Polish (into Polish direction) and pair that can be called low resourcedRussian-Polish (in both directions).

Here, Polish-English is also made available to allow for training in both directions. However, the test data is ONLY available for English-Polish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1
`'train'` | 129255
`'validation'` | 10001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "pl",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


