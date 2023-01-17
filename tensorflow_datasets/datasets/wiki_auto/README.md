WikiAuto provides a set of aligned sentences from English Wikipedia and Simple
English Wikipedia as a resource to train sentence simplification systems. The
authors first crowd-sourced a set of manual alignments between sentences in a
subset of the Simple English Wikipedia and their corresponding versions in
English Wikipedia (this corresponds to the `manual` config), then trained a
neural CRF system to predict these alignments. The trained model was then
applied to the other articles in Simple English Wikipedia with an English
counterpart to create a larger corpus of aligned sentences (corresponding to the
`auto`, `auto_acl`, `auto_full_no_split`, and `auto_full_with_split` configs
here).
