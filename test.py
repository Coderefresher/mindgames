total_A = 0
total_B = 0
while total_A < 3 and total_B < 3:
    inputA = input("A's turn: ")
    inputB = input("B's turn: ")
    
    if inputA == "Rock" and inputB == "Scissors":
        print("Rock bet Scissors")
        total_A += 1
        
    elif inputA == "Scissors" and inputB == "Rock" :
        print("Rock bet Scissors")
        total_B += 1
        
if total_A  == 3:
    print("Congratulations!!! A is the winner")
    
if total_B == 3:
    print("Congratulations!!! B is the winner")
        