# lccc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/lccc)
*   [Huggingface](https://huggingface.co/datasets/lccc)


## large


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lccc/large')
```

*   **Description**:

```
LCCC: Large-scale Cleaned Chinese Conversation corpus (LCCC) is a large corpus of Chinese conversations.
A rigorous data cleaning pipeline is designed to ensure the quality of the corpus.
This pipeline involves a set of rules and several classifier-based filters.
Noises such as offensive or sensitive words, special symbols, emojis,
grammatically incorrect sentences, and incoherent conversations are filtered.
```

*   **License**: MIT
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 12007759

*   **Features**:

```json
{
    "dialog": [
        {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    ]
}
```



## base


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lccc/base')
```

*   **Description**:

```
LCCC: Large-scale Cleaned Chinese Conversation corpus (LCCC) is a large corpus of Chinese conversations.
A rigorous data cleaning pipeline is designed to ensure the quality of the corpus.
This pipeline involves a set of rules and several classifier-based filters.
Noises such as offensive or sensitive words, special symbols, emojis,
grammatically incorrect sentences, and incoherent conversations are filtered.
```

*   **License**: MIT
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 6820506
`'validation'` | 20000

*   **Features**:

```json
{
    "dialog": [
        {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    ]
}
```


