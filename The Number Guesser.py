import random,math #Taking Imports
initiation = input(" Play ? ",)
while initiation == "yes":
    count = 0 #Counting no: of guesses
    lower = int(input("Enter Lower limit:- ")) #Taking Lower Limit
    lower-=1
    upper = int(input("Enter Upper limit:- ")) #Taking Upper Limit
    upper+=1
    stopper = round(math.log(upper - lower + 1, 2))
    print("I have only",stopper," guesses")
    print(int(((upper-lower)/2)+lower),"?")
    count+=1
    reply=int(input("enter '1' if the number is too high, enter '2' if correct, enter '3'if the number is too low :- "))
    while reply != 2:
        if reply == 1:
            if (upper-lower)<4:
                upper = ((upper-lower)/3) + lower
                x = random.uniform((lower+2), (upper-2) + 1)
                count+=1
                print(int(x),"?")
                print("from rando")
                reply=int(input("enter '1' if the number is too high,enter '2' if correct, enter '3' if the number is too low :- "))
                if reply == 2:
                    pass
            else:
                upper = ((upper-lower)/2) + lower
                print(int(((upper-lower)/2)+lower),"?")
                count+=1
                reply=int(input("enter '1' if the number is too high,enter '2' if correct, enter '3' if the number is too low :- "))
        elif reply == 3:
            if (upper-lower)<4:
                lower = ((upper-lower)/3) + lower
                x = random.uniform((lower+2), (upper-2) + 1)
                count+=1
                print(int(x),"?")
                reply=int(input("enter '1' if the number is too high,enter '2' if correct, enter '3' if the number is too low :- "))
                if reply == 2:
                    pass
            else:
                lower = ((upper-lower)/2) + lower
                print(int(((upper-lower)/2)+lower),"?")
                count+=1
                reply=int(input("enter '1' if the number is too high,enter '2' if correct, enter '3' if the number is too low :- "))
        else:
            print("wrong input")
            break
    print("I did it in",count,"try")
    if stopper < count:
        print("I failed")
    initiation = input(" Play again ? ",)
print(" bye ")
