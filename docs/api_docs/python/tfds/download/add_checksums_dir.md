<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.add_checksums_dir" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.download.add_checksums_dir

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/checksums.py">View
source</a>

Registers a new checksums dir.

```python
tfds.download.add_checksums_dir(checksums_dir)
```

<!-- Placeholder for "Used in" -->

This function allow external datasets not present in the tfds repository to
define their own checksums_dir containing the dataset downloads checksums.

Note: When redistributing your dataset, you should distribute the checksums
files with it and set `add_checksums_dir` when the user is importing your
`my_dataset.py`.

```
# Set-up the folder containing the 'my_dataset.txt' checksums.
checksum_dir = os.path.join(os.path.dirname(__file__), 'checksums/')
checksum_dir = os.path.normpath(checksum_dir)

# Add the checksum dir (will be executed when the user import your dataset)
tfds.download.add_checksums_dir(checksum_dir)

class MyDataset(tfds.core.DatasetBuilder):
  ...
```

#### Args:

*   <b>`checksums_dir`</b>: `str`, checksums dir to add to the registry
