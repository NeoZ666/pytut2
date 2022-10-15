is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
elif is_cold:
    print('''It's a cold day,
wear warm clothes''')
else:
    print("Enjoy your day")

print()

weather = input('Hello, is it a hot day?(y/n) ')
if str.upper(weather) == 'Y':
    print('''Indeed quite a hot day,
Drink plenty of water and keep yourself hydrated,
take care and goodbye.''')
if str.upper(weather) == 'N':
    wheather = input('Is it quite cold today then?(y/n) ')
    if str.upper(wheather) == 'Y':
        print('''Indeed quite freezing today,
Wear warm clothes and stay indoors, goodbye.''')
    elif str.upper(wheather) == 'N':
        print('It must be a lovely  then eh')

print()

price = f'USD $1000000'
has_good_credit = False
if has_good_credit:
    downpayment = 1000000 * 0.1
    print(f'Final downpayment on {price} home is USD ${str(downpayment)}')
else:
    downpayment = 1000000 * 0.2
    print(f'Final downpayment on {price} home is USD ${downpayment}')

print()

has_high_income = True
has_bad_credit = True

if has_high_income and not has_bad_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

print()

temp = input('What is the temperature(Celsius) today? ')
if int(temp) >= 30:
    print("It's quite a hot day")
elif int(temp) <= 10:
    print("It's a cold day")
else:
    print("It's neither cold or hot")

print()

name = input("What's your good name? ")
if len(name) < 3 :
    print("Name must be atleast 3 characters long.")
elif len(name) > 15 :
    print("Name can be maximum of 15 characters.")
else:
    print('Name looks great...')