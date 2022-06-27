# omp

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/omp)
*   [Huggingface](https://huggingface.co/datasets/omp)


## posts_labeled


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:omp/posts_labeled')
```

*   **Description**:

```
The “One Million Posts” corpus is an annotated data set consisting of
user comments posted to an Austrian newspaper website (in German language).

DER STANDARD is an Austrian daily broadsheet newspaper. On the newspaper’s website,
there is a discussion section below each news article where readers engage in
online discussions. The data set contains a selection of user posts from the
12 month time span from 2015-06-01 to 2016-05-31. There are 11,773 labeled and
1,000,000 unlabeled posts in the data set. The labeled posts were annotated by
professional forum moderators employed by the newspaper.

The data set contains the following data for each post:

* Post ID
* Article ID
* Headline (max. 250 characters)
* Main Body (max. 750 characters)
* User ID (the user names used by the website have been re-mapped to new numeric IDs)
* Time stamp
* Parent post (replies give rise to tree-like discussion thread structures)
* Status (online or deleted by a moderator)
* Number of positive votes by other community members
* Number of negative votes by other community members

For each article, the data set contains the following data:

* Article ID
* Publishing date
* Topic Path (e.g.: Newsroom / Sports / Motorsports / Formula 1)
* Title
* Body

Detailed descriptions of the post selection and annotation procedures are given in the paper.

## Annotated Categories

Potentially undesirable content:

* Sentiment (negative/neutral/positive)
    An important goal is to detect changes in the prevalent sentiment in a discussion, e.g.,
    the location within the fora and the point in time where a turn from positive/neutral
    sentiment to negative sentiment takes place.
* Off-Topic (yes/no)
    Posts which digress too far from the topic of the corresponding article.
* Inappropriate (yes/no)
    Swearwords, suggestive and obscene language, insults, threats etc.
* Discriminating (yes/no)
    Racist, sexist, misogynistic, homophobic, antisemitic and other misanthropic content.

Neutral content that requires a reaction:

* Feedback (yes/no)
    Sometimes users ask questions or give feedback to the author of the article or the
    newspaper in general, which may require a reply/reaction.

Potentially desirable content:

* Personal Stories (yes/no)
    In certain fora, users are encouraged to share their personal stories, experiences,
    anecdotes etc. regarding the respective topic.
* Arguments Used (yes/no)
    It is desirable for users to back their statements with rational argumentation,
    reasoning and sources.
```

*   **License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 40567

*   **Features**:

```json
{
    "ID_Post": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ID_Parent_Post": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ID_Article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ID_User": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "CreatedAt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Status": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Headline": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "PositiveVotes": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "NegativeVotes": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "Category": {
        "num_classes": 9,
        "names": [
            "ArgumentsUsed",
            "Discriminating",
            "Inappropriate",
            "OffTopic",
            "PersonalStories",
            "PossiblyFeedback",
            "SentimentNegative",
            "SentimentNeutral",
            "SentimentPositive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "Value": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "Fold": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## posts_unlabeled


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:omp/posts_unlabeled')
```

*   **Description**:

```
The “One Million Posts” corpus is an annotated data set consisting of
user comments posted to an Austrian newspaper website (in German language).

DER STANDARD is an Austrian daily broadsheet newspaper. On the newspaper’s website,
there is a discussion section below each news article where readers engage in
online discussions. The data set contains a selection of user posts from the
12 month time span from 2015-06-01 to 2016-05-31. There are 11,773 labeled and
1,000,000 unlabeled posts in the data set. The labeled posts were annotated by
professional forum moderators employed by the newspaper.

The data set contains the following data for each post:

* Post ID
* Article ID
* Headline (max. 250 characters)
* Main Body (max. 750 characters)
* User ID (the user names used by the website have been re-mapped to new numeric IDs)
* Time stamp
* Parent post (replies give rise to tree-like discussion thread structures)
* Status (online or deleted by a moderator)
* Number of positive votes by other community members
* Number of negative votes by other community members

For each article, the data set contains the following data:

* Article ID
* Publishing date
* Topic Path (e.g.: Newsroom / Sports / Motorsports / Formula 1)
* Title
* Body

Detailed descriptions of the post selection and annotation procedures are given in the paper.

## Annotated Categories

Potentially undesirable content:

* Sentiment (negative/neutral/positive)
    An important goal is to detect changes in the prevalent sentiment in a discussion, e.g.,
    the location within the fora and the point in time where a turn from positive/neutral
    sentiment to negative sentiment takes place.
* Off-Topic (yes/no)
    Posts which digress too far from the topic of the corresponding article.
* Inappropriate (yes/no)
    Swearwords, suggestive and obscene language, insults, threats etc.
* Discriminating (yes/no)
    Racist, sexist, misogynistic, homophobic, antisemitic and other misanthropic content.

Neutral content that requires a reaction:

* Feedback (yes/no)
    Sometimes users ask questions or give feedback to the author of the article or the
    newspaper in general, which may require a reply/reaction.

Potentially desirable content:

* Personal Stories (yes/no)
    In certain fora, users are encouraged to share their personal stories, experiences,
    anecdotes etc. regarding the respective topic.
* Arguments Used (yes/no)
    It is desirable for users to back their statements with rational argumentation,
    reasoning and sources.
```

*   **License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1000000

*   **Features**:

```json
{
    "ID_Post": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ID_Parent_Post": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ID_Article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ID_User": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "CreatedAt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Status": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Headline": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "PositiveVotes": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "NegativeVotes": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## articles


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:omp/articles')
```

*   **Description**:

```
The “One Million Posts” corpus is an annotated data set consisting of
user comments posted to an Austrian newspaper website (in German language).

DER STANDARD is an Austrian daily broadsheet newspaper. On the newspaper’s website,
there is a discussion section below each news article where readers engage in
online discussions. The data set contains a selection of user posts from the
12 month time span from 2015-06-01 to 2016-05-31. There are 11,773 labeled and
1,000,000 unlabeled posts in the data set. The labeled posts were annotated by
professional forum moderators employed by the newspaper.

The data set contains the following data for each post:

* Post ID
* Article ID
* Headline (max. 250 characters)
* Main Body (max. 750 characters)
* User ID (the user names used by the website have been re-mapped to new numeric IDs)
* Time stamp
* Parent post (replies give rise to tree-like discussion thread structures)
* Status (online or deleted by a moderator)
* Number of positive votes by other community members
* Number of negative votes by other community members

For each article, the data set contains the following data:

* Article ID
* Publishing date
* Topic Path (e.g.: Newsroom / Sports / Motorsports / Formula 1)
* Title
* Body

Detailed descriptions of the post selection and annotation procedures are given in the paper.

## Annotated Categories

Potentially undesirable content:

* Sentiment (negative/neutral/positive)
    An important goal is to detect changes in the prevalent sentiment in a discussion, e.g.,
    the location within the fora and the point in time where a turn from positive/neutral
    sentiment to negative sentiment takes place.
* Off-Topic (yes/no)
    Posts which digress too far from the topic of the corresponding article.
* Inappropriate (yes/no)
    Swearwords, suggestive and obscene language, insults, threats etc.
* Discriminating (yes/no)
    Racist, sexist, misogynistic, homophobic, antisemitic and other misanthropic content.

Neutral content that requires a reaction:

* Feedback (yes/no)
    Sometimes users ask questions or give feedback to the author of the article or the
    newspaper in general, which may require a reply/reaction.

Potentially desirable content:

* Personal Stories (yes/no)
    In certain fora, users are encouraged to share their personal stories, experiences,
    anecdotes etc. regarding the respective topic.
* Arguments Used (yes/no)
    It is desirable for users to back their statements with rational argumentation,
    reasoning and sources.
```

*   **License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 12087

*   **Features**:

```json
{
    "ID_Article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Path": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "publishingDate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


