# arabic_speech_corpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/arabic_speech_corpus)
*   [Huggingface](https://huggingface.co/datasets/arabic_speech_corpus)


## clean


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:arabic_speech_corpus/clean')
```

*   **Description**:

```
This Speech corpus has been developed as part of PhD work carried out by Nawar Halabi at the University of Southampton.
The corpus was recorded in south Levantine Arabic
(Damascian accent) using a professional studio. Synthesized speech as an output using this corpus has produced a high quality, natural voice.
Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .flac format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import soundfile as sf

def map_to_array(batch):
    speech_array, _ = sf.read(batch["file"])
    batch["speech"] = speech_array
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 100
`'train'` | 1813

*   **Features**:

```json
{
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 48000,
        "mono": true,
        "decode": true,
        "id": null,
        "_type": "Audio"
    },
    "phonetic": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "orthographic": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


