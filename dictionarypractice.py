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
print(alien_0)

# now let's move our alien to the right!
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # alien must be fast
    x_increment = 3

# the new position is the old plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"The alien's new position is {alien_0['x_position']}")
