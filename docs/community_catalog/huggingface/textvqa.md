# textvqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/textvqa)
*   [Huggingface](https://huggingface.co/datasets/textvqa)


## train


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:textvqa/train')
```

*   **Description**:

```
TextVQA requires models to read and reason about text in images to answer questions about them. 
Specifically, models need to incorporate a new modality of text present in the images and reason 
over it to answer TextVQA questions. TextVQA dataset contains 45,336 questions over 28,408 images
from the OpenImages dataset.
```

*   **License**: CC BY 4.0
*   **Version**: 0.5.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5734
`'train'` | 34602
`'validation'` | 5000

*   **Features**:

```json
{
    "image_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "image": {
        "decode": true,
        "id": null,
        "_type": "Image"
    },
    "image_width": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "image_height": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "flickr_original_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "flickr_300k_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "image_classes": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "set_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## val


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:textvqa/val')
```

*   **Description**:

```
TextVQA requires models to read and reason about text in images to answer questions about them. 
Specifically, models need to incorporate a new modality of text present in the images and reason 
over it to answer TextVQA questions. TextVQA dataset contains 45,336 questions over 28,408 images
from the OpenImages dataset.
```

*   **License**: CC BY 4.0
*   **Version**: 0.5.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5734
`'train'` | 34602
`'validation'` | 5000

*   **Features**:

```json
{
    "image_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "image": {
        "decode": true,
        "id": null,
        "_type": "Image"
    },
    "image_width": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "image_height": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "flickr_original_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "flickr_300k_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "image_classes": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "set_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## test


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:textvqa/test')
```

*   **Description**:

```
TextVQA requires models to read and reason about text in images to answer questions about them. 
Specifically, models need to incorporate a new modality of text present in the images and reason 
over it to answer TextVQA questions. TextVQA dataset contains 45,336 questions over 28,408 images
from the OpenImages dataset.
```

*   **License**: CC BY 4.0
*   **Version**: 0.5.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5734
`'train'` | 34602
`'validation'` | 5000

*   **Features**:

```json
{
    "image_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "image": {
        "decode": true,
        "id": null,
        "_type": "Image"
    },
    "image_width": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "image_height": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "flickr_original_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "flickr_300k_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "image_classes": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "set_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## textvqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:textvqa/textvqa')
```

*   **Description**:

```
TextVQA requires models to read and reason about text in images to answer questions about them.
Specifically, models need to incorporate a new modality of text present in the images and reason
over it to answer TextVQA questions. TextVQA dataset contains 45,336 questions over 28,408 images
from the OpenImages dataset.
```

*   **License**: CC BY 4.0
*   **Version**: 0.5.1
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5734
`'train'` | 34602
`'validation'` | 5000

*   **Features**:

```json
{
    "image_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question_tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "image": {
        "decode": true,
        "id": null,
        "_type": "Image"
    },
    "image_width": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "image_height": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "flickr_original_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "flickr_300k_url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "image_classes": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "set_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


