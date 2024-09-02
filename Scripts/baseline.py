import pandas
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_log_error

# Load the data
df = pandas.read_csv('Archive/train.csv')

# 

# Split the data into features(X) and target(y)
X = df.drop('SalePrice', axis=1)
y = df['SalePrice']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model on the training set
baseline_model = LinearRegression()
baseline_model.fit(X_train, y_train)

# Predict the target values on the test set
y_pred = baseline_model.predict(X_test)
y_true = y_test

# Evaluate the model on the test set
RMSE = root_mean_squared_log_error(y_true, y_pred)
print(f"RMSE between the logarithm of the predicted value and the logarithm of the observed sales price: {RMSE}")
