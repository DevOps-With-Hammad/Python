# 19. Dictionaries

point={"x": 1, "y": 2}
print(point)
point = dict(x= 1, y =2, z=3)
point["X"] = 10
print(point)
if "X" in point:
    print(point["X"])

print(point.get("x", 0))

for key in point:
    print("Key >>", key, "Value >>", point[key])

