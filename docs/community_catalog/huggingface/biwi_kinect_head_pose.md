# biwi_kinect_head_pose

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/biwi_kinect_head_pose)
*   [Huggingface](https://huggingface.co/datasets/biwi_kinect_head_pose)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:biwi_kinect_head_pose')
```

*   **Description**:

```
The Biwi Kinect Head Pose Database is acquired with the Microsoft Kinect sensor, a structured IR light device.It contains 15K images of 20 people with 6 females and 14 males where 4 people were recorded twice.
```

*   **License**: This database is made available for non-commercial use such as university research and education.
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 24

*   **Features**:

```json
{
    "sequence_number": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subject_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rgb": {
        "feature": {
            "decode": true,
            "id": null,
            "_type": "Image"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "rgb_cal": {
        "intrisic_mat": {
            "shape": [
                3,
                3
            ],
            "dtype": "float64",
            "id": null,
            "_type": "Array2D"
        },
        "extrinsic_mat": {
            "rotation": {
                "shape": [
                    3,
                    3
                ],
                "dtype": "float64",
                "id": null,
                "_type": "Array2D"
            },
            "translation": {
                "feature": {
                    "dtype": "float64",
                    "id": null,
                    "_type": "Value"
                },
                "length": 3,
                "id": null,
                "_type": "Sequence"
            }
        }
    },
    "depth": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "depth_cal": {
        "intrisic_mat": {
            "shape": [
                3,
                3
            ],
            "dtype": "float64",
            "id": null,
            "_type": "Array2D"
        },
        "extrinsic_mat": {
            "rotation": {
                "shape": [
                    3,
                    3
                ],
                "dtype": "float64",
                "id": null,
                "_type": "Array2D"
            },
            "translation": {
                "feature": {
                    "dtype": "float64",
                    "id": null,
                    "_type": "Value"
                },
                "length": 3,
                "id": null,
                "_type": "Sequence"
            }
        }
    },
    "head_pose_gt": {
        "feature": {
            "center": {
                "feature": {
                    "dtype": "float64",
                    "id": null,
                    "_type": "Value"
                },
                "length": 3,
                "id": null,
                "_type": "Sequence"
            },
            "rotation": {
                "shape": [
                    3,
                    3
                ],
                "dtype": "float64",
                "id": null,
                "_type": "Array2D"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "head_template": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


