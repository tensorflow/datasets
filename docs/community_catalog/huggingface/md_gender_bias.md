# md_gender_bias

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/md_gender_bias)
*   [Huggingface](https://huggingface.co/datasets/md_gender_bias)


## gendered_words


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/gendered_words')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 222

*   **Features**:

```json
{
    "word_masculine": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "word_feminine": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## name_genders


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/name_genders')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'yob1880'` | 2000
`'yob1881'` | 1935
`'yob1882'` | 2127
`'yob1883'` | 2084
`'yob1884'` | 2297
`'yob1885'` | 2294
`'yob1886'` | 2392
`'yob1887'` | 2373
`'yob1888'` | 2651
`'yob1889'` | 2590
`'yob1890'` | 2695
`'yob1891'` | 2660
`'yob1892'` | 2921
`'yob1893'` | 2831
`'yob1894'` | 2941
`'yob1895'` | 3049
`'yob1896'` | 3091
`'yob1897'` | 3028
`'yob1898'` | 3264
`'yob1899'` | 3042
`'yob1900'` | 3730
`'yob1901'` | 3153
`'yob1902'` | 3362
`'yob1903'` | 3389
`'yob1904'` | 3560
`'yob1905'` | 3655
`'yob1906'` | 3633
`'yob1907'` | 3948
`'yob1908'` | 4018
`'yob1909'` | 4227
`'yob1910'` | 4629
`'yob1911'` | 4867
`'yob1912'` | 6351
`'yob1913'` | 6968
`'yob1914'` | 7965
`'yob1915'` | 9357
`'yob1916'` | 9696
`'yob1917'` | 9913
`'yob1918'` | 10398
`'yob1919'` | 10369
`'yob1920'` | 10756
`'yob1921'` | 10857
`'yob1922'` | 10756
`'yob1923'` | 10643
`'yob1924'` | 10869
`'yob1925'` | 10638
`'yob1926'` | 10458
`'yob1927'` | 10406
`'yob1928'` | 10159
`'yob1929'` | 9820
`'yob1930'` | 9791
`'yob1931'` | 9298
`'yob1932'` | 9381
`'yob1933'` | 9013
`'yob1934'` | 9180
`'yob1935'` | 9037
`'yob1936'` | 8894
`'yob1937'` | 8946
`'yob1938'` | 9032
`'yob1939'` | 8918
`'yob1940'` | 8961
`'yob1941'` | 9085
`'yob1942'` | 9425
`'yob1943'` | 9408
`'yob1944'` | 9152
`'yob1945'` | 9025
`'yob1946'` | 9705
`'yob1947'` | 10371
`'yob1948'` | 10241
`'yob1949'` | 10269
`'yob1950'` | 10303
`'yob1951'` | 10462
`'yob1952'` | 10646
`'yob1953'` | 10837
`'yob1954'` | 10968
`'yob1955'` | 11115
`'yob1956'` | 11340
`'yob1957'` | 11564
`'yob1958'` | 11522
`'yob1959'` | 11767
`'yob1960'` | 11921
`'yob1961'` | 12182
`'yob1962'` | 12209
`'yob1963'` | 12282
`'yob1964'` | 12397
`'yob1965'` | 11952
`'yob1966'` | 12151
`'yob1967'` | 12397
`'yob1968'` | 12936
`'yob1969'` | 13749
`'yob1970'` | 14779
`'yob1971'` | 15295
`'yob1972'` | 15412
`'yob1973'` | 15682
`'yob1974'` | 16249
`'yob1975'` | 16944
`'yob1976'` | 17391
`'yob1977'` | 18175
`'yob1978'` | 18231
`'yob1979'` | 19039
`'yob1980'` | 19452
`'yob1981'` | 19475
`'yob1982'` | 19694
`'yob1983'` | 19407
`'yob1984'` | 19506
`'yob1985'` | 20085
`'yob1986'` | 20657
`'yob1987'` | 21406
`'yob1988'` | 22367
`'yob1989'` | 23775
`'yob1990'` | 24716
`'yob1991'` | 25109
`'yob1992'` | 25427
`'yob1993'` | 25966
`'yob1994'` | 25997
`'yob1995'` | 26080
`'yob1996'` | 26423
`'yob1997'` | 26970
`'yob1998'` | 27902
`'yob1999'` | 28552
`'yob2000'` | 29772
`'yob2001'` | 30274
`'yob2002'` | 30564
`'yob2003'` | 31185
`'yob2004'` | 32048
`'yob2005'` | 32549
`'yob2006'` | 34088
`'yob2007'` | 34961
`'yob2008'` | 35079
`'yob2009'` | 34709
`'yob2010'` | 34073
`'yob2011'` | 33908
`'yob2012'` | 33747
`'yob2013'` | 33282
`'yob2014'` | 33243
`'yob2015'` | 33121
`'yob2016'` | 33010
`'yob2017'` | 32590
`'yob2018'` | 32033

*   **Features**:

```json
{
    "name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "assigned_gender": {
        "num_classes": 2,
        "names": [
            "M",
            "F"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "count": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## new_data


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/new_data')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2345

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": [
        {
            "num_classes": 6,
            "names": [
                "ABOUT:female",
                "ABOUT:male",
                "PARTNER:female",
                "PARTNER:male",
                "SELF:female",
                "SELF:male"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        }
    ],
    "class_type": {
        "num_classes": 3,
        "names": [
            "about",
            "partner",
            "self"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "turker_gender": {
        "num_classes": 5,
        "names": [
            "man",
            "woman",
            "nonbinary",
            "prefer not to say",
            "no answer"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "episode_done": {
        "dtype": "bool_",
        "id": null,
        "_type": "Value"
    },
    "confidence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## funpedia


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/funpedia')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2938
`'train'` | 23897
`'validation'` | 2984

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "persona": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gender": {
        "num_classes": 3,
        "names": [
            "gender-neutral",
            "female",
            "male"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## image_chat


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/image_chat')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 9997
`'validation'` | 338180

*   **Features**:

```json
{
    "caption": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "male": {
        "dtype": "bool_",
        "id": null,
        "_type": "Value"
    },
    "female": {
        "dtype": "bool_",
        "id": null,
        "_type": "Value"
    }
}
```



## wizard


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/wizard')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 470
`'train'` | 10449
`'validation'` | 537

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "chosen_topic": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gender": {
        "num_classes": 3,
        "names": [
            "gender-neutral",
            "female",
            "male"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## convai2_inferred


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/convai2_inferred')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 7801
`'train'` | 131438
`'validation'` | 7801

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "binary_label": {
        "num_classes": 2,
        "names": [
            "ABOUT:female",
            "ABOUT:male"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "binary_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "ternary_label": {
        "num_classes": 3,
        "names": [
            "ABOUT:female",
            "ABOUT:male",
            "ABOUT:gender-neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "ternary_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```



## light_inferred


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/light_inferred')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 12765
`'train'` | 106122
`'validation'` | 6362

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "binary_label": {
        "num_classes": 2,
        "names": [
            "ABOUT:female",
            "ABOUT:male"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "binary_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "ternary_label": {
        "num_classes": 3,
        "names": [
            "ABOUT:female",
            "ABOUT:male",
            "ABOUT:gender-neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "ternary_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```



## opensubtitles_inferred


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/opensubtitles_inferred')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 49108
`'train'` | 351036
`'validation'` | 41957

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "binary_label": {
        "num_classes": 2,
        "names": [
            "ABOUT:female",
            "ABOUT:male"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "binary_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "ternary_label": {
        "num_classes": 3,
        "names": [
            "ABOUT:female",
            "ABOUT:male",
            "ABOUT:gender-neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "ternary_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```



## yelp_inferred


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:md_gender_bias/yelp_inferred')
```

*   **Description**:

```
Machine learning models are trained to find patterns in data.
NLP models can inadvertently learn socially undesirable patterns when training on gender biased text.
In this work, we propose a general framework that decomposes gender bias in text along several pragmatic and semantic dimensions:
bias from the gender of the person being spoken about, bias from the gender of the person being spoken to, and bias from the gender of the speaker.
Using this fine-grained framework, we automatically annotate eight large scale datasets with gender information.
In addition, we collect a novel, crowdsourced evaluation benchmark of utterance-level gender rewrites.
Distinguishing between gender bias along multiple dimensions is important, as it enables us to train finer-grained gender bias classifiers.
We show our classifiers prove valuable for a variety of important applications, such as controlling for gender bias in generative models,
detecting gender bias in arbitrary text, and shed light on offensive language in terms of genderedness.
```

*   **License**: MIT License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 534460
`'train'` | 2577862
`'validation'` | 4492

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "binary_label": {
        "num_classes": 2,
        "names": [
            "ABOUT:female",
            "ABOUT:male"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "binary_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


