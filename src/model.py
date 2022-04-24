"""Contains models to use for prediction and classification."""

from os import remove
from os.path import exists

import pandas as pd
import joblib
from pandas import DataFrame
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from tui import print_heading

from visualise import PlotParams, simple_plot


def eval_features() -> None:
    """Evaluates features of the dataset against fetal_health."""

    # Data
    df: DataFrame = pd.read_csv("data/raw/fetal_health.csv")
    X_train: DataFrame = df.drop(["fetal_health"], axis=1)
    y_train: DataFrame = df["fetal_health"]

    # Scaling
    scaler: StandardScaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)

    # Feature selection
    rfecv: RFECV = RFECV(
        estimator=LogisticRegression(max_iter=200),
        cv=StratifiedKFold(2),
        scoring="accuracy",
        min_features_to_select=1,
    )
    rfecv.fit(X_train_scaled, y_train)
    print(f"Optimal number of features: {rfecv.n_features_}")
    print(f"Selected features: {', '.join(X_train.columns[rfecv.support_])}")

    # Create a simple line plot
    data = PlotParams(
        x_values=range(1, len(rfecv.grid_scores_) + 1),
        y_values=rfecv.grid_scores_,
        title="Recursive feature elimination with cross-validation",
        x_label="Number of features selected",
        y_label="Cross validation score (accuracy)",
    )
    simple_plot(
        data=data,
        filename="feature-eval-plot.png",
    )


def mlp_classify() -> None:
    """Multilayer perceptron classifier."""

    # Data
    df: DataFrame = pd.read_csv("data/raw/fetal_health.csv")

    # Features chosen from the evaluation
    X_data: DataFrame = df[
        [
            "accelerations",
            "prolongued_decelerations",
            "abnormal_short_term_variability",
            "histogram_mean",
        ]
    ]
    y_data: DataFrame = df["fetal_health"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data)

    # Train model and score
    filepath = "models/mlp_classifier.joblib.pkl"
    last_score = None
    for i in range(1, 51):
        print_heading(f"Run {i}")
        model: MLPClassifier = MLPClassifier(max_iter=1000).fit(X_train, y_train)
        print(f"Score: {model.score(X_test, y_test)}")

        # Gets current saved model
        if last_score is None:
            last_score = joblib.load(filepath).score(X_test, y_test)
        else:
            last_score = model.score(X_test, y_test)

        # Replaces saved model if score is better
        if model.score(X_test, y_test) > last_score:
            if exists(filepath):
                remove(filepath)
            joblib.dump(model, filepath)

    print(f"Current model score: {joblib.load(filepath).score(X_test, y_test)}")
