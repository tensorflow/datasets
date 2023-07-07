A collection of 3 referring expression datasets based off images in the COCO
dataset. A referring expression is a piece of text that describes a unique
object in an image. These datasets are collected by asking human raters to
disambiguate objects delineated by bounding boxes in the COCO dataset.

RefCoco and RefCoco+ are from Kazemzadeh et al. 2014. RefCoco+ expressions are
strictly appearance based descriptions, which they enforced by preventing raters
from using location based descriptions (e.g., "person to the right" is not a
valid description for RefCoco+). RefCocoG is from Mao et al. 2016, and has more
rich description of objects compared to RefCoco due to differences in the
annotation process. In particular, RefCoco was collected in an interactive
game-based setting, while RefCocoG was collected in a non-interactive setting.
On average, RefCocoG has 8.4 words per expression while RefCoco has 3.5 words.

Each dataset has different split allocations that are typically all reported in
papers. The "testA" and "testB" sets in RefCoco and RefCoco+ contain only people
and only non-people respectively. Images are partitioned into the various
splits. In the "google" split, objects, not images, are partitioned between the
train and non-train splits. This means that the same image can appear in both
the train and validation split, but the objects being referred to in the image
will be different between the two sets. In contrast, the "unc" and "umd" splits
partition images between the train, validation, and test split. In RefCocoG, the
"google" split does not have a canonical test set, and the validation set is
typically reported in papers as "val*".

Stats for each dataset and split ("refs" is the number of referring expressions,
and "images" is the number of images):

dataset  | partition | split | refs  | images
-------- | --------- | ----- | ----- | ------
refcoco  | google    | train | 40000 | 19213
refcoco  | google    | val   | 5000  | 4559
refcoco  | google    | test  | 5000  | 4527
refcoco  | unc       | train | 42404 | 16994
refcoco  | unc       | val   | 3811  | 1500
refcoco  | unc       | testA | 1975  | 750
refcoco  | unc       | testB | 1810  | 750
refcoco+ | unc       | train | 42278 | 16992
refcoco+ | unc       | val   | 3805  | 1500
refcoco+ | unc       | testA | 1975  | 750
refcoco+ | unc       | testB | 1798  | 750
refcocog | google    | train | 44822 | 24698
refcocog | google    | val   | 5000  | 4650
refcocog | umd       | train | 42226 | 21899
refcocog | umd       | val   | 2573  | 1300
refcocog | umd       | test  | 5023  | 2600
