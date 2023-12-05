# Average Height Exercise.
# Don't change anything from the code below.
Stud_Higt = input(" please Enter the Students height separated by Comma.").split()
for n in range(0, len(Stud_Higt)):
    Stud_Higt[n] = int(Stud_Higt[n])
    print(Stud_Higt)
# here is how to calculate the number items in here.
print(len(Stud_Higt))
print(sum(Stud_Higt))
total_height = sum(Stud_Higt)
number_of_stud = len(Stud_Higt)

Total_avreage = round((total_height / number_of_stud))
print("the AverGe of the student  = \n" + str(Total_avreage))




