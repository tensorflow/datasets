The dataset contains pairs table-question, and the respective answer. The
questions require multi-step reasoning and various data operations such as
comparison, aggregation, and arithmetic computation. The tables were randomly
selected among Wikipedia tables with at least 8 rows and 5 columns.

(As per the documentation usage notes)

-   Dev: Mean accuracy over three (not five) splits of the training data. In
    other words, train on 'split-{1,2,3}-train' and test on 'split-{1,2,3}-dev',
    respectively, then average the accuracy.

-   Test: Train on 'train' and test on 'test'.
