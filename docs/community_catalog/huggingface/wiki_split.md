# wiki_split

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_split)
*   [Huggingface](https://huggingface.co/datasets/wiki_split)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_split')
```

*   **Description**:

```
One million English sentences, each split into two sentences that together preserve the original meaning, extracted from Wikipedia 
Google's WikiSplit dataset was constructed automatically from the publicly available Wikipedia revision history. Although 
the dataset contains some inherent noise, it can serve as valuable training data for models that split or merge sentences.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 989944
`'validation'` | 5000

*   **Features**:

```json
{
    "complex_sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simple_sentence_1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simple_sentence_2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


