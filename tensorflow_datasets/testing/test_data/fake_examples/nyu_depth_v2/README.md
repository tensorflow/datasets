Script to generate a fake example:

```python
import os

import h5py
import numpy as np

ref = h5py.File(
    os.path.expanduser(
        "~/tensorflow_datasets/downloads/extracted/TAR_GZ.datasets.lids.mit.edu_fastdept_nyudepthBjtXYu6zBBYUv0ByLqXPgFy4ygUuVvPRxjz9Ip5_97M.tar.gz/nyudepthv2/val/official/00001.h5"
    ),
    "r",
)

rgb = ref["rgb"][:]
depth = ref["depth"][:]
rgb_fake = np.ones(rgb.shape, dtype=np.uint8)  # np.zeros for val
depth_fake = np.ones(depth.shape).astype(depth.dtype)  # np.zeros for val

with h5py.File("00001.h5", "w") as f:  # 00001 and 00002 for train; 00001 for val
    f.create_dataset("rgb", data=rgb_fake, compression="gzip")
    f.create_dataset("depth", data=depth_fake, compression="gzip")
```