TyDi QA is a question answering dataset covering 11 typologically diverse
languages with 204K question-answer pairs. The languages of TyDi QA are diverse
with regard to their typology -- the set of linguistic features that each
language expresses -- such that we expect models performing well on this set to
generalize across a large number of the languages in the world. It contains
language phenomena that would not be found in English-only corpora. To provide a
realistic information-seeking task and avoid priming effects, questions are
written by people who want to know the answer, but don't know the answer yet,
(unlike SQuAD and its descendents) and the data is collected directly in each
language without the use of translation (unlike MLQA and XQuAD).

IMPORTANT: Please choose your training split carefully.

Training splits:

'train': This is the GoldP task from the original TyDi QA paper
[https://arxiv.org/abs/2003.05002] that has original-language labeled training
data.

'translate-train-*': These splits are the automatic translations from English to
each target language used in the translate-train baselines in the XTREME paper
[https://arxiv.org/abs/2003.11080]. This purposefully ignores the non-English
TyDiQA-GoldP training data to simulate the transfer learning scenario where
original-language data is not available and system builders must rely on labeled
English data plus existing machine translation systems.

Typically, you should use EITHER the train or translate-train split, but not
both.
