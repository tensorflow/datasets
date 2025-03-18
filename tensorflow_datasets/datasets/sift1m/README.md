Pre-trained embeddings for approximate nearest neighbor search using the
Euclidean distance. This dataset consists of two splits:

1.  'database': consists of 1,000,000 data points, each has features:
    'embedding' (128 floats), 'index' (int64), 'neighbors' (empty list).
2.  'test': consists of 10,000 data points, each has features: 'embedding' (128
    floats), 'index' (int64), 'neighbors' (list of 'index' and 'distance' of the
    nearest neighbors in the database.)
