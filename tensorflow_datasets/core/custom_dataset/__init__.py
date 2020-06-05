"""Custom Datasets APIs"""

from tensorflow_datasets.core import registered

with registered.skip_registration():
    from tensorflow_datasets.core.custom_dataset.image_folder import ImageFolder

__all__ = [
    "ImageFolder",
]
