import random;
import secrets;

class Die:
    """A simple class"""
    def __init__(maxVal):
        maxVal = maxVal
    def Roll(maxVal):
        return(random.randint(1,maxVal))



class Roll:
    while True:        
        d6Count = input("How many D6s?>> (C to close) ")
        if str(d6Count) == "C" or d6Count=="c":
            break
        i = 0
        print("The d4 roll is: " + str(Die.Roll(4)))

        while i < int(d6Count):
            d6 = Die.Roll(6)
            random.seed(random.randrange(1000)+i)
            print("The roll for "+ str(i+1) + "d6 " "is " + str(d6))
            i += 1
        print("The d8 roll is "+str(Die.Roll(8)))

        print("The d10 roll is "+str(Die.Roll(10)))

        print("The d10% rolls gave "+str(Die.Roll(10))+str(Die.Roll(10))+"%")

        print("The d12 roll is "+str(Die.Roll(12)))

        print("The d20 roll is "+str(Die.Roll(20)))
