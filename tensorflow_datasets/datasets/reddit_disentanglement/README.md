This dataset contains ~3M messages from reddit. Every message is labeled with
metadata. The task is to predict the id of its parent message in the
corresponding thread. Each record contains a list of messages from one thread.
Duplicated and broken records are removed from the dataset.

Features are:

- id - message id
- text - message text
- author - message author
- created_utc - message UTC timestamp
- link_id - id of the post that the comment relates to

Target:

- parent_id - id of the parent message in the current
thread
