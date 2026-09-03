"""
evaluate_model.py
==================
Canonical training + evaluation script for the Konkan flood stacking ensemble.

Replaces (delete these after adopting this file):
    - retrain.py          (injected label noise + artificially underfit model to
                            produce a "believable" accuracy number — not a real metric)
    - calc_metrics.py      (references a label_encoder that train_advanced.py sets to
                            None; crashes immediately, evaluates the wrong pipeline)
    - update_and_test.py   (duplicate of train_advanced.py's model logic, different
                            hyperparameters, unclear which one produced the deployed
                            models_compiled.py coefficients)
    - binary_test.py       (another duplicate, yet another set of hyperparameters)

This script:
    1. Uses ONE fixed set of hyperparameters (the ones train_advanced.py used to
       produce the coefficients currently baked into models_compiled.py).
    2. Does a single stratified 80/20 train/test split with a fixed random_state,
       so results are reproducible run to run.
    3. Never touches or shuffles the labels. Confirmed_Event is ground truth,
       not something to be "adjusted" to make output look plausible.
    4. Prints an explicit caveat about the small positive-class sample size,
       so any recall/precision number is reported honestly rather than bare.

Usage:
    python evaluate_model.py

Requires: pandas, scikit-learn, xgboost, and a local floodsense.db with the
rainfall_daily table (Confirmed_Event column populated).
"""

import sqlite3
import sys

import pandas as pd
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    recall_score,
)
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

DB_PATH = "floodsense.db"
FEATURES = ["Rainfall_mm", "Rainfall_3day", "Rainfall_7day", "Month"]
TARGET = "Confirmed_Event"
RANDOM_STATE = 42  # fixed everywhere for reproducibility


def load_data(db_path: str) -> pd.DataFrame:
    conn = sqlite3.connect(db_path)
    try:
        df = pd.read_sql(f"SELECT * FROM rainfall_daily", conn)
    finally:
        conn.close()
    missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
    if missing:
        raise ValueError(f"rainfall_daily is missing expected columns: {missing}")
    return df


def build_model(scale_pos_weight: float) -> StackingClassifier:
    base_estimators = [
        (
            "rf",
            RandomForestClassifier(
                n_estimators=100,
                max_depth=3,
                class_weight="balanced",
                random_state=RANDOM_STATE,
            ),
        ),
        (
            "xgb",
            XGBClassifier(
                n_estimators=100,
                max_depth=3,
                scale_pos_weight=scale_pos_weight,
                random_state=RANDOM_STATE,
                eval_metric="logloss",
            ),
        ),
    ]
    meta_learner = LogisticRegression(class_weight="balanced", random_state=RANDOM_STATE)
    return StackingClassifier(
        estimators=base_estimators,
        final_estimator=meta_learner,
        cv=5,
        n_jobs=-1,
    )


def main():
    df = load_data(DB_PATH)
    X = df[FEATURES]
    y = df[TARGET]

    total_positives = int(y.sum())
    print(f"Total days in dataset: {len(y)}")
    print(f"Confirmed flood days: {total_positives}")

    if total_positives < 10:
        print(
            "\n*** CAVEAT ***\n"
            f"Only {total_positives} confirmed flood days exist in the entire dataset.\n"
            "A stratified 80/20 split will put roughly "
            f"{round(total_positives * 0.2)} positive examples in the test set.\n"
            "Any recall/precision/F1 number below is computed on that handful of\n"
            "examples and can swing significantly with a different random split.\n"
            "Treat these numbers as directional, not as a precise accuracy claim.\n"
        )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
    )
    print(f"\nTrain set: {len(y_train)} rows ({int(y_train.sum())} flood days)")
    print(f"Test set:  {len(y_test)} rows ({int(y_test.sum())} flood days)")

    num_neg = int((y_train == 0).sum())
    num_pos = max(int((y_train == 1).sum()), 1)
    scale_weight = num_neg / num_pos

    model = build_model(scale_weight)
    model.fit(X_train, y_train)

    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    print("\n--- Training Set Metrics ---")
    print(f"Accuracy: {accuracy_score(y_train, y_pred_train):.4f}")
    print(f"Recall on floods: {recall_score(y_train, y_pred_train):.4f}")

    print("\n--- Held-Out Test Set Metrics (unseen data) ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_test):.4f}")
    print(f"Recall on floods: {recall_score(y_test, y_pred_test):.4f}")
    print("\nConfusion matrix (test set):")
    print(confusion_matrix(y_test, y_pred_test))
    print("\nFull classification report (test set):")
    print(classification_report(y_test, y_pred_test, zero_division=0))

    print(
        "\nNOTE: this script evaluates model quality only. It does not modify,\n"
        "shuffle, or otherwise alter Confirmed_Event labels — those are ground\n"
        "truth. If a number looks unrealistically good or bad, that reflects\n"
        "the small dataset, not a bug to be papered over."
    )


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        print(f"Could not find {DB_PATH}. Run this script from the project folder.")
        sys.exit(1)
