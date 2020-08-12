
    
def fibonacci(number):
    a = 1
    b = 1
    print(a)
    print(b)
    for i in range(2,number):
        
        c = a + b
        a = b
        b = c
        print(c)
fibonacci(5)

#How to use input function
def smaller_num(x,y):
    if x>y:
        number= y
    else:
        number= x
    return number

smaller_num(x= input("Enter first number:-") ,y= input("Enter second number:-"))