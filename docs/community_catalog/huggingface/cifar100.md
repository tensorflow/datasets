# cifar100

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cifar100)
*   [Huggingface](https://huggingface.co/datasets/cifar100)


## cifar100


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cifar100/cifar100')
```

*   **Description**:

```
The CIFAR-100 dataset consists of 60000 32x32 colour images in 100 classes, with 600 images
per class. There are 500 training images and 100 testing images per class. There are 50000 training images and 10000 test images. The 100 classes are grouped into 20 superclasses.
There are two labels per image - fine label (actual class) and coarse label (superclass).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 50000

*   **Features**:

```json
{
    "img": {
        "id": null,
        "_type": "Image"
    },
    "fine_label": {
        "num_classes": 100,
        "names": [
            "apple",
            "aquarium_fish",
            "baby",
            "bear",
            "beaver",
            "bed",
            "bee",
            "beetle",
            "bicycle",
            "bottle",
            "bowl",
            "boy",
            "bridge",
            "bus",
            "butterfly",
            "camel",
            "can",
            "castle",
            "caterpillar",
            "cattle",
            "chair",
            "chimpanzee",
            "clock",
            "cloud",
            "cockroach",
            "couch",
            "cra",
            "crocodile",
            "cup",
            "dinosaur",
            "dolphin",
            "elephant",
            "flatfish",
            "forest",
            "fox",
            "girl",
            "hamster",
            "house",
            "kangaroo",
            "keyboard",
            "lamp",
            "lawn_mower",
            "leopard",
            "lion",
            "lizard",
            "lobster",
            "man",
            "maple_tree",
            "motorcycle",
            "mountain",
            "mouse",
            "mushroom",
            "oak_tree",
            "orange",
            "orchid",
            "otter",
            "palm_tree",
            "pear",
            "pickup_truck",
            "pine_tree",
            "plain",
            "plate",
            "poppy",
            "porcupine",
            "possum",
            "rabbit",
            "raccoon",
            "ray",
            "road",
            "rocket",
            "rose",
            "sea",
            "seal",
            "shark",
            "shrew",
            "skunk",
            "skyscraper",
            "snail",
            "snake",
            "spider",
            "squirrel",
            "streetcar",
            "sunflower",
            "sweet_pepper",
            "table",
            "tank",
            "telephone",
            "television",
            "tiger",
            "tractor",
            "train",
            "trout",
            "tulip",
            "turtle",
            "wardrobe",
            "whale",
            "willow_tree",
            "wolf",
            "woman",
            "worm"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "coarse_label": {
        "num_classes": 20,
        "names": [
            "aquatic_mammals",
            "fish",
            "flowers",
            "food_containers",
            "fruit_and_vegetables",
            "household_electrical_devices",
            "household_furniture",
            "insects",
            "large_carnivores",
            "large_man-made_outdoor_things",
            "large_natural_outdoor_scenes",
            "large_omnivores_and_herbivores",
            "medium_mammals",
            "non-insect_invertebrates",
            "people",
            "reptiles",
            "small_mammals",
            "trees",
            "vehicles_1",
            "vehicles_2"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


