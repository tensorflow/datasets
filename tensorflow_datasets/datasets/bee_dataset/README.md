This dataset contains images and a set of labels that expose certain
characterisitics of that images, such as *varroa-mite* infections, bees carrying
*pollen-packets* or bee that are *cooling the hive* by flappingn their wings.
Additionally, this dataset contains images of *wasps* to be able to distinguish
bees and wasps.

The images of the bees are taken from above and rotated. The bee is vertical and
either its head or the trunk is on top. All images were taken with a green
background and the distance to the bees was always the same, thus all bees have
the same size.

Each image can have multiple labels assigned to it. E.g. a bee can be cooling
the hive and have a varrio-mite infection at the same time.

This dataset is designed as mutli-label dataset, where each label, e.g.
*varroa_output*, contains 1 if the characterisitic was present in the image and
a 0 if it wasn't. All images are provided by 300 pixel height and 150 pixel
witdh. As default the dataset provides the images as 150x75 (h,w) pixel. You can
select 300 pixel height by loading the datset with the name
"bee_dataset/bee_dataset_300" and with 200 pixel height by
"bee_dataset/bee_dataset_200".

License: GNU GENERAL PUBLIC LICENSE

Author: Fabian Hickert <Fabian.Hickert@raspbee.de>
