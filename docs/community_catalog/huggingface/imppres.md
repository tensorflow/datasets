# imppres

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/imppres)
*   [Huggingface](https://huggingface.co/datasets/imppres)


## presupposition_all_n_presupposition


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/presupposition_all_n_presupposition')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'all_n_presupposition'` | 1900

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "presupposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "UID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paradigmID": {
        "dtype": "int16",
        "id": null,
        "_type": "Value"
    }
}
```



## presupposition_both_presupposition


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/presupposition_both_presupposition')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'both_presupposition'` | 1900

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "presupposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "UID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paradigmID": {
        "dtype": "int16",
        "id": null,
        "_type": "Value"
    }
}
```



## presupposition_change_of_state


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/presupposition_change_of_state')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'change_of_state'` | 1900

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "presupposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "UID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paradigmID": {
        "dtype": "int16",
        "id": null,
        "_type": "Value"
    }
}
```



## presupposition_cleft_existence


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/presupposition_cleft_existence')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'cleft_existence'` | 1900

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "presupposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "UID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paradigmID": {
        "dtype": "int16",
        "id": null,
        "_type": "Value"
    }
}
```



## presupposition_cleft_uniqueness


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/presupposition_cleft_uniqueness')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'cleft_uniqueness'` | 1900

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "presupposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "UID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paradigmID": {
        "dtype": "int16",
        "id": null,
        "_type": "Value"
    }
}
```



## presupposition_only_presupposition


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/presupposition_only_presupposition')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'only_presupposition'` | 1900

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "presupposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "UID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paradigmID": {
        "dtype": "int16",
        "id": null,
        "_type": "Value"
    }
}
```



## presupposition_possessed_definites_existence


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/presupposition_possessed_definites_existence')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'possessed_definites_existence'` | 1900

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "presupposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "UID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paradigmID": {
        "dtype": "int16",
        "id": null,
        "_type": "Value"
    }
}
```



## presupposition_possessed_definites_uniqueness


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/presupposition_possessed_definites_uniqueness')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'possessed_definites_uniqueness'` | 1900

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "presupposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "UID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paradigmID": {
        "dtype": "int16",
        "id": null,
        "_type": "Value"
    }
}
```



## presupposition_question_presupposition


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/presupposition_question_presupposition')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'question_presupposition'` | 1900

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "presupposition": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "UID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pairID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paradigmID": {
        "dtype": "int16",
        "id": null,
        "_type": "Value"
    }
}
```



## implicature_connectives


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/implicature_connectives')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'connectives'` | 1200

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label_log": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "gold_label_prag": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "spec_relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "item_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lexemes": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## implicature_gradable_adjective


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/implicature_gradable_adjective')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'gradable_adjective'` | 1200

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label_log": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "gold_label_prag": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "spec_relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "item_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lexemes": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## implicature_gradable_verb


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/implicature_gradable_verb')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'gradable_verb'` | 1200

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label_log": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "gold_label_prag": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "spec_relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "item_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lexemes": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## implicature_modals


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/implicature_modals')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'modals'` | 1200

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label_log": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "gold_label_prag": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "spec_relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "item_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lexemes": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## implicature_numerals_10_100


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/implicature_numerals_10_100')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'numerals_10_100'` | 1200

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label_log": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "gold_label_prag": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "spec_relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "item_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lexemes": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## implicature_numerals_2_3


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/implicature_numerals_2_3')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'numerals_2_3'` | 1200

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label_log": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "gold_label_prag": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "spec_relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "item_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lexemes": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## implicature_quantifiers


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:imppres/implicature_quantifiers')
```

*   **Description**:

```
Over >25k semiautomatically generated sentence pairs illustrating well-studied pragmatic inference types. IMPPRES is an NLI dataset following the format of SNLI (Bowman et al., 2015), MultiNLI (Williams et al., 2018) and XNLI (Conneau et al., 2018), which was created to evaluate how well trained NLI models recognize several classes of presuppositions and scalar implicatures.
```

*   **License**: Creative Commons Attribution-NonCommercial 4.0 International Public License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'quantifiers'` | 1200

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gold_label_log": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "gold_label_prag": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "spec_relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "item_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "trigger": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lexemes": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


