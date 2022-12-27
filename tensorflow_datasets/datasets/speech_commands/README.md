An audio dataset of spoken words designed to help train and evaluate keyword
spotting systems. Its primary goal is to provide a way to build and test small
models that detect when a single word is spoken, from a set of ten target words,
with as few false positives as possible from background noise or unrelated
speech. Note that in the train and validation set, the label "unknown" is much
more prevalent than the labels of the target words or background noise. One
difference from the release version is the handling of silent segments. While in
the test set the silence segments are regular 1 second files, in the training
they are provided as long segments under "background_noise" folder. Here we
split these background noise into 1 second clips, and also keep one of the files
for the validation set.
