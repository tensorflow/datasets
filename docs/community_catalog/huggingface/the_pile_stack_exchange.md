# the_pile_stack_exchange

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/the_pile_stack_exchange)
*   [Huggingface](https://huggingface.co/datasets/the_pile_stack_exchange)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:the_pile_stack_exchange/plain_text')
```

*   **Description**:

```
This dataset is part of EleutherAI/The Pile dataset and is a dataset for Language Models from processing stackexchange data dump, which is an anonymized dump of all user-contributed content on the Stack Exchange network.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5096117

*   **Features**:

```json
{
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


