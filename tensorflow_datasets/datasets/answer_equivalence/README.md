The Answer Equivalence Dataset contains human ratings on model predictions from
several models on the SQuAD dataset. The ratings establish whether the predicted
answer is 'equivalent' to the gold answer (taking into account both question and
context).

More specifically, by 'equivalent' we mean that the predicted answer contains at
least the same information as the gold answer and does not add superfluous
information. The dataset contains annotations for: * predictions from BiDAF on
SQuAD dev * predictions from XLNet on SQuAD dev * predictions from Luke on SQuAD
dev * predictions from Albert on SQuAD training, dev and test examples
