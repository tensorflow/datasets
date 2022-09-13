# medmcqa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/medmcqa)
*   [Huggingface](https://huggingface.co/datasets/medmcqa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:medmcqa')
```

*   **Description**:

```
MedMCQA is a large-scale, Multiple-Choice Question Answering (MCQA) dataset designed to address real-world medical entrance exam questions. 
MedMCQA has more than 194k high-quality AIIMS & NEET PG entrance exam MCQs covering 2.4k healthcare topics and 21 medical subjects are collected with an average token length of 12.77 and high topical diversity.
The dataset contains questions about the following topics: Anesthesia, Anatomy, Biochemistry, Dental, ENT, Forensic Medicine (FM)
Obstetrics and Gynecology (O&G), Medicine, Microbiology, Ophthalmology, Orthopedics Pathology, Pediatrics, Pharmacology, Physiology, 
Psychiatry, Radiology Skin, Preventive & Social Medicine (PSM) and Surgery
```

*   **License**: Apache License 2.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6150
`'train'` | 182822
`'validation'` | 4183

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "opa": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "opb": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "opc": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "opd": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "cop": {
        "num_classes": 4,
        "names": [
            "a",
            "b",
            "c",
            "d"
        ],
        "id": null,
        "_type": "ClassLabel"
    },
    "choice_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "exp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "subject_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "topic_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


