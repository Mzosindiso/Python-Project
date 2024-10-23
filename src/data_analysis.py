import pandas as pd
import numpy as np
from scipy import stats

def calculate_summary_statistics(df):
    return df.describe()

def perform_t_test(df, category_column, value_column, group1, group2):
    group1_data = df[df[category_column] == group1][value_column]
    group2_data = df[df[category_column] == group2][value_column]
    t_stat, p_value = stats.ttest_ind(group1_data, group2_data)
    return t_stat, p_value

def create_pivot_table(df, values, index, columns, aggfunc='mean'):
    return pd.pivot_table(df, values=values, index=index, columns=columns, aggfunc=aggfunc, fill_value=0)