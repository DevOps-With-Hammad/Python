""""
class Family:

    def __init__(self,My_family, Father, Mother, Boy1, Boy2, Girl1, Girl2, Girl3):
        self.MyFamily = My_family
        self.Parents = [Father, Mother]
        self.Boys = [Boy1, Boy2]
        self.Girls = [Girl1, Girl2, Girl3]

    def __init__(self, My_Uncle_family, MyUncle, MyUncle_Wife, Uncle_Boy1, Uncle_Boy2, Uncle_Girl1, Uncle_Girl2, Uncle_Girl3):
        self.My_Uncle_Family = My_Uncle_family
        self.Uncle_Parents = [MyUncle, MyUncle_Wife]
        self.MyUncle_Boys = [Uncle_Boy1, Uncle_Boy2]
        self.MyUncle_Girls = [Uncle_Girl1, Uncle_Girl2, Uncle_Girl3]


Family_Head = Family ("ArabyFamily" )
Family_Parents = Family("Araby", "Salah")
Family_Boys = Family(["Alaa", "Sherif"])
Family_girls = Family(["ayat", "aya", "Yoya"])

print(f"Here is the family of {Family_Head}.\n"
      f" and the family Parents is {Family_Parents}.\n"
      f"and the family boys{Family_Boys} and girls{Family_girls}  ")

"""

class Family:
  def __init__(self, family_name, father, mother, boys=[], girls=[]):
    self.family_name = family_name
    self.parents = [father, mother]
    self.boys = boys
    self.girls = girls

    # Add methods to manage family members (optional)

# Create a Family object
araby_family = Family("ArabyFamily", "Araby", "Salah", ["Alaa", "Sherif"], ["Ayat", "Aya", "Yoya"])

# Print family information
print(f"The {araby_family.family_name} family:\n"
      f"  Parents: {araby_family.parents[0]} & {araby_family.parents[1]}\n"
      f"  Boys: {', '.join(araby_family.boys)}\n"
      f"  Girls: {', '.join(araby_family.boys)}")




