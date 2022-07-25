
# FUNCTIONS IN PYTHON
def hello():
    print("Hello")


def user_age_in_seconds():
    user_age = int(input("What is your age?"))
    age_seconds = user_age * 365 * 24 * 60*60
    print(age_seconds)


# run the function
# user_age_in_seconds()
# DESTRUCTURING VARIABLES
# brackets are not necessary for a tuple


""" head, *tail = [1, 2, 3, 4, 5]
print(head, tail)

person = ("Bob", 65, "Mechanic")
# underscore is used for when you dont' want to use a variable


# each tuple has to have equal number of values
people = [("Bob", 65, "Mechanic"),
          ("James", 56, "Artist"),
          ("Harry", 32, "Pumper")]

# will iterate through elements of each tuple
for name, age, profession in people:
    print(f"{name} is {age} years old and works as a {profession}") """

# can also use indeces

# assign x to 5 and y to 11
x, y = 5, 11

"""
student_attendance = {"Bob": 100, "James": 40, "Hannity": 95}

# returns list of tuples with keys and pairs
print(list(student_attendance.items()))

# t will refer to both key and values
for t in student_attendance.items():
    print(t)
 """
""" student_attendance = {"Bob": 100, "James": 40, "Hannity": 95}

# return students whose attendance is better than 95 percent
for student, attendance in student_attendance.items():
    if student_attendance[student] > 97:
        print(student)

print(student_attendance["Bob"])
attendance_values = student_attendance.values()
print(sum(attendance_values)/len(attendance_values))

# return average of attendance
# use in keywrod

if "Bob" in student_attendance:
    print(f'Bob:{student_attendance["Bob"]}')
else:
    print("Bob is not a student in this class")
# list of dictionaries

friends = [
    {"Name": "Rolf", "Age": 39},
    {"Name": "James", "Age": 25},
    {"Name": "Jennifer", "Age": 69},
    {"Name": "Jose", "Age": 56},
] """

# print(friends[0]["Name"])

# dictionaries
friend_ages = {'Rolf': 24, 'Jen': 89, 'Blair': 39}

# access item from dictionary
# print(friend_ages['Blair'])

# change a dictionary value
friend_ages['Blair'] = 40
# print(friend_ages['Blair'])


# list comprehension
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

# create list of names that start with an s
starts_s = [name for name in friends if name[0] == 'S']
# print(starts_s)


# alternative using .startswith() string method
starts_S = [name for name in friends if name.startswith('S')]
# print(starts_S)

# these lists have the same contents, but they are not the same list.
# They are stored in a different place in memory, different objects
# Check with id ()

# will return different ids i.e. memory address
# print('starts_s: ', id(starts_s), "starts_S: ", id(starts_S))


# create new lists on the fly from existing lists

numbers = [1, 3, 5]

# put a doubled number for every number in the numbers list
double = [num*2 for num in numbers]
# print(double)

# first item of list comprehension is what you want to do to each element


# LOOPS IN PYTHON


# Find average grade

""" grades = [35, 67, 98, 100, 100]

total = 0

for grade in grades:
    total += grade

print(total/len(grades))

# other option
print(sum(grades)/len(grades)) """

""" friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(friend)

for friend in range(4):
    print("your mom") """


# MAGIC NUMBER APP


# anython other than lower case will cause the progrma to continue

""" number = 7
# similar to sql in statement
# allows you to handle upper case input
# but better to use .lower()
while True:
    user_input = input("Would you like to play? (Y,n)")

    if user_input == "n":
        break

    user_number = int(input("Guess the number: "))
    if user_number == number:
        print(f"You guessed {user_number}. That's correct!")
    # check if user was one away using tuple
    # also could do abs(number - user_number)==1
    elif number - user_number in (1, -1):
        print("You were off by 1")
    else:
        print(f"You guessed {user_number}. That's not even close.")

print("Hope you enjoyed the game you sack of crud") """

# IF STATEMENTS WITH IN KEYWORDS
""" movies_watched = {"The Matrix", "Green Book", "Hez"}

user_movie = input("What's a movie you've seen recently? ")

if user_movie in movies_watched:
    print(f"Oh wow! I've watched {user_movie} as well!")
else:
    print(f"I haven't watched that yet.") """


# IN KEYWORD
# checks for membership

friends = ["Rolf", "Bob", "Jen"]

# print("Jen" in friends)

# set of movies
movies_watched = {"The Matrix", "Green Book", "Hez"}

# user_movie = input("What's a movie you've seen recently? ")

# print(user_movie in movies_watched)

# check for substrings

my_string = "Yo momma so fat"

# print("o" in my_string)

# IF STATEMENTS
""" day_of_week = input("What day of the week is it today?").lower()

if day_of_week == "monday":
    print("Your are right! Today is Monday!")
else:
    print(f"You fool! Today isn't {day_of_week}") """


# BOOLEANS
# use comparisons

# boolean comparison
""" print(5 == 5)
print(5 > 5)
print(10 != 10) """

# can also be used on other values
# can also use is, not

friends = ["Bob", "Joseph"]
abroad = ["Bob", "Joseph"]
# print(friends == abroad)

# friends is abroad won't work
# each lists has its own are in memory, these are different list objects, even though the elements are the same


# set operations
friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Robe', 'Anne'}
other_friends = {"your mom", "Chewey"}

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

# Calcualte difference  between two sets
local_friends = friends.difference(abroad)
# print(abroad)

# Unites two sets, giving total of both
abroad_other = abroad.union(other_friends)
# print(abroad_other)

# find which elements are held in common by both sets
both = art.intersection(science)
# print(both)

# LISTS,TUPLES AND SETS

# keeps order
my_list = ['Bob', 'Rolf', 'Anne']

# can't modify a tuple
# keeps order
my_tuple = ("Rob", "Rolf", "Anne")

# can modify sets, but not duplicates
# does not keep order
my_set = {"Bob", "Rolf", "Anne"}


# print(my_list[0])

""" # GETTING USER INPUT
# name = input("Enter your name: ")
# print(name)
# input function always returns string

# size_input = input("How big is your feet in square feet?")
# square_feet = int(size_input)
# square_meters = square_feet/10.8
# print(
#  f"{square_meters:.2f} square_meters is equal to {square_feet} square feet")
# .2f indicates number of digits


# format function
# can reuse template with multiple values
# name="Bob"
# greeting="Hello,{}"
# with_name=greeting.format(name)

# print(with_name)


# can create longer templates

# longer_phrase='Hello,{}. Today is {}'
# formatted=longer_phrase.format("Rolf", "Monday")
# print(formatted)

# F-string
# name='Bob'
# greeting=f'Hello,{name}'


# print(greeting)

# or
# name='Rolf'
# print(f"Hello,{name}")

# LAMBDA FUNCTIONS


def add(x, y):
    return x + y


# print(add(5, 7))


# rewrite as lambda function
def add(x, y): return x+y


# print(add)
# assign lambda function variable
# meant to be short functions, often without name

# or like this:
(lambda x, y: x+y)(5, 7)

# can also use in conjunction with map function


def double(x):
    return x*2


sequence = [1, 3, 5, 7, 9]

# applies double function on each element of sequence
doubled = map(double, sequence)

# or as list comprehension
doubled = [double(x) for x in sequence]

# as lambda function
doubled = [(lambda x: x*2)(x)for x in sequence]
doubled = list(map(lambda x: x*2, sequence))
 """
