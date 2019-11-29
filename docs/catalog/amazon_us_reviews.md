<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="amazon_us_reviews" />
  <meta itemprop="description" content="Amazon Customer Reviews (a.k.a. Product Reviews) is one of Amazons iconic products. In a period of over two decades since the first review in 1995, millions of Amazon customers have contributed over a hundred million reviews to express opinions and describe their experiences regarding products on the Amazon.com website. This makes Amazon Customer Reviews a rich source of information for academic researchers in the fields of Natural Language Processing (NLP), Information Retrieval (IR), and Machine Learning (ML), amongst others. Accordingly, we are releasing this data to further research in multiple disciplines related to understanding customer product experiences. Specifically, this dataset was constructed to represent a sample of customer evaluations and opinions, variation in the perception of a product across geographical regions, and promotional intent or bias in reviews.&#10;&#10;Over 130+ million customer reviews are available to researchers as part of this release. The data is available in TSV files in the amazon-reviews-pds S3 bucket in AWS US East Region. Each line in the data files corresponds to an individual review (tab delimited, with no quote and escape characters).&#10;&#10;Each Dataset contains the following columns : &#10;  marketplace       - 2 letter country code of the marketplace where the review was written.&#10;  customer_id       - Random identifier that can be used to aggregate reviews written by a single author.&#10;  review_id         - The unique ID of the review.&#10;  product_id        - The unique Product ID the review pertains to. In the multilingual dataset the reviews&#10;                      for the same product in different countries can be grouped by the same product_id.&#10;  product_parent    - Random identifier that can be used to aggregate reviews for the same product.&#10;  product_title     - Title of the product.&#10;  product_category  - Broad product category that can be used to group reviews &#10;                      (also used to group the dataset into coherent parts).&#10;  star_rating       - The 1-5 star rating of the review.&#10;  helpful_votes     - Number of helpful votes.&#10;  total_votes       - Number of total votes the review received.&#10;  vine              - Review was written as part of the Vine program.&#10;  verified_purchase - The review is on a verified purchase.&#10;  review_headline   - The title of the review.&#10;  review_body       - The review text.&#10;  review_date       - The date the review was written.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('amazon_us_reviews', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/amazon_us_reviews" />
  <meta itemprop="sameAs" content="https://s3.amazonaws.com/amazon-reviews-pds/readme.html" />
  <meta itemprop="citation" content="" />
</div>
# `amazon_us_reviews`

Amazon Customer Reviews (a.k.a. Product Reviews) is one of Amazons iconic
products. In a period of over two decades since the first review in 1995,
millions of Amazon customers have contributed over a hundred million reviews to
express opinions and describe their experiences regarding products on the
Amazon.com website. This makes Amazon Customer Reviews a rich source of
information for academic researchers in the fields of Natural Language
Processing (NLP), Information Retrieval (IR), and Machine Learning (ML), amongst
others. Accordingly, we are releasing this data to further research in multiple
disciplines related to understanding customer product experiences. Specifically,
this dataset was constructed to represent a sample of customer evaluations and
opinions, variation in the perception of a product across geographical regions,
and promotional intent or bias in reviews.

Over 130+ million customer reviews are available to researchers as part of this
release. The data is available in TSV files in the amazon-reviews-pds S3 bucket
in AWS US East Region. Each line in the data files corresponds to an individual
review (tab delimited, with no quote and escape characters).

Each Dataset contains the following columns : marketplace - 2 letter country
code of the marketplace where the review was written. customer_id - Random
identifier that can be used to aggregate reviews written by a single author.
review_id - The unique ID of the review. product_id - The unique Product ID the
review pertains to. In the multilingual dataset the reviews for the same product
in different countries can be grouped by the same product_id. product_parent -
Random identifier that can be used to aggregate reviews for the same product.
product_title - Title of the product. product_category - Broad product category
that can be used to group reviews (also used to group the dataset into coherent
parts). star_rating - The 1-5 star rating of the review. helpful_votes - Number
of helpful votes. total_votes - Number of total votes the review received.
vine - Review was written as part of the Vine program. verified_purchase - The
review is on a verified purchase. review_headline - The title of the review.
review_body - The review text. review_date - The date the review was written.

*   URL:
    [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)
*   `DatasetBuilder`:
    [`tfds.structured.amazon_us_reviews.AmazonUSReviews`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/amazon_us_reviews.py)

`amazon_us_reviews` is configured with
`tfds.structured.amazon_us_reviews.AmazonUSReviewsConfig` and has the following
configurations predefined (defaults to the first one):

*   `Wireless_v1_00` (`v0.1.0`) (`Size: 1.59 GiB`): A dataset consisting of
    reviews of Amazon Wireless_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Watches_v1_00` (`v0.1.0`) (`Size: 155.42 MiB`): A dataset consisting of
    reviews of Amazon Watches_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Video_Games_v1_00` (`v0.1.0`) (`Size: 453.19 MiB`): A dataset consisting of
    reviews of Amazon Video_Games_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Video_DVD_v1_00` (`v0.1.0`) (`Size: 1.41 GiB`): A dataset consisting of
    reviews of Amazon Video_DVD_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Video_v1_00` (`v0.1.0`) (`Size: 132.49 MiB`): A dataset consisting of
    reviews of Amazon Video_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Toys_v1_00` (`v0.1.0`) (`Size: 799.61 MiB`): A dataset consisting of
    reviews of Amazon Toys_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Tools_v1_00` (`v0.1.0`) (`Size: 318.32 MiB`): A dataset consisting of
    reviews of Amazon Tools_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Sports_v1_00` (`v0.1.0`) (`Size: 832.06 MiB`): A dataset consisting of
    reviews of Amazon Sports_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Software_v1_00` (`v0.1.0`) (`Size: 89.66 MiB`): A dataset consisting of
    reviews of Amazon Software_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Shoes_v1_00` (`v0.1.0`) (`Size: 612.50 MiB`): A dataset consisting of
    reviews of Amazon Shoes_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Pet_Products_v1_00` (`v0.1.0`) (`Size: 491.92 MiB`): A dataset consisting
    of reviews of Amazon Pet_Products_v1_00 products in US marketplace. Each
    product has its own version as specified with it.

*   `Personal_Care_Appliances_v1_00` (`v0.1.0`) (`Size: 16.82 MiB`): A dataset
    consisting of reviews of Amazon Personal_Care_Appliances_v1_00 products in
    US marketplace. Each product has its own version as specified with it.

*   `PC_v1_00` (`v0.1.0`) (`Size: 1.41 GiB`): A dataset consisting of reviews of
    Amazon PC_v1_00 products in US marketplace. Each product has its own version
    as specified with it.

*   `Outdoors_v1_00` (`v0.1.0`) (`Size: 428.16 MiB`): A dataset consisting of
    reviews of Amazon Outdoors_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Office_Products_v1_00` (`v0.1.0`) (`Size: 488.59 MiB`): A dataset
    consisting of reviews of Amazon Office_Products_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Musical_Instruments_v1_00` (`v0.1.0`) (`Size: 184.43 MiB`): A dataset
    consisting of reviews of Amazon Musical_Instruments_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Music_v1_00` (`v0.1.0`) (`Size: 1.42 GiB`): A dataset consisting of reviews
    of Amazon Music_v1_00 products in US marketplace. Each product has its own
    version as specified with it.

*   `Mobile_Electronics_v1_00` (`v0.1.0`) (`Size: 21.81 MiB`): A dataset
    consisting of reviews of Amazon Mobile_Electronics_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Mobile_Apps_v1_00` (`v0.1.0`) (`Size: 532.11 MiB`): A dataset consisting of
    reviews of Amazon Mobile_Apps_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Major_Appliances_v1_00` (`v0.1.0`) (`Size: 23.23 MiB`): A dataset
    consisting of reviews of Amazon Major_Appliances_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Luggage_v1_00` (`v0.1.0`) (`Size: 57.53 MiB`): A dataset consisting of
    reviews of Amazon Luggage_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Lawn_and_Garden_v1_00` (`v0.1.0`) (`Size: 464.22 MiB`): A dataset
    consisting of reviews of Amazon Lawn_and_Garden_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Kitchen_v1_00` (`v0.1.0`) (`Size: 887.63 MiB`): A dataset consisting of
    reviews of Amazon Kitchen_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Jewelry_v1_00` (`v0.1.0`) (`Size: 235.58 MiB`): A dataset consisting of
    reviews of Amazon Jewelry_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Home_Improvement_v1_00` (`v0.1.0`) (`Size: 480.02 MiB`): A dataset
    consisting of reviews of Amazon Home_Improvement_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Home_Entertainment_v1_00` (`v0.1.0`) (`Size: 184.22 MiB`): A dataset
    consisting of reviews of Amazon Home_Entertainment_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Home_v1_00` (`v0.1.0`) (`Size: 1.01 GiB`): A dataset consisting of reviews
    of Amazon Home_v1_00 products in US marketplace. Each product has its own
    version as specified with it.

*   `Health_Personal_Care_v1_00` (`v0.1.0`) (`Size: 964.34 MiB`): A dataset
    consisting of reviews of Amazon Health_Personal_Care_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Grocery_v1_00` (`v0.1.0`) (`Size: 382.74 MiB`): A dataset consisting of
    reviews of Amazon Grocery_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Gift_Card_v1_00` (`v0.1.0`) (`Size: 11.57 MiB`): A dataset consisting of
    reviews of Amazon Gift_Card_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Furniture_v1_00` (`v0.1.0`) (`Size: 142.08 MiB`): A dataset consisting of
    reviews of Amazon Furniture_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Electronics_v1_00` (`v0.1.0`) (`Size: 666.45 MiB`): A dataset consisting of
    reviews of Amazon Electronics_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Digital_Video_Games_v1_00` (`v0.1.0`) (`Size: 26.17 MiB`): A dataset
    consisting of reviews of Amazon Digital_Video_Games_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Digital_Video_Download_v1_00` (`v0.1.0`) (`Size: 483.49 MiB`): A dataset
    consisting of reviews of Amazon Digital_Video_Download_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Digital_Software_v1_00` (`v0.1.0`) (`Size: 18.12 MiB`): A dataset
    consisting of reviews of Amazon Digital_Software_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Digital_Music_Purchase_v1_00` (`v0.1.0`) (`Size: 241.82 MiB`): A dataset
    consisting of reviews of Amazon Digital_Music_Purchase_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Digital_Ebook_Purchase_v1_00` (`v0.1.0`) (`Size: 2.51 GiB`): A dataset
    consisting of reviews of Amazon Digital_Ebook_Purchase_v1_00 products in US
    marketplace. Each product has its own version as specified with it.

*   `Camera_v1_00` (`v0.1.0`) (`Size: 422.15 MiB`): A dataset consisting of
    reviews of Amazon Camera_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Books_v1_00` (`v0.1.0`) (`Size: 2.55 GiB`): A dataset consisting of reviews
    of Amazon Books_v1_00 products in US marketplace. Each product has its own
    version as specified with it.

*   `Beauty_v1_00` (`v0.1.0`) (`Size: 871.73 MiB`): A dataset consisting of
    reviews of Amazon Beauty_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Baby_v1_00` (`v0.1.0`) (`Size: 340.84 MiB`): A dataset consisting of
    reviews of Amazon Baby_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Automotive_v1_00` (`v0.1.0`) (`Size: 555.18 MiB`): A dataset consisting of
    reviews of Amazon Automotive_v1_00 products in US marketplace. Each product
    has its own version as specified with it.

*   `Apparel_v1_00` (`v0.1.0`) (`Size: 618.59 MiB`): A dataset consisting of
    reviews of Amazon Apparel_v1_00 products in US marketplace. Each product has
    its own version as specified with it.

*   `Digital_Ebook_Purchase_v1_01` (`v0.1.0`) (`Size: 1.21 GiB`): A dataset
    consisting of reviews of Amazon Digital_Ebook_Purchase_v1_01 products in US
    marketplace. Each product has its own version as specified with it.

*   `Books_v1_01` (`v0.1.0`) (`Size: 2.51 GiB`): A dataset consisting of reviews
    of Amazon Books_v1_01 products in US marketplace. Each product has its own
    version as specified with it.

*   `Books_v1_02` (`v0.1.0`) (`Size: 1.24 GiB`): A dataset consisting of reviews
    of Amazon Books_v1_02 products in US marketplace. Each product has its own
    version as specified with it.

## `amazon_us_reviews/Wireless_v1_00`

A dataset consisting of reviews of Amazon Wireless_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 9,002,021
TRAIN | 9,002,021

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Watches_v1_00`

A dataset consisting of reviews of Amazon Watches_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 960,872
TRAIN | 960,872

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Video_Games_v1_00`

A dataset consisting of reviews of Amazon Video_Games_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,785,997
TRAIN | 1,785,997

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Video_DVD_v1_00`

A dataset consisting of reviews of Amazon Video_DVD_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,069,140
TRAIN | 5,069,140

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Video_v1_00`

A dataset consisting of reviews of Amazon Video_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 380,604
TRAIN | 380,604

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Toys_v1_00`

A dataset consisting of reviews of Amazon Toys_v1_00 products in US marketplace.
Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 4,864,249
TRAIN | 4,864,249

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Tools_v1_00`

A dataset consisting of reviews of Amazon Tools_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,741,100
TRAIN | 1,741,100

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Sports_v1_00`

A dataset consisting of reviews of Amazon Sports_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 4,850,360
TRAIN | 4,850,360

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Software_v1_00`

A dataset consisting of reviews of Amazon Software_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 341,931
TRAIN | 341,931

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Shoes_v1_00`

A dataset consisting of reviews of Amazon Shoes_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 4,366,916
TRAIN | 4,366,916

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Pet_Products_v1_00`

A dataset consisting of reviews of Amazon Pet_Products_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,643,619
TRAIN | 2,643,619

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Personal_Care_Appliances_v1_00`

A dataset consisting of reviews of Amazon Personal_Care_Appliances_v1_00
products in US marketplace. Each product has its own version as specified with
it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 85,981
TRAIN | 85,981

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/PC_v1_00`

A dataset consisting of reviews of Amazon PC_v1_00 products in US marketplace.
Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 6,908,554
TRAIN | 6,908,554

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Outdoors_v1_00`

A dataset consisting of reviews of Amazon Outdoors_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,302,401
TRAIN | 2,302,401

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Office_Products_v1_00`

A dataset consisting of reviews of Amazon Office_Products_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,642,434
TRAIN | 2,642,434

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Musical_Instruments_v1_00`

A dataset consisting of reviews of Amazon Musical_Instruments_v1_00 products in
US marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 904,765
TRAIN | 904,765

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Music_v1_00`

A dataset consisting of reviews of Amazon Music_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 4,751,577
TRAIN | 4,751,577

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Mobile_Electronics_v1_00`

A dataset consisting of reviews of Amazon Mobile_Electronics_v1_00 products in
US marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 104,975
TRAIN | 104,975

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Mobile_Apps_v1_00`

A dataset consisting of reviews of Amazon Mobile_Apps_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,033,376
TRAIN | 5,033,376

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Major_Appliances_v1_00`

A dataset consisting of reviews of Amazon Major_Appliances_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 96,901
TRAIN | 96,901

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Luggage_v1_00`

A dataset consisting of reviews of Amazon Luggage_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 348,657
TRAIN | 348,657

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Lawn_and_Garden_v1_00`

A dataset consisting of reviews of Amazon Lawn_and_Garden_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,557,288
TRAIN | 2,557,288

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Kitchen_v1_00`

A dataset consisting of reviews of Amazon Kitchen_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 4,880,466
TRAIN | 4,880,466

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Jewelry_v1_00`

A dataset consisting of reviews of Amazon Jewelry_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,767,753
TRAIN | 1,767,753

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Home_Improvement_v1_00`

A dataset consisting of reviews of Amazon Home_Improvement_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,634,781
TRAIN | 2,634,781

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Home_Entertainment_v1_00`

A dataset consisting of reviews of Amazon Home_Entertainment_v1_00 products in
US marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 705,889
TRAIN | 705,889

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Home_v1_00`

A dataset consisting of reviews of Amazon Home_v1_00 products in US marketplace.
Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 6,221,559
TRAIN | 6,221,559

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Health_Personal_Care_v1_00`

A dataset consisting of reviews of Amazon Health_Personal_Care_v1_00 products in
US marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,331,449
TRAIN | 5,331,449

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Grocery_v1_00`

A dataset consisting of reviews of Amazon Grocery_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,402,458
TRAIN | 2,402,458

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Gift_Card_v1_00`

A dataset consisting of reviews of Amazon Gift_Card_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 149,086
TRAIN | 149,086

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Furniture_v1_00`

A dataset consisting of reviews of Amazon Furniture_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 792,113
TRAIN | 792,113

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Electronics_v1_00`

A dataset consisting of reviews of Amazon Electronics_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 3,093,869
TRAIN | 3,093,869

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Digital_Video_Games_v1_00`

A dataset consisting of reviews of Amazon Digital_Video_Games_v1_00 products in
US marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 145,431
TRAIN | 145,431

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Digital_Video_Download_v1_00`

A dataset consisting of reviews of Amazon Digital_Video_Download_v1_00 products
in US marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 4,057,147
TRAIN | 4,057,147

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Digital_Software_v1_00`

A dataset consisting of reviews of Amazon Digital_Software_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 102,084
TRAIN | 102,084

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Digital_Music_Purchase_v1_00`

A dataset consisting of reviews of Amazon Digital_Music_Purchase_v1_00 products
in US marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,688,884
TRAIN | 1,688,884

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Digital_Ebook_Purchase_v1_00`

A dataset consisting of reviews of Amazon Digital_Ebook_Purchase_v1_00 products
in US marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | ---------:
ALL   | 12,520,722
TRAIN | 12,520,722

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Camera_v1_00`

A dataset consisting of reviews of Amazon Camera_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,801,974
TRAIN | 1,801,974

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Books_v1_00`

A dataset consisting of reviews of Amazon Books_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | ---------:
ALL   | 10,319,090
TRAIN | 10,319,090

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Beauty_v1_00`

A dataset consisting of reviews of Amazon Beauty_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,115,666
TRAIN | 5,115,666

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Baby_v1_00`

A dataset consisting of reviews of Amazon Baby_v1_00 products in US marketplace.
Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,752,932
TRAIN | 1,752,932

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Automotive_v1_00`

A dataset consisting of reviews of Amazon Automotive_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 3,514,942
TRAIN | 3,514,942

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Apparel_v1_00`

A dataset consisting of reviews of Amazon Apparel_v1_00 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,906,333
TRAIN | 5,906,333

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Digital_Ebook_Purchase_v1_01`

A dataset consisting of reviews of Amazon Digital_Ebook_Purchase_v1_01 products
in US marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,101,693
TRAIN | 5,101,693

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Books_v1_01`

A dataset consisting of reviews of Amazon Books_v1_01 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 6,106,719
TRAIN | 6,106,719

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

## `amazon_us_reviews/Books_v1_02`

A dataset consisting of reviews of Amazon Books_v1_02 products in US
marketplace. Each product has its own version as specified with it.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | --------:
ALL   | 3,105,520
TRAIN | 3,105,520

### Features
```python
FeaturesDict({
    'data': FeaturesDict({
        'customer_id': Tensor(shape=(), dtype=tf.string),
        'helpful_votes': Tensor(shape=(), dtype=tf.int32),
        'marketplace': Tensor(shape=(), dtype=tf.string),
        'product_category': Tensor(shape=(), dtype=tf.string),
        'product_id': Tensor(shape=(), dtype=tf.string),
        'product_parent': Tensor(shape=(), dtype=tf.string),
        'product_title': Tensor(shape=(), dtype=tf.string),
        'review_body': Tensor(shape=(), dtype=tf.string),
        'review_date': Tensor(shape=(), dtype=tf.string),
        'review_headline': Tensor(shape=(), dtype=tf.string),
        'review_id': Tensor(shape=(), dtype=tf.string),
        'star_rating': Tensor(shape=(), dtype=tf.int32),
        'total_votes': Tensor(shape=(), dtype=tf.int32),
        'verified_purchase': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
        'vine': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    }),
})
```

### Homepage

*   [https://s3.amazonaws.com/amazon-reviews-pds/readme.html](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)

--------------------------------------------------------------------------------
