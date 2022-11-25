def display_message1():
    """Display a message about what I'm learning."""
    msg = "what is print is used for"
    print(msg)

display_message1()

def favorite_book1(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")

favorite_book1('Hercules')


def make_shirt1(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt1('medium', 'I love Python!')
make_shirt1(message="Readability counts.", size='small')

def make_shirt(size='extra large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='small')
make_shirt('medium', 'programmers are loopy.')


def describe_city(city, country='america'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('texas')
describe_city('illinois', '')
describe_city('michigan')

def max_of_two( a, b ):
    if a > b:
        return a
    return b
def max_of_three( a, b, z ):
    return max_of_two( a, max_of_two( b, z ) )
print(max_of_three(100, 7, -19))


def string_reverse(str2):
    
    rstr1 = ''
    index = len(str2)
    while index > 0:
        rstr1 += str2[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('Patrick Bateman'))

def is_odd_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_odd_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# demo is the function name
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ayaz", 18)


# function with default argument
def show1_employee(name, salary=2000):
    print("Name:", name, "salary:", salary)

show1_employee("Umer", 4000)
show1_employee("Abdullah")