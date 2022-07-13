# food101

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/food101)
*   [Huggingface](https://huggingface.co/datasets/food101)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:food101')
```

*   **Description**:

```
This dataset consists of 101 food categories, with 101'000 images. For each class, 250 manually reviewed test images are provided as well as 750 training images. On purpose, the training images were not cleaned, and thus still contain some amount of noise. This comes mostly in the form of intense colors and sometimes wrong labels. All images were rescaled to have a maximum side length of 512 pixels.
```

*   **License**: LICENSE AGREEMENT
=================
 - The Food-101 data set consists of images from Foodspotting [1] which are not
   property of the Federal Institute of Technology Zurich (ETHZ). Any use beyond
   scientific fair use must be negociated with the respective picture owners
   according to the Foodspotting terms of use [2].

[1] http://www.foodspotting.com/
[2] http://www.foodspotting.com/terms/

*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 75750
`'validation'` | 25250

*   **Features**:

```json
{
    "image": {
        "id": null,
        "_type": "Image"
    },
    "label": {
        "num_classes": 101,
        "names": [
            "apple_pie",
            "baby_back_ribs",
            "baklava",
            "beef_carpaccio",
            "beef_tartare",
            "beet_salad",
            "beignets",
            "bibimbap",
            "bread_pudding",
            "breakfast_burrito",
            "bruschetta",
            "caesar_salad",
            "cannoli",
            "caprese_salad",
            "carrot_cake",
            "ceviche",
            "cheesecake",
            "cheese_plate",
            "chicken_curry",
            "chicken_quesadilla",
            "chicken_wings",
            "chocolate_cake",
            "chocolate_mousse",
            "churros",
            "clam_chowder",
            "club_sandwich",
            "crab_cakes",
            "creme_brulee",
            "croque_madame",
            "cup_cakes",
            "deviled_eggs",
            "donuts",
            "dumplings",
            "edamame",
            "eggs_benedict",
            "escargots",
            "falafel",
            "filet_mignon",
            "fish_and_chips",
            "foie_gras",
            "french_fries",
            "french_onion_soup",
            "french_toast",
            "fried_calamari",
            "fried_rice",
            "frozen_yogurt",
            "garlic_bread",
            "gnocchi",
            "greek_salad",
            "grilled_cheese_sandwich",
            "grilled_salmon",
            "guacamole",
            "gyoza",
            "hamburger",
            "hot_and_sour_soup",
            "hot_dog",
            "huevos_rancheros",
            "hummus",
            "ice_cream",
            "lasagna",
            "lobster_bisque",
            "lobster_roll_sandwich",
            "macaroni_and_cheese",
            "macarons",
            "miso_soup",
            "mussels",
            "nachos",
            "omelette",
            "onion_rings",
            "oysters",
            "pad_thai",
            "paella",
            "pancakes",
            "panna_cotta",
            "peking_duck",
            "pho",
            "pizza",
            "pork_chop",
            "poutine",
            "prime_rib",
            "pulled_pork_sandwich",
            "ramen",
            "ravioli",
            "red_velvet_cake",
            "risotto",
            "samosa",
            "sashimi",
            "scallops",
            "seaweed_salad",
            "shrimp_and_grits",
            "spaghetti_bolognese",
            "spaghetti_carbonara",
            "spring_rolls",
            "steak",
            "strawberry_shortcake",
            "sushi",
            "tacos",
            "takoyaki",
            "tiramisu",
            "tuna_tartare",
            "waffles"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


