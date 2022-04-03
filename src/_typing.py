"""Type aliases for the project."""

from numpy.typing import NDArray
from pandas._typing import DataFrame

GetColsValue = tuple[NDArray] | DataFrame
