# Attribution Statement

# Test set results

## BP (binary: normal / abnormal)

**Table 1:** Dated history of BP predictions on held-out 20% local test set (`bp_test_Rock_Doves`, 1141 rows). Best per metric **bolded**.


| Date | Model | macro-F1 | macro-recall | accuracy | Notes |
| ---- | ----- | -------- | ------------ | -------- | ----- |
| 2026-05-05 | AdaBoost | 0.6365 | 0.6394 | 0.6547 | Submission #1. Default hyperparameters. |
| 2026-05-09 | AdaBoost **live submission** | 0.6397 | 0.6412 | 0.6547 | Submission #2. Hyperparameters from RandomizedSearchCV: `learning_rate=0.236`, `n_estimators=239`. Default base estimator (decision stump). +0.003 macro-F1 over Submission #1 |
| 2026-05-09 | AdaBoost | 0.6307 | 0.6339 | 0.6494 | Submission #3. Adds `DecisionTreeClassifier(max_depth=3)` as the AdaBoost base estimator (search expanded). Preprocessor changed to drop `INDFMMPC` and `INQ300` and remove column-transformer duplications. Worse than Submission #2 on all 3 metrics |
| 2026-05-10 | AdaBoost (Extra Credit B) | **0.6452** | **0.6465** | **0.6599** | Submission #4. Augmented features (BMX_L body measurements, SMQ_L smoking, PAQ_L sedentary minutes, DIQ_L diabetes status). Re-tuned: `learning_rate=0.051`, `n_estimators=493`. Best on all 3 metrics by a small margin. CV difference vs Submission #2 not significant on any metric (p > 0.24); test-set lift consistent but small (+0.005). |


## CHOL (3-class: normal / borderline / high)

**Table 2:** Dated history of CHOL predictions on held-out 20% local test set (`chol_test_Rock_Doves`, 1141 rows). Best per metric **bolded**.


| Date | Model | macro-F1 | macro-recall | accuracy | Notes |
|----- | ----- | -------- | ------------ | -------- | ----- |
| 2026-05-05 | DecisionTree | 0.3443 | 0.3450 | 0.4216 | Submission #1. Default hyperparameters |
| 2026-05-09 | RandomForest | 0.3979 | 0.4072 | 0.4522 | Submission #2. Hyperparameters from RandomizedSearchCV with `class_weight="balanced"` fixed: `n_estimators=171`, `max_depth=33`, `max_features=None`, `min_samples_leaf=11` |
| 2026-05-09 | RandomForest **live submission** | 0.4044 | 0.4168 | 0.4549 | Submission #3. `class_weight` added to the search distribution, picked `balanced_subsample`. Search also landed on `max_depth=13` (shallower than Submission #2). Preprocessor changed to drop `INDFMMPC` and `INQ300` and remove column-transformer duplications. +0.007 macro-F1 over Submission #2 |
| 2026-05-10 | RandomForest (Extra Credit B) | **0.4267** | **0.4424** | **0.4926** | Submission #4. Augmented features (BMX_L body measurements, SMQ_L smoking, PAQ_L sedentary minutes, DIQ_L diabetes status). Re-tuned: `class_weight="balanced"`, `n_estimators=287`, `max_depth=13`, `max_features="sqrt"`, `min_samples_leaf=10`. Best on all 3 metrics. CV paired t-test vs Submission #3 RF: macro-F1 +0.020 (p=0.13), recall +0.026 (p=0.07), accuracy +0.029 (p=0.037, significant). Test set: +0.009 macro-F1, +0.026 accuracy. |


# Gradescope withheld-data tests

**Table 3:** Dated history of Rock Doves submissions to the Gradescope autograder with both targets included. Best per metric **bolded**.


| Date | Target | Model | macro-F1 | accuracy | Notes |
| ---- | ----- | ----- | ----- | ----- | ----- |
| 2026-05-05 | BP | AdaBoost | 0.6204 | 0.6595 | Submission #1. Default hyperparameters. Within 1σ of local CV (0.637 ± 0.022). |
| 2026-05-05 | CHOL | DecisionTree | 0.2787 | 0.5297 | Submission #1. Default hyperparameters. |
| 2026-05-09 | BP | AdaBoost | 0.6654 | 0.6811 | Submission #2. Hyperparameters from RandomizedSearchCV: `learning_rate=0.236`, `n_estimators=239`. Within 1σ of local CV (0.647 ± 0.023). +0.045 macro-F1 over Submission #1. |
| 2026-05-09 | CHOL | RandomForest | 0.3388 | 0.4018 | Submission #2. Hyperparameters from RandomizedSearchCV with `class_weight="balanced"` fixed: `n_estimators=171`, `max_depth=33`, `max_features=None`, `min_samples_leaf=11`. About 0.06 below local CV (0.409 ± 0.024). +0.060 macro-F1 over Submission #1. |
| 2026-05-09 | BP | AdaBoost | 0.6483 | 0.6685 | Submission #3. AdaBoost search expanded to include `DecisionTreeClassifier(max_depth=3)` as the base estimator (search picked it). Preprocessor changed to drop `INDFMMPC` and `INQ300` and remove column-transformer duplications. Worse than Submission #2 on both metrics, so we restored Submission #2 on Hugging Face as the live BP model. |
| 2026-05-09 | CHOL | RandomForest | 0.3392 | 0.4090 | Submission #3. `class_weight` added to the search distribution, picked `balanced_subsample`. Search also landed on `max_depth=13` (shallower than Submission #2). Preprocessor changed to drop `INDFMMPC` and `INQ300` and remove column-transformer duplications. Marginally better than Submission #2 (+0.0004 macro-F1, +0.0072 accuracy). |
| 2026-05-10 | BP | AdaBoost (Extra Credit B) **live submission** | **0.6730** | **0.6883** | Submission #4. Augmented features (BMX_L body measurements, SMQ_L smoking, PAQ_L sedentary minutes, DIQ_L diabetes status) joined by SEQN at predict time. Re-tuned: `learning_rate=0.051`, `n_estimators=493`. +0.0076 macro-F1 / +0.0072 accuracy over Submission #2. New features did add signal. Also fixed ALQ121 duplication in preprocessor. |
| 2026-05-10 | CHOL | RandomForest (Extra Credit B) **live submission** | **0.3593** | **0.4631** | Submission #4. Same augmented features. Re-tuned: `class_weight="balanced"`, `n_estimators=287`, `max_depth=13`, `max_features="sqrt"`, `min_samples_leaf=10`. +0.0201 macro-F1 / +0.0541 accuracy over Submission #3. Also fixed ALQ121 duplication in preprocessor. |


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

# Extra Credit B

## Features added

11 new features were merged in from the NHANES Aug 2021–Aug 2023 public release files (file suffix `_L`), joined by SEQN. All 5703 rows in `nhanes.csv` matched 100% to the new files and no instances were dropped on merge.

**Table 4:** NHANES public-release files used for Submission #4, the variables kept from each, and the clinical rationale.


| File | NHANES category | Features kept | Why |
| ---- | ----- | ----- | ----- |
| `BMX_L.xpt` | Examination — Body Measures | `BMXWT`, `BMXHT`, `BMXBMI`, `BMXWAIST`, `BMXARMC` | Body measurements (weight, height, BMI, waist, arm) correlate with high cholesterol and blood pressure |
| `SMQ_L.xpt` | Questionnaire — Smoking | `SMQ020`, `SMQ040` | Smoking is a large risk factor for cardiovascular disease |
| `PAQ_L.xpt` | Questionnaire — Physical Activity | `PAD680` (sedentary minutes/day) | Sedentary lifestyle can lead to worse cholesterol levels |
| `DIQ_L.xpt` | Questionnaire — Diabetes | `DIQ010`, `DIQ160`, `DIQ180` | Diabetes and prediabetes are correlated with abnormal cholesterol levels |


Lab values, glucose, triglycerides, and prescription medications were deliberately excluded as borderline-leaky predictors of LBXTC.

## Test set results (augmented vs. baseline, 1141 rows not used for tuning)

### CHOL

**Table 5:** Local test-set comparison of Submission #3 vs #4 CHOL model, both with the same 1141-row test split. Best per metric **bolded**.


| Model                                  | macro-F1   | macro-recall | accuracy   |
| -------------------------------------- | ---------- | ------------ | ---------- |
| Submission #3 RF, original 30 features | 0.4177     | 0.4328       | 0.4663     |
| Augmented features + re-tuned RF       | **0.4267** | **0.4424**   | **0.4926** |
| $\delta$                               | +0.009     | +0.010       | +0.026     |


Augmented model: `class_weight="balanced", n_estimators=287, max_depth=13, max_features="sqrt", min_samples_leaf=10`.

### BP

**Table 6:** Local test-set comparison of the live Submission #2 vs #4 BP model. Best per metric **bolded**.


| Model                                        | macro-F1   | macro-recall | accuracy   |
| -------------------------------------------- | ---------- | ------------ | ---------- |
| Submission #2 AdaBoost, original 30 features | 0.6397     | 0.6412       | 0.6547     |
| Augmented features + re-tuned AdaBoost       | **0.6452** | **0.6465**   | **0.6599** |
| $\delta$                                     | +0.005     | +0.005       | +0.005     |


Augmented model: `learning_rate=0.051, n_estimators=493`. No statistically significant CV difference on any metric (p > 0.24 across all three).

## Cross-validation comparison (10-fold, 4562-row training split)

**Table 7:** Paired t-test results for Submission #3 vs #4 on CHOL, computed on per-fold CV scores from the same 10 deterministic stratified folds. p-values at α=0.05.


| Metric       | $\delta$ (augmented − Submission #3) | p-value   | Verdict                   |
| ------------ | ------------------------------------ | --------- | ------------------------- |
| macro-F1     | +0.020                               | 0.13      | not significant           |
| macro-recall | +0.026                               | 0.07      | borderline                |
| accuracy     | +0.029                               | **0.037** | **significant at α=0.05** |


## Interpretation

