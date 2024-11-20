# Data Analysis Project

## Overview

This project is designed to perform various data analysis tasks using Python. It includes functions for calculating summary statistics, performing t-tests, and creating pivot tables.

## Project Structure
```
Python-Project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── results/
│   └── figures/
│
├── src/
│   ├── data_analysis.py
│   ├── data_cleaning.py
│   └── visualization.py
│
├── venv/
│
└── README.md
```

## Installation

1. Clone this repository

2. Navigate to the project directory

3. Create and activate a virtual environment

4. Install the required packages: `pip install -r requirements.txt`

## Usage

The main analysis functions are located in `src/data_analysis.py`. Here's a brief overview of the available functions:

1. `calculate_summary_statistics(df)`: Calculates summary statistics for a given DataFrame.
2. `perform_t_test(df, category_column, value_column, group1, group2)`: Performs a t-test between two groups in the data.
3. `create_pivot_table(df, values, index, columns, aggfunc='mean')`: Creates a pivot table from the given DataFrame.

To use these functions, import them from the `data_analysis` module:

```python
from src.data_analysis import calculate_summary_statistics, perform_t_test, create_pivot_table

Data
Raw data should be placed in the data/raw/ directory.
Processed data will be stored in the data/processed/ directory.


Results
Analysis results and generated figures will be saved in the results/ directory.
