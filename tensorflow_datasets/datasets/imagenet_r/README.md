ImageNet-R is a set of images labelled with ImageNet labels that were obtained
by collecting art, cartoons, deviantart, graffiti, embroidery, graphics,
origami, paintings, patterns, plastic objects, plush objects, sculptures,
sketches, tattoos, toys, and video game renditions of ImageNet classes.
ImageNet-R has renditions of 200 ImageNet classes resulting in 30,000 images. by
collecting new data and keeping only those images that ResNet-50 models fail to
correctly classify. For more details please refer to the paper.

The label space is the same as that of ImageNet2012. Each example is represented
as a dictionary with the following keys:

*   'image': The image, a (H, W, 3)-tensor.
*   'label': An integer in the range [0, 1000).
*   'file_name': A unique sting identifying the example within the dataset.
