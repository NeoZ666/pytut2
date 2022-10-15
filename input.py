name = input('What is your name? ')
color = input('What is your favourite color? ')
birth_year = input('What year were you born in? ')
age = 2021 - int(birth_year)
print(str.capitalize(name), ',whose age is',age,'years old, likes the color',str.capitalize(color))


course = 'Python for beginners'
another = course[:]
print(another)
print(course[3:7])


name = input('May I know your fine name? ')
weight = input('Now please may I know your weight? ')
weight_type = input('Is it in pounds or kilograms? Answer by writing "lbs" for pounds or "kg" for kilograms: ')
if str.upper(weight_type) == 'KG':
    pound_weight = float(weight) * 2.205
    print('Weight of',str.capitalize(name),'is',pound_weight,'lbs.')
else:
    kilo_weight = float(weight) * 0.454
    print('Weight of',str.capitalize(name),'is',kilo_weight,'kgs.')
