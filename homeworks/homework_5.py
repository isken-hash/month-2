from homeworks.distance import Distance

a = Distance(120, "см")
b = Distance(1, "м")
c = Distance(0.003, "км")

print(a)
print(b)
print(c)

print(a + b)
print(c - b)
print(a - Distance(20, "см"))
