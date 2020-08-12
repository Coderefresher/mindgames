import random
import string
lists = ["Apple", "Mango", "Jack fruit", "Strawberry", "Pineapple"]

guess = random.choice(lists)

count = 0

while count < 5:
    fruit = input("Enter any fruit: ")
    if fruit == guess:
        print("Congratulations !!! You won")
        break
    
    if count == 4:
        print("This is the second clue:")
        if guess[0] == "A":
            print("""This is something that grows on a tree
                    It is a fruit that is green or red
                    It’s said gravity was discovered
                    When one of these fell on Newton’s head""")
             
        if guess[0] == "M":
            print(""" I am a tropical fruit. I am
                    many colours from outside.
                    To say my name, say the opposite of WOMAN and
                    then say the opposite of STOP. Who am I?""")
             
        if guess[0] == "J":
            print("""I/ am a fruit that’s red
                    That’s often used in a smoothie
                    I’m bought in a punnet
                    And made into jam and jelly""")
             
        if guess[0] == "P":
            print("""This fruit is made of two words conjoined
                    The first part of it is also a tree
                    The second part is a different fruit
                    And goes on a pizza from Hawaii""")
         
        
    count +=1

if count > 5:
    
    print("You loose,  The fruit is ", guess)