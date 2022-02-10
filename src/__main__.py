"""Main runtime"""

from process import preview_raw, get_cols

preview_raw()

print(get_cols(["accelerations", "baseline value"]))
