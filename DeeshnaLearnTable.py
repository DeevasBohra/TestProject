#This program will help Deeshna to learn Tables by heart :)
import random

i = 1
j=1
while i <= 10:
    num = random.randint(4,9 )
    num1 = random.randint(3,9 )
    print(str(num1) + "*" + str(num))
    tabquestions = input("Please enter your answer here: ")
    if int(tabquestions) == num1 * num:
        print("Contratulations! Your Point is ---Yayyy****  " + str(j) + "  ****")
        j = j + 1
    else:
        j = j - 1
        print("Incorrect ----**** " + str(j) + " ***** :( Negative Marks!!")
    i += 1
