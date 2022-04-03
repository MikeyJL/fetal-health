"""Type aliases for the project."""

from numpy import float64
from numpy.typing import NDArray
from pandas._typing import DataFrame

GetColsValue = tuple[NDArray[float64]] | DataFrame
AxisValues = NDArray[float64]
