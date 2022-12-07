ILSVRC 2012, commonly known as 'ImageNet' is an image dataset organized
according to the WordNet hierarchy. Each meaningful concept in WordNet, possibly
described by multiple words or word phrases, is called a "synonym set" or
"synset". There are more than 100,000 synsets in WordNet, majority of them are
nouns (80,000+). In ImageNet, we aim to provide on average 1000 images to
illustrate each synset. Images of each concept are quality-controlled and
human-annotated. In its completion, we hope ImageNet will offer tens of millions
of cleanly sorted images for most of the concepts in the WordNet hierarchy.

The test split contains 100K images but no labels because no labels have been
publicly released. We provide support for the test split from 2012 with the
minor patch released on October 10, 2019. In order to manually download this
data, a user must perform the following operations:

1.  Download the 2012 test split available
    [here](https://image-net.org/challenges/LSVRC/2012/2012-downloads.php#Images).
2.  Download the October 10, 2019 patch. There is a Google Drive link to the
    patch provided on the same page.
3.  Combine the two tar-balls, manually overwriting any images in the original
    archive with images from the patch. According to the instructions on
    image-net.org, this procedure overwrites just a few images.

The resulting tar-ball may then be processed by TFDS.

To assess the accuracy of a model on the ImageNet test split, one must run
inference on all images in the split, export those results to a text file that
must be uploaded to the ImageNet evaluation server. The maintainers of the
ImageNet evaluation server permits a single user to submit up to 2 submissions
per week in order to prevent overfitting.

To evaluate the accuracy on the test split, one must first create an account at
image-net.org. This account must be approved by the site administrator. After
the account is created, one can submit the results to the test server at
https://image-net.org/challenges/LSVRC/eval_server.php The submission consists
of several ASCII text files corresponding to multiple tasks. The task of
interest is "Classification submission (top-5 cls error)". A sample of an
exported text file looks like the following:

```
771 778 794 387 650
363 691 764 923 427
737 369 430 531 124
755 930 755 59 168
```

The export format is described in full in "readme.txt" within the 2013
development kit available here:
https://image-net.org/data/ILSVRC/2013/ILSVRC2013_devkit.tgz Please see the
section entitled "3.3 CLS-LOC submission format". Briefly, the format of the
text file is 100,000 lines corresponding to each image in the test split. Each
line of integers correspond to the rank-ordered, top 5 predictions for each test
image. The integers are 1-indexed corresponding to the line number in the
corresponding labels file. See labels.txt.
