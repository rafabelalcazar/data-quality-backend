import pandas as pd
import numpy as np

def get_dataset_info(df):
    instances = df.shape[0]
    features = df.shape[1]
    
    missing_values = df.isnull().sum()
    missing_values_percentage= missing_values.sum()/df.size
    
    duplicate_rows = df.duplicated().sum()
    duplicate_rows_percentage = (duplicate_rows / instances) * 100
    
    result = {
        "instances": instances,
        "features": features,
        "missing_values": missing_values.to_dict(),
        "missing_values_percentage": missing_values_percentage,
        "duplicate_rows": int(duplicate_rows) ,
        "duplicate_rows_percentage": duplicate_rows_percentage
    }
    
    return result

# Create a function that for each column in the DataFrame, calculates the following statistics: Mamimun, Minimum, 1st quartile, 3rd quartile, Mean, Median, Standard Deviation, skewness, kurtosis, candidate outliers, missing values. The function should be called get_column_stats and should be defined in the utils.py file.
def get_columns_stats(df):
    
    columns = df.columns
    stats = {}
    for column in columns:
        column_data = df[column]
        if column_data.dtype == 'object':
            stats[column] = process_categorical_attribute(column_data)
            continue
        elif column_data.dtype in [np.float64, np.int64]:
            stats[column] = process_numeric_aatribute(column_data)
        # print(column,df[column].dtype)
        # print('column data',column_data.max())
        # print('column data std',column_data.std())
        # else:
        #     continue
        # else:
            # stats[column] = get_categorical_stats(column_data)
        # Parse the stats dictionary to replace NaN values with None
        stats[column] = {key: value if not pd.isnull(value) else None for key, value in stats[column].items()}
    print(stats)            
    return stats

def process_numeric_aatribute(column_data):
    return {
        "max": float(column_data.max()),
        "min": float(column_data.min()),
        "q1": float(column_data.quantile(0.25)),
        "q3": float(column_data.quantile(0.75)),
        "mean": float(column_data.mean()),
        "median": float(column_data.median()),
        "std": float(column_data.std()),
        "skewness": float(column_data.skew()),
        "kurtosis": float(column_data.kurt()),
        "missing_values": float(column_data.isnull().sum())
    }
    
def process_categorical_attribute(column_data):
    return {
        "type": "categorical",
        # "labels": column_data.unique(),
        "missing_values": int(column_data.isnull().sum()),
        "unique_values": column_data.nunique(),
        "entropy": float(calculate_entropy(column_data)),
        # "mode": column_data.mode().values[0],
        "imbalance_ratio": float(calculate_imbalance_ratio(column_data))
        # "mode_frequency": column_data.mode().value_counts().values[0],
    }
    
    
    
def calculate_entropy(column)->float:
    """
    Calculate the entropy of a given column.
    Parameters:
    column (array-like): The column for which to calculate the entropy.
    Returns:
    float: The entropy value.
    """
    # Get the unique values and their counts
    frequencies = column.value_counts(normalize=True)
    
    # Calculate the entropy
    entropy = -np.sum(frequencies * np.log2(frequencies))
    return entropy

# Calculate imbalance ratio
def calculate_imbalance_ratio(column):
    """
    Calculate the imbalance ratio of a given column.
    Parameters:
    column (array-like): The column for which to calculate the imbalance ratio.
    Returns:
    float: The imbalance ratio value.
    """
    # Get the unique values and their counts
    # unique_values, value_counts = np.unique(column, return_counts=True)
    frequencies = column.value_counts(normalize=True)
    
    # Calculate the imbalance ratio
    imbalance_ratio = np.max(frequencies) / np.sum(frequencies)
    
    return imbalance_ratio
