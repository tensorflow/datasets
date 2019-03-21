import pickle
import os
import numpy as np
import tensorflow as tf


def generate_data():
    """Generates dummy train, validation and test images file and corresponding labels file   .
    Returns:
        dict_data_train (dict): train data dict of images.
            keys:
                "images" (np.ndarray, shape=[num_train, 84, 84, 3],
                              dtype=np.uint8)
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

    return train_images,train_labels, test_images, test_labels, val_images, val_labels


def dump_data(path, train_images,train_labels, test_images, test_labels, val_images, val_labels):
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
    data = generate_data(_NUM_CLASSES_TRAIN, _NUM_CLASSES_VALIDATION,
                         _NUM_CLASSES_TEST, _NUM_IMAGES_PER_CLASS)
    dump_data(*data, _PATH_DUMMY_DATA)
