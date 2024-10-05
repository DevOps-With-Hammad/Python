#007 [Interactive Coding Exercise] Treasure Map
row1 = ["   ", "   ", "   "]
row2 = ["   ", "   ", "   "]
row3 = ["   ", "   ", "   "]

map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}")

position = input("Please Enter you position here ")
horizontal = int(position[1])
vertical = int(position[0])

selected_row = map[vertical-1]
selected_row[horizontal-1] = "👽"

print(f"{row1}\n{row2}\n{row3}")

