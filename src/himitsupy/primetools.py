from random import randint 

def is_prime(n): 
    if n <= 1: 
        return False 
    if n == 2: 
        return True 
    if n % 2 == 0: 
        return False 
    for i in range(3, int(n**0.5)+1, 2): 
        if n % i == 0: 
            return False 
        return True 
        
def generate_prime(): 
    while True: 
        p = randint(1000000000,9000000000) 
        if is_prime(p): 
            return p