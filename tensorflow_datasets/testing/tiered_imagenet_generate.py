import pickle
import os
import numpy as np
import tensorflow as tf

_NUM_CATEGORIES_TRAIN = 20
_NUM_CATEGORIES_VAL = 6
_NUM_CATEGORIES_TEST = 8

_NUM_CLASSES_TRAIN = 351
_NUM_CLASSES_VAL = 97
_NUM_CLASSES_TEST = 160
_NUM_IMAGES_TRAIN = 400  # 448695
_NUM_IMAGES_VAL = 100  # 124261
_NUM_IMAGES_TEST = 200  # 206209
_PATH_DUMMY_DATA = "tensorflow_datasets/testing/test_data/fake_examples/tiered_imagenet"

def generate_data():
    """Generates dummy train, validation and test images file and corresponding labels file   .
    Returns:
    """
    # generate dummy train data
    train_images_data = np.random.randint(
        0, 255, (_NUM_IMAGES_TRAIN, 84, 84, 3), np.uint8)
    train_specific_labels = [str(i) for i in range(_NUM_CLASSES_TRAIN)]
    train_general_labels = [str(i) for i in range(_NUM_CATEGORIES_TRAIN)]
    train_specific_labels_str = [str(i) for i in range(_NUM_CLASSES_TRAIN)]
    train_general_labels_str = [str(i) for i in range(_NUM_CATEGORIES_TRAIN)]
    train_images = {"images":train_images_data}
    train_labels = {"label_general":train_general_labels, "label_general_str":train_general_labels_str,
                            "label_specific":train_specific_labels, "label_specific_str":train_specific_labels_str}
    # generate dummy validation data
    validation_images_data = np.random.randint(
        0, 255, (_NUM_IMAGES_VAL, 84, 84, 3), np.uint8)
    validation_specific_labels = [str(i) for i in range(_NUM_CLASSES_VAL)]
    validation_general_labels = [str(i) for i in range(_NUM_CATEGORIES_VAL)]
    validation_specific_labels_str = [str(i) for i in range(_NUM_CLASSES_VAL)]
    validation_general_labels_str = [str(i)
                                     for i in range(_NUM_CATEGORIES_VAL)]
    val_images = {"images":validation_images_data}
    val_labels = {"label_general":validation_general_labels, "label_general_str":validation_general_labels_str,
                            "label_specific":validation_specific_labels, "label_specific_str":validation_specific_labels_str}
    # generate dummy test data
    test_images_data = np.random.randint(
        0, 255, (_NUM_IMAGES_TEST, 84, 84, 3), np.uint8)
    test_specific_labels = [str(i) for i in range(_NUM_CLASSES_TEST)]
    test_general_labels = [str(i) for i in range(_NUM_CATEGORIES_TEST)]
    test_specific_labels_str = [str(i) for i in range(_NUM_CLASSES_TEST)]
    test_general_labels_str = [str(i) for i in range(_NUM_CATEGORIES_TEST)]
    test_images = {"images":test_images_data}
    test_labels = {"label_general":test_general_labels, "label_general_str":test_general_labels_str,
                            "label_specific":test_specific_labels, "label_specific_str":test_specific_labels_str}
    return train_images, train_labels, test_images, test_labels, val_images, val_labels


def dump_data(path, train_images, train_labels, test_images, test_labels, val_images, val_labels):
    """Saves images and labels in respective pickle files.
    Args:
        path (string): path to directory where files will be saved.
        train_images,train_labels, test_images, test_labels, val_images, val_labels
    """
    # save train images
    path_train = os.path.join(path, "train_images_png.pkl")
    with tf.io.gfile.GFile(path_train, "wb") as f:
        pickle.dump(train_images, f, pickle.HIGHEST_PROTOCOL)
    # save train labels
    path_train = os.path.join(path, "train_labels.pkl")
    with tf.io.gfile.GFile(path_train, "wb") as f:
        pickle.dump(train_labels, f, pickle.HIGHEST_PROTOCOL)
    # save validation images
    path_validation = os.path.join(path, "val_images_png.pkl")
    with tf.io.gfile.GFile(path_validation, "wb") as f:
        pickle.dump(val_images, f, pickle.HIGHEST_PROTOCOL)
    # save validation labels
    path_validation = os.path.join(path, "val_labels.pkl")
    with tf.io.gfile.GFile(path_validation, "wb") as f:
        pickle.dump(val_labels, f, pickle.HIGHEST_PROTOCOL)
    # save test images
    path_test = os.path.join(path, "test_images_png.pkl")
    with tf.io.gfile.GFile(path_test, "wb") as f:
        pickle.dump(test_images, f, pickle.HIGHEST_PROTOCOL)
    # save test labels
    path_test = os.path.join(path, "test_labels.pkl")
    with tf.io.gfile.GFile(path_test, "wb") as f:
        pickle.dump(test_labels, f, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    data = generate_data()
    dump_data(_PATH_DUMMY_DATA, *data)
