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

co2 = np.where((co2Data[:,0]=="Croatia")&(co2Data[:,1]==2020))
co2 = co2Data[co2[0][0]][2]

methane = np.where((methaneData[:,0]=="Croatia")&(methaneData[:,1]==2019))
methane = methaneData[methane[0][0]][2]

nitrous = np.where((nitrousData[:,0]=="Croatia")&(nitrousData[:,1]==2019))
nitrous = nitrousData[nitrous[0][0]][2]

yields = np.where((yieldData[:,0]=="Croatia")&(yieldData[:,1]==2020))
yields = yieldData[yields[0][0]][2]
print(yields)

indexBegin = np.where(dates == "2020-04-10T00:00")
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

maxNumber = 50
minNumber = -50

while True:
    solution = (minNumber*sumTemp
        + minNumber*sumHum
        + minNumber*sumDew
        + minNumber*sumPressure
        + minNumber*sumPrecipitation
        + minNumber*sumRain
        + minNumber*sumRadiation
        + minNumber*sumWindspeed
        + minNumber*sumWindDirection
        + minNumber*sumEvapotranspiration
        + minNumber*sumSoilTemp
        + minNumber*sumSoilMoisture
        + minNumber*co2
        + minNumber*methane
        + minNumber*nitrous) / yields
    #print("solution: " + str(solution))
    if solution >= -100 and solution <= 100:
        break
    maxNumber = maxNumber/2
    minNumber = minNumber/2

print("Max and min numbers: " + str(maxNumber) + " " + str(minNumber))

step = 0.0012
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

def calculate_solution():
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
        + o*nitrous) / yields
    
    return solution

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
                                                            solution = calculate_solution()
                                                            if solution >= minSolution and solution <= maxSolution:
                                                                #print("I am here: " + str(solution))
                                                                if abs(max - solution) < abs(max - 1):
                                                                    print("New max here: " + str(solution))
                                                                    print_variables()
                                                                    max = solution
                                                            o += step

                                                        solution = calculate_solution()
                                                        if solution >= minSolution and solution <= maxSolution:
                                                            #print("I am here: " + str(solution))
                                                            if abs(max - solution) < abs(max - 1):
                                                                print("New max here: " + str(solution))
                                                                print_variables()
                                                                max = solution
                                                        n += step
                                                        o = minNumber

                                                    solution = calculate_solution()
                                                    if solution >= minSolution and solution <= maxSolution:
                                                        #print("I am here: " + str(solution))
                                                        if abs(max - solution) < abs(max - 1):
                                                            print("New max here: " + str(solution))
                                                            print_variables()
                                                            max = solution
                                                    m += step
                                                    n = minNumber
                                                    o = minNumber

                                                solution = calculate_solution()
                                                if solution >= minSolution and solution <= maxSolution:
                                                    #print("I am here: " + str(solution))
                                                    if abs(max - solution) < abs(max - 1):
                                                        print("New max here: " + str(solution))
                                                        print_variables()
                                                        max = solution
                                                l += step
                                                m = minNumber
                                                n = minNumber
                                                o = minNumber

                                            solution = calculate_solution()
                                            if solution >= minSolution and solution <= maxSolution:
                                                #print("I am here: " + str(solution))
                                                if abs(max - solution) < abs(max - 1):
                                                    print("New max here: " + str(solution))
                                                    print_variables()
                                                    max = solution
                                            k += step
                                            l = minNumber
                                            m = minNumber
                                            n = minNumber
                                            o = minNumber

                                        solution = calculate_solution()
                                        if solution >= minSolution and solution <= maxSolution:
                                            #print("I am here: " + str(solution))
                                            if abs(max - solution) < abs(max - 1):
                                                print("New max here: " + str(solution))
                                                print_variables()
                                                max = solution
                                        j += step
                                        k = minNumber
                                        l = minNumber
                                        m = minNumber
                                        n = minNumber
                                        o = minNumber

                                    solution = calculate_solution()
                                    if solution >= minSolution and solution <= maxSolution:
                                        #print("I am here: " + str(solution))
                                        if abs(max - solution) < abs(max - 1):
                                            print("New max here: " + str(solution))
                                            print_variables()
                                            max = solution
                                    i += step
                                    j = minNumber
                                    k = minNumber
                                    l = minNumber
                                    m = minNumber
                                    n = minNumber
                                    o = minNumber

                                solution = calculate_solution()
                                if solution >= minSolution and solution <= maxSolution:
                                    #print("I am here: " + str(solution))
                                    if abs(max - solution) < abs(max - 1):
                                        print("New max here: " + str(solution))
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

                            solution = calculate_solution()
                            if solution >= minSolution and solution <= maxSolution:
                                #print("I am here: " + str(solution))
                                if abs(max - solution) < abs(max - 1):
                                    print("New max here: " + str(solution))
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

                        solution = calculate_solution()
                        if solution >= minSolution and solution <= maxSolution:
                            #print("I am here: " + str(solution))
                            if abs(max - solution) < abs(max - 1):
                                print("New max here: " + str(solution))
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

                    solution = calculate_solution()
                    if solution >= minSolution and solution <= maxSolution:
                        #print("I am here: " + str(solution))
                        if abs(max - solution) < abs(max - 1):
                            print("New max here: " + str(solution))
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

                solution = calculate_solution()
                if solution >= minSolution and solution <= maxSolution:
                    #print("I am here: " + str(solution))
                    if abs(max - solution) < abs(max - 1):
                        print("New max here: " + str(solution))
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

            solution = calculate_solution()
            if solution >= minSolution and solution <= maxSolution:
                #print("I am here: " + str(solution))
                if abs(max - solution) < abs(max - 1):
                    print("New max here: " + str(solution))
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

        solution = calculate_solution()
        if solution >= minSolution and solution <= maxSolution:
            #print("I am here: " + str(solution))
            if abs(max - solution) < abs(max - 1):
                print("New max here: " + str(solution))
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

    solution = calculate_solution()
    if solution >= minSolution and solution <= maxSolution:
        #print("I am here: " + str(solution))
        if abs(max - solution) < abs(max - 1):
            print("New max here: " + str(solution))
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