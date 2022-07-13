# bookcorpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/bookcorpus)
*   [Huggingface](https://huggingface.co/datasets/bookcorpus)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bookcorpus/plain_text')
```

*   **Description**:

```
Books are a rich source of both fine-grained information, how a character, an object or a scene looks like, as well as high-level semantics, what someone is thinking, feeling and how these states evolve through a story.This work aims to align books to their movie releases in order to providerich descriptive explanations for visual content that go semantically farbeyond the captions available in current datasets.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 74004228

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


