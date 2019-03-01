# Using Google Cloud Storage to cache preprocessed data

You can use Google Cloud Storage to cache the preprocessed data. This way, downloading from source and pre-processing can happen only once.

## Why ?

It is especially useful when you're running in the mode where you don't have persistent local storage (for example colab) or when you're running multiple instances of training on multiple machines.

## How ?

First, create google cloud bucket (you might also need to create a Google Cloud Platform project first).

https://console.cloud.google.com/storage/browser

Then, create a Service Account, give it "read and write" access to your bucket and save the JSON file with the authentication information.

Finally, set the environment variable:


```
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credential/json/file
```

And run the tfds and set the data_dir to "gs://YOUR_BUCKET_NAME"

```python
ds_train, ds_test = tfds.load(name="mnist", split=["train", "test"], data_dir="gs://YOUR_BUCKET_NAME")
```


## Caveats:

  * This approach works for datasets that only use tf.gfile for data access. This is true for most datasets, but not all.
  * Please check whether license of the dataset allows such storage.
  * Data will be constantly streamed from the internet (which could lead to network costs).
