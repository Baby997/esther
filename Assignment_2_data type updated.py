# Create a data processing script that:

# Initializes a list called data_entries with ten string values (e.g., filenames)
# Uses slicing to extract the first 3, last 3, and middle 4 elements
# Creates a string and reverses it using slicing
# Samples every 3rd element from the list
# Uses input() to get a number from the user (as string)
# Converts the string to an integer and multiplies by 2
# Adds the result as a new entry to the list
# Prints both the updated list and calculation result

# Initializes a list called data_entries with ten string values (e.g., filenames)
data_entries = [ "/filename1.csv",
                "/filename2.csv",
                "/filename3.csv",
                "/filename4.csv",
                "/filename5.csv",
                "/filename6.csv",
                "/filename7.csv",
                "/filename8.csv",
                "/filename9.csv",
                "/filename10.csv",
                ]

# Uses slicing to extract the first 3, last 3, and middle 4 elements
print(data_entries[0:3])
print(data_entries[-3:])
print(data_entries[3:7])

# Creates a string and reverses it using slicing
string_element= "Dike Uruchi"

# Samples every 3rd element from the list
print(string_element[::-1])
print(data_entries[::3])

# Uses input() to get a number from the user (as string)
user_input = input("Enter a number:")

# Converts the string to an integer and multiplies by 2
conv_number = int(user_input) * 2
print(conv_number)

# Adds the result as a new entry to the list
data_entries.append(conv_number)
print(data_entries)







