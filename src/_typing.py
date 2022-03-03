"""Type aliases for the project."""

from typing import Union, Tuple
from numpy.typing import NDArray
from pandas._typing import DataFrame

GetColsValue = Union[Tuple[NDArray], DataFrame]
