# sbu_captions

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sbu_captions)
*   [Huggingface](https://huggingface.co/datasets/sbu_captions)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sbu_captions')
```

*   **Description**:

```
The SBU Captioned Photo Dataset is a collection of over 1 million images with associated text descriptions extracted from Flicker.
```

*   **License**: unknown
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1000000

*   **Features**:

```json
{
    "image_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "user_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "caption": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


