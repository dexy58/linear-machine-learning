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

co2_2019 = np.where((co2Data[:,0]=="Croatia")&(co2Data[:,1]==2019))
co2_2019 = co2Data[co2_2019[0][0]][2]
co2_2020 = np.where((co2Data[:,0]=="Croatia")&(co2Data[:,1]==2020))
co2_2020 = co2Data[co2_2020[0][0]][2]

methane_2019 = np.where((methaneData[:,0]=="Croatia")&(methaneData[:,1]==2019))
methane_2019 = methaneData[methane_2019[0][0]][2]
methane_2020 = np.where((methaneData[:,0]=="Croatia")&(methaneData[:,1]==2019))
methane_2020 = methaneData[methane_2020[0][0]][2]

nitrous_2019 = np.where((nitrousData[:,0]=="Croatia")&(nitrousData[:,1]==2019))
nitrous_2019 = nitrousData[nitrous_2019[0][0]][2]
nitrous_2020 = np.where((nitrousData[:,0]=="Croatia")&(nitrousData[:,1]==2019))
nitrous_2020 = nitrousData[nitrous_2020[0][0]][2]

yields_2019 = np.where((yieldData[:,0]=="Croatia")&(yieldData[:,1]==2019))
yields_2019 = yieldData[yields_2019[0][0]][2]
yields_2020 = np.where((yieldData[:,0]=="Croatia")&(yieldData[:,1]==2020))
yields_2020 = yieldData[yields_2020[0][0]][2]
print("Yield 2019: " + str(yields_2019))
print("Yield 2020: " + str(yields_2020))

indexBegin_2019 = np.where(dates == "2019-04-10T00:00")
indexEnd_2019 = indexBegin_2019[0][0] + 120 * 24

indexBegin_2020 = np.where(dates == "2020-04-10T00:00")
indexEnd_2020 = indexBegin_2020[0][0] + 120 * 24

sumTemp_2019 = 0
sumHum_2019 = 0
sumDew_2019 = 0
sumPressure_2019 = 0
sumPrecipitation_2019 = 0
sumRain_2019 = 0
sumRadiation_2019 = 0
sumWindspeed_2019 = 0
sumWindDirection_2019 = 0
sumEvapotranspiration_2019 = 0
sumSoilTemp_2019 = 0
sumSoilMoisture_2019 = 0

sumTemp_2020 = 0
sumHum_2020 = 0
sumDew_2020 = 0
sumPressure_2020 = 0
sumPrecipitation_2020 = 0
sumRain_2020 = 0
sumRadiation_2020 = 0
sumWindspeed_2020 = 0
sumWindDirection_2020 = 0
sumEvapotranspiration_2020 = 0
sumSoilTemp_2020 = 0
sumSoilMoisture_2020 = 0

for x in range(indexBegin_2019[0][0], indexEnd_2019):
    sumTemp_2019 += temperature[x][0]
    sumHum_2019 += humidity[x][0]
    sumDew_2019 += dewpoint[x][0]
    sumPressure_2019 += pressure[x][0]
    sumPrecipitation_2019 += precipitation[x][0]
    sumRain_2019 += rain[x][0]
    sumRadiation_2019 += radiation[x][0]
    sumWindspeed_2019 += windspeed[x][0]
    sumWindDirection_2019 += winddirection[x][0]
    sumEvapotranspiration_2019 += evapotranspiration[x][0]
    sumSoilTemp_2019 += soiltemp[x][0]
    sumSoilMoisture_2019 += soilmoisture[x][0]

for x in range(indexBegin_2020[0][0], indexEnd_2020):
    sumTemp_2020 += temperature[x][0]
    sumHum_2020 += humidity[x][0]
    sumDew_2020 += dewpoint[x][0]
    sumPressure_2020 += pressure[x][0]
    sumPrecipitation_2020 += precipitation[x][0]
    sumRain_2020 += rain[x][0]
    sumRadiation_2020 += radiation[x][0]
    sumWindspeed_2020 += windspeed[x][0]
    sumWindDirection_2020 += winddirection[x][0]
    sumEvapotranspiration_2020 += evapotranspiration[x][0]
    sumSoilTemp_2020 += soiltemp[x][0]
    sumSoilMoisture_2020 += soilmoisture[x][0]

print("suma temp 2019: " + str(sumTemp_2019))
print("suma hum 2019: " + str(sumHum_2019))
print("suma dew 2019: " + str(sumDew_2019))
print("suma pressure 2019: " + str(sumPressure_2019))
print("suma precipitation 2019: " + str(sumPrecipitation_2019))
print("suma rain 2019: " + str(sumRain_2019))
print("suma radiation 2019: " + str(sumRadiation_2019))
print("suma wind speed 2019: " + str(sumWindspeed_2019))
print("suma wind direction 2019: " + str(sumWindDirection_2019))
print("suma evapotranspiration 2019: " + str(sumEvapotranspiration_2019))
print("suma soil temp 2019: " + str(sumSoilTemp_2019))
print("suma soil moisture 2019: " + str(sumSoilMoisture_2019))
print("co2 2019: " + str(co2_2019))
print("methane 2019: " + str(methane_2019))
print("nitrous 2019: " + str(nitrous_2019))

print("suma temp 2020: " + str(sumTemp_2020))
print("suma hum 2020: " + str(sumHum_2020))
print("suma dew 2020: " + str(sumDew_2020))
print("suma pressure 2020: " + str(sumPressure_2020))
print("suma precipitation 2020: " + str(sumPrecipitation_2020))
print("suma rain 2020: " + str(sumRain_2020))
print("suma radiation 2020: " + str(sumRadiation_2020))
print("suma wind speed 2020: " + str(sumWindspeed_2020))
print("suma wind direction 2020: " + str(sumWindDirection_2020))
print("suma evapotranspiration 2020: " + str(sumEvapotranspiration_2020))
print("suma soil temp 2020: " + str(sumSoilTemp_2020))
print("suma soil moisture 2020: " + str(sumSoilMoisture_2020))
print("co2 2020: " + str(co2_2020))
print("methane 2020: " + str(methane_2020))
print("nitrous 2020: " + str(nitrous_2020))

maxNumber = 230
minNumber = -230

while True:
    solution_2019 = (minNumber*sumTemp_2019
        + minNumber*sumHum_2019
        + minNumber*sumDew_2019
        + minNumber*sumPressure_2019
        + minNumber*sumPrecipitation_2019
        + minNumber*sumRain_2019
        + minNumber*sumRadiation_2019
        + minNumber*sumWindspeed_2019
        + minNumber*sumWindDirection_2019
        + minNumber*sumEvapotranspiration_2019
        + minNumber*sumSoilTemp_2019
        + minNumber*sumSoilMoisture_2019
        + minNumber*co2_2019
        + minNumber*methane_2019
        + minNumber*nitrous_2019) / yields_2019

    solution_2020 = (minNumber*sumTemp_2020
        + minNumber*sumHum_2020
        + minNumber*sumDew_2020
        + minNumber*sumPressure_2020
        + minNumber*sumPrecipitation_2020
        + minNumber*sumRain_2020
        + minNumber*sumRadiation_2020
        + minNumber*sumWindspeed_2020
        + minNumber*sumWindDirection_2020
        + minNumber*sumEvapotranspiration_2020
        + minNumber*sumSoilTemp_2020
        + minNumber*sumSoilMoisture_2020
        + minNumber*co2_2020
        + minNumber*methane_2020
        + minNumber*nitrous_2020) / yields_2020
    print("solution 2019: " + str(solution_2019))
    print("solution 2020: " + str(solution_2020))
    if solution_2019 >= -10 and solution_2019 <= 10 and solution_2020 >=-10 and solution_2020 <= 10:
        print("found optimal min and max numbers")
        break
    maxNumber = maxNumber/2
    minNumber = minNumber/2

print("Max and min numbers: " + str(maxNumber) + " " + str(minNumber))

#Max and min numbers: 0.000438690185546875 -0.000438690185546875 for -250 and 250
step = 0.000002
a = minNumber
b = minNumber
c = minNumber
d = minNumber
e = minNumber
f = minNumber
g = minNumber
h = minNumber
i = minNumber
j = minNumber
k = minNumber
l = minNumber
m = minNumber
n = minNumber
o = minNumber

minSolution = 0.95
maxSolution = 1.05

def calculate_solution_2019():
    solution_2019 = (a*sumTemp_2019
        + b*sumHum_2019
        + c*sumDew_2019
        + d*sumPressure_2019
        + e*sumPrecipitation_2019
        + f*sumRain_2019
        + g*sumRadiation_2019
        + h*sumWindspeed_2019
        + i*sumWindDirection_2019
        + j*sumEvapotranspiration_2019
        + k*sumSoilTemp_2019
        + l*sumSoilMoisture_2019
        + m*co2_2019
        + n*methane_2019
        + o*nitrous_2019) / yields_2019
    
    return solution_2019

def calculate_solution_2020():
    solution_2020 = (a*sumTemp_2020
        + b*sumHum_2020
        + c*sumDew_2020
        + d*sumPressure_2020
        + e*sumPrecipitation_2020
        + f*sumRain_2020
        + g*sumRadiation_2020
        + h*sumWindspeed_2020
        + i*sumWindDirection_2020
        + j*sumEvapotranspiration_2020
        + k*sumSoilTemp_2020
        + l*sumSoilMoisture_2020
        + m*co2_2020
        + n*methane_2020
        + o*nitrous_2020) / yields_2020
    
    return solution_2020

def print_variables():
    print("a: " + str(a))
    print("b: " + str(b))
    print("c: " + str(c))
    print("d: " + str(d))
    print("e: " + str(e))
    print("f: " + str(f))
    print("g: " + str(g))
    print("h: " + str(h))
    print("i: " + str(i))
    print("j: " + str(j))
    print("k: " + str(k))
    print("l: " + str(l))
    print("m: " + str(m))
    print("n: " + str(n))
    print("o: " + str(o))

max_2019 = 0
max_2020 = 0
max = 0

while a < maxNumber:
    while b < maxNumber:
        while c <maxNumber:
            while d <maxNumber:
                while e <maxNumber:
                    while f <maxNumber:
                        while g <maxNumber:
                            while h <maxNumber:
                                while i <maxNumber:
                                    while j <maxNumber:
                                        while k <maxNumber:
                                            while l <maxNumber:
                                                while m <maxNumber:
                                                    while n <maxNumber:
                                                        while o <maxNumber:
                                                            solution_2019 = calculate_solution_2019()
                                                            solution_2020 = calculate_solution_2020()
                                                            if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                                                                #print("I am here: " + str(solution))
                                                                solution = (solution_2019 + solution_2020) / 2
                                                                if abs(max - solution) < abs(max - 1):
                                                                    print("New max here 2019: " + str(solution_2019))
                                                                    print("New max here 2020: " + str(solution_2020))
                                                                    print("Average solution: " + str(solution))
                                                                    print_variables()
                                                                    max = solution
                                                            o += step

                                                        solution_2019 = calculate_solution_2019()
                                                        solution_2020 = calculate_solution_2020()
                                                        if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                                                            #print("I am here: " + str(solution))
                                                            solution = (solution_2019 + solution_2020) / 2
                                                            if abs(max - solution) < abs(max - 1):
                                                                print("New max here 2019: " + str(solution_2019))
                                                                print("New max here 2020: " + str(solution_2020))
                                                                print("Average solution: " + str(solution))
                                                                print_variables()
                                                                max = solution
                                                        n += step
                                                        o = minNumber

                                                    solution_2019 = calculate_solution_2019()
                                                    solution_2020 = calculate_solution_2020()
                                                    if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                                                        #print("I am here: " + str(solution))
                                                        solution = (solution_2019 + solution_2020) / 2
                                                        if abs(max - solution) < abs(max - 1):
                                                            print("New max here 2019: " + str(solution_2019))
                                                            print("New max here 2020: " + str(solution_2020))
                                                            print("Average solution: " + str(solution))
                                                            print_variables()
                                                            max = solution
                                                    m += step
                                                    n = minNumber
                                                    o = minNumber

                                                solution_2019 = calculate_solution_2019()
                                                solution_2020 = calculate_solution_2020()
                                                if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                                                    #print("I am here: " + str(solution))
                                                    solution = (solution_2019 + solution_2020) / 2
                                                    if abs(max - solution) < abs(max - 1):
                                                        print("New max here 2019: " + str(solution_2019))
                                                        print("New max here 2020: " + str(solution_2020))
                                                        print("Average solution: " + str(solution))
                                                        print_variables()
                                                        max = solution
                                                l += step
                                                m = minNumber
                                                n = minNumber
                                                o = minNumber

                                            solution_2019 = calculate_solution_2019()
                                            solution_2020 = calculate_solution_2020()
                                            if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                                                #print("I am here: " + str(solution))
                                                solution = (solution_2019 + solution_2020) / 2
                                                if abs(max - solution) < abs(max - 1):
                                                    print("New max here 2019: " + str(solution_2019))
                                                    print("New max here 2020: " + str(solution_2020))
                                                    print("Average solution: " + str(solution))
                                                    print_variables()
                                                    max = solution
                                            k += step
                                            l = minNumber
                                            m = minNumber
                                            n = minNumber
                                            o = minNumber

                                        solution_2019 = calculate_solution_2019()
                                        solution_2020 = calculate_solution_2020()
                                        if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                                            #print("I am here: " + str(solution))
                                            solution = (solution_2019 + solution_2020) / 2
                                            if abs(max - solution) < abs(max - 1):
                                                print("New max here 2019: " + str(solution_2019))
                                                print("New max here 2020: " + str(solution_2020))
                                                print("Average solution: " + str(solution))
                                                print_variables()
                                                max = solution
                                        j += step
                                        k = minNumber
                                        l = minNumber
                                        m = minNumber
                                        n = minNumber
                                        o = minNumber

                                    solution_2019 = calculate_solution_2019()
                                    solution_2020 = calculate_solution_2020()
                                    if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                                        #print("I am here: " + str(solution))
                                        solution = (solution_2019 + solution_2020) / 2
                                        if abs(max - solution) < abs(max - 1):
                                            print("New max here 2019: " + str(solution_2019))
                                            print("New max here 2020: " + str(solution_2020))
                                            print("Average solution: " + str(solution))
                                            print_variables()
                                            max = solution
                                    i += step
                                    j = minNumber
                                    k = minNumber
                                    l = minNumber
                                    m = minNumber
                                    n = minNumber
                                    o = minNumber

                                solution_2019 = calculate_solution_2019()
                                solution_2020 = calculate_solution_2020()
                                if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                                    #print("I am here: " + str(solution))
                                    solution = (solution_2019 + solution_2020) / 2
                                    if abs(max - solution) < abs(max - 1):
                                        print("New max here 2019: " + str(solution_2019))
                                        print("New max here 2020: " + str(solution_2020))
                                        print("Average solution: " + str(solution))
                                        print_variables()
                                        max = solution
                                h += step
                                i = minNumber
                                j = minNumber
                                k = minNumber
                                l = minNumber
                                m = minNumber
                                n = minNumber
                                o = minNumber

                            solution_2019 = calculate_solution_2019()
                            solution_2020 = calculate_solution_2020()
                            if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                                #print("I am here: " + str(solution))
                                solution = (solution_2019 + solution_2020) / 2
                                if abs(max - solution) < abs(max - 1):
                                    print("New max here 2019: " + str(solution_2019))
                                    print("New max here 2020: " + str(solution_2020))
                                    print("Average solution: " + str(solution))
                                    print_variables()
                                    max = solution
                            g += step
                            h = minNumber
                            i = minNumber
                            j = minNumber
                            k = minNumber
                            l = minNumber
                            m = minNumber
                            n = minNumber
                            o = minNumber

                        solution_2019 = calculate_solution_2019()
                        solution_2020 = calculate_solution_2020()
                        if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                            #print("I am here: " + str(solution))
                            solution = (solution_2019 + solution_2020) / 2
                            if abs(max - solution) < abs(max - 1):
                                print("New max here 2019: " + str(solution_2019))
                                print("New max here 2020: " + str(solution_2020))
                                print("Average solution: " + str(solution))
                                print_variables()
                                max = solution
                        f += step
                        g = minNumber
                        h = minNumber
                        i = minNumber
                        j = minNumber
                        k = minNumber
                        l = minNumber
                        m = minNumber
                        n = minNumber
                        o = minNumber

                    solution_2019 = calculate_solution_2019()
                    solution_2020 = calculate_solution_2020()
                    if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                        #print("I am here: " + str(solution))
                        solution = (solution_2019 + solution_2020) / 2
                        if abs(max - solution) < abs(max - 1):
                            print("New max here 2019: " + str(solution_2019))
                            print("New max here 2020: " + str(solution_2020))
                            print("Average solution: " + str(solution))
                            print_variables()
                            max = solution
                    e += step
                    f = minNumber
                    g = minNumber
                    h = minNumber
                    i = minNumber
                    j = minNumber
                    k = minNumber
                    l = minNumber
                    m = minNumber
                    n = minNumber
                    o = minNumber

                solution_2019 = calculate_solution_2019()
                solution_2020 = calculate_solution_2020()
                if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                    #print("I am here: " + str(solution))
                    solution = (solution_2019 + solution_2020) / 2
                    if abs(max - solution) < abs(max - 1):
                        print("New max here 2019: " + str(solution_2019))
                        print("New max here 2020: " + str(solution_2020))
                        print("Average solution: " + str(solution))
                        print_variables()
                        max = solution
                d += step
                e = minNumber
                f = minNumber
                g = minNumber
                h = minNumber
                i = minNumber
                j = minNumber
                k = minNumber
                l = minNumber
                m = minNumber
                n = minNumber
                o = minNumber

            solution_2019 = calculate_solution_2019()
            solution_2020 = calculate_solution_2020()
            if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
                #print("I am here: " + str(solution))
                solution = (solution_2019 + solution_2020) / 2
                if abs(max - solution) < abs(max - 1):
                    print("New max here 2019: " + str(solution_2019))
                    print("New max here 2020: " + str(solution_2020))
                    print("Average solution: " + str(solution))
                    print_variables()
                    max = solution
            c += step
            d = minNumber
            e = minNumber
            f = minNumber
            g = minNumber
            h = minNumber
            i = minNumber
            j = minNumber
            k = minNumber
            l = minNumber
            m = minNumber
            n = minNumber
            o = minNumber

        solution_2019 = calculate_solution_2019()
        solution_2020 = calculate_solution_2020()
        if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
            #print("I am here: " + str(solution))
            solution = (solution_2019 + solution_2020) / 2
            if abs(max - solution) < abs(max - 1):
                print("New max here 2019: " + str(solution_2019))
                print("New max here 2020: " + str(solution_2020))
                print("Average solution: " + str(solution))
                print_variables()
                max = solution
        b += step
        c = minNumber
        d = minNumber
        e = minNumber
        f = minNumber
        g = minNumber
        h = minNumber
        i = minNumber
        j = minNumber
        k = minNumber
        l = minNumber
        m = minNumber
        n = minNumber
        o = minNumber

    solution_2019 = calculate_solution_2019()
    solution_2020 = calculate_solution_2020()
    if solution_2019 >= minSolution and solution_2019 <= maxSolution and solution_2020 >= minSolution and solution_2020 <= maxSolution:
        #print("I am here: " + str(solution))
        solution = (solution_2019 + solution_2020) / 2
        if abs(max - solution) < abs(max - 1):
            print("New max here 2019: " + str(solution_2019))
            print("New max here 2020: " + str(solution_2020))
            print("Average solution: " + str(solution))
            print_variables()
            max = solution
    a += step
    b = minNumber
    c = minNumber
    d = minNumber
    e = minNumber
    f = minNumber
    g = minNumber
    h = minNumber
    i = minNumber
    j = minNumber
    k = minNumber
    l = minNumber
    m = minNumber
    n = minNumber
    o = minNumber

print("I am done :)")