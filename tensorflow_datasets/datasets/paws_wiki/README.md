Existing paraphrase identification datasets lack sentence pairs that have high
lexical overlap without being paraphrases. Models trained on such data fail to
distinguish pairs like flights from New York to Florida and flights from Florida
to New York. This dataset contains 108,463 human-labeled and 656k noisily
labeled pairs that feature the importance of modeling structure, context, and
word order information for the problem of paraphrase identification.

For further details, see the accompanying paper: PAWS: Paraphrase Adversaries
from Word Scrambling at https://arxiv.org/abs/1904.01130

This corpus contains pairs generated from Wikipedia pages, containing pairs that
are generated from both word swapping and back translation methods. All pairs
have human judgements on both paraphrasing and fluency and they are split into
Train/Dev/Test sections.

All files are in the tsv format with four columns:

1. `id`: A unique id for each pair.
2. `sentence1`: The first sentence.
3. `sentence2`: The second sentence.
4. `(noisy_)label`: (Noisy) label for each pair.

Each label has two possible values: 0 indicates the pair has different meaning,
while 1 indicates the pair is a paraphrase.
