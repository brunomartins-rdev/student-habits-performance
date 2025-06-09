from src.data_loader import DataLoader

def main():
    # Load data
    student_data = DataLoader().load_raw_data('student-habits-performance.csv')
    print(student_data.head())

    # Clean data

    # Explore data
    
    # Model data

    pass


if __name__ == '__main__':
    main()
