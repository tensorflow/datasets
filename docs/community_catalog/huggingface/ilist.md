# ilist

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ilist)
*   [Huggingface](https://huggingface.co/datasets/ilist)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ilist')
```

*   **Description**:

```
This dataset is introduced in a task which aimed at identifying 5 closely-related languages of Indo-Aryan language family –
Hindi (also known as Khari Boli), Braj Bhasha, Awadhi, Bhojpuri, and Magahi.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9692
`'train'` | 70351
`'validation'` | 10329

*   **Features**:

```json
{
    "language_id": {
        "num_classes": 5,
        "names": [
            "AWA",
            "BRA",
            "MAG",
            "BHO",
            "HIN"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


