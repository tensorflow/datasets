Procedurally Generated Matrices (PGM) data from the paper Measuring Abstract
Reasoning in Neural Networks, Barrett, Hill, Santoro et al. 2018. The goal is to
infer the correct answer from the context panels based on abstract reasoning.

To use this data set, please download all the *.tar.gz files from the data set
page and place them in ~/tensorflow_datasets/abstract_reasoning/.

$R$ denotes the set of relation types (progression, XOR, OR, AND, consistent
union), $O$ denotes the object types (shape, line), and $A$ denotes the
attribute types (size, colour, position, number). The structure of a matrix,
$S$, is the set of triples $S={[r, o, a]}$ that determine the challenge posed by
a particular matrix.
