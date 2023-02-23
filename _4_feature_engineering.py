from _3_data_preprocessing import data_preprocessing
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

def feature_engineering():
    df = data_preprocessing()
    df['POSTED_BY'] = label_encoder.fit_transform(df['POSTED_BY'])
    df['BHK_OR_RK'] = label_encoder.fit_transform(df['BHK_OR_RK'])

    df = df.drop(columns = ["READY_TO_MOVE", "ADDRESS"], axis=1)
    
    df.to_csv('cleaned.csv')

    print(df.shape)
    return df
