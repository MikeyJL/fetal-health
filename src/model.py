"""Contains models to use for prediction and classification."""

import pandas as pd
import joblib
from pandas import DataFrame
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

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
        estimator=SVC(kernel="linear"),
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


def svm_train() -> None:
    """Trains a support vector classifier."""

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
    X_train, X_test, y_train, y_test = train_test_split(X_data.values, y_data.values)

    # Scales the data
    scaler: StandardScaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train model and score
    filepath = "models/svm_classifier.joblib.pkl"
    model: SVC = SVC(kernel="linear").fit(X_train_scaled, y_train)

    # Saves model
    joblib.dump(model, filepath)

    print(f"Model score: {model.score(X_test_scaled, y_test)}")
