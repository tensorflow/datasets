# About
> As you know, it really requires a lot of data, especially, accurate data in order to also achieve a successful model at the end of the training process. Considering sometimes data, which is completely custom and really hard to find high quality ones on the internet, this script is going to increase your current data size by a few times with different methods of image manipulation to give you a much more accurate and stable model at the end.

# Data Generator / Extender
>Based on your current available data, this simple script will go over, and extend your current dataset by using image manipulation methods as following:
>* Blurred
>* Black and White
>* Noisy
>* Flip (over X, Y, Center)
>* Bright
>* Hue
>* More to come...

### Input Images
Test input images are as following:

![Input Images](https://i.imgur.com/KAawPkx.png "This is a sample input data.")

### Blurred Images
Blurred output images are as following:

![Blurred Images](https://i.imgur.com/iwF5IUh.png "This is a sample blurred data.")

### Noisy Images
Noisy output images are as following:

![Noisy Images](https://i.imgur.com/PTKlIWg.png "This is a sample noisy data.")


### Flip Images
Flip images based on the flip over X, Y, and Center are attached below:

![Flipped Images 1](https://i.imgur.com/ALxK0a9.png "This is a sample flipped1 data.")
![Flipped Images 2](https://i.imgur.com/IJoZ8Qe.png "This is a sample flipped2 data.")
![Flipped Images 3](https://i.imgur.com/luasBTF.png "This is a sample flipped3 data.")


### Black&White Images
Black & White output images are as following:

![Black&White Images](https://i.imgur.com/UgACXa8.png "This is a sample black and white data.")


### Bright Images
Bright input images are as following:

![Bright Images](https://i.imgur.com/WMXh8Ye.png "This is a sample bright data.")

### Hue Images
Hue input images are as following:

![Hue Images](https://i.imgur.com/OvIN5mL.png "This is a sample hue data.")

## Requirements

|Libraries|
|:--------------------------:|
|numpy                       |
|opencv-python|
|scikit-image|
|random|

### Run the script

|Windows|Linux & MacOS|
|--------------------------|:--------------------------|
|```$python main.py```|```$python3 main.py```|

### Folder Structure

```
custom_data_generator
    │
    └── BlackAndWhite
    │    └── __init__.py
    │
    └── Blur
    │    └── __init__.py
    │
    └── Brightness
    │    └── __init__.py
    │
    └── Flip
    │    └── __init__.py
    │
    └── Hue
    │    └── __init__.py
    │
    └── Noise
    │    └── __init__.py
    │
    └── Shear
    │   └── __init__.py
    │
    └── main.py
    │
    │
    └── README.md
    │
    └── src 
        └── input
        │    └──  image1.jpg
        │    │
        │    └──  image2.jpg
        │    │
        │    └──  image3.jpg
        │    │
        │    └──  image4.jpg
        │    │
        │    └──  image5.jpg
        └── output    


```

### Features to come
>Current version of the script allows the users to prepare their data before annotating them. However, in the next version, script will also be ready to be easily used by the users on a ready to train data, where the script itself will also generate the label data of the given inputs by itself automatically, letting user only spend a few seconds on the generation, and then directly set on training.

> New image manipulation **methods** to increase the data as much as we can and more!

### Contributors:
<a href="https://www.github.com/woosal1337"><img src="https://i.imgur.com/oW4JaIe.jpg" width="75" height="75"></a>