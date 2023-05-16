# irc_disentangle

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/irc_disentangle)
*   [Huggingface](https://huggingface.co/datasets/irc_disentangle)


## ubuntu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:irc_disentangle/ubuntu')
```

*   **Description**:

```
Disentangling conversations mixed together in a single stream of messages is
a difficult task, made harder by the lack of large manually annotated
datasets. This new dataset of 77,563 messages manually annotated with
reply-structure graphs that both disentangle conversations and define
internal conversation structure. The dataset is 16 times larger than all
previously released datasets combined, the first to include adjudication of
annotation disagreements, and the first to include context.
```

*   **License**: Creative Commons Attribution 4.0 International Public License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15010
`'train'` | 220616
`'validation'` | 12510

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "raw": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ascii": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokenized": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "connections": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## channel_two


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:irc_disentangle/channel_two')
```

*   **Description**:

```
Disentangling conversations mixed together in a single stream of messages is
a difficult task, made harder by the lack of large manually annotated
datasets. This new dataset of 77,563 messages manually annotated with
reply-structure graphs that both disentangle conversations and define
internal conversation structure. The dataset is 16 times larger than all
previously released datasets combined, the first to include adjudication of
annotation disagreements, and the first to include context.
```

*   **License**: Creative Commons Attribution 4.0 International Public License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'all_'` | 2602
`'dev'` | 1001
`'pilot'` | 501
`'pilot_dev'` | 1501
`'test'` | 1001

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "raw": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ascii": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokenized": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "connections": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


