person = {
    'first_name': 'Muhammad',
    'last_name': 'Umer',
    'age': 18,
    'city': 'Sharjah',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

glossary = {
    'cake': 'A oven baked sweetbread.',
    'bread': 'A dough made with flour and yeast.',
    'chips': 'a crunchy solid dough eaten as a snack.',
    'juice': 'A sweet and sour liqiud for refreshment.',
    'tea': "A hot liquid used to refesh you in the morning.",
    }

word = 'cake'
print("\n" + word.title() + ": " + glossary[word])

word = 'bread'
print("\n" + word.title() + ": " + glossary[word])

word = 'chips'
print("\n" + word.title() + ": " + glossary[word])

word = 'juice'
print("\n" + word.title() + ": " + glossary[word])

word = 'tea'
print("\n" + word.title() + ": " + glossary[word])


glossary = {
    'cake': 'A oven baked sweetbread.',
    'bread': 'A dough made with flour and yeast.',
    'chips': 'a crunchy solid dough eaten as a snack.',
    'juice': 'A sweet and sour liqiud for refreshment.',
    'tea': "A hot liquid used to refesh you in the morning.",
    'biscuits': 'A snack to eat in tea time.',
    'marshmellow': 'a fluffy candy to sweetwn your mouth .',
    'jam': ' A spread used on bread.',
    'peanuts': 'dryfruits.',
    'cold drink': 'fizzy drink.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

rivers_world = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers_world.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers_world.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers_world.values():
    print("- " + country.title())


pet_one = {'tiger': 'Tony'}
pet_two = {'lion': 'Natasha'}
pet_three = {'deer': 'Sally'}
pet_four = {'falcon': 'Bruce'}

pets_name = [pet_one, pet_two, pet_three, pet_four]
for pet in pets_name:
    print(f"{pet_one}is a very wild animal ")
    print(f"{pet_two}is a the kind of the jungle")
    print(f"{pet_three}is a prey of the tiger")
    print(f"{pet_four}is a kind of the desert")

import operator
e = {2: 4, 1: 3, 6: 8, 5: 7, 0: 0}
print('Original dictionary : ',e)
sorted_e = sorted(e.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_e)
sorted_e = dict( sorted(e.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_e)

my_dict1 = {'data1':99,'data2':-1,'data3':750}
print(sum(my_dict1.values()))

keys_color = ['indian red', 'dark salmon', 'deep pink']
values_code = ['#CD5C5C','#E9967A', '#FF1493']
color_dictionary3 = dict(zip(keys_color, values_code))
print(color_dictionary3)

from collections import Counter
a1 = {'x': 100, 'y': 200, 'z':300}
a2 = {'x': 300, 'y': 200, 'a':400}
a = Counter(a1) + Counter(a2)
print(a)


keys_number = ['eighty', 'ninety', 'hundred']
values_number = [80, 90, 100]

res_dict70 = dict(zip(keys_number, values_number))
print(res_dict70)