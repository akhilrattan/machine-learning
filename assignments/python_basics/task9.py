t = (10, 20, 30, 20)

print("Tuple:", t)
print("First Element:", t[0])

print("Count of 20 =", t.count(20))
print("Length =", len(t))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.add(10)
set1.remove(2)
print("Union =", set1.union(set2))
print("Intersection =", set1.intersection(set2))
print("Difference =", set1.difference(set2))
