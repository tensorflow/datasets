# miam

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/miam)
*   [Huggingface](https://huggingface.co/datasets/miam)


## dihana


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:miam/dihana')
```

*   **Description**:

```
Multilingual dIalogAct benchMark is a collection of resources for training, evaluating, and
analyzing natural language understanding systems specifically designed for spoken language. Datasets
are in English, French, German, Italian and Spanish. They cover a variety of domains including
spontaneous speech, scripted scenarios, and joint task completion. Some datasets additionally include
emotion and/or sentimant labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2361
`'train'` | 19063
`'validation'` | 2123

*   **Features**:

```json
{
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "File_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 11,
        "names": [
            "Afirmacion",
            "Apertura",
            "Cierre",
            "Confirmacion",
            "Espera",
            "Indefinida",
            "Negacion",
            "No_entendido",
            "Nueva_consulta",
            "Pregunta",
            "Respuesta"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## ilisten


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:miam/ilisten')
```

*   **Description**:

```
Multilingual dIalogAct benchMark is a collection of resources for training, evaluating, and
analyzing natural language understanding systems specifically designed for spoken language. Datasets
are in English, French, German, Italian and Spanish. They cover a variety of domains including
spontaneous speech, scripted scenarios, and joint task completion. Some datasets additionally include
emotion and/or sentimant labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 971
`'train'` | 1986
`'validation'` | 230

*   **Features**:

```json
{
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 15,
        "names": [
            "AGREE",
            "ANSWER",
            "CLOSING",
            "ENCOURAGE-SORRY",
            "GENERIC-ANSWER",
            "INFO-REQUEST",
            "KIND-ATTITUDE_SMALL-TALK",
            "OFFER-GIVE-INFO",
            "OPENING",
            "PERSUASION-SUGGEST",
            "QUESTION",
            "REJECT",
            "SOLICITATION-REQ_CLARIFICATION",
            "STATEMENT",
            "TALK-ABOUT-SELF"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## loria


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:miam/loria')
```

*   **Description**:

```
Multilingual dIalogAct benchMark is a collection of resources for training, evaluating, and
analyzing natural language understanding systems specifically designed for spoken language. Datasets
are in English, French, German, Italian and Spanish. They cover a variety of domains including
spontaneous speech, scripted scenarios, and joint task completion. Some datasets additionally include
emotion and/or sentimant labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1047
`'train'` | 8465
`'validation'` | 942

*   **Features**:

```json
{
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "File_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 31,
        "names": [
            "ack",
            "ask",
            "find_mold",
            "find_plans",
            "first_step",
            "greet",
            "help",
            "inform",
            "inform_engine",
            "inform_job",
            "inform_material_space",
            "informer_conditioner",
            "informer_decoration",
            "informer_elcomps",
            "informer_end_manufacturing",
            "kindAtt",
            "manufacturing_reqs",
            "next_step",
            "no",
            "other",
            "quality_control",
            "quit",
            "reqRep",
            "security_policies",
            "staff_enterprise",
            "staff_job",
            "studies_enterprise",
            "studies_job",
            "todo_failure",
            "todo_irreparable",
            "yes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## maptask


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:miam/maptask')
```

*   **Description**:

```
Multilingual dIalogAct benchMark is a collection of resources for training, evaluating, and
analyzing natural language understanding systems specifically designed for spoken language. Datasets
are in English, French, German, Italian and Spanish. They cover a variety of domains including
spontaneous speech, scripted scenarios, and joint task completion. Some datasets additionally include
emotion and/or sentimant labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5335
`'train'` | 25382
`'validation'` | 5221

*   **Features**:

```json
{
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "File_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 12,
        "names": [
            "acknowledge",
            "align",
            "check",
            "clarify",
            "explain",
            "instruct",
            "query_w",
            "query_yn",
            "ready",
            "reply_n",
            "reply_w",
            "reply_y"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## vm2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:miam/vm2')
```

*   **Description**:

```
Multilingual dIalogAct benchMark is a collection of resources for training, evaluating, and
analyzing natural language understanding systems specifically designed for spoken language. Datasets
are in English, French, German, Italian and Spanish. They cover a variety of domains including
spontaneous speech, scripted scenarios, and joint task completion. Some datasets additionally include
emotion and/or sentimant labels.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2855
`'train'` | 25060
`'validation'` | 2860

*   **Features**:

```json
{
    "Utterance": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_Act": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Speaker": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Dialogue_ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Label": {
        "num_classes": 31,
        "names": [
            "ACCEPT",
            "BACKCHANNEL",
            "BYE",
            "CLARIFY",
            "CLOSE",
            "COMMIT",
            "CONFIRM",
            "DEFER",
            "DELIBERATE",
            "DEVIATE_SCENARIO",
            "EXCLUDE",
            "EXPLAINED_REJECT",
            "FEEDBACK",
            "FEEDBACK_NEGATIVE",
            "FEEDBACK_POSITIVE",
            "GIVE_REASON",
            "GREET",
            "INFORM",
            "INIT",
            "INTRODUCE",
            "NOT_CLASSIFIABLE",
            "OFFER",
            "POLITENESS_FORMULA",
            "REJECT",
            "REQUEST",
            "REQUEST_CLARIFY",
            "REQUEST_COMMENT",
            "REQUEST_COMMIT",
            "REQUEST_SUGGEST",
            "SUGGEST",
            "THANK"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


