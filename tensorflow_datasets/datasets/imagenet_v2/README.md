ImageNet-v2 is an ImageNet test set (10 per class) collected by closely
following the original labelling protocol. Each image has been labelled by at
least 10 MTurk workers, possibly more, and depending on the strategy used to
select which images to include among the 10 chosen for the given class there are
three different versions of the dataset. Please refer to section four of the
paper for more details on how the different variants were compiled.

The label space is the same as that of ImageNet2012. Each example is represented
as a dictionary with the following keys:

*   'image': The image, a (H, W, 3)-tensor.
*   'label': An integer in the range [0, 1000).
*   'file_name': A unique sting identifying the example within the dataset.
