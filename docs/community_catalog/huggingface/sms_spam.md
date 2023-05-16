# sms_spam

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sms_spam)
*   [Huggingface](https://huggingface.co/datasets/sms_spam)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sms_spam/plain_text')
```

*   **Description**:

```
The SMS Spam Collection v.1 is a public set of SMS labeled messages that have been collected for mobile phone spam research.
It has one collection composed by 5,574 English, real and non-enconded messages, tagged according being legitimate (ham) or spam.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5574

*   **Features**:

```json
{
    "sms": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "ham",
            "spam"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


