# speech_commands

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/speech_commands)
*   [Huggingface](https://huggingface.co/datasets/speech_commands)


## v0.01


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:speech_commands/v0.01')
```

*   **Description**:

```
This is a set of one-second .wav audio files, each containing a single spoken
English word or background noise. These words are from a small set of commands, and are spoken by a
variety of different speakers. This data set is designed to help train simple
machine learning models. This dataset is covered in more detail at
[https://arxiv.org/abs/1804.03209](https://arxiv.org/abs/1804.03209).

Version 0.01 of the data set (configuration `"v0.01"`) was released on August 3rd 2017 and contains
64,727 audio files.

In version 0.01 thirty different words were recoded: "Yes", "No", "Up", "Down", "Left",
"Right", "On", "Off", "Stop", "Go", "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
"Bed", "Bird", "Cat", "Dog", "Happy", "House", "Marvin", "Sheila", "Tree", "Wow".


In version 0.02 more words were added: "Backward", "Forward", "Follow", "Learn", "Visual".

In both versions, ten of them are used as commands by convention: "Yes", "No", "Up", "Down", "Left",
"Right", "On", "Off", "Stop", "Go". Other words are considered to be auxiliary (in current implementation
it is marked by `True` value of `"is_unknown"` feature). Their function is to teach a model to distinguish core words
from unrecognized ones.

The `_silence_` class contains a set of longer audio clips that are either recordings or
a mathematical simulation of noise.
```

*   **License**: Creative Commons BY 4.0 License
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3081
`'train'` | 51093
`'validation'` | 6799

*   **Features**:

```json
{
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 16000,
        "mono": true,
        "_storage_dtype": "struct",
        "id": null,
        "_type": "Audio"
    },
    "label": {
        "num_classes": 31,
        "names": [
            "yes",
            "no",
            "up",
            "down",
            "left",
            "right",
            "on",
            "off",
            "stop",
            "go",
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "bed",
            "bird",
            "cat",
            "dog",
            "happy",
            "house",
            "marvin",
            "sheila",
            "tree",
            "wow",
            "_silence_"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "is_unknown": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "speaker_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterance_id": {
        "dtype": "int8",
        "id": null,
        "_type": "Value"
    }
}
```



## v0.02


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:speech_commands/v0.02')
```

*   **Description**:

```
This is a set of one-second .wav audio files, each containing a single spoken
English word or background noise. These words are from a small set of commands, and are spoken by a
variety of different speakers. This data set is designed to help train simple
machine learning models. This dataset is covered in more detail at
[https://arxiv.org/abs/1804.03209](https://arxiv.org/abs/1804.03209).

Version 0.01 of the data set (configuration `"v0.01"`) was released on August 3rd 2017 and contains
64,727 audio files.

In version 0.01 thirty different words were recoded: "Yes", "No", "Up", "Down", "Left",
"Right", "On", "Off", "Stop", "Go", "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
"Bed", "Bird", "Cat", "Dog", "Happy", "House", "Marvin", "Sheila", "Tree", "Wow".


In version 0.02 more words were added: "Backward", "Forward", "Follow", "Learn", "Visual".

In both versions, ten of them are used as commands by convention: "Yes", "No", "Up", "Down", "Left",
"Right", "On", "Off", "Stop", "Go". Other words are considered to be auxiliary (in current implementation
it is marked by `True` value of `"is_unknown"` feature). Their function is to teach a model to distinguish core words
from unrecognized ones.

The `_silence_` class contains a set of longer audio clips that are either recordings or
a mathematical simulation of noise.
```

*   **License**: Creative Commons BY 4.0 License
*   **Version**: 0.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4890
`'train'` | 84848
`'validation'` | 9982

*   **Features**:

```json
{
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 16000,
        "mono": true,
        "_storage_dtype": "struct",
        "id": null,
        "_type": "Audio"
    },
    "label": {
        "num_classes": 36,
        "names": [
            "yes",
            "no",
            "up",
            "down",
            "left",
            "right",
            "on",
            "off",
            "stop",
            "go",
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "bed",
            "bird",
            "cat",
            "dog",
            "happy",
            "house",
            "marvin",
            "sheila",
            "tree",
            "wow",
            "backward",
            "forward",
            "follow",
            "learn",
            "visual",
            "_silence_"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "is_unknown": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "speaker_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterance_id": {
        "dtype": "int8",
        "id": null,
        "_type": "Value"
    }
}
```


