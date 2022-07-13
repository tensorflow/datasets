# vivos

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/vivos)
*   [Huggingface](https://huggingface.co/datasets/vivos)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:vivos')
```

*   **Description**:

```
VIVOS is a free Vietnamese speech corpus consisting of 15 hours of recording speech prepared for
Vietnamese Automatic Speech Recognition task.
The corpus was prepared by AILAB, a computer science lab of VNUHCM - University of Science, with Prof. Vu Hai Quan is the head of.
We publish this corpus in hope to attract more scientists to solve Vietnamese speech recognition problems.
```

*   **License**: cc-by-sa-4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 760
`'train'` | 11660

*   **Features**:

```json
{
    "speaker_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "path": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 16000,
        "mono": true,
        "_storage_dtype": "struct",
        "id": null,
        "_type": "Audio"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


