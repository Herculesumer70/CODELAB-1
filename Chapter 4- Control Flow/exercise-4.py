Alien_color = 'Green'
if Alien_color == 'Green':
    print('The player has earned five points.')

Alien_color = 'Red'
if Alien_color == 'Green':
    print('The player has earned five points.')


# the alien’s color is green

Alien_color = 'Green'
if Alien_color == 'Green':
    print('The player has earned five points.')

# alien’s color isn’t green

Alien_color = 'Red'
if Alien_color == 'Green':
    print('The player has earned five points.')
else: print("The player has 10 points.")

# Write one version of this program that runs the if block and another that runs the else block.

Alien_color = 'Green'
if Alien_color == 'Green':
    print('The player has earned five points.')
else: print("The player has 10 points.")

Alien_color = 'Yellow'
if Alien_color == 'Green':
    print('The player has earned five points.')
else: print("The player has 15 points.")

# Exercise 3: Alien Colors if elif else chain green color

Alien_color = 'Green'
if Alien_color == 'Green':
    print('The player has earned 5 points.')
elif Alien_color == 'Red':
    print('The player has earned 15 points.')
elif Alien_color == 'Yellow':
    print('The player has earned 10 points.')
else: print('The player has earned 0 points.')

# Red color

Alien_color = 'Red'
if Alien_color == 'Green':
    print('The player has earned 5 points.')
elif Alien_color == 'Red':
    print('The player has earned 15 points.')
elif Alien_color == 'Yellow':
    print('The player has earned 10 points.')
else: print('The player has earned 0 points.')

# Yellow color

Alien_color = 'Yellow'
if Alien_color == 'Green':
    print('The player has earned 5 points.')
elif Alien_color == 'Red':
    print('The player has earned 15 points.')
elif Alien_color == 'Yellow':
    print('The player has earned 10 points.')
else: print('The player has earned 0 points.')


#Exercise 4: Stages of Life

# Baby

Age_human = 1
if Age_human <= 2:
    #print("the person is a baby.")

    print("the person is a toddler.")
elif Age_human <= 13:
    print("the person is a kid.")
elif Age_human <= 20:
    print(" the person is a teenager.")
elif Age_human <= 65:
    print("the person is an adult.")
elif Age_human <= 110:
    print("the person is an elder.")
else: print("The person is dead.")

# Toddler

Age_human = 3
if Age_human <= 2:
    print("the person is a baby.")
elif Age_human <= 4:
    print("the person is a toddler.")
elif Age_human <= 13:
    print("the person is a kid.")
elif Age_human <= 20:
    print(" the person is a teenager.")
elif Age_human <= 65:
    print("the person is an adult.")
elif Age_human <= 110:
    print("the person is an elder.")
else: print("The person is dead.")

# Kid

Age_human = 9
if Age_human <= 2:
    print("the person is a baby.")
elif Age_human <= 4:
    print("the person is a toddler.")
elif Age_human <= 13:
    print("the person is a kid.")
elif Age_human <= 20:
    print(" the person is a teenager.")
elif Age_human <= 65:
    print("the person is an adult.")
elif Age_human <= 110:
    print("the person is an elder.")
else: print("The person is dead.")

# Teenager

Age_human = 16
if Age_human <= 2:
    print("the person is a baby.")
elif Age_human <= 4:
    print("the person is a toddler.")
elif Age_human <= 13:
    print("the person is a kid.")
elif Age_human <= 20:
    print("the person is a teenager.")
elif Age_human <= 65:
    print("the person is an adult.")
elif Age_human <= 110:
    print("the person is an elder.")
else: print("The person is dead.")

# Adult

Age_human = 30
if Age_human <= 2:
    print("the person is a baby.")
elif Age_human <= 4:
    print("the person is a toddler.")
elif Age_human <= 13:
    print("the person is a kid.")
elif Age_human <= 20:
    print(" the person is a teenager.")
elif Age_human <= 65:
    print("the person is an adult.")
elif Age_human <= 110:
    print("the person is an elder.")
else: print("The person is dead.")

# Elder

Age_human = 75
if Age_human <= 2:
    print("the person is a baby.")
elif Age_human <= 4:
    print("the person is a toddler.")
elif Age_human <= 13:
    print("the person is a kid.")
elif Age_human <= 20:
    print(" the person is a teenager.")
elif Age_human <= 65:
    print("the person is an adult.")
elif Age_human <= 110:
    print("the person is an elder.")
else: print("The person is dead.")


# Exercise 5: Favorite Fruit

favorite_fruit = ['Grapes', 'Gavaua', 'Orange']
if 'Strawberry' in Favorite_Fruit:
    print("You really like Grapes")
if 'banana' in Favorite_Fruit:
    print("You really like banana")
if 'Apple' in Favorite_Fruit:
    print("You really like Gavaua")
if 'grapes' in Favorite_Fruit:
    print("You really like grapes")
if 'Mango' in Favorite_Fruit:
    print("You really like Orange")

  number_code = 1000
if number_code > 50:
    # Calculate square
    print(number_code * number_code)
print('Next lines of code')

# program 1: Print first 10 natural numbers
i = 1
while i <= 5:
    print(i)
    i += 1

# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
print("Sum is: ", s)


n = 7
# stop: 11 (because range never include stop number in result)
# run loop 10 times
for i in range(1, 11, 1):
    # 2 *i (current number)
    product141 = n * i
    print(product141)


num_123 = 889901
count = 0
while num_123 != 0:
    # floor division
    # to reduce the last digit from number
    num_123 = num_123 // 10

    # increment counter by 1
    count = count + 1
print("Total digits are:", count)