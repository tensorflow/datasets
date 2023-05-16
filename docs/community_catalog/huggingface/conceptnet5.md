# conceptnet5

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/conceptnet5)
*   [Huggingface](https://huggingface.co/datasets/conceptnet5)


## conceptnet5


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conceptnet5/conceptnet5')
```

*   **Description**:

```
\ This dataset is designed to provide training data
for common sense relationships pulls together from various
sources. 

The dataset is multi-lingual. See langauge codes and language info
here: https://github.com/commonsense/conceptnet5/wiki/Languages


This dataset provides an interface for the conceptnet5 csv file, and
some (but not all) of the raw text data used to build conceptnet5:
omcsnet_sentences_free.txt, and omcsnet_sentences_more.txt.

One use of this dataset would be to learn to extract the conceptnet
relationship from the omcsnet sentences.

Conceptnet5 has 34,074,917 relationships. Of those relationships,
there are 2,176,099 surface text sentences related to those 2M
entries.

omcsnet_sentences_free has 898,161 lines. omcsnet_sentences_more has
2,001,736 lines.

Original downloads are available here
https://github.com/commonsense/conceptnet5/wiki/Downloads. For more
information, see: https://github.com/commonsense/conceptnet5/wiki

The omcsnet data comes with the following warning from the authors of
the above site: 

Remember: this data comes from various forms of
crowdsourcing. Sentences in these files are not necessarily true,
useful, or appropriate.
```

*   **License**: 
This work includes data from ConceptNet 5, which was compiled by the
Commonsense Computing Initiative. ConceptNet 5 is freely available under
the Creative Commons Attribution-ShareAlike license (CC BY SA 3.0) from
http://conceptnet.io.

The included data was created by contributors to Commonsense Computing
projects, contributors to Wikimedia projects, DBPedia, OpenCyc, Games
with a Purpose, Princeton University's WordNet, Francis Bond's Open
Multilingual WordNet, and Jim Breen's JMDict.

There are various othe licenses. See:
https://github.com/commonsense/conceptnet5/wiki/Copying-and-sharing-ConceptNet

*   **Version**: 5.7.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 34074917

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "full_rel": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rel": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "arg1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "arg2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "extra_info": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "weight": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```



## omcs_sentences_free


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conceptnet5/omcs_sentences_free')
```

*   **Description**:

```
\ This dataset is designed to provide training data
for common sense relationships pulls together from various
sources. 

The dataset is multi-lingual. See langauge codes and language info
here: https://github.com/commonsense/conceptnet5/wiki/Languages


This dataset provides an interface for the conceptnet5 csv file, and
some (but not all) of the raw text data used to build conceptnet5:
omcsnet_sentences_free.txt, and omcsnet_sentences_more.txt.

One use of this dataset would be to learn to extract the conceptnet
relationship from the omcsnet sentences.

Conceptnet5 has 34,074,917 relationships. Of those relationships,
there are 2,176,099 surface text sentences related to those 2M
entries.

omcsnet_sentences_free has 898,161 lines. omcsnet_sentences_more has
2,001,736 lines.

Original downloads are available here
https://github.com/commonsense/conceptnet5/wiki/Downloads. For more
information, see: https://github.com/commonsense/conceptnet5/wiki

The omcsnet data comes with the following warning from the authors of
the above site: 

Remember: this data comes from various forms of
crowdsourcing. Sentences in these files are not necessarily true,
useful, or appropriate.
```

*   **License**: 
This work includes data from ConceptNet 5, which was compiled by the
Commonsense Computing Initiative. ConceptNet 5 is freely available under
the Creative Commons Attribution-ShareAlike license (CC BY SA 3.0) from
http://conceptnet.io.

The included data was created by contributors to Commonsense Computing
projects, contributors to Wikimedia projects, DBPedia, OpenCyc, Games
with a Purpose, Princeton University's WordNet, Francis Bond's Open
Multilingual WordNet, and Jim Breen's JMDict.

There are various othe licenses. See:
https://github.com/commonsense/conceptnet5/wiki/Copying-and-sharing-ConceptNet

*   **Version**: 5.7.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 898160

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "raw_data": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## omcs_sentences_more


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:conceptnet5/omcs_sentences_more')
```

*   **Description**:

```
\ This dataset is designed to provide training data
for common sense relationships pulls together from various
sources. 

The dataset is multi-lingual. See langauge codes and language info
here: https://github.com/commonsense/conceptnet5/wiki/Languages


This dataset provides an interface for the conceptnet5 csv file, and
some (but not all) of the raw text data used to build conceptnet5:
omcsnet_sentences_free.txt, and omcsnet_sentences_more.txt.

One use of this dataset would be to learn to extract the conceptnet
relationship from the omcsnet sentences.

Conceptnet5 has 34,074,917 relationships. Of those relationships,
there are 2,176,099 surface text sentences related to those 2M
entries.

omcsnet_sentences_free has 898,161 lines. omcsnet_sentences_more has
2,001,736 lines.

Original downloads are available here
https://github.com/commonsense/conceptnet5/wiki/Downloads. For more
information, see: https://github.com/commonsense/conceptnet5/wiki

The omcsnet data comes with the following warning from the authors of
the above site: 

Remember: this data comes from various forms of
crowdsourcing. Sentences in these files are not necessarily true,
useful, or appropriate.
```

*   **License**: 
This work includes data from ConceptNet 5, which was compiled by the
Commonsense Computing Initiative. ConceptNet 5 is freely available under
the Creative Commons Attribution-ShareAlike license (CC BY SA 3.0) from
http://conceptnet.io.

The included data was created by contributors to Commonsense Computing
projects, contributors to Wikimedia projects, DBPedia, OpenCyc, Games
with a Purpose, Princeton University's WordNet, Francis Bond's Open
Multilingual WordNet, and Jim Breen's JMDict.

There are various othe licenses. See:
https://github.com/commonsense/conceptnet5/wiki/Copying-and-sharing-ConceptNet

*   **Version**: 5.7.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2001735

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "raw_data": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


