import tensorflow_datasets as tfds

data = tfds.load('spine_web', split="train")
for ele in data:
    print(ele)
    break
