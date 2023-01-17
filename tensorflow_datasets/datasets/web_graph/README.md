This dataset contains a sparse graph representing web link structure for a small
subset of the Web.

Its a processed version of a single crawl performed by CommonCrawl in 2021 where
we strip everything and keep only the link->outlinks structure. The final
dataset is basically int -> List[int] format with each integer id representing a
url.

Also, in order to increase the value of this resource, we created 6 different
version of WebGraph, each varying in the sparsity pattern and locale. We took
the following processing steps, in order:

-   We started with WAT files from June 2021 crawl.
-   Since the outlinks in HTTP-Response-Metadata are stored as relative paths,
    we convert them to absolute paths using urllib after validating each link.
-   To study locale-specific graphs, we further filter based on 2 top level
    domains: ‘de’ and ‘in’, each producing a graph with an order of magnitude
    less number of nodes.
-   These graphs can still have arbitrary sparsity patterns and dangling links.
    Thus we further filter the nodes in each graph to have minimum of K ∈ [10,
    50] inlinks and outlinks. Note that we only do this processing once, thus
    this is still an approximation i.e. the resulting graph might have nodes
    with less than K links.
-   Using both locale and count filters, we finalize 6 versions of WebGraph
    dataset, summarized in the folling table.

Version   | Top level domain | Min count | Num nodes | Num edges
--------- | ---------------- | --------- | --------- | ---------
sparse    |                  | 10        | 365.4M    | 30B
dense     |                  | 50        | 136.5M    | 22B
de-sparse | de               | 10        | 19.7M     | 1.19B
de-dense  | de               | 50        | 5.7M      | 0.82B
in-sparse | in               | 10        | 1.5M      | 0.14B
in-dense  | in               | 50        | 0.5M      | 0.12B

All versions of the dataset have following features:

-   "row_tag": a unique identifier of the row (source link).
-   "col_tag": a list of unique identifiers of non-zero columns (dest outlinks).
-   "gt_tag": a list of unique identifiers of non-zero columns used as ground
    truth (dest outlinks), empty for train/train_t splits.
