# moroco

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/moroco)
*   [Huggingface](https://huggingface.co/datasets/moroco)


## moroco


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:moroco/moroco')
```

*   **Description**:

```
The MOROCO (Moldavian and Romanian Dialectal Corpus) dataset contains 33564 samples of text collected from the news domain.
The samples belong to one of the following six topics:
    - culture
    - finance
    - politics
    - science
    - sports
    - tech
```

*   **License**: CC BY-SA 4.0 License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5924
`'train'` | 21719
`'validation'` | 5921

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "num_classes": 6,
        "names": [
            "culture",
            "finance",
            "politics",
            "science",
            "sports",
            "tech"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "sample": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


