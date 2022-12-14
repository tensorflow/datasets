OPUS is a collection of translated texts from the web.

Create your own config to choose which data / language pair to load.

```
config = tfds.translate.opus.OpusConfig(
    version=tfds.core.Version('0.1.0'),
    language_pair=("de", "en"),
    subsets=["GNOME", "EMEA"]
)
builder = tfds.builder("opus", config=config)
```
