# tunizi

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tunizi)
*   [Huggingface](https://huggingface.co/datasets/tunizi)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tunizi')
```

*   **Description**:

```
On social media, Arabic speakers tend to express themselves in their own local dialect. To do so, Tunisians use "Tunisian Arabizi", which consists in supplementing numerals to the Latin script rather than the Arabic alphabet. TUNIZI is the first Tunisian Arabizi Dataset including 3K sentences, balanced, covering different topics, preprocessed and annotated as positive and negative.
```

*   **License**: No known license
*   **Version**: 0.9.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3000

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "num_classes": 2,
        "names": [
            "1",
            "-1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


