# Amazon Review Data v2 (2018)

In a period of over two decades since the first review in 1995,
millions of Amazon customers have contributed over a hundred million reviews to
express opinions and describe their experiences regarding products on the
`Amazon.com` website. This makes Amazon Customer Reviews a rich source of
information for academic researchers in the fields of Natural Language
Processing (NLP), Information Retrieval (IR), and Machine Learning (ML), amongst
others. Accordingly, we are releasing this data to further research in multiple
disciplines related to understanding customer product experiences. Specifically,
this dataset was constructed to represent a sample of customer evaluations and
opinions, variation in the perception of a product across geographical regions,
and promotional intent or bias in reviews.

233.1 million reviews in the range of May 1996 - Oct 2018 are available to researchers as part of this
release. The data is available in JSON files on [Jianmo Ni's home page](https://nijianmo.github.io/amazon/index.html). 
Each file contains the reviews written for a product in a particular category and each line in the data files is a JSON corresponding to an individual review.

## Per-category data

| Category                     | No of Reviews | No of Metadata |
| ---------------------------- | ------------- | ------------ |
| AMAZON FASHION               | 883,636       | 186,637      |
| All Beauty                   | 371,345       | 32,992       |
| Appliances                   | 602,777       | 30,459       |
| Arts Crafts and Sewing       | 2,875,917     | 303,426      |
| Automotive                  | 7,990,166     | 932,019      |
| Books                       | 51,311,621    | 2,935,525    |
| CDs and Vinyl               | 4,543,369     | 544,442      |
| Cell Phones and Accessories | 10,063,255    | 590,269      |
| Clothing Shoes and Jewelry  | 32,292,099    | 2,685,059    |
| Digital Music               | 1,584,082     | 465,392      |
| Electronics                 | 20,994,353    | 786,868      |
| Gift Cards                  | 147,194       | 1,548        |
| Grocery and Gourmet Food    | 5,074,160     | 287,209      |
| Home and Kitchen            | 21,928,568    | 1,301,225    |
| Industrial and Scientific   | 1,758,333     | 167,524      |
| Kindle Store                | 5,722,988     | 493,859      |
| Luxury Beauty               | 574,628       | 12,308       |
| Magazine Subscriptions      | 89,689        | 3,493        |
| Movies and TV               | 8,765,568     | 203,970      |
| Musical Instruments         | 1,512,530     | 120,400      |
| Office Products            | 5,581,313     | 315,644      |
| Patio Lawn and Garden       | 5,236,058     | 279,697      |
| Pet Supplies               | 6,542,483     | 206,141      |
| Prime Pantry               | 471,614       | 10,815       |
| Software                   | 459,436       | 26,815       |
| Sports and Outdoors        | 12,980,837    | 962,876      |
| Tools and Home Improvement | 9,015,203     | 571,982      |
| Toys and Games             | 8,201,231     | 634,414      |
| Video Games               | 2,565,349     | 84,893       |

## Columns

| Column Name    | Type | Description                                                                                           |
| -------------- | ---- | ----------------------------------------------------------------------------------------------------- |
| image          | str  | Images that users post after they have received the product                                           |
| overall        | int  | The overall rating (1-5 stars) of the review                                                          |
| vote           | int  | Number of helpful votes the review received                                                           |
| verified       | bool | Is the review on a verified purchase?                                                                 |
| reviewTime     | str  | The date (raw) the review was written                                                                 |
| reviewerID     | str  | ID of the reviewer, e.g. `A2SUAM1J3GNN3B`                                                             |
| asin           | str  | Amazon Standard Identification Number - a unique ID assigned to products on Amazon, e.g. `0000013714` |
| style          | str  | A JSON string containing the product metadata, e.g., `{"Format": "Hardcover"}`                        |
| reviewerName   | str  | Name of the reviewer                                                                                  |
| reviewText     | str  | The review text                                                                                       |
| summary        | str  | The summary (title) of the review                                                                     |
| unixReviewTime | int  | The date (Unix time) the review was written                                                           |

## Citation
If you use the data in any way:
1. Complete [this](https://forms.gle/A8hBfPxKkKGFCP238) form.
2. Cite this paper: [Justifying Recommendations using Distantly-Labeled Reviews and Fine-Grained Aspects](https://aclanthology.org/D19-1018) (Ni et al., EMNLP-IJCNLP 2019)
