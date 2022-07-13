# narrativeqa_manual

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/narrativeqa_manual)
*   [Huggingface](https://huggingface.co/datasets/narrativeqa_manual)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:narrativeqa_manual')
```

*   **Description**:

```
The Narrative QA Manual dataset is a reading comprehension dataset, in which the reader must answer questions about stories by reading entire books or movie scripts. The QA tasks are designed so that successfully answering their questions requires understanding the underlying narrative rather than relying on shallow pattern matching or salience.\
THIS DATASET REQUIRES A MANUALLY DOWNLOADED FILE! Because of a script in the original repository which downloads the stories from original URLs everytime, The links are sometimes broken or invalid.  Therefore, you need to manually download the stories for this dataset using the script provided by the authors (https://github.com/deepmind/narrativeqa/blob/master/download_stories.sh). Running the shell script creates a folder named "tmp" in the root directory and downloads the stories there. This folder containing the storiescan be used to load the dataset via `datasets.load_dataset("narrativeqa_manual", data_dir="<path/to/folder>")`.
```

*   **License**: https://github.com/deepmind/narrativeqa/blob/master/LICENSE
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10557
`'train'` | 32747
`'validation'` | 3461

*   **Features**:

```json
{
    "document": {
        "id": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "kind": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "url": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "file_size": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "word_count": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "start": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "end": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "summary": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "tokens": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            },
            "url": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "title": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "question": {
        "text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "tokens": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        }
    },
    "answers": [
        {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "tokens": {
                "feature": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        }
    ]
}
```


