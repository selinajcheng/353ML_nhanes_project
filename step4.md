# Attribution Statement

# Test set results

> Predictions on `bp_test_Rock_Doves` and `chol_test_Rock_Doves` (20% held-out local splits, 1141 rows each). Best per metric **bolded**.

## BP (binary: normal / abnormal)


| Date       | Model                   | macro-F1   | macro-recall | accuracy   | Notes                                                                                                                                                                                                                                                   |
| ---------- | ----------------------- | ---------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-05-05 | AdaBoost                | 0.6365     | 0.6394       | **0.6547** | Submission #1. Default hyperparameters.                                                                                                                                                                                                                 |
| 2026-05-09 | AdaBoost **final pick** | **0.6397** | **0.6412**   | **0.6547** | Submission #2. Hyperparameters from RandomizedSearchCV: `learning_rate=0.236`, `n_estimators=239`. Default base estimator (decision stump). +0.003 macro-F1 over Submission #1.                                                                         |
| 2026-05-09 | AdaBoost                | 0.6307     | 0.6339       | 0.6494     | Submission #3. Adds `DecisionTreeClassifier(max_depth=3)` as the AdaBoost base estimator (search expanded). Preprocessor changed to drop `INDFMMPC` and `INQ300` and remove column-transformer duplications. Worse than Submission #2 on all 3 metrics. |


## CHOL (3-class: normal / borderline / high)


| Date       | Model                       | macro-F1   | macro-recall | accuracy   | Notes                                                                                                                                                                                                                                                                                                  |
| ---------- | --------------------------- | ---------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-05-05 | DecisionTree                | 0.3443     | 0.3450       | 0.4216     | Submission #1. Default hyperparameters.                                                                                                                                                                                                                                                                |
| 2026-05-09 | RandomForest                | 0.3979     | 0.4072       | 0.4522     | Submission #2. Hyperparameters from RandomizedSearchCV with `class_weight="balanced"` fixed: `n_estimators=171`, `max_depth=33`, `max_features=None`, `min_samples_leaf=11`.                                                                                                                           |
| 2026-05-09 | RandomForest **final pick** | **0.4044** | **0.4168**   | **0.4549** | Submission #3. `class_weight` added to the search distribution, picked `balanced_subsample`. Search also landed on `max_depth=13` (shallower than Submission #2). Preprocessor changed to drop `INDFMMPC` and `INQ300` and remove column-transformer duplications. +0.007 macro-F1 over Submission #2. |


# Gradescope withheld-data tests


| Date       | Target | Model                            | macro-F1   | accuracy   | Notes                                                                                                                                                                                                                                                                                                                                            |
| ---------- | ------ | -------------------------------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-05-05 | BP     | AdaBoost                         | 0.6204     | 0.6595     | Submission #1. Default hyperparameters. Within 1σ of local CV (0.637 ± 0.022).                                                                                                                                                                                                                                                                   |
| 2026-05-05 | CHOL   | DecisionTree                     | 0.2787     | 0.5297     | Submission #1. Default hyperparameters.                                                                                                                                                                                                                                                                                                          |
| 2026-05-09 | BP     | AdaBoost **live submission**     | **0.6654** | **0.6811** | Submission #2. Hyperparameters from RandomizedSearchCV: `learning_rate=0.236`, `n_estimators=239`. Within 1σ of local CV (0.647 ± 0.023). +0.045 macro-F1 over Submission #1.                                                                                                                                                                    |
| 2026-05-09 | CHOL   | RandomForest                     | 0.3388     | 0.4018     | Submission #2. Hyperparameters from RandomizedSearchCV with `class_weight="balanced"` fixed: `n_estimators=171`, `max_depth=33`, `max_features=None`, `min_samples_leaf=11`. About 0.06 below local CV (0.409 ± 0.024). +0.060 macro-F1 over Submission #1.                                                                                      |
| 2026-05-09 | BP     | AdaBoost                         | 0.6483     | 0.6685     | Submission #3. AdaBoost search expanded to include `DecisionTreeClassifier(max_depth=3)` as the base estimator (search picked it). Preprocessor changed to drop `INDFMMPC` and `INQ300` and remove column-transformer duplications. Worse than Submission #2 on both metrics, so we restored Submission #2 on Hugging Face as the live BP model. |
| 2026-05-09 | CHOL   | RandomForest **live submission** | **0.3392** | **0.4090** | Submission #3. `class_weight` added to the search distribution, picked `balanced_subsample`. Search also landed on `max_depth=13` (shallower than Submission #2). Preprocessor revised to drop `INDFMMPC` and `INQ300` and remove column-transformer duplications. Marginally better than Submission #2 (+0.0004 macro-F1, +0.0072 accuracy).    |


# Task 11

## a.

## b.

## c.

## d.

## e.

## f.

## g.

# Task 12

# Task 13

## a.

## b.

## c.

