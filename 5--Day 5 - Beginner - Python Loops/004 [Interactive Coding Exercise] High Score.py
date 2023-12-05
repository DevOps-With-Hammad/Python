# 004 [Interactive Coding Exercise] High Score
St_Scor = input("The students score is = \n").split()
for n in range(0, len(St_Scor)):
    St_Scor[n] = int(St_Scor[n])

# Second Step to find the max between the existing values.

Highest_score = 0
for score in St_Scor:
    if score > Highest_score:
        Highest_score = score
print(f"The Highest Scre in the class is: {Highest_score}")
