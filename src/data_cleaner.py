import pandas as pd
from typing import List

class Preprocessor:
    def __init__(self, data_frame: pd.DataFrame) -> None:
        self.data_frame = data_frame.copy()
        self.category_maps = {
            'gender': {'Female': 0, 'Male': 1, 'Other': 2},
            'diet_quality': {'Poor': 0, 'Fair': 1, 'Good': 2},
            'part_time_job': {'No': 0, 'Yes': 1},
            'parental_education_level': {'Unknown': -1, 'High School': 0, 'Bachelor': 1, 'Master': 2},
            'internet_quality': {'Poor': 0, 'Average': 1, 'Good': 2},
            'extracurricular_participation': {'No': 0, 'Yes': 1}
        }

    def remove_columns(self, cols_to_drop: list) -> None:
        self.data_frame.drop(cols_to_drop, axis=1, inplace=True)

    def remove_na(self) -> None:
        self.data_frame.dropna(inplace=True)

    def see_uniques(self, variables_to_see: List) -> List:
        uniques_list = [{var: self.data_frame[var].unique()} for var in variables_to_see]
        for uniques in uniques_list:
            print(uniques)
        return uniques_list

    def replace_nas_with_value(self, variable_to_replace: str, value: str = 'Unknown') -> None:
        self.data_frame[variable_to_replace] = self.data_frame[variable_to_replace].fillna(value)

    def encode_categoricals(self) -> None:
        for column, mapping in self.category_maps.items():
                self.data_frame[column] = self.data_frame[column].map(mapping)

    def get_data(self) -> pd.DataFrame:
        return self.data_frame

    def get_head(self) -> pd.DataFrame:
        return self.data_frame.head()
