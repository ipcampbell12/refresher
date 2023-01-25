from operator import itemgetter


def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [

    {"name": "Your Mom", "age": 24},
    {"name": "Bubba Thumpa", "age": 30},
    {"name": "Hinga Binga", "age": 47},
]


def get_friend_name(friend):
    return friend["name"]

# can include argument name or not, either is okay


# 1 NAMED FUNCTION
print(search(friends, "Bubba Thumpa", finder=get_friend_name))

# 2 LAMBDA FUNCTION
# You can also use lambda function
print(search(friends, "Bubba Thumpa", finder=lambda x: x["name"]))


# 3 BUILT IN ITEMGETTER FUNCTION
print(search(friends, "Bubba Thumpa", itemgetter("name")))
