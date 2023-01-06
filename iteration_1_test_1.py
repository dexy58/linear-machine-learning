import pandas as pd
import numpy as np
import time

maizeYield = pd.read_csv("data/maize-yields.csv")
co2File = pd.read_csv("data/co2 - per capita.csv")
weather = pd.read_csv("data/hours weather data.csv")
methaneFile = pd.read_csv("data/methane - per capita.csv")
nitrousFile = pd.read_csv("data/nitrous oxide per capita.csv")

temperature = weather.iloc[:, [1]].values
humidity = weather.iloc[:, [2]].values
dewpoint = weather.iloc[:, [3]].values
pressure = weather.iloc[:, [4]].values
precipitation = weather.iloc[:, [5]].values
rain = weather.iloc[:, [6]].values
radiation = weather.iloc[:, [7]].values
windspeed = weather.iloc[:, [8]].values
winddirection = weather.iloc[:, [9]].values
evapotranspiration = weather.iloc[:, [10]].values
soiltemp = weather.iloc[:, [11]].values
soilmoisture = weather.iloc[:, [12]].values

co2Data = co2File.iloc[:, [0, 2, 3]].values
methaneData = methaneFile.iloc[:, [0, 2, 3]].values
nitrousData = nitrousFile.iloc[:, [0, 2, 3]].values

dates = weather.iloc[:, 0].values

yieldData = maizeYield.iloc[:, [0, 2, 3]].values

co2 = np.where((co2Data[:,0]=="Croatia")&(co2Data[:,1]==2018))
co2 = co2Data[co2[0][0]][2]

methane = np.where((methaneData[:,0]=="Croatia")&(methaneData[:,1]==2018))
methane = methaneData[methane[0][0]][2]

nitrous = np.where((nitrousData[:,0]=="Croatia")&(nitrousData[:,1]==2018))
nitrous = nitrousData[nitrous[0][0]][2]

yields = np.where((yieldData[:,0]=="Croatia")&(yieldData[:,1]==2018))
yields = yieldData[yields[0][0]][2]

indexBegin = np.where(dates == "2018-04-10T00:00")
indexEnd = indexBegin[0][0] + 120 * 24

sumTemp = 0
sumHum = 0
sumDew = 0
sumPressure = 0
sumPrecipitation = 0
sumRain = 0
sumRadiation = 0
sumWindspeed = 0
sumWindDirection = 0
sumEvapotranspiration = 0
sumSoilTemp = 0
sumSoilMoisture = 0

for x in range(indexBegin[0][0], indexEnd):
    sumTemp += temperature[x][0]
    sumHum += humidity[x][0]
    sumDew += dewpoint[x][0]
    sumPressure += pressure[x][0]
    sumPrecipitation += precipitation[x][0]
    sumRain += rain[x][0]
    sumRadiation += radiation[x][0]
    sumWindspeed += windspeed[x][0]
    sumWindDirection += winddirection[x][0]
    sumEvapotranspiration += evapotranspiration[x][0]
    sumSoilTemp += soiltemp[x][0]
    sumSoilMoisture += soilmoisture[x][0]

print("suma: " + str(sumTemp))
print("suma: " + str(sumHum))
print("suma: " + str(sumDew))
print("suma: " + str(sumPressure))
print("suma: " + str(sumPrecipitation))
print("suma: " + str(sumRain))
print("suma: " + str(sumRadiation))
print("suma: " + str(sumWindspeed))
print("suma: " + str(sumWindDirection))
print("suma: " + str(sumEvapotranspiration))
print("suma: " + str(sumSoilTemp))
print("suma: " + str(sumSoilMoisture))
print("co2: " + str(co2))
print("methane: " + str(methane))
print("nitrous: " + str(nitrous))

a = -0.003051758
b = -0.003051758
c = -0.003051758
d = -0.000651758
e = 0.000548242
f = 0.002948242
g = 0.002948242
h = 0.001748242
i = 0.002948242
j = 0.002948242
k = 0.000548242
l = 0.001748242
m = 0.001748242
n = -0.001851758
o = 0.001748242


solution = (a*sumTemp
        + b*sumHum
        + c*sumDew
        + d*sumPressure
        + e*sumPrecipitation
        + f*sumRain
        + g*sumRadiation
        + h*sumWindspeed
        + i*sumWindDirection
        + j*sumEvapotranspiration
        + k*sumSoilTemp
        + l*sumSoilMoisture
        + m*co2
        + n*methane
        + o*nitrous)

print("Crop yield 2018: " + str(yields))
print("Calculated solution: " + str(solution))