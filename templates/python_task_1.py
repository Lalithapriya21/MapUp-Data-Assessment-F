import pandas as pd
import numpy as np
from datetime import datetime as dt
from itertools import product
import warnings
warnings.filterwarnings('ignore')
path=r'C:\Users\lalitha\OneDrive\Documents\GitHub\MapUp-Data-Assessment-F\datasets'
file1=r'\dataset-1.csv'
file2=r'\dataset-2.csv'


#Q1 Car Generation matrix
def generate_car-matrix(dataset):
     df = pd.read_csv(dataset)
     #pivot the data frame to create a matrix
    car_matrix=df.pivot(index='id=1',columns='id_2',values='car').fillna(0)
    #set diagonal values to 0
    for col in car_matrix.columns.tolist():
        car_matrix.at[col,col]=0
    return car_matrix    

def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here

    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here

    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
