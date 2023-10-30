import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Read the data from 'HouseNew.csv' file
data = pd.read_csv('HouseNew.csv')

# Select features and the target variable
X = data[['Elevator', 'Floor', 'Area', 'Parking', 'Room', 'Warehouse', 'YearOfConstruction']]
y = data['Price']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=32)

# Impute missing values with the mean of each column
imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Create a KNeighborsRegressor model with three neighbors
knn = KNeighborsRegressor(n_neighbors=3)

# Train the model with the training data
knn.fit(X_train, y_train)

# Make predictions with the test data
y_pred = knn.predict(X_test)

# Calculate the mean squared error to evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Plot the actual vs. predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs. Predicted Prices")
plt.show()
