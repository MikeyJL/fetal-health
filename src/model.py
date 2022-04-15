"""Contains models to use for prediction and classification."""

from pandas import DataFrame
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from process import get_cols
from visualise import PlotParams, simple_plot


def eval_features() -> None:
    """Evaluates features of the dataset against fetal_health."""

    # Data
    raw_df: DataFrame = get_cols(as_df=True)
    X_train: DataFrame = raw_df.drop(["fetal_health"], axis=1)
    y_train: DataFrame = raw_df["fetal_health"]

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
    print(f"Optional number of features: {rfecv.n_features_}")
    print(f"Selected features: {', '.join(X_train.columns[rfecv.support_])}")

    data = PlotParams(
        x_values=range(1, len(rfecv.grid_scores_) + 1),
        y_values=rfecv.grid_scores_,
        title="Recursive feature elimination with cross-validation",
        x_label="Number of features selected",
        y_label="Cross validation score (accuracy)",
    )
    simple_plot(
        data=data,
        filename="feature_eval_plot.png",
    )


def mlp_classify() -> None:
    """Multilayer perceptron classifier."""

    # Data
    raw_df: DataFrame = get_cols(as_df=True)

    # Features chosen from the evaluation
    X_data: DataFrame = raw_df[
        [
            "accelerations",
            "prolongued_decelerations",
            "abnormal_short_term_variability",
            "histogram_mean",
        ]
    ]
    y_data: DataFrame = raw_df["fetal_health"]

    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data)

    model: MLPClassifier = MLPClassifier(max_iter=1000).fit(X_train, y_train)
    print(f"Score: {model.score(X_test, y_test)}")
