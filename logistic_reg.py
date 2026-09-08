from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = LogisticRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Predicted:", prediction)
print("Accuracy:", model.score(X_test, y_test))