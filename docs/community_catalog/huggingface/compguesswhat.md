# compguesswhat

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/compguesswhat)
*   [Huggingface](https://huggingface.co/datasets/compguesswhat)


## compguesswhat-original


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:compguesswhat/compguesswhat-original')
```

*   **Description**:

```
CompGuessWhat?! is an instance of a multi-task framework for evaluating the quality of learned neural representations,
        in particular concerning attribute grounding. Use this dataset if you want to use the set of games whose reference
        scene is an image in VisualGenome. Visit the website for more details: https://compguesswhat.github.io
```

*   **License**: No known license
*   **Version**: 0.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9621
`'train'` | 46341
`'validation'` | 9738

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "target_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "timestamp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "status": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "image": {
        "id": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "file_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "flickr_url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "coco_url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "height": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "width": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "visual_genome": {
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
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "coco_id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "flickr_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "image_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        }
    },
    "qas": {
        "feature": {
            "question": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "objects": {
        "feature": {
            "id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "bbox": {
                "feature": {
                    "dtype": "float32",
                    "id": null,
                    "_type": "Value"
                },
                "length": 4,
                "id": null,
                "_type": "Sequence"
            },
            "category": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "area": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "category_id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "segment": {
                "feature": {
                    "feature": {
                        "dtype": "float32",
                        "id": null,
                        "_type": "Value"
                    },
                    "length": -1,
                    "id": null,
                    "_type": "Sequence"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## compguesswhat-zero_shot


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:compguesswhat/compguesswhat-zero_shot')
```

*   **Description**:

```
CompGuessWhat?! is an instance of a multi-task framework for evaluating the quality of learned neural representations,
        in particular concerning attribute grounding. Use this dataset if you want to use the set of games whose reference
        scene is an image in VisualGenome. Visit the website for more details: https://compguesswhat.github.io
```

*   **License**: No known license
*   **Version**: 0.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'nd_test'` | 13836
`'nd_valid'` | 5343
`'od_test'` | 13300
`'od_valid'` | 5372

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "target_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "status": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "image": {
        "id": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "file_name": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "coco_url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "height": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "width": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "license": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "open_images_id": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "date_captured": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "objects": {
        "feature": {
            "id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "bbox": {
                "feature": {
                    "dtype": "float32",
                    "id": null,
                    "_type": "Value"
                },
                "length": 4,
                "id": null,
                "_type": "Sequence"
            },
            "category": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "area": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "category_id": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "IsOccluded": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "IsTruncated": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "segment": {
                "feature": {
                    "MaskPath": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "LabelName": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "BoxID": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "BoxXMin": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "BoxXMax": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "BoxYMin": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "BoxYMax": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "PredictedIoU": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "Clicks": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


