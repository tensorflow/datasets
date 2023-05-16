# civil_comments

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/civil_comments)
*   [Huggingface](https://huggingface.co/datasets/civil_comments)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:civil_comments')
```

*   **Description**:

```
The comments in this dataset come from an archive of the Civil Comments
platform, a commenting plugin for independent news sites. These public comments
were created from 2015 - 2017 and appeared on approximately 50 English-language
news sites across the world. When Civil Comments shut down in 2017, they chose
to make the public comments available in a lasting open archive to enable future
research. The original data, published on figshare, includes the public comment
text, some associated metadata such as article IDs, timestamps and
commenter-generated "civility" labels, but does not include user ids. Jigsaw
extended this dataset by adding additional labels for toxicity and identity
mentions. This data set is an exact replica of the data released for the
Jigsaw Unintended Bias in Toxicity Classification Kaggle challenge.  This
dataset is released under CC0, as is the underlying comment text.
```

*   **License**: No known license
*   **Version**: 0.9.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 97320
`'train'` | 1804874
`'validation'` | 97320

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "toxicity": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "severe_toxicity": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "obscene": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "threat": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "insult": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "identity_attack": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "sexual_explicit": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


