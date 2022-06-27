# indic_glue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/indic_glue)
*   [Huggingface](https://huggingface.co/datasets/indic_glue)


## wnli.en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wnli.en')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The Winograd Schema Challenge (Levesque et al., 2011) is a reading comprehension task
in which a system must read a sentence with a pronoun and select the referent of that pronoun from
a list of choices. The examples are manually constructed to foil simple statistical methods: Each
one is contingent on contextual information provided by a single word or phrase in the sentence.
To convert the problem into sentence pair classification, we construct sentence pairs by replacing
the ambiguous pronoun with each possible referent. The task is to predict if the sentence with the
pronoun substituted is entailed by the original sentence. We use a small evaluation set consisting of
new examples derived from fiction books that was shared privately by the authors of the original
corpus. While the included training set is balanced between two classes, the test set is imbalanced
between them (65% not entailment). Also, due to a data quirk, the development set is adversarial:
hypotheses are sometimes shared between training and development examples, so if a model memorizes the
training examples, they will predict the wrong label on corresponding development set
example. As with QNLI, each example is evaluated separately, so there is not a systematic correspondence
between a model's score on this task and its score on the unconverted original task. We
call converted dataset WNLI (Winograd NLI). This dataset is translated and publicly released for 3
Indian languages by AI4Bharat.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 146
`'train'` | 635
`'validation'` | 71

*   **Features**:

```json
{
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "not_entailment",
            "entailment",
            "None"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## wnli.hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wnli.hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The Winograd Schema Challenge (Levesque et al., 2011) is a reading comprehension task
in which a system must read a sentence with a pronoun and select the referent of that pronoun from
a list of choices. The examples are manually constructed to foil simple statistical methods: Each
one is contingent on contextual information provided by a single word or phrase in the sentence.
To convert the problem into sentence pair classification, we construct sentence pairs by replacing
the ambiguous pronoun with each possible referent. The task is to predict if the sentence with the
pronoun substituted is entailed by the original sentence. We use a small evaluation set consisting of
new examples derived from fiction books that was shared privately by the authors of the original
corpus. While the included training set is balanced between two classes, the test set is imbalanced
between them (65% not entailment). Also, due to a data quirk, the development set is adversarial:
hypotheses are sometimes shared between training and development examples, so if a model memorizes the
training examples, they will predict the wrong label on corresponding development set
example. As with QNLI, each example is evaluated separately, so there is not a systematic correspondence
between a model's score on this task and its score on the unconverted original task. We
call converted dataset WNLI (Winograd NLI). This dataset is translated and publicly released for 3
Indian languages by AI4Bharat.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 146
`'train'` | 635
`'validation'` | 71

*   **Features**:

```json
{
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "not_entailment",
            "entailment",
            "None"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## wnli.gu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wnli.gu')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The Winograd Schema Challenge (Levesque et al., 2011) is a reading comprehension task
in which a system must read a sentence with a pronoun and select the referent of that pronoun from
a list of choices. The examples are manually constructed to foil simple statistical methods: Each
one is contingent on contextual information provided by a single word or phrase in the sentence.
To convert the problem into sentence pair classification, we construct sentence pairs by replacing
the ambiguous pronoun with each possible referent. The task is to predict if the sentence with the
pronoun substituted is entailed by the original sentence. We use a small evaluation set consisting of
new examples derived from fiction books that was shared privately by the authors of the original
corpus. While the included training set is balanced between two classes, the test set is imbalanced
between them (65% not entailment). Also, due to a data quirk, the development set is adversarial:
hypotheses are sometimes shared between training and development examples, so if a model memorizes the
training examples, they will predict the wrong label on corresponding development set
example. As with QNLI, each example is evaluated separately, so there is not a systematic correspondence
between a model's score on this task and its score on the unconverted original task. We
call converted dataset WNLI (Winograd NLI). This dataset is translated and publicly released for 3
Indian languages by AI4Bharat.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 146
`'train'` | 635
`'validation'` | 71

*   **Features**:

```json
{
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "not_entailment",
            "entailment",
            "None"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## wnli.mr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wnli.mr')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The Winograd Schema Challenge (Levesque et al., 2011) is a reading comprehension task
in which a system must read a sentence with a pronoun and select the referent of that pronoun from
a list of choices. The examples are manually constructed to foil simple statistical methods: Each
one is contingent on contextual information provided by a single word or phrase in the sentence.
To convert the problem into sentence pair classification, we construct sentence pairs by replacing
the ambiguous pronoun with each possible referent. The task is to predict if the sentence with the
pronoun substituted is entailed by the original sentence. We use a small evaluation set consisting of
new examples derived from fiction books that was shared privately by the authors of the original
corpus. While the included training set is balanced between two classes, the test set is imbalanced
between them (65% not entailment). Also, due to a data quirk, the development set is adversarial:
hypotheses are sometimes shared between training and development examples, so if a model memorizes the
training examples, they will predict the wrong label on corresponding development set
example. As with QNLI, each example is evaluated separately, so there is not a systematic correspondence
between a model's score on this task and its score on the unconverted original task. We
call converted dataset WNLI (Winograd NLI). This dataset is translated and publicly released for 3
Indian languages by AI4Bharat.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 146
`'train'` | 635
`'validation'` | 71

*   **Features**:

```json
{
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "not_entailment",
            "entailment",
            "None"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## copa.en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/copa.en')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The Choice Of Plausible Alternatives (COPA) evaluation provides researchers with a tool for assessing
progress in open-domain commonsense causal reasoning. COPA consists of 1000 questions, split equally
into development and test sets of 500 questions each. Each question is composed of a premise and two
alternatives, where the task is to select the alternative that more plausibly has a causal relation
with the premise. The correct alternative is randomized so that the expected performance of randomly
guessing is 50%. This dataset is translated and publicly released for 3 languages by AI4Bharat.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'train'` | 400
`'validation'` | 100

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## copa.hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/copa.hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The Choice Of Plausible Alternatives (COPA) evaluation provides researchers with a tool for assessing
progress in open-domain commonsense causal reasoning. COPA consists of 1000 questions, split equally
into development and test sets of 500 questions each. Each question is composed of a premise and two
alternatives, where the task is to select the alternative that more plausibly has a causal relation
with the premise. The correct alternative is randomized so that the expected performance of randomly
guessing is 50%. This dataset is translated and publicly released for 3 languages by AI4Bharat.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 449
`'train'` | 362
`'validation'` | 88

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## copa.gu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/copa.gu')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The Choice Of Plausible Alternatives (COPA) evaluation provides researchers with a tool for assessing
progress in open-domain commonsense causal reasoning. COPA consists of 1000 questions, split equally
into development and test sets of 500 questions each. Each question is composed of a premise and two
alternatives, where the task is to select the alternative that more plausibly has a causal relation
with the premise. The correct alternative is randomized so that the expected performance of randomly
guessing is 50%. This dataset is translated and publicly released for 3 languages by AI4Bharat.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 448
`'train'` | 362
`'validation'` | 88

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## copa.mr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/copa.mr')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The Choice Of Plausible Alternatives (COPA) evaluation provides researchers with a tool for assessing
progress in open-domain commonsense causal reasoning. COPA consists of 1000 questions, split equally
into development and test sets of 500 questions each. Each question is composed of a premise and two
alternatives, where the task is to select the alternative that more plausibly has a causal relation
with the premise. The correct alternative is randomized so that the expected performance of randomly
guessing is 50%. This dataset is translated and publicly released for 3 languages by AI4Bharat.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 449
`'train'` | 362
`'validation'` | 88

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choice2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## sna.bn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/sna.bn')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


This dataset is a collection of Bengali News articles. The dataset is used for classifying articles into
5 different classes namely international, state, kolkata, entertainment and sports.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1411
`'train'` | 11284
`'validation'` | 1411

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 6,
        "names": [
            "kolkata",
            "state",
            "national",
            "sports",
            "entertainment",
            "international"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## csqa.as


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.as')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2942

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.bn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.bn')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 38845

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.gu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.gu')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 22861

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 35140

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.kn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.kn')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 13666

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.ml


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.ml')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 26537

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.mr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.mr')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 11370

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.or


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.or')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1975

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.pa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.pa')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5667

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.ta


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.ta')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 38590

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## csqa.te


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/csqa.te')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4
candidate entities. The dataset contains around 239k examples across 11 languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 41338

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "out_of_context_options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wstp.as


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.as')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 626
`'train'` | 5000
`'validation'` | 625

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.bn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.bn')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5948
`'train'` | 47580
`'validation'` | 5947

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.gu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.gu')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1251
`'train'` | 10004
`'validation'` | 1251

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5509
`'train'` | 44069
`'validation'` | 5509

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.kn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.kn')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4423
`'train'` | 35379
`'validation'` | 4422

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.ml


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.ml')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3441
`'train'` | 27527
`'validation'` | 3441

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.mr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.mr')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1306
`'train'` | 10446
`'validation'` | 1306

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.or


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.or')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 502
`'train'` | 4015
`'validation'` | 502

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.pa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.pa')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1097
`'train'` | 8772
`'validation'` | 1097

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.ta


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.ta')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6118
`'train'` | 48940
`'validation'` | 6117

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wstp.te


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wstp.te')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Predict the correct title for a Wikipedia section from a given list of four candidate titles.
The dataset has 400k examples across 11 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 80000
`'validation'` | 10000

*   **Features**:

```json
{
    "sectionText": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correctTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleC": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "titleD": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## inltkh.gu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/inltkh.gu')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Obtained from inltk project. The corpus is a collection of headlines tagged with their news category.
Available for langauges: gu, ml, mr and ta.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 659
`'train'` | 5269
`'validation'` | 659

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 10,
        "names": [
            "entertainment",
            "business",
            "tech",
            "sports",
            "state",
            "spirituality",
            "tamil-cinema",
            "positive",
            "negative",
            "neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## inltkh.ml


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/inltkh.ml')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Obtained from inltk project. The corpus is a collection of headlines tagged with their news category.
Available for langauges: gu, ml, mr and ta.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 630
`'train'` | 5036
`'validation'` | 630

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 10,
        "names": [
            "entertainment",
            "business",
            "tech",
            "sports",
            "state",
            "spirituality",
            "tamil-cinema",
            "positive",
            "negative",
            "neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## inltkh.mr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/inltkh.mr')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Obtained from inltk project. The corpus is a collection of headlines tagged with their news category.
Available for langauges: gu, ml, mr and ta.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1210
`'train'` | 9672
`'validation'` | 1210

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 10,
        "names": [
            "entertainment",
            "business",
            "tech",
            "sports",
            "state",
            "spirituality",
            "tamil-cinema",
            "positive",
            "negative",
            "neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## inltkh.ta


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/inltkh.ta')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Obtained from inltk project. The corpus is a collection of headlines tagged with their news category.
Available for langauges: gu, ml, mr and ta.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 669
`'train'` | 5346
`'validation'` | 669

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 10,
        "names": [
            "entertainment",
            "business",
            "tech",
            "sports",
            "state",
            "spirituality",
            "tamil-cinema",
            "positive",
            "negative",
            "neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## inltkh.te


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/inltkh.te')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


Obtained from inltk project. The corpus is a collection of headlines tagged with their news category.
Available for langauges: gu, ml, mr and ta.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 541
`'train'` | 4328
`'validation'` | 541

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 10,
        "names": [
            "entertainment",
            "business",
            "tech",
            "sports",
            "state",
            "spirituality",
            "tamil-cinema",
            "positive",
            "negative",
            "neutral"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## bbca.hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/bbca.hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


This release consists of 4335 Hindi documents with tags from the BBC Hindi News website.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 866
`'train'` | 3467

*   **Features**:

```json
{
    "label": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## cvit-mkb-clsr.en-bn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/cvit-mkb-clsr.en-bn')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


CVIT Maan ki Baat Dataset - Given a sentence in language $L_1$ the task is to retrieve its translation
from a set of candidate sentences in language $L_2$.
The dataset contains around 39k parallel sentence pairs across 8 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5522

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
    }
}
```



## cvit-mkb-clsr.en-gu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/cvit-mkb-clsr.en-gu')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


CVIT Maan ki Baat Dataset - Given a sentence in language $L_1$ the task is to retrieve its translation
from a set of candidate sentences in language $L_2$.
The dataset contains around 39k parallel sentence pairs across 8 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6463

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
    }
}
```



## cvit-mkb-clsr.en-hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/cvit-mkb-clsr.en-hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


CVIT Maan ki Baat Dataset - Given a sentence in language $L_1$ the task is to retrieve its translation
from a set of candidate sentences in language $L_2$.
The dataset contains around 39k parallel sentence pairs across 8 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5169

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
    }
}
```



## cvit-mkb-clsr.en-ml


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/cvit-mkb-clsr.en-ml')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


CVIT Maan ki Baat Dataset - Given a sentence in language $L_1$ the task is to retrieve its translation
from a set of candidate sentences in language $L_2$.
The dataset contains around 39k parallel sentence pairs across 8 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4886

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
    }
}
```



## cvit-mkb-clsr.en-mr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/cvit-mkb-clsr.en-mr')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


CVIT Maan ki Baat Dataset - Given a sentence in language $L_1$ the task is to retrieve its translation
from a set of candidate sentences in language $L_2$.
The dataset contains around 39k parallel sentence pairs across 8 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5760

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
    }
}
```



## cvit-mkb-clsr.en-or


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/cvit-mkb-clsr.en-or')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


CVIT Maan ki Baat Dataset - Given a sentence in language $L_1$ the task is to retrieve its translation
from a set of candidate sentences in language $L_2$.
The dataset contains around 39k parallel sentence pairs across 8 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 752

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
    }
}
```



## cvit-mkb-clsr.en-ta


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/cvit-mkb-clsr.en-ta')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


CVIT Maan ki Baat Dataset - Given a sentence in language $L_1$ the task is to retrieve its translation
from a set of candidate sentences in language $L_2$.
The dataset contains around 39k parallel sentence pairs across 8 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5637

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
    }
}
```



## cvit-mkb-clsr.en-te


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/cvit-mkb-clsr.en-te')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


CVIT Maan ki Baat Dataset - Given a sentence in language $L_1$ the task is to retrieve its translation
from a set of candidate sentences in language $L_2$.
The dataset contains around 39k parallel sentence pairs across 8 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5049

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
    }
}
```



## cvit-mkb-clsr.en-ur


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/cvit-mkb-clsr.en-ur')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


CVIT Maan ki Baat Dataset - Given a sentence in language $L_1$ the task is to retrieve its translation
from a set of candidate sentences in language $L_2$.
The dataset contains around 39k parallel sentence pairs across 8 Indian languages.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1006

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
    }
}
```



## iitp-mr.hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/iitp-mr.hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


IIT Patna Product Reviews: Sentiment analysis corpus for product reviews posted in Hindi.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 310
`'train'` | 2480
`'validation'` | 310

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## iitp-pr.hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/iitp-pr.hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


IIT Patna Product Reviews: Sentiment analysis corpus for product reviews posted in Hindi.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 523
`'train'` | 4182
`'validation'` | 523

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## actsa-sc.te


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/actsa-sc.te')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


ACTSA Corpus: Sentiment analysis corpus for Telugu sentences.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 541
`'train'` | 4328
`'validation'` | 541

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "positive",
            "negative"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## md.hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/md.hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The Hindi Discourse Analysis dataset is a corpus for analyzing discourse modes present in its sentences.
It contains sentences from stories written by 11 famous authors from the 20th Century. 4-5 stories by
each author have been selected which were available in the public domain resulting in a collection of 53 stories.
Most of these short stories were originally written in Hindi but some of them were written in other Indian languages
and later translated to Hindi.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 997
`'train'` | 7974
`'validation'` | 997

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "discourse_mode": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "story_number": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## wiki-ner.as


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.as')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 160
`'train'` | 1021
`'validation'` | 157

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.bn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.bn')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2690
`'train'` | 20223
`'validation'` | 2985

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.gu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.gu')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 255
`'train'` | 2343
`'validation'` | 297

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.hi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.hi')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1256
`'train'` | 9463
`'validation'` | 1114

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.kn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.kn')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 476
`'train'` | 2679
`'validation'` | 412

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.ml


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.ml')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2042
`'train'` | 15620
`'validation'` | 2067

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.mr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.mr')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1329
`'train'` | 12151
`'validation'` | 1498

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.or


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.or')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 153
`'train'` | 1077
`'validation'` | 132

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.pa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.pa')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 179
`'train'` | 1408
`'validation'` | 186

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.ta


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.ta')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2611
`'train'` | 20466
`'validation'` | 2586

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wiki-ner.te


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indic_glue/wiki-ner.te')
```

*   **Description**:

```
IndicGLUE is a natural language understanding benchmark for Indian languages. It contains a wide
    variety of tasks and covers 11 major Indian languages - as, bn, gu, hi, kn, ml, mr, or, pa, ta, te.


The WikiANN dataset (Pan et al. 2017) is a dataset with NER annotations for PER, ORG and LOC. It has been constructed using
the linked entities in Wikipedia pages for 282 different languages including Danish.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1110
`'train'` | 7978
`'validation'` | 841

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 7,
            "names": [
                "B-LOC",
                "B-ORG",
                "B-PER",
                "I-LOC",
                "I-ORG",
                "I-PER",
                "O"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "additional_info": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


