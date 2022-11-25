bathspa= "Ras Al Khaimah"
print(bathspa)
bathspa= "python"
print(bathspa)

print('If you want to find the secrets of the universe, think in terms of energy, frequency and vibration."Nikola Tesla"')

name_id = "\tElon Musk\n"

print("Unmodified:")
print(name_id)

print("\nUsing lstrip():")
print(name_id.lstrip())

print("\nUsing rstrip():")
print(name_id.rstrip())

print("\nUsing strip():")
print(name_id.strip())

fav_num = 7
msg = f"My favorite number is {fav_num}."

print(msg)

total_cost = 'total usbs bought = '
total_pounds = 'total amount of pounds left = '
print(total_cost + str(int(50 / 6)))
print(total_pounds + str(50 % 6))

cars = "Toyota\nsupra!"
print(cars)

variables = "it is used to assign the value."

x = variables.capitalize()

print (x)

x = y = z = "r34"

print(x)
print(y)
print(z)


x = "is best"

def myfunc():
  print("Breaking bad " + x)

myfunc()


x = "best show"

def myfunc():
  global x
  x = "full comedy"

myfunc()

print("The office is " + x)