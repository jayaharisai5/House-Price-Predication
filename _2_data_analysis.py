# Importing load data funtion from the python file
from _1_load_data import load_data
import pandas as pd

def data_analysis():
    train_df, test_df, test_target = load_data()
    # Adding target column to the test data set
    test_df['TARGET(PRICE_IN_LACS)'] = test_target
    # Merging 
    merge = [train_df, test_df]
    # Making a data set by merging test and train data set
    df = pd.concat(merge)
    # Shape of the datasets
    print("df: ", df.shape)
    # Checking for the null values
    check_null = df.isnull().sum().sum()

    if check_null == 0:
        print('There is no null values')
    else:
        print("There are null values")

    # Checking for the duplicates
    check_duplicates = df.duplicated().sum().sum()
    if check_duplicates == 0:
        print('There are no duplicates')
    else:
        print("Duplicates")

    # inpormation about teh data set
    print(df.info())
    # lISTING THE COLUMNS
    print(df.columns)

    return df

