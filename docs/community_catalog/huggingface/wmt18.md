# wmt18

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wmt18)
*   [Huggingface](https://huggingface.co/datasets/wmt18)


## cs-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt18/cs-en')
```

*   **Description**:

```
Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `datasets.translate.wmt.WmtConfig`.


config = datasets.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        datasets.Split.TRAIN: ["commoncrawl_frde"],
        datasets.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = datasets.builder("wmt_translate", config=config)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2983
`'train'` | 11046024
`'validation'` | 3005

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "cs",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## de-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt18/de-en')
```

*   **Description**:

```
Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `datasets.translate.wmt.WmtConfig`.


config = datasets.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        datasets.Split.TRAIN: ["commoncrawl_frde"],
        datasets.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = datasets.builder("wmt_translate", config=config)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2998
`'train'` | 42271874
`'validation'` | 3004

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "de",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## et-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt18/et-en')
```

*   **Description**:

```
Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `datasets.translate.wmt.WmtConfig`.


config = datasets.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        datasets.Split.TRAIN: ["commoncrawl_frde"],
        datasets.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = datasets.builder("wmt_translate", config=config)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2000
`'train'` | 2175873
`'validation'` | 2000

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "et",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## fi-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt18/fi-en')
```

*   **Description**:

```
Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `datasets.translate.wmt.WmtConfig`.


config = datasets.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        datasets.Split.TRAIN: ["commoncrawl_frde"],
        datasets.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = datasets.builder("wmt_translate", config=config)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3000
`'train'` | 3280600
`'validation'` | 6004

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "fi",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## kk-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt18/kk-en')
```

*   **Description**:

```
Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `datasets.translate.wmt.WmtConfig`.


config = datasets.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        datasets.Split.TRAIN: ["commoncrawl_frde"],
        datasets.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = datasets.builder("wmt_translate", config=config)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 0
`'train'` | 0
`'validation'` | 0

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "kk",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## ru-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt18/ru-en')
```

*   **Description**:

```
Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `datasets.translate.wmt.WmtConfig`.


config = datasets.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        datasets.Split.TRAIN: ["commoncrawl_frde"],
        datasets.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = datasets.builder("wmt_translate", config=config)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3000
`'train'` | 36858512
`'validation'` | 3001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "ru",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## tr-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt18/tr-en')
```

*   **Description**:

```
Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `datasets.translate.wmt.WmtConfig`.


config = datasets.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        datasets.Split.TRAIN: ["commoncrawl_frde"],
        datasets.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = datasets.builder("wmt_translate", config=config)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3000
`'train'` | 205756
`'validation'` | 3007

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "tr",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```



## zh-en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wmt18/zh-en')
```

*   **Description**:

```
Translate dataset based on the data from statmt.org.

Versions exists for the different years using a combination of multiple data
sources. The base `wmt_translate` allows you to create your own config to choose
your own data/language pair by creating a custom `datasets.translate.wmt.WmtConfig`.


config = datasets.wmt.WmtConfig(
    version="0.0.1",
    language_pair=("fr", "de"),
    subsets={
        datasets.Split.TRAIN: ["commoncrawl_frde"],
        datasets.Split.VALIDATION: ["euelections_dev2019"],
    },
)
builder = datasets.builder("wmt_translate", config=config)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3981
`'train'` | 25160346
`'validation'` | 2001

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "zh",
            "en"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


