SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

Most splits are described at https://github.com/brendenlake/SCAN. For the MCD
splits please see https://arxiv.org/abs/1912.09713.pdf.

Basic usage:

```
data = tfds.load('scan/length')
```

More advanced example:

```
import tensorflow_datasets as tfds
from tensorflow_datasets.datasets.scan import scan_dataset_builder

data = tfds.load(
    'scan',
    builder_kwargs=dict(
        config=scan_dataset_builder.ScanConfig(
            name='simple_p8', directory='simple_split/size_variations')))
```
