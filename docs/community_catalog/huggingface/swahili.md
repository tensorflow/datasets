# swahili

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/swahili)
*   [Huggingface](https://huggingface.co/datasets/swahili)


## swahili


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:swahili/swahili')
```

*   **Description**:

```
The Swahili dataset developed specifically for language modeling task.
The dataset contains 28,000 unique words with 6.84M, 970k, and 2M words for the train,
valid and test partitions respectively which represent the ratio 80:10:10.
The entire dataset is lowercased, has no punctuation marks and,
the start and end of sentence markers have been incorporated to facilitate easy tokenization during language modeling.
```

*   **License**: Attribution 4.0 International
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3371
`'train'` | 42069
`'validation'` | 3372

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


