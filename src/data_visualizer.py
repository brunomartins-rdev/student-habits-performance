import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

from src.config import Config

class DataVisualizer:
    def __init__(self, 
                 data_frame: pd.DataFrame, 
                 save_dir: str = Config.OUTPUT_PATH) -> None:
        self.data_frame = data_frame
        self.save_dir = Path(save_dir)

    def histogram_boxplot(self, variable: str, name: str) -> None:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        sns.histplot(self.data_frame[variable], kde=True, ax=axes[0])
        axes[0].set_title(f'Histogram of {variable}')
        sns.boxplot(x=self.data_frame[variable], ax=axes[1])
        axes[1].set_title(f'Boxplot of {variable}')
        plt.tight_layout()
        plt.savefig(Path(self.save_dir / name))
        plt.close()
