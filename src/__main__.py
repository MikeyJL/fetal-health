"""Main runtime."""

from process import preview_raw, get_cols

if __name__ == "__main__":
    preview_raw()

    df = get_cols(["histogram_mean", "baseline value"], as_df=True)
    print(df)
