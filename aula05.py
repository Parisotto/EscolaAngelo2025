v1 = "dia"
v2 = "noite"
v3 = "dia"

print(v1 == "dia" and v2 == "noite")
print(v1 == v3 and v1 == v2)

print(v1 != v2 or v1 == v2)
print(v1 == v2 or v1 != v3)

print(not v1 == v3)
print(not v1 != v3)

