This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406
machine translated training pairs in six typologically distinct languages:

*   French
*   Spanish
*   German
*   Chinese
*   Japanese
*   Korean

For further details, see the accompanying paper: PAWS-X: A Cross-lingual
Adversarial Dataset for Paraphrase Identification at
https://arxiv.org/abs/1908.11828

Similar to PAWS Dataset, examples are split into Train/Dev/Test sections. All
files are in the tsv format with four columns:

1. `id`: A unique id for each pair.
2. `sentence1`: The first sentence.
3. `sentence2`: The second sentence.
4. `(noisy_)label`: (Noisy) label for each pair.

Each label has two possible values: 0 indicates the pair has different meaning,
while 1 indicates the pair is a paraphrase.
