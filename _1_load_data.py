# Importing the libraries
import pandas as pd 

# Load json files
def load_data():
    train_df = pd.read_json("Train.json")
    test_df = pd.read_json("Test.json")
    print("Hello world")
    test_target = pd.read_json("sample_submission.json")
    return(train_df, test_df, test_target)
