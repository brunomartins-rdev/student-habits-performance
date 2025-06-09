from pathlib import Path
import pandas as pd
from .config import Config

class DataLoader:
    def __init__(self, 
                 raw_path: str = Config.RAW_PATH, 
                 processed_path: str = Config.PROCESSED_PATH, 
                 sep:str = ',') -> None:
        self.raw_path       = Path(raw_path)
        self.processed_path = Path(processed_path)
        self.sep            = sep
        self.df             = None

    def load_raw_data(self, filename: str) -> pd.DataFrame:
        return pd.read_csv(self.raw_path / filename, sep=self.sep)

    def load_processed_data(self, filename: str) -> pd.DataFrame:
        return pd.read_csv(self.processed_path / filename, sep=self.sep)

