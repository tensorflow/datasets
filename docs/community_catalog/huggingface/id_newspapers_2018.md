# id_newspapers_2018

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/id_newspapers_2018)
*   [Huggingface](https://huggingface.co/datasets/id_newspapers_2018)


## id_newspapers_2018


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:id_newspapers_2018/id_newspapers_2018')
```

*   **Description**:

```
The dataset contains around 500K articles (136M of words) from 7 Indonesian newspapers: Detik, Kompas, Tempo,
CNN Indonesia, Sindo, Republika and Poskota. The articles are dated between 1st January 2018 and 20th August 2018
(with few exceptions dated earlier). The size of uncompressed 500K json files (newspapers-json.tgz) is around 2.2GB,
and the cleaned uncompressed in a big text file (newspapers.txt.gz) is about 1GB. The original source in Google Drive
contains also a dataset in html format which include raw data (pictures, css, javascript, ...)
from the online news website
```

*   **License**: Creative Commons Attribution-ShareAlike 4.0 International Public License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 499164

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


