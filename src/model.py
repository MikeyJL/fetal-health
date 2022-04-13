"""Contains models to use for prediction and classification."""

from pandas import DataFrame
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from process import get_cols
from visualise import simple_plot


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

    simple_plot(
        x_values=range(1, len(rfecv.grid_scores_) + 1),
        y_values=rfecv.grid_scores_,
        title="Recursive feature elimination with cross-validation",
        x_label="Number of features selected",
        y_label="Cross validation score (accuracy)",
    )


def decision_tree_predict(
    X: list[list[float]], y: list[float], values: list[list[float]]
) -> None:
    """Uses a decision tree to classify an input.

    Args:
        X (list[list[float]]): Input data which is 2D.
        y (list[float]): Label data which is a vector.
        values (list[list[float]]): The values used to predict.
    """

    model = DecisionTreeClassifier()
    model.fit(X, y)
    prediction = model.predict(values)

    print(prediction)
