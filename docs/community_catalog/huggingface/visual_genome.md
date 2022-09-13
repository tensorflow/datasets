# visual_genome

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/visual_genome)
*   [Huggingface](https://huggingface.co/datasets/visual_genome)


## region_descriptions_v1.0.0


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:visual_genome/region_descriptions_v1.0.0')
```

*   **Description**:

```
Visual Genome enable to model objects and relationships between objects.
They collect dense annotations of objects, attributes, and relationships within each image.
Specifically, the dataset contains over 108K images where each image has an average of 35 objects, 26 attributes, and 21 pairwise relationships between objects.
```

*   **License**: Creative Commons Attribution 4.0 International License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 108077

*   **Features**:

```json
{
    "image": {
        "decode": true,
        "id": null,
        "_type": "Image"
    },
    "image_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "width": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "height": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "coco_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "flickr_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "regions": [
        {
            "region_id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "image_id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "phrase": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "x": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "y": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "width": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "height": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```


