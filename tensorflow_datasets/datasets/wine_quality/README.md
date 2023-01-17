Two datasets were created, using red and white wine samples. The inputs include
objective tests (e.g. PH values) and the output is based on sensory data (median
of at least 3 evaluations made by wine experts). Each expert graded the wine
quality between 0 (very bad) and 10 (very excellent). Several data mining
methods were applied to model these datasets under a regression approach. The
support vector machine model achieved the best results. Several metrics were
computed: MAD, confusion matrix for a fixed error tolerance (T), etc. Also, we
plot the relative importances of the input variables (as measured by a
sensitivity analysis procedure).

The two datasets are related to red and white variants of the Portuguese "Vinho
Verde" wine. For more details, consult: http://www.vinhoverde.pt/en/ or the
reference [Cortez et al., 2009]. Due to privacy and logistic issues, only
physicochemical (inputs) and sensory (the output) variables are available (e.g.
there is no data about grape types, wine brand, wine selling price, etc.).

Number of Instances: red wine - 1599; white wine - 4898

Input variables (based on physicochemical tests):

1.  fixed acidity
2.  volatile acidity
3.  citric acid
4.  residual sugar
5.  chlorides
6.  free sulfur dioxide
7.  total sulfur dioxide
8.  density
9.  pH
10. sulphates
11. alcohol

Output variable (based on sensory data):

1.  quality (score between 0 and 10)
