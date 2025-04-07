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
def avgTempYear(dictionary, user_year):
    dict = open(f'{dictionary}')
    dict = dict.read().split()
    try:
        avg = round(sum(dict[user_year])/len(dict[user_year]),2)
        return avg
    except KeyError:
        print('Sorry that year is not in the dictionary')
        return
def topThreeYears(dictionary):
    dict = open(f'{dictionary}')
    dict = dict.read().split()
    year_averages = []
    for year in dict:
        avg = sum(dict[year]) / len(dict[year])
        year_averages.append((year, round(avg, 2)))
    for i in range(len(year_averages)):
        for j in range(i + 1, len(year_averages)):
            if year_averages[j][1] > year_averages[i][1]:
                year_averages[i], year_averages[j] = year_averages[j], year_averages[i]
    return year_averages[:3]
def avgTempMonth(dictionary, month_str):
    month_dict = {'JAN': 0, 'FEB': 1, 'MAR': 2, 'APR': 3, 'MAY': 4, 'JUN': 5,
                  'JUL': 6, 'AUG': 7, 'SEP': 8, 'OCT': 9, 'NOV': 10, 'DEC': 11}
    if month_str not in month_dict:
        print("Invalid month abbreviation.")
        return
    month_index = month_dict[month_str]
    total = 0
    count = 0
    for year in dictionary:
        if len(dictionary[year]) > month_index:
            total += dictionary[year][month_index]
            count += 1
    if count == 0:
        return 0
    return round(total / count, 2)