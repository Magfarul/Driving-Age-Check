def headings():
    print("Check if you are fit to drive")
    print("\nPlease Enter Your Age\n")
def main():
    number= input()
    age = number

    while True:
        try:
            age = (int(number))
            while  age <5 or age>100 :
               age= int(input("\nPlease enter your correct age\n"))

            if 60 > age > 18:
               print("\nYou Can Drive The Car")
               break
            elif age == 18:
               print("\nCome Physically, We can't decide by your age.")
               break
            elif age < 18 or age > 60:
               print("\nYou Can't Drive Car")
               break

        except ValueError:
            print("You have Entered "+ str(age)+ " which is not age" "\nPlease Enter Your Correct Age")
            main()



    restart=input("\nDo you want to try again\n""Type Yes for run the program\n").capitalize()
    if restart=="Yes".capitalize():
        headings()
        main()

    else:
        exit()

headings()
main()
