password = input("Enter any strong password to maintain account securely: ")
def password_genertor(password):
    l , u, d , s = 0, 0, 0, 0
    
    if len(password) > 8:
        for i in password:
            if i.isupper():
                u +=1
            elif i.islower():
                l +=1
            elif i.isdigit():
                d +=1
            elif i == "@" or i == "&":
                s +=1
                
        if u > 1 and l > 1 and d > 1 and s > 1 and len(u + l + d + s)>=8:
            print("The password generated is strong")
        else:
            print("Please make the password stronger to prevent breaching")
password_genertor(password)
            
        
        
    
