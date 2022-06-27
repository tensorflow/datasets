# msr_zhen_translation_parity

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/msr_zhen_translation_parity)
*   [Huggingface](https://huggingface.co/datasets/msr_zhen_translation_parity)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:msr_zhen_translation_parity')
```

*   **Description**:

```
Translator Human Parity Data

Human evaluation results and translation output for the Translator Human Parity Data release, 
as described in https://blogs.microsoft.com/ai/machine-translation-news-test-set-human-parity/. 
The Translator Human Parity Data release contains all human evaluation results and translations
related to our paper "Achieving Human Parity on Automatic Chinese to English News Translation", 
published on March 14, 2018.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2001

*   **Features**:

```json
{
    "Reference-HT": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Reference-PE": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Combo-4": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Combo-5": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Combo-6": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Online-A-1710": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


