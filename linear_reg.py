from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()

model.fit(X, y)

x = [[6]]

print("Prediction:", model.predict(x))