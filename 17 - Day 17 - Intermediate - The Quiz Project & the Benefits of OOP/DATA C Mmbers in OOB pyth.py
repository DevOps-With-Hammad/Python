# Let's declare our class using our current data
class DATAC :
    def __init__(self, Co_Founders=[], Companies=[] , D_C_Employees=[], Mc_Employyees=[]):
        self.Heads = Co_Founders
        self.Companiess = Companies
        self.DCEMPS = D_C_Employees
        self.MCEMPS = Mc_Employyees

DATAC_Comapny= DATAC (["Hassan", "Abeed"] ,
                      ["DATA C ", "Macrocare"] ,
                      ["Hammad ", "Abraam ", "Awwad", "Ragad"] ,
                      ["faten ", "Heba" , "Haleem " , "Abeed"])

print(f" Here is the CO_founder of  {DATAC_Comapny.Companiess[0]}, MR :  {DATAC_Comapny.Heads[0]}\n"
       f"The {DATAC_Comapny.Companiess[0]} Includes EEmployees Like {', '.join(DATAC_Comapny.DCEMPS)}\n "
      f" Here is  The CO_Founder of {DATAC_Comapny.Companiess[1]}, Mr : {DATAC_Comapny.Heads[1]}\n"
      f"The {DATAC_Comapny.Companiess[1]} Includes EEmployees Like {', '.join(DATAC_Comapny.MCEMPS)}\n "

      )
