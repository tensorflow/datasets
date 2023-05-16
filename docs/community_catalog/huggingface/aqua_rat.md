# aqua_rat

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/aqua_rat)
*   [Huggingface](https://huggingface.co/datasets/aqua_rat)


## raw


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:aqua_rat/raw')
```

*   **Description**:

```
A large-scale dataset consisting of approximately 100,000 algebraic word problems. 
The solution to each question is explained step-by-step using natural language. 
This data is used to train a program generation model that learns to generate the explanation, 
while generating the program that solves the question.
```

*   **License**: Copyright 2017 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 254
`'train'` | 97467
`'validation'` | 254

*   **Features**:

```json
{
    "question": {
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
    "rationale": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tokenized


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:aqua_rat/tokenized')
```

*   **Description**:

```
A large-scale dataset consisting of approximately 100,000 algebraic word problems. 
The solution to each question is explained step-by-step using natural language. 
This data is used to train a program generation model that learns to generate the explanation, 
while generating the program that solves the question.
```

*   **License**: Copyright 2017 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 254
`'train'` | 97467
`'validation'` | 254

*   **Features**:

```json
{
    "question": {
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
    "rationale": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


