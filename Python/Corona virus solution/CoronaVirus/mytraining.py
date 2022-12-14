import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle


def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    # np.random.permutation(7)          array([3, 1, 2, 6, 0, 4, 5])
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

if __name__ == '__main__':
    #read data
    df = pd.read_csv('data.csv')
    # print(df.head())    read first 5 
    # print(df.tail())      read last 5
    # print(df.info())      get details
    # print(df['diffBreath'].value_counts())   counts similar option
    # print(df.describe())
    train, test = data_split(df, 0.2)
    # print(train, test)

    x_train = train[['fever', 'bodyPain', 'age', 'runnyNose', 'diffBreath']].to_numpy()
    x_test = test[['fever', 'bodyPain', 'age', 'runnyNose', 'diffBreath']].to_numpy()

    y_train = train[['infectionProb']].to_numpy().reshape(2060,)
    y_test = test[['infectionProb']].to_numpy().reshape(515,)

    clf = LogisticRegression()
    clf.fit(x_train, y_train)

    # open a file, where you ant to store the data
    with open('model.pkl', 'wb') as file:

        # dump information to that file
        pickle.dump(clf, file)
    
   
