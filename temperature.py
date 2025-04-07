def toCelcius(F):
    C = round(float((F-32)*(5/9)),2)
    return C
data = open('data.txt', 'r')
temp_dict = {}
data = data.read().split()
start = []
for i in range(len(data)):
    if data[i] == '1964':
        start.append(i)
start.remove(start[0])
start = start[-1]
data = list(map(float,data[start:]))
years = []
for i in data:
    if len(str(i)) >= 5:
        data[data.index(i)] = int(i)
        years.append(data.index(i))
temps = []
for i in range(len(years)-1):
    temps.append([years[i]+1, years[i+1]-1])
for i in range(len(data)):
    if type(data[i]) == float:
        data[i] = toCelcius(data[i])
for i in range(len(years)-1):
    year = data[years[i]]
    start = years[i] +1
    end = years[i+1]
    year_temps = data[start:end]
    temp_dict[year] = year_temps
start = temps[-1][0]
end = temps[-1][1]
year = years[-1]
temp_dict[data[year]] = data[start:end]
print(temp_dict)