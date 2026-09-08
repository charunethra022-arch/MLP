from sklearn.neural_network import MLPClassifier

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

model = MLPClassifier(
    hidden_layer_sizes=(4,),
    max_iter=2000,
    random_state=1
)

model.fit(X, y)

print("Prediction:", model.predict([[1, 0]]))