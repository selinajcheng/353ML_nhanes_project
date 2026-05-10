# Attribution Statement

# Test set results (per Step 4 page-2 requirement)

> Predictions on `bp_test_Rock_Doves` and `chol_test_Rock_Doves` (the 20% held-out local splits, 1141 rows each). Best per metric **bolded**.

## BP (binary: normal / abnormal)

| Date | Model | macro-F1 | macro-recall | accuracy | Notes |
| ---- | ----- | -------- | ------------ | -------- | ----- |
| 2026-05-05 | AdaBoost (baseline, defaults) | 0.6365 | 0.6394 | **0.6547** | First submission baseline. Defaults with no tuning. |
| 2026-05-09 | AdaBoost (tuned) **final pick** | **0.6397** | **0.6412** | **0.6547** | RandomizedSearchCV picks lr=0.236, n_est=239. Tuning gave +0.003 macro-F1, +0.002 recall over baseline. Accuracy tied. |

## CHOL (3-class: normal / borderline / high)

| Date | Model | macro-F1 | macro-recall | accuracy | Notes |
| ---- | ----- | -------- | ------------ | -------- | ----- |
| 2026-05-05 | DecisionTree (baseline, defaults) | 0.3443 | 0.3450 | 0.4216 | First submission baseline. Defaults with no tuning. |
| 2026-05-09 | RandomForest (tuned) **final pick** | **0.3979** | **0.4072** | **0.4522** | RandomizedSearchCV with class_weight=balanced. max_depth=33, max_features=None, min_leaf=11, n_est=171. +0.054 macro-F1 over baseline. |


# Gradescope withheld-data tests

| Date | Target | Model | macro-F1 | accuracy | Notes |
| ---- | ------ | ----- | -------- | -------- | ----- |
| 2026-05-05 | BP | AdaBoost (baseline) | 0.6204 | 0.6595 | First submission baseline. Within 1σ of local CV (0.637 ± 0.022). |
| 2026-05-05 | CHOL | DecisionTree (baseline) | 0.2787 | 0.5297 | First submission baseline. |
| 2026-05-09 | BP | AdaBoost (tuned) | **0.6654** | **0.6811** | Post bug fixes plus RandomizedSearchCV. Within 1σ of local CV (0.647 ± 0.023). +0.045 over prior BP baseline. |
| 2026-05-09 | CHOL | RandomForest (tuned) | **0.3388** | 0.4018 | Post bug fixes plus RandomizedSearchCV with class_weight=balanced. About 0.06 below local CV (0.409 ± 0.024) and local test (0.398). +0.060 over prior CHOL baseline. |


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
