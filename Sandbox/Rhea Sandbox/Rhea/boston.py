# Code source: Jaques Grobler
# License: BSD 3 clause


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
boston = datasets.load_boston()


# Use only one feature
boston_X = boston.data[:, np.newaxis, 2]

# Split the data into training/testing sets
boston_X_train=boston_X[:-20]
boston_X_test = boston_X[-20:]

# Split the targets into training/testing sets
boston_y_train = boston.target[:-20]
boston_y_test= boston.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(boston_X_train, boston_y_train)

# Make predictions using the testing set
boston_y_pred = regr.predict(boston_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(boston_y_test, boston_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(boston_y_test, boston_y_pred))

# Plot outputs
plt.scatter(boston_X_test, boston_y_test,  color='black')
plt.plot(boston_X_test, boston_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()