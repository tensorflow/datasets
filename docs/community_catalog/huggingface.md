# Huggingface datasets

Huggingface has forked TFDS and provides a lot of text datasets. See
[here](https://huggingface.co/docs/datasets/) for more documentation.

You can load a Huggingface dataset using TFDS `load` method, using the community
namespace `huggingface:` as in the following example:

```python
ds = tfds.load('huggingface:glue/sst2', split='train')
```

