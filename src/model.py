"""Contains models to use for prediction and classification."""

from sklearn.tree import DecisionTreeClassifier


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
