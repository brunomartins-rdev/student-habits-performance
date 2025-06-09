import pandas as pd

class Preprocessor:
    def __init__(self, data_frame: pd.DataFrame) -> None:
        self.data_frame = data_frame.copy()

    def remove_columns(self, cols_to_drop: list) -> None:
        self.data_frame.drop(cols_to_drop, axis=1)

    def remove_na(self) -> None:
        self.data_frame.dropna()

    def get_data(self) -> pd.DataFrame:
        return self.data_frame

    def get_head(self) -> pd.DataFrame:
        return self.data_frame.head()
