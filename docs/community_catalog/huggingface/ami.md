# ami

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ami)
*   [Huggingface](https://huggingface.co/datasets/ami)


## microphone-single


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ami/microphone-single')
```

*   **Description**:

```
The AMI Meeting Corpus consists of 100 hours of meeting recordings. The recordings use a range of signals
synchronized to a common timeline. These include close-talking and far-field microphones, individual and
room-view video cameras, and output from a slide projector and an electronic whiteboard. During the meetings,
the participants also have unsynchronized pens available to them that record what is written. The meetings
were recorded in English using three different rooms with different acoustic properties, and include mostly
non-native speakers. 

Far field audio of single microphone. This configuration only includes audio belonging the first microphone, *i.e.* 1-1, of the microphone array.
```

*   **License**: No known license
*   **Version**: 1.6.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 16
`'train'` | 134
`'validation'` | 18

*   **Features**:

```json
{
    "word_ids": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_start_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_end_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_ids": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_start_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_end_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "words": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "channels": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 16000,
        "mono": true,
        "decode": true,
        "id": null,
        "_type": "Audio"
    }
}
```



## microphone-multi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ami/microphone-multi')
```

*   **Description**:

```
The AMI Meeting Corpus consists of 100 hours of meeting recordings. The recordings use a range of signals
synchronized to a common timeline. These include close-talking and far-field microphones, individual and
room-view video cameras, and output from a slide projector and an electronic whiteboard. During the meetings,
the participants also have unsynchronized pens available to them that record what is written. The meetings
were recorded in English using three different rooms with different acoustic properties, and include mostly
non-native speakers. 

Far field audio of microphone array. This configuration includes audio of the first microphone array 1-1, 1-2, ..., 1-8.
```

*   **License**: No known license
*   **Version**: 1.6.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 16
`'train'` | 134
`'validation'` | 18

*   **Features**:

```json
{
    "word_ids": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_start_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_end_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_ids": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_start_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_end_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "words": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "channels": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "file-1-1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-1-2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-1-3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-1-4": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-1-5": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-1-6": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-1-7": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-1-8": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## headset-single


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ami/headset-single')
```

*   **Description**:

```
The AMI Meeting Corpus consists of 100 hours of meeting recordings. The recordings use a range of signals
synchronized to a common timeline. These include close-talking and far-field microphones, individual and
room-view video cameras, and output from a slide projector and an electronic whiteboard. During the meetings,
the participants also have unsynchronized pens available to them that record what is written. The meetings
were recorded in English using three different rooms with different acoustic properties, and include mostly
non-native speakers. 

Close talking audio of single headset. This configuration only includes audio belonging to the headset of the person currently speaking.
```

*   **License**: No known license
*   **Version**: 1.6.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 16
`'train'` | 136
`'validation'` | 18

*   **Features**:

```json
{
    "word_ids": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_start_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_end_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_ids": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_start_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_end_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "words": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "channels": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 16000,
        "mono": true,
        "decode": true,
        "id": null,
        "_type": "Audio"
    }
}
```



## headset-multi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ami/headset-multi')
```

*   **Description**:

```
The AMI Meeting Corpus consists of 100 hours of meeting recordings. The recordings use a range of signals
synchronized to a common timeline. These include close-talking and far-field microphones, individual and
room-view video cameras, and output from a slide projector and an electronic whiteboard. During the meetings,
the participants also have unsynchronized pens available to them that record what is written. The meetings
were recorded in English using three different rooms with different acoustic properties, and include mostly
non-native speakers. 

Close talking audio of four individual headset. This configuration includes audio belonging to four individual headsets. For each annotation there are 4 audio files 0, 1, 2, 3.
```

*   **License**: No known license
*   **Version**: 1.6.2
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 16
`'train'` | 136
`'validation'` | 18

*   **Features**:

```json
{
    "word_ids": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_start_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_end_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "word_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_ids": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_start_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_end_times": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "segment_speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "words": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "channels": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "file-0": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file-3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


