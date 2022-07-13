# competition_math

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/competition_math)
*   [Huggingface](https://huggingface.co/datasets/competition_math)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:competition_math')
```

*   **Description**:

```
The Mathematics Aptitude Test of Heuristics (MATH) dataset consists of problems
from mathematics competitions, including the AMC 10, AMC 12, AIME, and more.
Each problem in MATH has a full step-by-step solution, which can be used to teach
models to generate answer derivations and explanations.
```

*   **License**: https://github.com/hendrycks/math/blob/main/LICENSE
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 7500

*   **Features**:

```json
{
    "problem": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "level": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "solution": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


