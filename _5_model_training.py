from _4_feature_engineering import feature_engineering

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

def model_training():
    df = feature_engineering()

    X = df.drop('TARGET(PRICE_IN_LACS)', axis = 1)
    y = df['TARGET(PRICE_IN_LACS)']

    # Spliting the data to train ans test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.33, random_state=42)
    print(X_train.shape)
    print(X_test.shape)
    # Model training

    forest_regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
    tree_regressor = DecisionTreeRegressor(random_state = 0)

    models  = [forest_regressor, tree_regressor]
    for model in models:
        model.fit(X_train, y_train)
        scores = model.score(X_test, y_test)
        print(f"{model}, {scores}")


model_training()