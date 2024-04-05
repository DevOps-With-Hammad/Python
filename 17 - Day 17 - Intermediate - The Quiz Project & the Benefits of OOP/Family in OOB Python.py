# Class
import self


class Family:
    def __init__(self, F_name, Father, Mother, Boys=[], Girls=[] ):
        self.Family_name = F_name
        self.Family_Parent = [Father, Mother]
        self.Family_Boys = Boys
        self.Family_Girls = Girls

# Adding method to manage Family Members .

# Create Family Object
My_Family_Name = Family("Elaraby Family ", "Abdo", "Naglaa",
                        ["Hazem", "Zeyad", "Zezo"],
                        ["Basmalah", "Semsema", "Samsemo", "Semsems"])
# Print out the output
print(f"The {My_Family_Name.Family_name}\n"
      f"Parent {My_Family_Name.Family_Parent[0]} & {My_Family_Name.Family_Parent[1] }\n"
      f" Boys are {', '.join(My_Family_Name.Family_Boys)}\n"
      f" Girls are {', ' .join(My_Family_Name.Family_Girls)}")