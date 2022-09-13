# discovery

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/discovery)
*   [Huggingface](https://huggingface.co/datasets/discovery)


## discovery


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:discovery/discovery')
```

*   **Description**:

```
Discourse marker prediction with 174 different markers
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 87000
`'train'` | 1566000
`'validation'` | 87000

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 174,
        "names": [
            "[no-conn]",
            "absolutely,",
            "accordingly",
            "actually,",
            "additionally",
            "admittedly,",
            "afterward",
            "again,",
            "already,",
            "also,",
            "alternately,",
            "alternatively",
            "although,",
            "altogether,",
            "amazingly,",
            "and",
            "anyway,",
            "apparently,",
            "arguably,",
            "as_a_result,",
            "basically,",
            "because_of_that",
            "because_of_this",
            "besides,",
            "but",
            "by_comparison,",
            "by_contrast,",
            "by_doing_this,",
            "by_then",
            "certainly,",
            "clearly,",
            "coincidentally,",
            "collectively,",
            "consequently",
            "conversely",
            "curiously,",
            "currently,",
            "elsewhere,",
            "especially,",
            "essentially,",
            "eventually,",
            "evidently,",
            "finally,",
            "first,",
            "firstly,",
            "for_example",
            "for_instance",
            "fortunately,",
            "frankly,",
            "frequently,",
            "further,",
            "furthermore",
            "generally,",
            "gradually,",
            "happily,",
            "hence,",
            "here,",
            "historically,",
            "honestly,",
            "hopefully,",
            "however",
            "ideally,",
            "immediately,",
            "importantly,",
            "in_contrast,",
            "in_fact,",
            "in_other_words",
            "in_particular,",
            "in_short,",
            "in_sum,",
            "in_the_end,",
            "in_the_meantime,",
            "in_turn,",
            "incidentally,",
            "increasingly,",
            "indeed,",
            "inevitably,",
            "initially,",
            "instead,",
            "interestingly,",
            "ironically,",
            "lastly,",
            "lately,",
            "later,",
            "likewise,",
            "locally,",
            "luckily,",
            "maybe,",
            "meaning,",
            "meantime,",
            "meanwhile,",
            "moreover",
            "mostly,",
            "namely,",
            "nationally,",
            "naturally,",
            "nevertheless",
            "next,",
            "nonetheless",
            "normally,",
            "notably,",
            "now,",
            "obviously,",
            "occasionally,",
            "oddly,",
            "often,",
            "on_the_contrary,",
            "on_the_other_hand",
            "once,",
            "only,",
            "optionally,",
            "or,",
            "originally,",
            "otherwise,",
            "overall,",
            "particularly,",
            "perhaps,",
            "personally,",
            "plus,",
            "preferably,",
            "presently,",
            "presumably,",
            "previously,",
            "probably,",
            "rather,",
            "realistically,",
            "really,",
            "recently,",
            "regardless,",
            "remarkably,",
            "sadly,",
            "second,",
            "secondly,",
            "separately,",
            "seriously,",
            "significantly,",
            "similarly,",
            "simultaneously",
            "slowly,",
            "so,",
            "sometimes,",
            "soon,",
            "specifically,",
            "still,",
            "strangely,",
            "subsequently,",
            "suddenly,",
            "supposedly,",
            "surely,",
            "surprisingly,",
            "technically,",
            "thankfully,",
            "then,",
            "theoretically,",
            "thereafter,",
            "thereby,",
            "therefore",
            "third,",
            "thirdly,",
            "this,",
            "though,",
            "thus,",
            "together,",
            "traditionally,",
            "truly,",
            "truthfully,",
            "typically,",
            "ultimately,",
            "undoubtedly,",
            "unfortunately,",
            "unsurprisingly,",
            "usually,",
            "well,",
            "yet,"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## discoverysmall


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:discovery/discoverysmall')
```

*   **Description**:

```
Discourse marker prediction with 174 different markers
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 869
`'train'` | 15662
`'validation'` | 871

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 174,
        "names": [
            "[no-conn]",
            "absolutely,",
            "accordingly",
            "actually,",
            "additionally",
            "admittedly,",
            "afterward",
            "again,",
            "already,",
            "also,",
            "alternately,",
            "alternatively",
            "although,",
            "altogether,",
            "amazingly,",
            "and",
            "anyway,",
            "apparently,",
            "arguably,",
            "as_a_result,",
            "basically,",
            "because_of_that",
            "because_of_this",
            "besides,",
            "but",
            "by_comparison,",
            "by_contrast,",
            "by_doing_this,",
            "by_then",
            "certainly,",
            "clearly,",
            "coincidentally,",
            "collectively,",
            "consequently",
            "conversely",
            "curiously,",
            "currently,",
            "elsewhere,",
            "especially,",
            "essentially,",
            "eventually,",
            "evidently,",
            "finally,",
            "first,",
            "firstly,",
            "for_example",
            "for_instance",
            "fortunately,",
            "frankly,",
            "frequently,",
            "further,",
            "furthermore",
            "generally,",
            "gradually,",
            "happily,",
            "hence,",
            "here,",
            "historically,",
            "honestly,",
            "hopefully,",
            "however",
            "ideally,",
            "immediately,",
            "importantly,",
            "in_contrast,",
            "in_fact,",
            "in_other_words",
            "in_particular,",
            "in_short,",
            "in_sum,",
            "in_the_end,",
            "in_the_meantime,",
            "in_turn,",
            "incidentally,",
            "increasingly,",
            "indeed,",
            "inevitably,",
            "initially,",
            "instead,",
            "interestingly,",
            "ironically,",
            "lastly,",
            "lately,",
            "later,",
            "likewise,",
            "locally,",
            "luckily,",
            "maybe,",
            "meaning,",
            "meantime,",
            "meanwhile,",
            "moreover",
            "mostly,",
            "namely,",
            "nationally,",
            "naturally,",
            "nevertheless",
            "next,",
            "nonetheless",
            "normally,",
            "notably,",
            "now,",
            "obviously,",
            "occasionally,",
            "oddly,",
            "often,",
            "on_the_contrary,",
            "on_the_other_hand",
            "once,",
            "only,",
            "optionally,",
            "or,",
            "originally,",
            "otherwise,",
            "overall,",
            "particularly,",
            "perhaps,",
            "personally,",
            "plus,",
            "preferably,",
            "presently,",
            "presumably,",
            "previously,",
            "probably,",
            "rather,",
            "realistically,",
            "really,",
            "recently,",
            "regardless,",
            "remarkably,",
            "sadly,",
            "second,",
            "secondly,",
            "separately,",
            "seriously,",
            "significantly,",
            "similarly,",
            "simultaneously",
            "slowly,",
            "so,",
            "sometimes,",
            "soon,",
            "specifically,",
            "still,",
            "strangely,",
            "subsequently,",
            "suddenly,",
            "supposedly,",
            "surely,",
            "surprisingly,",
            "technically,",
            "thankfully,",
            "then,",
            "theoretically,",
            "thereafter,",
            "thereby,",
            "therefore",
            "third,",
            "thirdly,",
            "this,",
            "though,",
            "thus,",
            "together,",
            "traditionally,",
            "truly,",
            "truthfully,",
            "typically,",
            "ultimately,",
            "undoubtedly,",
            "unfortunately,",
            "unsurprisingly,",
            "usually,",
            "well,",
            "yet,"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


