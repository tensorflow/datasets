<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.testing.mock_kaggle_api" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.testing.mock_kaggle_api

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Mock out the kaggle CLI.

``` python
tfds.testing.mock_kaggle_api(
    *args,
    **kwds
)
```

<!-- Placeholder for "Used in" -->

#### Args:

*   <b>`filenames`</b>: `list<str>`, names of the competition files.
*   <b>`err_msg`</b>: `str`, if provided, the kaggle CLI will raise a
    CalledProcessError and this will be the command output.

#### Yields:

None, context will have kaggle CLI mocked out.
