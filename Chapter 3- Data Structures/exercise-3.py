names_uni = ['Hamad', 'Abdullah', 'Hashir']

print(names_uni[0])
print(names_uni[1])
print(names_uni[2])

names_uni = ['hamad', 'abdullah', 'hashir']

msg = f"Hello, {names_uni[0].title()}!"
print(msg)

msg = f"Hello, {names_uni[1].title()}!"
print(msg)

msg = f"Hello, {names_uni[2].title()}!"
print(msg)

transportation_vechile = ['car', 'motorcycle', 'helicopter', 'bus,']
print(transportation_vechile[0] + ' My dream car is to drive a LaFerrari.')
print(transportation_vechile[1] + ' it is a very reliable transportation for travelling short distances .')
print(transportation_vechile[2] + ' it shows u the around the world in one glance.')
print(transportation_vechile[3] + ' a transportation use to travel from one place to another')

Invitation_everyone = ['Friends ', 'Relatives ', 'Family ']
print(Invitation_everyone[0] + ',we would love to have you over dinner party.')
print(Invitation_everyone[1] + ',we would love to have you over dinner party.')
print(Invitation_everyone[2] + ',we would love to have you over dinner party.')

Invitation_everyone = ['Friends ', 'Relatives ', 'Family ']
print(Invitation_everyone[0] + ',we would love to have you over dinner party.')
print(Invitation_everyone[1] + ',we would love to have you over dinner party.')
print(Invitation_everyone[2] + ',we would love to have you over dinner party.')
print(Invitation_everyone[1] + "can't make it.")
Invitation_everyone.pop(1)
Invitation_everyone.append('Nighbours ')
print(Invitation_everyone)
print(Invitation_everyone[0] + ',we would love to have you over dinner party.')
print(Invitation_everyone[1] + ',we would love to have you over dinner party.')
print(Invitation_everyone[2] + ',we would love to have you over dinner party.')


Invitation_everyone = ['Friends ', 'Relatives ', 'Family ']
print(Invitation_everyone[0] + ',we would love to have you over dinner party.')
print(Invitation_everyone[1] + ',we would love to have you over dinner party.')
print(Invitation_everyone[2] + ',we would love to have you over dinner party.')
print(Invitation_everyone[1] + "can't make it.")
Invitation_everyone.pop(1)
Invitation_everyone.append('Nighbours ')
print(Invitation_everyone)
print(Invitation_everyone[0] + ',we would love to have you over dinner party.')
print(Invitation_everyone[1] + ',we would love to have you over dinner party.')
print(Invitation_everyone[2] + ',we would love to have you over dinner party.')


del Friends_forever[:]
print('Friends: ', Friends_forever)

Touring_world = ['America ', 'Equadour ', 'Turkey ', 'England ', 'Pakistan ']
print(Touring_world)

# Using sorted()

print(sorted(Touring_world))
print(Touring_world)

# Using sorted() reverse

print(sorted(Touring_world, reverse = True))
print(Touring_world)

# Using reverse()

Touring_world.reverse()
print(Touring_world)

# Using reverse() again to bring it back to its original form.

Touring_world.reverse()
print(Touring_world)

# Sorting the list by using .sort()

Touring_world.sort()
print(Touring_world)

# Sorting the list by using .sort() in reverse

Touring_world.sort(reverse = True)
print(Touring_world)


import bisect
def index(a, x):
    i = bisect.bisect_left(a, x)
    return i
    
x = [8,10,12,14]
print(index(x, 10))
print(index(x, 14))

import bisect
# Sample list
my_list1 = [10, 20, 30, 40, 50, 60, 70, 77, 89, 99]

print("Original List:")
print(my_list1)
sorted_list = []
for i in my_list1:
    position = bisect.bisect(sorted_list, i)
    bisect.insort(sorted_list, i)
print("Sorted List:")
print(sorted_list)

import queue
y = queue.LifoQueue()
#insert items at the head of the queue 
for x in range(9):
    y.put(str(x))
#remove items from the head of the queue 
while not y.empty():
    print(y.get(), end=" ")
print()