# the_pile_books3

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/the_pile_books3)
*   [Huggingface](https://huggingface.co/datasets/the_pile_books3)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:the_pile_books3/plain_text')
```

*   **Description**:

```
This dataset is Shawn Presser's work and is part of EleutherAi/The Pile dataset. This dataset contains all of bibliotik in plain .txt form, aka 197,000 books processed in exactly the same way as did for bookcorpusopen (a.k.a. books1). seems to be similar to OpenAI's mysterious "books2" dataset referenced in their papers. Unfortunately OpenAI will not give details, so we know very little about any differences. People suspect it's "all of libgen", but it's purely conjecture.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 196639

*   **Features**:

```json
{
    "title": {
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


