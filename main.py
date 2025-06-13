from src.data_cleaner import Preprocessor
from src.data_loader import DataLoader
from src.data_visualizer import DataVisualizer

def main() -> None:
    # Load data ----------
    student_data = DataLoader().load_raw_data('student-habits-performance.csv')

    # Data cleaning ----------
    prep = Preprocessor(student_data)
    prep.remove_columns(['student_id'])
    prep.replace_nas_with_value('parental_education_level')
    prep.encode_categoricals()


    # Save clean data ----------
    DataLoader().save_processed_data(prep.get_data())


    # Model data ----------


    return None


if __name__ == '__main__':
    main()
