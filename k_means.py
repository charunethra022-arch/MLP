from sklearn.cluster import KMeans

X = [[1, 1], [1, 2], [2, 1],
     [8, 8], [9, 8], [8, 9]]

model = KMeans(n_clusters=2, random_state=1, n_init=10)

model.fit(X)

print("Cluster Labels:", model.labels_)
print("Centroids:", model.cluster_centers_)