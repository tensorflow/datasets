# telugu_books

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/telugu_books)
*   [Huggingface](https://huggingface.co/datasets/telugu_books)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:telugu_books')
```

*   **Description**:

```
This dataset is created by scraping telugu novels from teluguone.com this dataset can be used for nlp tasks like topic modeling, word embeddings, transfer learning etc
```

*   **License**: Data files © Original Authors
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 25794

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


