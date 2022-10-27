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
