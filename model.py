import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("Housing.csv")

print(df)

# df.fillna(df.mean(), inplace=True)

X = df[["area", "bedrooms", "bathrooms", "stories"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

model = LinearRegression()
model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))