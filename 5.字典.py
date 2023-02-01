#1 dx
alien_0 = {'color':'green','points':5}

print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

favorite_lauguages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

language = favorite_lauguages['sarah'].title()
print(f"Sarah's favorite languages is {language}.")

#2 dx[kx]
alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print(new_points)

alien_0 = {'color':'green','points':5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#3 del dx[kx]
alien_0 = {'color':'green','points':5}
del alien_0['points']
print(alien_0)

#4 .get(kx,txt)
alien_0 = {'color':'green','speed':'slow'}
point_value = alien_0.get('points',"No point value assigned.")
print(point_value)

#5 .items() .keys() .value()
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
for key,value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

for key in user_0.keys():
    print(key)

for value in user_0.values():
    print(value)

for key in user_0:
    print(key)


favorite_lauguages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

friends = ['phil','sarah']
for name in favorite_lauguages.keys():
    print(f"Hi,{name}")
    if name in friends:
        language = favorite_lauguages[name].title()
        print(f"\t{name.title()},I see you love {language}")

copy = {}
for key,value in favorite_lauguages.items():
    copy[key] = value
print(copy)

# *review
favorite_lauguages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rdby',
    'phil':'python'
}

for name in sorted(favorite_lauguages.keys()):
    print(f"{name.title()},thank you for taking the poll.")

#6 sx set()
languages = {'python','ruby','python','c'}
print(languages)

favorite_lauguages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

print("The following languages have been mentioned:")
for language in set(favorite_lauguages.values()):
    print(language)

#7 <nested>
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print(len(aliens))

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [
    {'colour':'green','points':5},
    {'colour':'yellow','points':10},
    {'colour':'yellow','points':10}
    ]

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)

pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_lauguages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

for user,languages in favorite_lauguages.items():
    print(f"{user}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
    print("\n")

for user,languages in favorite_lauguages.items():
    if len(languages) < 2:
        print(f"{user}'s favorite language is:")
    else:
        print(f"{user}'s favorite languages are:")
    for language in languages:
        print(f"\t{language}")
    print("\n")

users = {
    'Mr_49':{
        'first':'Mr',
        'last':'49',
        'IP':'Fuzhou University'
    },
    
    'wuxi_xiao':{
        'first':'wuxi',
        'last':'xiao',
        'IP':'Australia'
    }
}

for user,information in users.items():
    full_name = information['first'] + "_" + information['last']

    print(f"\nusername : {user}")
    print(f"\tfull name: {full_name}")
    print(f"\tIP: {information['IP'].title()}")