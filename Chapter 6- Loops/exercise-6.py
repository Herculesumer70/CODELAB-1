Choose_1topping = "\nWhat topping would you like?"
Choose_1topping += "\nEnter 'quit' if you are done: "

while True:
    topping_2 = input(Choose_1topping)
    if topping_2 != 'quit':
        print("  I'll add " + topping_2 + " to your pizza.")
    else:
        break

ticket_agent1 = 'What is your age?'
ticket_agent1 += "\nEnter 'quit' when you are finished. "

while True:
    age_person = input(ticket_agent1)
    if age_person == 'quit':
        break
    age_person = int(age_person)

    if age_person < 3:
        print(" the ticket is free.")
    elif age_person < 13:
        print(" the ticket is $10.")
    else:
        print(" the ticket is $15.")

age_person = int(input('Enter the age = '))
while True:
    if age_person == 18:
        print("you can apply for license")

sandwich_orders1 = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches1= []

while sandwich_orders1:
    current_sandwich2 = sandwich_orders1.pop()
    print("I'm working on your " + current_sandwich3 + " sandwich.")
    finished_sandwiches1.append(current_sandwich3)

print("\n")
for sandwich in finished_sandwiches1:
    print("I made a " + sandwich + " sandwich.")

sandwich_orders1 = ['chicken', 'pastrami', 'egg', 'pastrami', 'seafood', 'pastrami', 'nutella']
finished_sandwiches1 = []
print("I apologize we're completely out of pastrami today.")
while 'pastrami' in sandwich_orders2:
    sandwich_orders2.remove('pastrami')

print("\n")
while sandwich_orders1:
    current_sandwich3 = sandwich_orders1.pop()
    print("I'm working on your " + current_sandwich3 + " sandwich.")
    finished_sandwiches1.append(current_sandwich3)

print("\n")
for sandwich in finished_sandwiches1:
    print("I made a " + sandwich + " sandwich.")

cars = ["supra", "r35", "nissan gtr"]
for x in cars:
  print(x) 


countries = ["nehtherland", "mexico", "pakistan"]
for x in countries:
  if x == "mexico":
    continue
  print(x) 


n = 100
k = 100
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()

listone = [30, 60, 90, 120, 150]
# reverse list
new_list = reversed(listone)
# iterate reversed list
for item in new_list:
    print(item)

my_list22 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list22[1::2]:
    print(i, end=" ")

    