import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

def elbow(max_cluster):
    sns.set()

    data = pd.read_csv('/Users/Bowen/Downloads/Final_Project/Machine-learning/data/transformation-precipitation-LasVegas.csv')

    print(data)

    x = data.iloc[:, 3:5]

    print(x)

    # within cluster sum of square
    wcss=[]
    number_clusters = range(1,max_cluster)

    for i in number_clusters:
        kmeans = KMeans(i)

        kmeans.fit(x)

        wcss_iter = kmeans.inertia_

        wcss.append(wcss_iter)

    print(wcss)

    plt.plot(number_clusters,wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')

    plt.savefig('/Users/Bowen/Downloads/Final_Project/Machine-learning/output/calculate_elbow.png')

if __name__ == '__main__':
    elbow(7)
