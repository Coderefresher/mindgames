
    
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