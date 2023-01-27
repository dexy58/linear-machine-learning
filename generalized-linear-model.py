import pandas as pd
from sklearn.linear_model import PoissonRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load the data
corn_yield = pd.read_csv("data/maize-yields.csv")
temperature_data = pd.read_csv("data/hours weather data.csv", parse_dates=['time'])
temperature_data['time'] = pd.to_datetime(temperature_data['time'])
temperature_data = temperature_data[temperature_data['time'].dt.year != 2021]

corn_yield_croatia = corn_yield[corn_yield["Entity"] == "Croatia"]
corn_yield_croatia = corn_yield_croatia.iloc[:, [2, 3]].values

print(corn_yield_croatia)

# Group temperature by year and sum the values
temperature_data['year'] = temperature_data['time'].dt.year

temperature_sum = temperature_data.groupby(['year'])['temperature_2m (°C)'].sum()

#print(temperature_sum['temperature_2m (°C)'])
print(temperature_sum.size)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(temperature_sum, corn_yield_croatia, test_size=0.25, random_state=42)

# Fit the GLM model
glm_model = PoissonRegressor()
glm_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = glm_model.predict(X_test)

# Calculate the absolute error
mae = mean_absolute_error(y_test, y_pred)
print(mae)