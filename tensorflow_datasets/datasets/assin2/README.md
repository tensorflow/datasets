## Contextualization

ASSIN 2 is the second edition of the Avaliação de Similaridade Semântica e
Inferência Textual (Evaluating Semantic Similarity and Textual Entailment), and
was a workshop collocated with
[STIL 2019](http://www.google.com/url?q=http%3A%2F%2Fcomissoes.sbc.org.br%2Fce-pln%2Fstil2019%2F&sa=D&sntz=1&usg=AFQjCNHN8DosAsJ-gd48TfkXFX5YD6xM7g).
It follows the
[first edition of ASSIN](http://www.google.com/url?q=http%3A%2F%2Fpropor2016.di.fc.ul.pt%2F%3Fpage_id%3D381&sa=D&sntz=1&usg=AFQjCNHV7ySeNzH4k6MWKBLqO9yUkqiUqw),
proposing a new shared task with new data.

The workshop evaluated systems that assess two types of relations between two
sentences: Semantic Textual Similarity and Textual Entailment.

Semantic Textual Similarity consists of quantifying the level of semantic
equivalence between sentences, while Textual Entailment Recognition consists of
classifying whether the first sentence entails the second.

## Data

The corpus used in ASSIN 2 is composed of rather simple sentences. Following the
procedures of SemEval 2014 Task 1, we tried to remove from the corpus named
entities and indirect speech, and tried to have all verbs in the present tense.
The
[annotation instructions](https://drive.google.com/open?id=1aUPhywEHD0r_pxPiTqZwS0fRj-1Xda2w)
given to annotators are available (in Portuguese).

The training and validation data are composed, respectively, of 6,500 and 500
sentence pairs in Brazilian Portuguese, annotated for entailment and semantic
similarity. Semantic similarity values range from 1 to 5, and text entailment
classes are either entailment or none. The test data are composed of
approximately 3,000 sentence pairs with the same annotation. All data were
manually annotated.

## Evaluation

Evaluation The evaluation of submissions to ASSIN 2 was with the same metrics as
the first ASSIN, with the F1 of precision and recall as the main metric for text
entailment and Pearson correlation for semantic similarity. The
[evaluation scripts](https://github.com/erickrf/assin) are the same as in the
last edition.

PS.: Description is extracted from
[official homepage](https://sites.google.com/view/assin2/english).
