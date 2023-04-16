import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
data = pd.read_csv("train.csv")
X = data.drop("VERDICT", axis=1).values
y = data["VERDICT"].values
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000)
mlp.fit(X_train_scaled, y_train)
accuracy = mlp.score(X_val_scaled, y_val)
print("Accuracy:", accuracy)
test_data = pd.read_csv("test.csv")
X_test = test_data.values
X_test_scaled = scaler.transform(X_test)
predictions = mlp.predict(X_test_scaled)
submission = pd.DataFrame(predictions, columns=["VERDICT"])
submission.to_csv("predictions.csv", index=False)