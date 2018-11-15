<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.file_adapter.CSVAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="filetype_suffix"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="dataset_from_filename"/>
<meta itemprop="property" content="write_from_generator"/>
</div>

# tfds.file_adapter.CSVAdapter

## Class `CSVAdapter`

Inherits From: [`FileFormatAdapter`](../../tfds/file_adapter/FileFormatAdapter.md)



Defined in [`core/file_format_adapter.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/file_format_adapter.py).

Writes/reads features to/from CSV files.

Constraints on generators:

* The generator must yield feature dictionaries (`dict<str feature_name,
  feature_value>`).
* The allowed feature types are `int`, `float`, and `str`. By default, only
  scalar features are supported (that is, not lists).

You can modify how records are written by passing `csv_writer_ctor`.

You can modify how records are read by passing `csv_dataset_kwargs`.

Note that all CSV files produced will have a header row.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    feature_types,
    csv_dataset_kwargs=None,
    csv_writer_ctor=csv.writer
)
```

Constructs CSVAdapter.

#### Args:

feature_types (dict<name, type>): specifies the dtypes of each of the
  features (columns in the CSV file).
csv_dataset_kwargs (dict): forwarded to `tf.contrib.data.CsvDataset`.
csv_writer_ctor (function): takes file handle and returns writer.


#### Raises:

* <b>`ValueError`</b>: if csv_dataset_kwargs["header"] is present.



## Properties

<h3 id="filetype_suffix"><code>filetype_suffix</code></h3>





## Methods

<h3 id="dataset_from_filename"><code>dataset_from_filename</code></h3>

``` python
dataset_from_filename(filename)
```



<h3 id="write_from_generator"><code>write_from_generator</code></h3>

``` python
write_from_generator(
    generator_fn,
    output_files
)
```





