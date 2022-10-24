Cityscapes is a dataset consisting of diverse urban street scenes across 50
different cities at varying times of the year as well as ground truths for
several vision tasks including semantic segmentation, instance level
segmentation (TODO), and stereo pair disparity inference.

For segmentation tasks (default split, accessible via
'cityscapes/semantic_segmentation'), Cityscapes provides dense pixel level
annotations for 5000 images at 1024 * 2048 resolution pre-split into training
(2975), validation (500) and test (1525) sets. Label annotations for
segmentation tasks span across 30+ classes commonly encountered during driving
scene perception. Detailed label information may be found here:
https://github.com/mcordts/cityscapesScripts/blob/master/cityscapesscripts/helpers/labels.py#L52-L99

Cityscapes also provides coarse grain segmentation annotations (accessible via
'cityscapes/semantic_segmentation_extra') for 19998 images in a 'train_extra'
split which may prove useful for pretraining / data-heavy models.

Besides segmentation, cityscapes also provides stereo image pairs and ground
truths for disparity inference tasks on both the normal and extra splits
(accessible via 'cityscapes/stereo_disparity' and
'cityscapes/stereo_disparity_extra' respectively).

Ingored examples:

-   For 'cityscapes/stereo_disparity_extra':
    -   troisdorf_000000_000073_{*} images (no disparity map present)

WARNING: this dataset requires users to setup a login and password in order to
get the files.
