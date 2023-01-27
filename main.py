# Step 1: Import the necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Step 2: Load the corn yield data
corn_yield_data = pd.read_csv('data/maize-yields.csv')
co2_data = pd.read_csv('data/co2 - per capita.csv')
methane_data = pd.read_csv('data/methane - per capita.csv')
nitrous_oxide_data = pd.read_csv('data/nitrous oxide per capita.csv')
# Step 3: Load the weather data
weather_data = pd.read_csv('data/hours weather data.csv')

# Step 4: Filter corn yield data for Croatia only
croatia_data = corn_yield_data[corn_yield_data['Entity'] == 'Croatia']
co2_croatia_data = co2_data[co2_data['Entity'] == 'Croatia']
methane_croatia_data = methane_data[methane_data['Entity'] == 'Croatia']
nitrous_oxide_croatia_data = nitrous_oxide_data[nitrous_oxide_data['Entity'] == 'Croatia']

# Step 5: Filter weather data by year and date
#weather_data['time'] = pd.to_datetime(weather_data['time'])
###weather_data = weather_data[weather_data['time'].dt.year != 2021]
nitrous_oxide_croatia_data = nitrous_oxide_croatia_data[
    (nitrous_oxide_croatia_data['Year'] == 1992)
    | (nitrous_oxide_croatia_data['Year'] == 1993)
    | (nitrous_oxide_croatia_data['Year'] == 1994)
    | (nitrous_oxide_croatia_data['Year'] == 1995)
    | (nitrous_oxide_croatia_data['Year'] == 1996)
    | (nitrous_oxide_croatia_data['Year'] == 1997)
    | (nitrous_oxide_croatia_data['Year'] == 1998)
    | (nitrous_oxide_croatia_data['Year'] == 1999)
    | (nitrous_oxide_croatia_data['Year'] == 2000)
    | (nitrous_oxide_croatia_data['Year'] == 2001)
    | (nitrous_oxide_croatia_data['Year'] == 2002)
    | (nitrous_oxide_croatia_data['Year'] == 2003)
    | (nitrous_oxide_croatia_data['Year'] == 2004)
    | (nitrous_oxide_croatia_data['Year'] == 2005)
    | (nitrous_oxide_croatia_data['Year'] == 2006)
    | (nitrous_oxide_croatia_data['Year'] == 2007)
    | (nitrous_oxide_croatia_data['Year'] == 2008)
    | (nitrous_oxide_croatia_data['Year'] == 2009)
    | (nitrous_oxide_croatia_data['Year'] == 2010)
    | (nitrous_oxide_croatia_data['Year'] == 2011)
    | (nitrous_oxide_croatia_data['Year'] == 2012)
    | (nitrous_oxide_croatia_data['Year'] == 2013)
    | (nitrous_oxide_croatia_data['Year'] == 2014)
    | (nitrous_oxide_croatia_data['Year'] == 2015)
    | (nitrous_oxide_croatia_data['Year'] == 2016)
    | (nitrous_oxide_croatia_data['Year'] == 2017)
    | (nitrous_oxide_croatia_data['Year'] == 2018)
    | (nitrous_oxide_croatia_data['Year'] == 2019)
    | (nitrous_oxide_croatia_data['Year'] == 2020)]
methane_croatia_data = methane_croatia_data[
    (methane_croatia_data['Year'] == 1992)
    | (methane_croatia_data['Year'] == 1993)
    | (methane_croatia_data['Year'] == 1994)
    | (methane_croatia_data['Year'] == 1995)
    | (methane_croatia_data['Year'] == 1996)
    | (methane_croatia_data['Year'] == 1997)
    | (methane_croatia_data['Year'] == 1998)
    | (methane_croatia_data['Year'] == 1999)
    | (methane_croatia_data['Year'] == 2000)
    | (methane_croatia_data['Year'] == 2001)
    | (methane_croatia_data['Year'] == 2002)
    | (methane_croatia_data['Year'] == 2003)
    | (methane_croatia_data['Year'] == 2004)
    | (methane_croatia_data['Year'] == 2005)
    | (methane_croatia_data['Year'] == 2006)
    | (methane_croatia_data['Year'] == 2007)
    | (methane_croatia_data['Year'] == 2008)
    | (methane_croatia_data['Year'] == 2009)
    | (methane_croatia_data['Year'] == 2010)
    | (methane_croatia_data['Year'] == 2011)
    | (methane_croatia_data['Year'] == 2012)
    | (methane_croatia_data['Year'] == 2013)
    | (methane_croatia_data['Year'] == 2014)
    | (methane_croatia_data['Year'] == 2015)
    | (methane_croatia_data['Year'] == 2016)
    | (methane_croatia_data['Year'] == 2017)
    | (methane_croatia_data['Year'] == 2018)
    | (methane_croatia_data['Year'] == 2019)
    | (methane_croatia_data['Year'] == 2020)]
co2_croatia_data = co2_croatia_data[
    (co2_croatia_data['Year'] == 1992)
    | (co2_croatia_data['Year'] == 1993)
    | (co2_croatia_data['Year'] == 1994)
    | (co2_croatia_data['Year'] == 1995)
    | (co2_croatia_data['Year'] == 1996)
    | (co2_croatia_data['Year'] == 1997)
    | (co2_croatia_data['Year'] == 1998)
    | (co2_croatia_data['Year'] == 1999)
    | (co2_croatia_data['Year'] == 2000)
    | (co2_croatia_data['Year'] == 2001)
    | (co2_croatia_data['Year'] == 2002)
    | (co2_croatia_data['Year'] == 2003)
    | (co2_croatia_data['Year'] == 2004)
    | (co2_croatia_data['Year'] == 2005)
    | (co2_croatia_data['Year'] == 2006)
    | (co2_croatia_data['Year'] == 2007)
    | (co2_croatia_data['Year'] == 2008)
    | (co2_croatia_data['Year'] == 2009)
    | (co2_croatia_data['Year'] == 2010)
    | (co2_croatia_data['Year'] == 2011)
    | (co2_croatia_data['Year'] == 2012)
    | (co2_croatia_data['Year'] == 2013)
    | (co2_croatia_data['Year'] == 2014)
    | (co2_croatia_data['Year'] == 2015)
    | (co2_croatia_data['Year'] == 2016)
    | (co2_croatia_data['Year'] == 2017)
    | (co2_croatia_data['Year'] == 2018)
    | (co2_croatia_data['Year'] == 2019)
    | (co2_croatia_data['Year'] == 2020)]
weather_data = weather_data[(weather_data['time'].str.contains('2021')) == False]
weather_data = weather_data[(weather_data['time'].str.contains('-04-10'))
    | (weather_data['time'].str.contains('-04-11'))
    | (weather_data['time'].str.contains('-04-12'))
    | (weather_data['time'].str.contains('-04-13'))
    | (weather_data['time'].str.contains('-04-14'))
    | (weather_data['time'].str.contains('-04-15'))
    | (weather_data['time'].str.contains('-04-16'))
    | (weather_data['time'].str.contains('-04-17'))
    | (weather_data['time'].str.contains('-04-18'))
    | (weather_data['time'].str.contains('-04-19'))
    | (weather_data['time'].str.contains('-04-20'))
    | (weather_data['time'].str.contains('-04-21'))
    | (weather_data['time'].str.contains('-04-22'))
    | (weather_data['time'].str.contains('-04-23'))
    | (weather_data['time'].str.contains('-04-24'))
    | (weather_data['time'].str.contains('-04-25'))
    | (weather_data['time'].str.contains('-04-26'))
    | (weather_data['time'].str.contains('-04-27'))
    | (weather_data['time'].str.contains('-04-28'))
    | (weather_data['time'].str.contains('-04-29'))
    | (weather_data['time'].str.contains('-04-30'))
    | (weather_data['time'].str.contains('-05-01'))
    | (weather_data['time'].str.contains('-05-02'))
    | (weather_data['time'].str.contains('-05-03'))
    | (weather_data['time'].str.contains('-05-04'))
    | (weather_data['time'].str.contains('-05-05'))
    | (weather_data['time'].str.contains('-05-06'))
    | (weather_data['time'].str.contains('-05-07'))
    | (weather_data['time'].str.contains('-05-08'))
    | (weather_data['time'].str.contains('-05-09'))
    | (weather_data['time'].str.contains('-05-10'))
    | (weather_data['time'].str.contains('-05-11'))
    | (weather_data['time'].str.contains('-05-12'))
    | (weather_data['time'].str.contains('-05-13'))
    | (weather_data['time'].str.contains('-05-14'))
    | (weather_data['time'].str.contains('-05-15'))
    | (weather_data['time'].str.contains('-05-16'))
    | (weather_data['time'].str.contains('-05-17'))
    | (weather_data['time'].str.contains('-05-18'))
    | (weather_data['time'].str.contains('-05-19'))
    | (weather_data['time'].str.contains('-05-20'))
    | (weather_data['time'].str.contains('-05-21'))
    | (weather_data['time'].str.contains('-05-22'))
    | (weather_data['time'].str.contains('-05-23'))
    | (weather_data['time'].str.contains('-05-24'))
    | (weather_data['time'].str.contains('-05-25'))
    | (weather_data['time'].str.contains('-05-26'))
    | (weather_data['time'].str.contains('-05-27'))
    | (weather_data['time'].str.contains('-05-28'))
    | (weather_data['time'].str.contains('-05-29'))
    | (weather_data['time'].str.contains('-05-30'))
    | (weather_data['time'].str.contains('-05-31'))
    | (weather_data['time'].str.contains('-06-01'))
    | (weather_data['time'].str.contains('-06-02'))
    | (weather_data['time'].str.contains('-06-03'))
    | (weather_data['time'].str.contains('-06-04'))
    | (weather_data['time'].str.contains('-06-05'))
    | (weather_data['time'].str.contains('-06-06'))
    | (weather_data['time'].str.contains('-06-07'))
    | (weather_data['time'].str.contains('-06-08'))
    | (weather_data['time'].str.contains('-06-09'))
    | (weather_data['time'].str.contains('-06-10'))
    | (weather_data['time'].str.contains('-06-11'))
    | (weather_data['time'].str.contains('-06-12'))
    | (weather_data['time'].str.contains('-06-13'))
    | (weather_data['time'].str.contains('-06-14'))
    | (weather_data['time'].str.contains('-06-15'))
    | (weather_data['time'].str.contains('-06-16'))
    | (weather_data['time'].str.contains('-06-17'))
    | (weather_data['time'].str.contains('-06-18'))
    | (weather_data['time'].str.contains('-06-19'))
    | (weather_data['time'].str.contains('-06-20'))
    | (weather_data['time'].str.contains('-06-21'))
    | (weather_data['time'].str.contains('-06-22'))
    | (weather_data['time'].str.contains('-06-23'))
    | (weather_data['time'].str.contains('-06-24'))
    | (weather_data['time'].str.contains('-06-25'))
    | (weather_data['time'].str.contains('-06-26'))
    | (weather_data['time'].str.contains('-06-27'))
    | (weather_data['time'].str.contains('-06-28'))
    | (weather_data['time'].str.contains('-06-29'))
    | (weather_data['time'].str.contains('-06-30'))
    | (weather_data['time'].str.contains('-07-01'))
    | (weather_data['time'].str.contains('-07-02'))
    | (weather_data['time'].str.contains('-07-03'))
    | (weather_data['time'].str.contains('-07-04'))
    | (weather_data['time'].str.contains('-07-05'))
    | (weather_data['time'].str.contains('-07-06'))
    | (weather_data['time'].str.contains('-07-07'))
    | (weather_data['time'].str.contains('-07-08'))
    | (weather_data['time'].str.contains('-07-09'))
    | (weather_data['time'].str.contains('-07-10'))
    | (weather_data['time'].str.contains('-07-11'))
    | (weather_data['time'].str.contains('-07-12'))
    | (weather_data['time'].str.contains('-07-13'))
    | (weather_data['time'].str.contains('-07-14'))
    | (weather_data['time'].str.contains('-07-15'))
    | (weather_data['time'].str.contains('-07-16'))
    | (weather_data['time'].str.contains('-07-17'))
    | (weather_data['time'].str.contains('-07-18'))
    | (weather_data['time'].str.contains('-07-19'))
    | (weather_data['time'].str.contains('-07-20'))
    | (weather_data['time'].str.contains('-07-21'))
    | (weather_data['time'].str.contains('-07-22'))
    | (weather_data['time'].str.contains('-07-23'))
    | (weather_data['time'].str.contains('-07-24'))
    | (weather_data['time'].str.contains('-07-25'))
    | (weather_data['time'].str.contains('-07-26'))
    | (weather_data['time'].str.contains('-07-27'))
    | (weather_data['time'].str.contains('-07-28'))
    | (weather_data['time'].str.contains('-07-29'))
    | (weather_data['time'].str.contains('-07-30'))
    | (weather_data['time'].str.contains('-07-31'))
    | (weather_data['time'].str.contains('-08-01'))
    | (weather_data['time'].str.contains('-08-02'))
    | (weather_data['time'].str.contains('-08-03'))
    | (weather_data['time'].str.contains('-08-04'))
    | (weather_data['time'].str.contains('-08-05'))
    | (weather_data['time'].str.contains('-08-06'))
    | (weather_data['time'].str.contains('-08-07'))
    | (weather_data['time'].str.contains('-08-08'))
    | (weather_data['time'].str.contains('-08-09'))
    | (weather_data['time'].str.contains('-08-10'))
    | (weather_data['time'].str.contains('-08-11'))
    | (weather_data['time'].str.contains('-08-12'))
    | (weather_data['time'].str.contains('-08-13'))
    | (weather_data['time'].str.contains('-08-14'))
    | (weather_data['time'].str.contains('-08-15'))
    | (weather_data['time'].str.contains('-08-16'))
    | (weather_data['time'].str.contains('-08-17'))
    | (weather_data['time'].str.contains('-08-18'))
    | (weather_data['time'].str.contains('-08-19'))
    | (weather_data['time'].str.contains('-08-20'))
    | (weather_data['time'].str.contains('-08-21'))
    | (weather_data['time'].str.contains('-08-22'))
    | (weather_data['time'].str.contains('-08-23'))
    | (weather_data['time'].str.contains('-08-24'))
    | (weather_data['time'].str.contains('-08-25'))
    | (weather_data['time'].str.contains('-08-26'))
    | (weather_data['time'].str.contains('-08-27'))
    | (weather_data['time'].str.contains('-08-28'))
    | (weather_data['time'].str.contains('-08-29'))
    | (weather_data['time'].str.contains('-08-30'))
    | (weather_data['time'].str.contains('-08-31'))
    | (weather_data['time'].str.contains('-09-01'))
    | (weather_data['time'].str.contains('-09-02'))
    | (weather_data['time'].str.contains('-09-03'))
    | (weather_data['time'].str.contains('-09-04'))
    | (weather_data['time'].str.contains('-09-05'))
    | (weather_data['time'].str.contains('-09-06'))
    | (weather_data['time'].str.contains('-09-07'))
    | (weather_data['time'].str.contains('-09-08'))
    | (weather_data['time'].str.contains('-09-09'))
    | (weather_data['time'].str.contains('-09-10'))
    | (weather_data['time'].str.contains('-09-11'))
    | (weather_data['time'].str.contains('-09-12'))
    | (weather_data['time'].str.contains('-09-13'))
    | (weather_data['time'].str.contains('-09-14'))
    | (weather_data['time'].str.contains('-09-15'))
    | (weather_data['time'].str.contains('-09-16'))
    | (weather_data['time'].str.contains('-09-17'))
    | (weather_data['time'].str.contains('-09-18'))
    | (weather_data['time'].str.contains('-09-19'))
    | (weather_data['time'].str.contains('-09-20'))
    | (weather_data['time'].str.contains('-09-21'))
    | (weather_data['time'].str.contains('-09-22'))
    | (weather_data['time'].str.contains('-09-23'))
    | (weather_data['time'].str.contains('-09-24'))
    | (weather_data['time'].str.contains('-09-25'))
    | (weather_data['time'].str.contains('-09-26'))
    | (weather_data['time'].str.contains('-09-27'))
    | (weather_data['time'].str.contains('-09-28'))
    | (weather_data['time'].str.contains('-09-29'))
    | (weather_data['time'].str.contains('-09-30'))]
weather_data['time'] = pd.to_datetime(weather_data['time'])
weather_data['year'] = weather_data['time'].dt.year

#weather_data = weather_data[weather_data['time'].dt.year == 2004]

#print(weather_data.to_string())
#print(weather_data)
#weather_data.to_csv('out.csv') 

# Step 6: Sum weather parameters
weather_data_sum = weather_data.groupby(['year'])[
    'temperature_2m (°C)',
    'relativehumidity_2m (%)',
    'rain (mm)',
    'dewpoint_2m (°C)',
    'surface_pressure (hPa)',
    'precipitation (mm)',
    'direct_radiation (W/m²)',
    'windspeed_10m (km/h)',
    'winddirection_10m (°)',
    'et0_fao_evapotranspiration (mm)',
    'soil_temperature_0_to_7cm (°C)',
    'soil_moisture_0_to_7cm (m³/m³)'].sum()

#print(weather_data_sum)

# Step 7: Rename headers
nitrous_oxide_croatia_data = nitrous_oxide_croatia_data.rename(columns={'Total including LUCF (per capita)' : 'annual_nitrous_oxide'})
methane_croatia_data = methane_croatia_data.rename(columns={'Total including LUCF (per capita)' : 'annual_methane'})
co2_croatia_data = co2_croatia_data.rename(columns={'Annual CO emissions (per capita)' : 'annual_co2'})
croatia_data = croatia_data.rename(columns={'Maize | 00000056 || Yield | 005419 || tonnes per hectare': 'corn_yield'})
weather_data_sum = weather_data_sum.rename(columns={
    'temperature_2m (°C)': 'temperature_sum',
    'relativehumidity_2m (%)': 'relativehumidity_sum',
    'rain (mm)':'rain_sum',
    'dewpoint_2m (°C)': 'dewpoint_sum',
    'surface_pressure (hPa)': 'surface_pressure_sum',
    'precipitation (mm)' : 'precipitation_sum',
    'direct_radiation (W/m²)': "direct_radiation_sum",
    'windspeed_10m (km/h)': 'windspeed_sum',
    'winddirection_10m (°)': 'winddirection_sum',
    'et0_fao_evapotranspiration (mm)': 'evapotranspiration_sum',
    'soil_temperature_0_to_7cm (°C)': 'soil_temp_sum',
    'soil_moisture_0_to_7cm (m³/m³)': 'soil_moisture_sum'})

# Step 8: merge the data and select columns
merged_data = pd.merge(croatia_data, weather_data_sum, left_on='Year', right_on='year')
merged_data = merged_data[[
    'Year',
    'corn_yield',
    'temperature_sum',
    'relativehumidity_sum',
    'rain_sum',
    'dewpoint_sum',
    'surface_pressure_sum',
    'precipitation_sum',
    'direct_radiation_sum',
    'windspeed_sum',
    'winddirection_sum',
    'evapotranspiration_sum',
    'soil_temp_sum',
    'soil_moisture_sum']]

merged_data = pd.merge(merged_data, co2_croatia_data, left_on='Year', right_on='Year')
merged_data = merged_data[[
    'Year',
    'corn_yield',
    'temperature_sum',
    'relativehumidity_sum',
    'rain_sum',
    'dewpoint_sum',
    'surface_pressure_sum',
    'precipitation_sum',
    'direct_radiation_sum',
    'windspeed_sum',
    'winddirection_sum',
    'evapotranspiration_sum',
    'soil_temp_sum',
    'soil_moisture_sum',
    'annual_co2']]

merged_data = pd.merge(merged_data, methane_croatia_data, left_on='Year', right_on='Year')
merged_data = merged_data[[
    'Year',
    'corn_yield',
    'temperature_sum',
    'relativehumidity_sum',
    'rain_sum',
    'dewpoint_sum',
    'surface_pressure_sum',
    'precipitation_sum',
    'direct_radiation_sum',
    'windspeed_sum',
    'winddirection_sum',
    'evapotranspiration_sum',
    'soil_temp_sum',
    'soil_moisture_sum',
    'annual_co2',
    'annual_methane']]

merged_data = pd.merge(merged_data, nitrous_oxide_croatia_data, left_on='Year', right_on='Year')
merged_data = merged_data[[
    'Year',
    'corn_yield',
    'temperature_sum',
    'relativehumidity_sum',
    'rain_sum',
    'dewpoint_sum',
    'surface_pressure_sum',
    'precipitation_sum',
    'direct_radiation_sum',
    'windspeed_sum',
    'winddirection_sum',
    'evapotranspiration_sum',
    'soil_temp_sum',
    'soil_moisture_sum',
    'annual_co2',
    'annual_methane',
    'annual_nitrous_oxide']]

# Step 9: Split the data into training and testing sets
X = merged_data[[
    'temperature_sum',
    'relativehumidity_sum',
    'rain_sum',
    'dewpoint_sum',
    'surface_pressure_sum',
    'precipitation_sum',
    'direct_radiation_sum',
    'windspeed_sum',
    'winddirection_sum',
    'evapotranspiration_sum',
    'soil_temp_sum',
    'soil_moisture_sum',
    'annual_co2',
    'annual_methane',
    'annual_nitrous_oxide']]
y = merged_data['corn_yield']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 10: Fit the model using the training data
glm_model = LinearRegression()
summary = glm_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = glm_model.predict(X_test)

# Calculate the absolute error
mae = mean_absolute_error(y_test, y_pred)
print(mae)

print("weighted parameter values: ")
print(glm_model.coef_)

print(y_test)
print(y_pred)

print("relative error")
relative_error = (mean_absolute_error(y_test, y_pred) / y_test.mean()) * 100
print(relative_error)