"""3D volumetric datasets, including point clouds, meshes and voxels."""

# from tensorflow_datasets.volume import modelnet
from tensorflow_datasets.volume.modelnet import Modelnet10
from tensorflow_datasets.volume.modelnet import Modelnet40
from tensorflow_datasets.volume.modelnet import ModelnetAligned40
from tensorflow_datasets.volume.modelnet import ModelnetSampled
from tensorflow_datasets.volume.modelnet import ModelnetSampledConfig
# from tensorflow_datasets.volume import shapenet
from tensorflow_datasets.volume.shapenet import ShapenetPart2017
from tensorflow_datasets.volume import utils
