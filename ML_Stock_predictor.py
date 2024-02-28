import pickle
import pandas as pd
# from Ml import warning
try:
    from Data_Updater import update_checker, accuracy
except Exception as e:
    print(e)


update_checker()
print("DISCLAIMER!\n\n THIS PROGRAM CAN MAKE MISTAKES. USE IT AT YOUR OWN RISK! \n\n\n")

open_price = input("Enter today's open price: ")
print("Please wait while your AI does its thing...")
# scores = scores


pickle_in = open("IRFC_AdjClose_Decision_Tree.pkl", "rb")
DT_model = pickle.load(pickle_in)
pickle_in = open("IRFC_AdjClose_Random_Forest.pkl", "rb")
RF_model = pickle.load(pickle_in)

X_tom = pd.DataFrame({"Open": [float(open_price)]})
RF_y_tom = RF_model.predict(X_tom)
DT_y_tom = DT_model.predict(X_tom)

# DT_score = scores[0]
# RF_score = scores[1]
print(f"Random Forest: {RF_y_tom[0]}", f"Decision Tree: {DT_y_tom[0]}", sep = "\n")
# print("Accuracy of Decision Tree Model:", DT_score)
# warning(DT_score)
# print("Accuracy of Decision Tree Model:", RF_score)
# warning(RF_score)
print("Expect it to be around: " + str(((RF_y_tom+DT_y_tom)/2)[0]))