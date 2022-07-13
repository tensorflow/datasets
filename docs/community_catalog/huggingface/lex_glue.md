# lex_glue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/lex_glue)
*   [Huggingface](https://huggingface.co/datasets/lex_glue)


## ecthr_a


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lex_glue/ecthr_a')
```

*   **Description**:

```
The European Court of Human Rights (ECtHR) hears allegations that a state has
breached human rights provisions of the European Convention of Human Rights (ECHR).
For each case, the dataset provides a list of factual paragraphs (facts) from the case description.
Each case is mapped to articles of the ECHR that were violated (if any).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 9000
`'validation'` | 1000

*   **Features**:

```json
{
    "text": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "labels": {
        "feature": {
            "num_classes": 10,
            "names": [
                "2",
                "3",
                "5",
                "6",
                "8",
                "9",
                "10",
                "11",
                "14",
                "P1-1"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ecthr_b


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lex_glue/ecthr_b')
```

*   **Description**:

```
The European Court of Human Rights (ECtHR) hears allegations that a state has
breached human rights provisions of the European Convention of Human Rights (ECHR).
For each case, the dataset provides a list of factual paragraphs (facts) from the case description.
Each case is mapped to articles of ECHR that were allegedly violated (considered by the court).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 9000
`'validation'` | 1000

*   **Features**:

```json
{
    "text": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "labels": {
        "feature": {
            "num_classes": 10,
            "names": [
                "2",
                "3",
                "5",
                "6",
                "8",
                "9",
                "10",
                "11",
                "14",
                "P1-1"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## eurlex


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lex_glue/eurlex')
```

*   **Description**:

```
European Union (EU) legislation is published in EUR-Lex portal.
All EU laws are annotated by EU's Publications Office with multiple concepts from the EuroVoc thesaurus,
a multilingual thesaurus maintained by the Publications Office.
The current version of EuroVoc contains more than 7k concepts referring to various activities
of the EU and its Member States (e.g., economics, health-care, trade).
Given a document, the task is to predict its EuroVoc labels (concepts).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 55000
`'validation'` | 5000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 127,
            "names": [
                "100163",
                "100164",
                "100165",
                "100166",
                "100167",
                "100168",
                "100169",
                "100170",
                "100171",
                "100172",
                "100173",
                "100174",
                "100175",
                "100176",
                "100177",
                "100178",
                "100179",
                "100180",
                "100181",
                "100182",
                "100183",
                "100184",
                "100185",
                "100186",
                "100187",
                "100188",
                "100189",
                "100190",
                "100191",
                "100192",
                "100193",
                "100194",
                "100195",
                "100196",
                "100197",
                "100198",
                "100199",
                "100200",
                "100201",
                "100202",
                "100203",
                "100204",
                "100205",
                "100206",
                "100207",
                "100208",
                "100209",
                "100210",
                "100211",
                "100212",
                "100213",
                "100214",
                "100215",
                "100216",
                "100217",
                "100218",
                "100219",
                "100220",
                "100221",
                "100222",
                "100223",
                "100224",
                "100225",
                "100226",
                "100227",
                "100228",
                "100229",
                "100230",
                "100231",
                "100232",
                "100233",
                "100234",
                "100235",
                "100236",
                "100237",
                "100238",
                "100239",
                "100240",
                "100241",
                "100242",
                "100243",
                "100244",
                "100245",
                "100246",
                "100247",
                "100248",
                "100249",
                "100250",
                "100251",
                "100252",
                "100253",
                "100254",
                "100255",
                "100256",
                "100257",
                "100258",
                "100259",
                "100260",
                "100261",
                "100262",
                "100263",
                "100264",
                "100265",
                "100266",
                "100267",
                "100268",
                "100269",
                "100270",
                "100271",
                "100272",
                "100273",
                "100274",
                "100275",
                "100276",
                "100277",
                "100278",
                "100279",
                "100280",
                "100281",
                "100282",
                "100283",
                "100284",
                "100285",
                "100286",
                "100287",
                "100288",
                "100289"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## scotus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lex_glue/scotus')
```

*   **Description**:

```
The US Supreme Court  (SCOTUS) is the highest federal court in the United States of America
and generally hears only the most controversial or otherwise complex cases which have not
been sufficiently well solved by lower courts. This is a single-label multi-class classification
task, where given a document (court opinion), the task is to predict the relevant issue areas.
The 14 issue areas cluster 278 issues whose focus is on the subject matter of the controversy (dispute).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1400
`'train'` | 5000
`'validation'` | 1400

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 13,
        "names": [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## ledgar


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lex_glue/ledgar')
```

*   **Description**:

```
LEDGAR dataset aims contract provision (paragraph) classification.
The contract provisions come from contracts obtained from the US Securities and Exchange Commission (SEC)
filings, which are publicly available from EDGAR. Each label represents the single main topic
(theme) of the corresponding contract provision.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 60000
`'validation'` | 10000

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 100,
        "names": [
            "Adjustments",
            "Agreements",
            "Amendments",
            "Anti-Corruption Laws",
            "Applicable Laws",
            "Approvals",
            "Arbitration",
            "Assignments",
            "Assigns",
            "Authority",
            "Authorizations",
            "Base Salary",
            "Benefits",
            "Binding Effects",
            "Books",
            "Brokers",
            "Capitalization",
            "Change In Control",
            "Closings",
            "Compliance With Laws",
            "Confidentiality",
            "Consent To Jurisdiction",
            "Consents",
            "Construction",
            "Cooperation",
            "Costs",
            "Counterparts",
            "Death",
            "Defined Terms",
            "Definitions",
            "Disability",
            "Disclosures",
            "Duties",
            "Effective Dates",
            "Effectiveness",
            "Employment",
            "Enforceability",
            "Enforcements",
            "Entire Agreements",
            "Erisa",
            "Existence",
            "Expenses",
            "Fees",
            "Financial Statements",
            "Forfeitures",
            "Further Assurances",
            "General",
            "Governing Laws",
            "Headings",
            "Indemnifications",
            "Indemnity",
            "Insurances",
            "Integration",
            "Intellectual Property",
            "Interests",
            "Interpretations",
            "Jurisdictions",
            "Liens",
            "Litigations",
            "Miscellaneous",
            "Modifications",
            "No Conflicts",
            "No Defaults",
            "No Waivers",
            "Non-Disparagement",
            "Notices",
            "Organizations",
            "Participations",
            "Payments",
            "Positions",
            "Powers",
            "Publicity",
            "Qualifications",
            "Records",
            "Releases",
            "Remedies",
            "Representations",
            "Sales",
            "Sanctions",
            "Severability",
            "Solvency",
            "Specific Performance",
            "Submission To Jurisdiction",
            "Subsidiaries",
            "Successors",
            "Survival",
            "Tax Withholdings",
            "Taxes",
            "Terminations",
            "Terms",
            "Titles",
            "Transactions With Affiliates",
            "Use Of Proceeds",
            "Vacations",
            "Venues",
            "Vesting",
            "Waiver Of Jury Trials",
            "Waivers",
            "Warranties",
            "Withholdings"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## unfair_tos


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lex_glue/unfair_tos')
```

*   **Description**:

```
The UNFAIR-ToS dataset contains 50 Terms of Service (ToS) from on-line platforms (e.g., YouTube,
Ebay, Facebook, etc.). The dataset has been annotated on the sentence-level with 8 types of
unfair contractual terms (sentences), meaning terms that potentially violate user rights
according to the European consumer law.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1607
`'train'` | 5532
`'validation'` | 2275

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 8,
            "names": [
                "Limitation of liability",
                "Unilateral termination",
                "Unilateral change",
                "Content removal",
                "Contract by using",
                "Choice of law",
                "Jurisdiction",
                "Arbitration"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## case_hold


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lex_glue/case_hold')
```

*   **Description**:

```
The CaseHOLD (Case Holdings on Legal Decisions) dataset contains approx. 53k multiple choice
questions about holdings of US court cases from the Harvard Law Library case law corpus.
Holdings are short summaries of legal rulings accompany referenced decisions relevant for the present case.
The input consists of an excerpt (or prompt) from a court decision, containing a reference
to a particular case, while the holding statement is masked out. The model must identify
the correct (masked) holding statement from a selection of five choices.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3600
`'train'` | 45000
`'validation'` | 3900

*   **Features**:

```json
{
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "endings": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "label": {
        "num_classes": 5,
        "names": [
            "0",
            "1",
            "2",
            "3",
            "4"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


