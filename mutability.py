a = []
b = a

# a and b are names, the value is the list
# have the same id, different names for same object
# references to the same object
print(id(a))
print(id(b))


a.append(35)

# will return same thing
print(a)
print(b)

# but if b had it's own empty list, they would be different objects and have different ids
# changing a list after creating is means list is mutable

# now ways to add or remove elements from tuples
# tuples are immutable

c = 345
d = 345

# unlike the two empty, lists these will have the same id
# won't recreate identical integer
# integers are immutable
# strings are immutable


h = "hello"
i = a

# these will be the same
print(id(h))
print(id(i))

# b will stay the same, change string a but not string "hello"
# changing the existing name, not the value
a += "world"
