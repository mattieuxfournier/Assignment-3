
# Mattieux Fournier 2445249

# Assigning file and processing data
file = open('data.txt', 'r')
lines = file.read().split()
file.close()

# Finding index of JAN and DEC
start = lines.index('JAN')
end = lines.index('DEC')  # This should correctly capture the 'DEC' position

# Making all strings floats except for the months
float_lines = []
i = end + 1
while i < len(lines):
    float_lines.append(float(lines[i]))
    i += 1

lines = lines[start:end+1] + float_lines[:]  # Include DEC in the lines list

# Making the months into a list of keys
keys = []
i = 0
while i < len(lines):
    if type(lines[i]) == str:
        keys.append(lines[i])
    i += 1

# Removing months from the data safely
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

# Turning the years from floats to integers in the data
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
if len(temp_val) > 0:  # Check if temp_val is not empty
    for i in range(len(temp_val[0])):  # Loop over the first list (i.e., months)
        temp = []
        for j in range(len(temp_val)):  # Loop over all other lists (i.e., years)
            if i < len(temp_val[j]):  # Ensure index is valid in each sublist
                temp.append(temp_val[j][i])
        new_val.append(temp)

# Making the months keys and the newly made lists values
new_dict = {}
i = 0
while i < len(keys):
    new_dict[keys[i]] = new_val[i]
    i += 1

# Debug: Check if 'DEC' is present in the keys and dictionary
if 'DEC' not in new_dict:
    print("Warning: 'DEC' is missing from the new_dict.")
else:
    print("'DEC' is correctly included in the new_dict.")

# Convert temperatures to Celsius (Fahrenheit to Celsius)
for key in new_dict:
    for j in range(len(new_val)):
        new_dict[key][j] = round((new_dict[key][j] - 32)*(5/9), 2)

#find months with below-freezing temps
def belowFreezing(dict:dict):
    months_dict = {'JAN':'January', 'FEB':'February', 'MAR':'March', 'APR':'April', 'MAY':'May', 'JUN':'June',
                   'JUL':'July', 'AUG':'August', 'SEP':'September', 'OCT':'October', 'NOV':'November', 'DEC':'December'}
    below = []
    for key in dict:
        for i in range(len(new_val)):
            if dict[key][i] < 0:
                below.append(months_dict[key])
                break
    return below

below_freezing_months = belowFreezing(new_dict)
print(f"Months with below freezing temperatures: {below_freezing_months}")

# Open the files for reading and writing
data = open('data.txt', 'r')
data_cel = open('data_celcius.txt', 'w')
data_cel.writelines(data.readlines()[:4])  # Writing the first 4 lines to the file

# Calculate the maximum width for formatting (length of the longest value in the dictionary)
max_width = 0
for k in new_dict:
    for value in new_dict[k]:
        value_length = len(str(value))
        if value_length > max_width:
            max_width = value_length

# Write the formatted data to the new file with 4 spaces between each value and columns properly aligned
for k in new_dict:
    values = ""
    for value in new_dict[k]:
        formatted_value = str(value)
        # Add 4 spaces between each word and ensure each value is aligned
        values += f"{formatted_value:<{max_width}}   "  # 4 spaces between each value
    # Write the key with the corresponding values
    data_cel.write(f"{str(k):<{max_width}}")  # Align the key with the maximum width
    data_cel.write(" ")  # 4 spaces between key and values
    data_cel.write(values.strip())  # Add the values, removing the trailing space
    data_cel.write("\n")

# Print the dictionary for verification
print(new_dict)

# Close the file after writing
data_cel.close()