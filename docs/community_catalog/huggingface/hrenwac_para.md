# hrenwac_para

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hrenwac_para)
*   [Huggingface](https://huggingface.co/datasets/hrenwac_para)


## hrenWaC


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hrenwac_para/hrenWaC')
```

*   **Description**:

```
The hrenWaC corpus version 2.0 consists of parallel Croatian-English texts crawled from the .hr top-level domain for Croatia. The corpus was built with Spidextor (https://github.com/abumatran/spidextor), a tool that glues together the output of SpiderLing used for crawling and Bitextor used for bitext extraction. The accuracy of the extracted bitext on the segment level is around 80% and on the word level around 84%.
```

*   **License**: CC BY-SA 3.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 99001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "hr"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


