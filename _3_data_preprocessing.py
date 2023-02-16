from _2_data_analysis import data_analysis

def data_preprocessing():
    df = data_analysis()
    print("Removing duplicates.....")
    df.drop_duplicates(inplace=True)
    print(df.shape)
    return df
