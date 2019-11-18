import tensorflow_datasets as tfds
import tensorflow as tf

# Show bbbp dataset info
bbbp_builder = tfds.builder("bbbp")
print(bbbp_builder.info)


# Very simple way to create/prepare/split bbbp dataset
dataset = tfds.load(name="bbbp", split=tfds.Split.TRAIN)

dataset = dataset.shuffle(128).batch(32).prefetch(tf.data.experimental.AUTOTUNE)
for features in dataset.take(1):
  smile, label = features["smile"], features["label"]
  print(smile, label)

