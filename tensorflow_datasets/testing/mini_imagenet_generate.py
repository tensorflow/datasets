import pickle
import os
import numpy as np
import tensorflow as tf

_NUM_CLASSES_TRAIN = 3
_NUM_CLASSES_VALIDATION = 2
_NUM_CLASSES_TEST = 2

_NUM_IMAGES_PER_CLASS = 2

_PATH_DUMMY_DATA = \
    "tensorflow_datasets/testing/test_data/fake_examples/mini_imagenet"


def generate_data(num_classes_train,
                  num_classes_validation,
                  num_classes_test,
                  num_images_per_class):
    """Generates dummy train, validation and test data.

    Args:
        num_classes_train (int): number of classes in train.
        num_classes_validation (int): number of classes in validation.
        num_classes_test (int): number of classes in test.
        num_images_per_class (int): number of images per class.

    Returns:
        dict_data_train (dict): train data dict of image and label.
            keys:
                "image_data" (np.ndarray, shape=[num_train, 84, 84, 3],
                              dtype=np.uint8)
                "class_dict" (dict): class name to list of image indices.
                    value: (list of int, len=num_images_per_class)
        dict_data_validation (dict): validation data dict of image and label.
            keys:
                "image_data" (np.ndarray, shape=[num_validation, 84, 84, 3],
                              dtype=np.uint8)
                "class_dict" (dict): class name to list of image indices.
                    value: (list of int, len=num_images_per_class)
        dict_data_test (dict): test data dict of image and label.
            keys:
                "image_data" (np.ndarray, shape=[num_test, 84, 84, 3],
                              dtype=np.uint8)
                "class_dict" (dict): class name to list of image indices.
                    value: (list of int, len=num_images_per_class)
    """
    num_train = num_classes_train * num_images_per_class
    num_validation = num_classes_validation * num_images_per_class
    num_test = num_classes_test * num_images_per_class

    # generate dummy train data
    image_data_train = np.random.randint(
        0, 255, (num_train, 84, 84, 3), np.uint8)
    keys_train = [str(i) for i in range(num_classes_train)]
    values_train = np.reshape(
        np.arange(num_train),
        (num_classes_train, num_images_per_class)
    ).tolist()
    class_dict_train = dict(zip(keys_train, values_train))
    dict_data_train = {
        "image_data": image_data_train,
        "class_dict": class_dict_train,
    }

    # generate dummy validation data
    image_data_validation = np.random.randint(
        0, 255, (num_validation, 84, 84, 3), np.uint8)
    keys_validation = [str(i+num_classes_train)
                       for i in range(num_classes_validation)]
    values_validation = np.reshape(
        np.arange(num_validation),
        (num_classes_validation, num_images_per_class)
    ).tolist()
    class_dict_validation = dict(zip(keys_validation, values_validation))
    dict_data_validation = {
        "image_data": image_data_validation,
        "class_dict": class_dict_validation,
    }

    # generate dummy test data
    image_data_test = np.random.randint(
        0, 255, (num_test, 84, 84, 3), np.uint8)
    keys_test = [str(i+num_classes_train+num_classes_validation)
                 for i in range(num_classes_test)]
    values_test = np.reshape(
        np.arange(num_test),
        (num_classes_test, num_images_per_class)
    ).tolist()
    class_dict_test = dict(zip(keys_test, values_test))
    dict_data_test = {
        "image_data": image_data_test,
        "class_dict": class_dict_test,
    }

    return dict_data_train, dict_data_validation, dict_data_test


def dump_data(dict_data_train, dict_data_validation, dict_data_test, path):
    """Saves data in pickle file.

    Args:
        dict_data_train (dict): train data dict of image and label.
            keys:
                "image_data" (np.ndarray, shape=[num_train, 84, 84, 3],
                              dtype=np.uint8)
                "class_dict" (dict): class name to list of image indices.
                    value: (list of int, len=num_images_per_class)
        dict_data_validation (dict): validation data dict of image and label.
            keys:
                "image_data" (np.ndarray, shape=[num_validation, 84, 84, 3],
                              dtype=np.uint8)
                "class_dict" (dict): class name to list of image indices.
                    value: (list of int, len=num_images_per_class)
        dict_data_test (dict): test data dict of image and label.
            keys:
                "image_data" (np.ndarray, shape=[num_test, 84, 84, 3],
                              dtype=np.uint8)
                "class_dict" (dict): class name to list of image indices.
                    value: (list of int, len=num_images_per_class)
        path (string): path to directory where files will be saved.
    """
    # save train data
    path_train = os.path.join(path, "mini-imagenet-cache-train.pkl")
    with tf.io.gfile.GFile(path_train, "wb") as f:
        pickle.dump(dict_data_train, f, pickle.HIGHEST_PROTOCOL)

    # save validation data
    path_validation = os.path.join(path, "mini-imagenet-cache-val.pkl")
    with tf.io.gfile.GFile(path_validation, "wb") as f:
        pickle.dump(dict_data_validation, f, pickle.HIGHEST_PROTOCOL)

    # save test data
    path_test = os.path.join(path, "mini-imagenet-cache-test.pkl")
    with tf.io.gfile.GFile(path_test, "wb") as f:
        pickle.dump(dict_data_test, f, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    data = generate_data(_NUM_CLASSES_TRAIN, _NUM_CLASSES_VALIDATION,
                         _NUM_CLASSES_TEST, _NUM_IMAGES_PER_CLASS)
    dump_data(*data, _PATH_DUMMY_DATA)
