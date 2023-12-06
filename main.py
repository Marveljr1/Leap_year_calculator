print("Welcome to the Leap year Calculator")
print("Please enter any year below\n")
years = int(input())

if years %  4 == 0:
    if years % 100 == 0:
        if years % 400 == 0:
            print("This is a leap year")
        else: 
            print("This is not a leap year")
    else: 
        print("This is a leap year")    
else:
    print("This is not a leap year")