import pandas

# Read CSV data into a DataFrame
data = pandas.read_csv("Day 25/nato_phonetic_alphabet.csv")

# Create a dictionary from the DataFrame
phonetics = {row.letter: row.code for (index, row) in data.iterrows()}

# Take user input and convert to uppercase
word = input("Enter your name: ").upper()

# Convert each letter to its phonetic code
output = [phonetics[letter] for letter in word] #we faced error here as we were creating another dictionary from recent dictionary.As it is unordered it cannot show code in sequential order

# Print the result
print(output)
