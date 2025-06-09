from src.data_cleaner import Preprocessor
from src.data_loader import DataLoader

def main():
    # Load data
    student_data = DataLoader().load_raw_data('student-habits-performance.csv')

    # Clean data
    prep = Preprocessor(student_data)
    print(prep.get_head())


    # Save clean data
    DataLoader().save_processed_data(prep.get_data())





    # Explore data
    
    # Model data

    pass


if __name__ == '__main__':
    main()
