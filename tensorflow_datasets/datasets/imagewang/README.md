Imagewang contains Imagenette and Imagewoof combined Image网 (pronounced
"Imagewang"; 网 means "net" in Chinese) contains Imagenette and Imagewoof
combined, but with some twists that make it into a tricky semi-supervised
unbalanced classification problem:

*   The validation set is the same as Imagewoof (i.e. 30% of Imagewoof images);
    there are no Imagenette images in the validation set (they're all in the
    training set)
*   Only 10% of Imagewoof images are in the training set!
*   The remaining are in the unsup ("unsupervised") directory, and you can not
    use their labels in training!
*   It's even hard to type and hard to say!

The dataset comes in three variants:

*   Full size
*   320 px
*   160 px

This dataset consists of the Imagenette dataset {size} variant.
