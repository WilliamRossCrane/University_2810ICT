import string 

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 

data = input("Enter a string: ") 

# Translates and Replaces Chars with Desired Charecters  

data = data.translate(str.maketrans('', '', string.punctuation)) 

# Changes the Input to Uppercase and splits it into a list 

data_arr = data.upper().split(' ') 

a = {} 

# Checks if a Word Appears More than Once in the list 

# It will Append it to Add +1 

for i in data_arr: 

    if i not in a: 

        a[i] = 1 

    else: 

        a[i] = a[i] + 1 

# Sorts all the Items, key=lambda a: a[0] to Sort Alphabetically        

data = sorted(a.items()) 

# Removes Tuple Brackets  

data = [', '.join(map(str, x)) for x in data] 

# Prints Vertically  

print(*data, sep = '\n') 