import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def model_trainer(file:str, update:bool):
    df = pd.read_csv(file)
    filtered_df = df.dropna(axis=0)
    df = filtered_df.copy()
    del filtered_df
    features = ["Open"]
    y = df["Adj Close"]
    X = df[features]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size=0.8, test_size=0.2)

    if update:
        DT_model = DecisionTreeRegressor(max_leaf_nodes=434, random_state=0)
        RF_model = RandomForestRegressor(max_leaf_nodes=340, random_state=0)
        DT_model.fit(X_train, y_train)
        RF_model.fit(X_train, y_train)

        with open('IRFC_AdjClose_Decision_Tree.pkl', 'wb') as f:
            pickle.dump(DT_model, f)
        with open('IRFC_AdjClose_Random_Forest.pkl', 'wb') as f:
            pickle.dump(RF_model, f)
        y_val_DT = DT_model.predict(X_test)
        y_val_RF = RF_model.predict(X_test)
        global DT_score, RF_score
        DT_score = DT_model.score(X_test, y_test) * 100
        RF_score = RF_model.score(X_test, y_test) * 100
    else:
        pickle_in = open("DT_score.pkl", 'rb')
        DT_score = pickle.load(pickle_in)
        pickle_in =  open("RF_score.pkl", 'rb')
        RF_score = pickle.load(pickle_in)

    print("DT mean absolute error: ", mean_absolute_error(y_test, y_val_DT))
    print("DT score: ", DT_score)
    warning(DT_score)
    print("RF score: ", RF_score)
    warning(RF_score)
    print("RF mean absolute error: ", mean_absolute_error(y_test, y_val_RF))
    return [DT_score, RF_score]


def warning(score):
    if score < 99:
        print("**WARNING!**: Score is less than 99%. This may not be a very good match.")

if __name__ == "__main__":
    model_trainer("C:/Users/krish/Desktop/Kaggle_ML_training/Intro_to_ML/data/IRFC.NS.csv",True)