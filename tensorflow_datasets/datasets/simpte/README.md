Full name: Simulations for Personalized Treatment Effects

Generated with the R's Uplift package:
 https://rdrr.io/cran/uplift/man/sim_pte.html

The package could be downloaded here:
 https://cran.r-project.org/src/contrib/Archive/uplift/

Dataset generated in R version 4.1.2 with following code:

```
  library(uplift)

  set.seed(123)

  train <- sim_pte(n = 1000, p = 20, rho = 0, sigma = sqrt(2), beta.den = 4)
  test <- sim_pte(n = 2000, p = 20, rho = 0, sigma = sqrt(2), beta.den = 4)

  train$treat <- ifelse(train$treat == 1, 2, 1)
  test$treat <- ifelse(test$treat == 1, 2, 1)

  train$y <- ifelse(train$y == 1, 2, 1)
  test$y <- ifelse(test$y == 1, 2, 1)

  train$ts = NULL
  test$ts = NULL
```

Parameters:

  - `n` = number of samples
  - `p` = number of predictors
  - `ro` = covariance between predictors
  - `sigma` = mutiplier of the error term
  - `beta.den` = beta is mutiplied by 1/beta.den

Creator: Leo Guelman leo.guelman@gmail.com