import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pickle
from sklearn.cluster import KMeans

def run():
    file_path = '/Users/Bowen/Downloads/Final_Project/Machine-learning/data/transformation-precipitation-LasVegas.csv'

    sns.set()
    data = pd.read_csv(file_path)

    x = data.iloc[:,3:5]

    n_cluster = 3

    kmeans = KMeans(n_cluster)
    kmeans.fit(x)

    with open('/Users/Bowen/Downloads/Final_Project/Machine-learning/output/kmeans_location.pkl', 'wb') as f:
        pickle.dump(kmeans, f)

if __name__ == '__main__':
    run()