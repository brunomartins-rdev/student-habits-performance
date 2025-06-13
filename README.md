# Student Habits Performance

The objective for this study is to compare several machine learning models to predict the `exam_score` variable on the `student-habits-performance` dataset available [here](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance).

## Instalation

To install and reproduce analysis:

```
pip3 install virtualenv
virtualenv .env
source .env/bin/activate
pip3 install -r requirements.txt
```

The entry point for the analysis is:

```
python3 main.py
```

## Contents
In the `notebooks/` directory are the notebooks used for initial exploration of the dataset including data wrangling, cleaning and EDA.

In the `src/` directory you will find the main pkg for this analysis with class definitions and config files.

The `main.py` file has all the steps done in Notebooks condensed, but commented out, without outputs, since this will produce a report in the end.
