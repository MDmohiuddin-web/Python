age=int(input("Enter your age:",))
if age<7 or age>100:
                print("This is not a logical age")
elif age<18:
                print("You cannot drive")
elif age==18:
                print("We will think about it")
else:
                print("You can drive")