# conceptual_12m

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/conceptual_12m)
*   [Huggingface](https://huggingface.co/datasets/conceptual_12m)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conceptual_12m')
```

*   **Description**:

```
Conceptual 12M is a large-scale dataset of 12 million
image-text pairs specifically meant to be used for visionand-language pre-training.
Its data collection pipeline is a relaxed version of the one used in Conceptual Captions 3M.
```

*   **License**: The dataset may be freely used for any purpose, although acknowledgement of
Google LLC ("Google") as the data source would be appreciated. The dataset is
provided "AS IS" without any warranty, express or implied. Google disclaims all
liability for any damages, direct or indirect, resulting from the use of the
dataset.

*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 12423374

*   **Features**:

```json
{
    "image_url": {
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


