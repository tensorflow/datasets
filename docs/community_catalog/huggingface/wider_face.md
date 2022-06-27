# wider_face

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wider_face)
*   [Huggingface](https://huggingface.co/datasets/wider_face)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wider_face')
```

*   **Description**:

```
WIDER FACE dataset is a face detection benchmark dataset, of which images are
selected from the publicly available WIDER dataset. We choose 32,203 images and
label 393,703 faces with a high degree of variability in scale, pose and
occlusion as depicted in the sample images. WIDER FACE dataset is organized
based on 61 event classes. For each event class, we randomly select 40%/10%/50%
data as training, validation and testing sets. We adopt the same evaluation
metric employed in the PASCAL VOC dataset. Similar to MALF and Caltech datasets,
we do not release bounding box ground truth for the test images. Users are
required to submit final prediction files, which we shall proceed to evaluate.
```

*   **License**: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 16097
`'train'` | 12880
`'validation'` | 3226

*   **Features**:

```json
{
    "image": {
        "decode": true,
        "id": null,
        "_type": "Image"
    },
    "faces": {
        "feature": {
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
            "blur": {
                "num_classes": 3,
                "names": [
                    "clear",
                    "normal",
                    "heavy"
                ],
                "id": null,
                "_type": "ClassLabel"
            },
            "expression": {
                "num_classes": 2,
                "names": [
                    "typical",
                    "exaggerate"
                ],
                "id": null,
                "_type": "ClassLabel"
            },
            "illumination": {
                "num_classes": 2,
                "names": [
                    "normal",
                    "exaggerate "
                ],
                "id": null,
                "_type": "ClassLabel"
            },
            "occlusion": {
                "num_classes": 3,
                "names": [
                    "no",
                    "partial",
                    "heavy"
                ],
                "id": null,
                "_type": "ClassLabel"
            },
            "pose": {
                "num_classes": 2,
                "names": [
                    "typical",
                    "atypical"
                ],
                "id": null,
                "_type": "ClassLabel"
            },
            "invalid": {
                "dtype": "bool",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


