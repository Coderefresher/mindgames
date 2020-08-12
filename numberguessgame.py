# import random
# print("Lets play number guessing game")
# guess = random.randint(1,20)
# print("""You will be given 5 chances to guess.
#            ** Let me guess any number from 1 to 20.
#            ** Identify the number.
#            ** You guess , you win.
#            ** LET'S BEGIN!!! :)""" )
# 
# count = 0
# while count <=5 :
#     number = int(input("Guess any number: "))
#     if number == guess:
#         print("CONGRATULATIONS, YOU WON !!!")
#         break
#     if number < guess:
#         print(f"The number {number} is too low from the actual number")
#     if number > guess:
#         print("Your guess was too high: Guess a number lower than", number)
#     
#     count +=1
# 
# if count > 5:
#     print("Oops you loose, The actual number is", guess)

file = open("hey", "w")
print(file)
file.write("Something")
print(file.write("Some"))