# Dictionary practice chapter 6 Python Crash Course
# a dictionary uses curly brackets {} and key:value pairs
# keys - can be string, list, even another dictionary
# values - any object in python can be a value in a dictionary

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

# dictionaries are dynamic - can add key:value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(f"The alien's original x,y-position is: {alien_0['x_position']}, {alien_0['y_position']}")

# now let's move our alien to the right!
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # alien must be fast
    x_increment = 3

# now let's move our alien up!
if alien_0['speed'] == 'slow':
    y_increment = 1
elif alien_0['speed'] == 'medium':
    y_increment = 2
else:
    # alien must be fast
    y_increment = 3

# the new position is the old plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_0['y_position'] = alien_0['y_position'] + y_increment

print(f"The alien's new x,y-position is: {alien_0['x_position']}, {alien_0['y_position']}")

# New example - users on a website - LOOPING
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',  # use a comma at the end so you can add more key:value pairs to the dictionary later
    }
# you can choose any name here for key, value - could use k,v or bob, sally but key,value is easiest to understand
# this for loop will loop through all of the values in the dictionary user_0
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# example favorite languages
favorite_languages = {
    'jen': 'C',
    'bob': 'R',
    'sally': 'ruby',
    'paul': 'python',
    'eli': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# loop through the dictionary in order using the sorted() function and dictionary.keys method
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# the following looks at the information stored in the dictionary but doesn't check for repeats
print('The following languages have been mentioned:')
for language in sorted(favorite_languages.values()):
    print(language.title())

# a set is a collection of items without repeats (each item is unique)
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())