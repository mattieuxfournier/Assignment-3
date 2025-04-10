# change farenheit to celcius
def toCelcius(F):
    C = round(float((F-32)*(5/9)),2)
    return C
og_data = open('data.txt', 'r')
temp_dict = {}
data = og_data.read().split()
og_data.close()
# find starting point
start = []
for i in range(len(data)):
    if data[i] == '1964':
        start.append(i)
# remove first instance
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

def avgTempYear(dict, user_year):
    dict = open(f'{dict}')
    dict = dict.read().split()
    try:
        avg = round(sum(dict[user_year])/len(dict[user_year]),2)
        return avg
    except KeyError:
        print('Sorry that year is not in the dictionary')
        return
def topThreeYears(dict: dict):
    dict = open(f'{dict}')
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
def avgTempMonth(dict: dict, month_str):
    month_dict = {'JAN': 0, 'FEB': 1, 'MAR': 2, 'APR': 3, 'MAY': 4, 'JUN': 5,
                  'JUL': 6, 'AUG': 7, 'SEP': 8, 'OCT': 9, 'NOV': 10, 'DEC': 11}
    if month_str not in month_dict:
        print("Invalid month abbreviation.")
        return
    month_index = month_dict[month_str]
    total = 0
    count = 0
    for year in dict:
        if len(dict[year]) > month_index:
            total += dict[year][month_index]
            count += 1
    if count == 0:
        return 0
    return round(total / count, 2)
# Part 2
file = open('data.txt', 'r')
lines = file.read().split()
file.close()

# Finding index of JAN and DEC
start = lines.index('JAN')
end = lines.index('DEC')

# Making all strings floats except for the months
float_lines = []
i = end + 1
while i < len(lines):
    float_lines.append(float(lines[i]))
    i += 1

lines = lines[start:end+1] + float_lines[:]

# Making the months into a list of keys
keys = []
i = 0
while i < len(lines):
    if type(lines[i]) == str:
        keys.append(lines[i])
    i += 1

# Removing months from the data
clean_lines = []
i = 0
while i < len(lines):
    if type(lines[i]) != str:
        clean_lines.append(lines[i])
    i += 1
lines = clean_lines

# Turning the years into integers, adding them to a list, and making another list to store their indexes in the data
values = []
years = []
i = 0
while i < len(lines):
    if len(str(lines[i])) >= 5:
        years.append(int(lines[i]))
        values.append(i)
    i += 1

# Turning the years from floats to integers
i = 0
while i < len(values):
    lines[values[i]] = int(lines[values[i]])
    i += 1

# Creating 2 lists, temp holds all the floats. Once an integer is encountered, it appends all collected floats to the second list and resets it
temp_val = []
temp = []
i = 0
while i < len(lines):
    if type(lines[i]) == float:
        temp.append(lines[i])
    elif type(lines[i]) == int:
        if len(temp) > 0:
            temp_val.append(temp)
            temp = []
    i += 1
if len(temp) > 0:
    temp_val.append(temp)

# Making new nested list so that the first list holds all first elements of other lists and so on
new_val = []
if len(temp_val) > 0:
    for i in range(len(temp_val[0])):
        temp = []
        for j in range(len(temp_val)):
            if i < len(temp_val[j]):
                temp.append(temp_val[j][i])
        new_val.append(temp)

# Making the months keys and the lists values
new_dict = {}
i = 0
while i < len(keys):
    new_dict[keys[i]] = new_val[i]
    i += 1

# Convert temperatures to Celsius
for key in new_dict:
    for j in range(len(new_dict[key])):
        new_dict[key][j] = round(toCelcius(new_dict[key][j]),2)

# Find months with below-freezing temps
def belowFreezing(dict: dict):
    months_dict = {
        'JAN': 'January', 'FEB': 'February', 'MAR': 'March', 'APR': 'April',
        'MAY': 'May', 'JUN': 'June', 'JUL': 'July', 'AUG': 'August',
        'SEP': 'September', 'OCT': 'October', 'NOV': 'November', 'DEC': 'December'
    }
    below = []
    for key in dict:
        for i in range(len(dict[key])):
            if dict[key][i] < 0:
                below.append(months_dict[key])
                break
    return below

# Writing first 4 lines to new file
data = open('data.txt', 'r')
data_cel = open('data_celcius.txt', 'w')
data_cel.writelines(data.readlines()[:4])

# maximum width for all formatted values
max_width = 6
# function to make all values the same length in order to align them
def format_value(value):
    formatted = f'{value:.2f}'
    if len(formatted) < 6:
        formatted += (6-len(formatted))*'0'
    if len(formatted) > 6:
        formatted = formatted[:-1]
    while len(formatted) < max_width:
        formatted += ' '
    
    return formatted

for key in new_dict:
    formatted_key = key
    while len(formatted_key) < max_width:
        formatted_key += ' '
    
    formatted_values = []
    for value in new_dict[key]:
        formatted_values.append(format_value(value))
    
    values_line = ('    '.join(formatted_values)).strip()
    

    data_cel.write(f"{formatted_key} {values_line}\n")

data_cel.close()