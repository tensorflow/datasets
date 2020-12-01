<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="movielens" />
  <meta itemprop="description" content="This dataset contains a set of movie ratings from the MovieLens website, a movie&#10;recommendation service. This dataset was collected and maintained by [GroupLens]&#10;(https://grouplens.org/), a research group at the University of Minnesota. There&#10;are 5 versions included: &quot;25m&quot;, &quot;latest-small&quot;, &quot;100k&quot;, &quot;1m&quot;, &quot;20m&quot;. In all&#10;datasets, the movies data and ratings data are joined on &quot;movieId&quot;. The 25m&#10;dataset, latest-small dataset, and 20m dataset contain only movie data and&#10;rating data. The 1m dataset and 100k dataset contain demographic data in&#10;addition to movie and rating data.&#10;&#10;- &quot;25m&quot;: This is the latest stable version of the MovieLens dataset. It is&#10;recommended for research purposes.&#10;- &quot;latest-small&quot;: This is a small subset of the latest version of the MovieLens&#10;dataset. It is changed and updated over time by GroupLens.&#10;- &quot;100k&quot;: This is the oldest version of the MovieLens datasets. It is a small&#10;dataset with demographic data.&#10;- &quot;1m&quot;: This is the largest MovieLens dataset that contains demographic data.&#10;- &quot;20m&quot;: This is one of the most used MovieLens datasets in academic papers&#10;along with the 1m dataset.&#10;&#10;For each version, users can view either only the movies data by adding the&#10;&quot;-movies&quot; suffix (e.g. &quot;25m-movies&quot;) or the ratings data joined with the movies&#10;data (and users data in the 1m and 100k datasets) by adding the &quot;-ratings&quot;&#10;suffix (e.g. &quot;25m-ratings&quot;).&#10;&#10;The features below are included in all versions with the &quot;-ratings&quot; suffix.&#10;&#10;- &quot;movie_id&quot;: a unique identifier of the rated movie&#10;- &quot;movie_title&quot;: the title of the rated movie with the release year in&#10;parentheses&#10;- &quot;movie_genres&quot;: a sequence of genres to which the rated movie belongs&#10;- &quot;user_id&quot;: a unique identifier of the user who made the rating&#10;- &quot;user_rating&quot;: the score of the rating on a five-star scale&#10;- &quot;timestamp&quot;: the timestamp of the ratings, represented in seconds since&#10;midnight Coordinated Universal Time (UTC) of January 1, 1970&#10;&#10;The &quot;100k-ratings&quot; and &quot;1m-ratings&quot; versions in addition include the following&#10;demographic features.&#10;&#10;- &quot;user_gender&quot;: gender of the user who made the rating; a true value&#10;corresponds to male&#10;- &quot;bucketized_user_age&quot;: bucketized age values of the user who made the rating,&#10;the values and the corresponding ranges are:&#10;  - 1: &quot;Under 18&quot;&#10;  - 18: &quot;18-24&quot;&#10;  - 25: &quot;25-34&quot;&#10;  - 35: &quot;35-44&quot;&#10;  - 45: &quot;45-49&quot;&#10;  - 50: &quot;50-55&quot;&#10;  - 56: &quot;56+&quot;&#10;- &quot;user_occupation_label&quot;: the occupation of the user who made the rating&#10;represented by an integer-encoded label; labels are preprocessed to be&#10;consistent across different versions&#10;- &quot;user_occupation_text&quot;: the occupation of the user who made the rating in&#10;the original string; different versions can have different set of raw text&#10;labels&#10;- &quot;user_zip_code&quot;: the zip code of the user who made the rating&#10;&#10;In addition, the &quot;100k-ratings&quot; dataset would also have a feature &quot;raw_user_age&quot;&#10;which is the exact ages of the users who made the rating&#10;&#10;Datasets with the &quot;-movies&quot; suffix contain only &quot;movie_id&quot;, &quot;movie_title&quot;, and&#10;&quot;movie_genres&quot; features.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;movielens&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/movielens" />
  <meta itemprop="sameAs" content="https://grouplens.org/datasets/movielens/" />
  <meta itemprop="citation" content="@article{10.1145/2827872,&#10;author = {Harper, F. Maxwell and Konstan, Joseph A.},&#10;title = {The MovieLens Datasets: History and Context},&#10;year = {2015},&#10;issue_date = {January 2016},&#10;publisher = {Association for Computing Machinery},&#10;address = {New York, NY, USA},&#10;volume = {5},&#10;number = {4},&#10;issn = {2160-6455},&#10;url = {https://doi.org/10.1145/2827872},&#10;doi = {10.1145/2827872},&#10;journal = {ACM Trans. Interact. Intell. Syst.},&#10;month = dec,&#10;articleno = {19},&#10;numpages = {19},&#10;keywords = {Datasets, recommendations, ratings, MovieLens}&#10;}" />
</div>

# `movielens`

*   **Description**:

This dataset contains a set of movie ratings from the MovieLens website, a movie
recommendation service. This dataset was collected and maintained by
[GroupLens](https://grouplens.org/), a research group at the University of
Minnesota. There are 5 versions included: "25m", "latest-small", "100k", "1m",
"20m". In all datasets, the movies data and ratings data are joined on
"movieId". The 25m dataset, latest-small dataset, and 20m dataset contain only
movie data and rating data. The 1m dataset and 100k dataset contain demographic
data in addition to movie and rating data.

-   "25m": This is the latest stable version of the MovieLens dataset. It is
    recommended for research purposes.
-   "latest-small": This is a small subset of the latest version of the
    MovieLens dataset. It is changed and updated over time by GroupLens.
-   "100k": This is the oldest version of the MovieLens datasets. It is a small
    dataset with demographic data.
-   "1m": This is the largest MovieLens dataset that contains demographic data.
-   "20m": This is one of the most used MovieLens datasets in academic papers
    along with the 1m dataset.

For each version, users can view either only the movies data by adding the
"-movies" suffix (e.g. "25m-movies") or the ratings data joined with the movies
data (and users data in the 1m and 100k datasets) by adding the "-ratings"
suffix (e.g. "25m-ratings").

The features below are included in all versions with the "-ratings" suffix.

-   "movie_id": a unique identifier of the rated movie
-   "movie_title": the title of the rated movie with the release year in
    parentheses
-   "movie_genres": a sequence of genres to which the rated movie belongs
-   "user_id": a unique identifier of the user who made the rating
-   "user_rating": the score of the rating on a five-star scale
-   "timestamp": the timestamp of the ratings, represented in seconds since
    midnight Coordinated Universal Time (UTC) of January 1, 1970

The "100k-ratings" and "1m-ratings" versions in addition include the following
demographic features.

-   "user_gender": gender of the user who made the rating; a true value
    corresponds to male
-   "bucketized_user_age": bucketized age values of the user who made the
    rating, the values and the corresponding ranges are:
    -   1: "Under 18"
    -   18: "18-24"
    -   25: "25-34"
    -   35: "35-44"
    -   45: "45-49"
    -   50: "50-55"
    -   56: "56+"
-   "user_occupation_label": the occupation of the user who made the rating
    represented by an integer-encoded label; labels are preprocessed to be
    consistent across different versions
-   "user_occupation_text": the occupation of the user who made the rating in
    the original string; different versions can have different set of raw text
    labels
-   "user_zip_code": the zip code of the user who made the rating

In addition, the "100k-ratings" dataset would also have a feature "raw_user_age"
which is the exact ages of the users who made the rating

Datasets with the "-movies" suffix contain only "movie_id", "movie_title", and
"movie_genres" features.

*   **Homepage**:
    [https://grouplens.org/datasets/movielens/](https://grouplens.org/datasets/movielens/)

*   **Source code**:
    [`tfds.structured.Movielens`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/movielens.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@article{10.1145/2827872,
author = {Harper, F. Maxwell and Konstan, Joseph A.},
title = {The MovieLens Datasets: History and Context},
year = {2015},
issue_date = {January 2016},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {5},
number = {4},
issn = {2160-6455},
url = {https://doi.org/10.1145/2827872},
doi = {10.1145/2827872},
journal = {ACM Trans. Interact. Intell. Syst.},
month = dec,
articleno = {19},
numpages = {19},
keywords = {Datasets, recommendations, ratings, MovieLens}
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

## movielens/25m-ratings (default config)

*   **Config description**: This dataset contains 25,000,095 ratings across
    62,423 movies, created by 162,541 users between January 09, 1995 and
    November 21,
*   This dataset is the latest stable version of the MovieLens dataset,
    generated on November 21, 2019.

Each user has rated at least 20 movies. The ratings are in half-star increments.
This dataset does not include demographic data.

*   **Download size**: `249.84 MiB`

*   **Dataset size**: `3.89 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 25,000,095

*   **Features**:

```python
FeaturesDict({
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
    'timestamp': tf.int64,
    'user_id': tf.string,
    'user_rating': tf.float32,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-25m-ratings-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## movielens/25m-movies

*   **Config description**: This dataset contains data of 62,423 movies rated in
    the 25m dataset.

*   **Download size**: `249.84 MiB`

*   **Dataset size**: `5.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 62,423

*   **Features**:

```python
FeaturesDict({
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-25m-movies-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## movielens/latest-small-ratings

*   **Config description**: This dataset contains 100,836 ratings across 9,742
    movies, created by 610 users between March 29, 1996 and September 24, 2018.
    This dataset is generated on September 26, 2018 and is the a subset of the
    full latest version of the MovieLens dataset. This dataset is changed and
    updated over time.

Each user has rated at least 20 movies. The ratings are in half-star increments.
This dataset does not include demographic data.

*   **Download size**: `955.28 KiB`

*   **Dataset size**: `15.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 100,836

*   **Features**:

```python
FeaturesDict({
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
    'timestamp': tf.int64,
    'user_id': tf.string,
    'user_rating': tf.float32,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-latest-small-ratings-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## movielens/latest-small-movies

*   **Config description**: This dataset contains data of 9,742 movies rated in
    the latest-small dataset.

*   **Download size**: `955.28 KiB`

*   **Dataset size**: `910.64 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,742

*   **Features**:

```python
FeaturesDict({
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-latest-small-movies-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## movielens/100k-ratings

*   **Config description**: This dataset contains 100,000 ratings from 943 users
    on 1,682 movies. This dataset is the oldest version of the MovieLens
    dataset.

Each user has rated at least 20 movies. Ratings are in whole-star increments.
This dataset contains demographic data of users in addition to data on movies
and ratings.

*   **Download size**: `4.70 MiB`

*   **Dataset size**: `32.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 100,000

*   **Features**:

```python
FeaturesDict({
    'bucketized_user_age': tf.float32,
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
    'raw_user_age': tf.float32,
    'timestamp': tf.int64,
    'user_gender': tf.bool,
    'user_id': tf.string,
    'user_occupation_label': ClassLabel(shape=(), dtype=tf.int64, num_classes=22),
    'user_occupation_text': tf.string,
    'user_rating': tf.float32,
    'user_zip_code': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-100k-ratings-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## movielens/100k-movies

*   **Config description**: This dataset contains data of 1,682 movies rated in
    the 100k dataset.

*   **Download size**: `4.70 MiB`

*   **Dataset size**: `150.35 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 1,682

*   **Features**:

```python
FeaturesDict({
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-100k-movies-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## movielens/1m-ratings

*   **Config description**: This dataset contains 1,000,209 anonymous ratings of
    approximately 3,900 movies made by 6,040 MovieLens users who joined
    MovieLens in
*   This dataset is the largest dataset that includes demographic data.

Each user has rated at least 20 movies. Ratings are in whole-star increments. In
demographic data, age values are divided into ranges and the lowest age value
for each range is used in the data instead of the actual values.

*   **Download size**: `5.64 MiB`

*   **Dataset size**: `308.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,000,209

*   **Features**:

```python
FeaturesDict({
    'bucketized_user_age': tf.float32,
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
    'timestamp': tf.int64,
    'user_gender': tf.bool,
    'user_id': tf.string,
    'user_occupation_label': ClassLabel(shape=(), dtype=tf.int64, num_classes=22),
    'user_occupation_text': tf.string,
    'user_rating': tf.float32,
    'user_zip_code': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-1m-ratings-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## movielens/1m-movies

*   **Config description**: This dataset contains data of approximately 3,900
    movies rated in the 1m dataset.

*   **Download size**: `5.64 MiB`

*   **Dataset size**: `351.12 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,883

*   **Features**:

```python
FeaturesDict({
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-1m-movies-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## movielens/20m-ratings

*   **Config description**: This dataset contains 20,000,263 ratings across
    27,278 movies, created by 138,493 users between January 09, 1995 and March
    31, 2015. This dataset was generated on October 17, 2016.

Each user has rated at least 20 movies. Ratings are in half-star increments.
This dataset does not contain demographic data.

*   **Download size**: `189.50 MiB`

*   **Dataset size**: `3.10 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 20,000,263

*   **Features**:

```python
FeaturesDict({
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
    'timestamp': tf.int64,
    'user_id': tf.string,
    'user_rating': tf.float32,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-20m-ratings-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## movielens/20m-movies

*   **Config description**: This dataset contains data of 27,278 movies rated in
    the 20m dataset

*   **Download size**: `189.50 MiB`

*   **Dataset size**: `2.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 27,278

*   **Features**:

```python
FeaturesDict({
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movielens-20m-movies-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->