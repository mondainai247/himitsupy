#Diffie Helman Handshake to generte shared secret

#sender_gen_A_Secret = Alice sends Bob A
#receiver_gen_B_Secret = Bob sends Alice B

# sender_gen_shared_secret



#1) generate A from Sender

def sender_gen_A_Secret(s,sender_pin, p):
    sender_secret = ((s**sender_pin)%p)
    return sender_secret
#2) Generate B from Receiver
def receiver_gen_B_Secret(s,rec_pin,p):
    receiver_secret = ((s**rec_pin)%p)
    return receiver_secret

# 3)  
def sender_gen_shared_secret(rec_secret,sender_pin,p):
    sender_shared_secret = ((rec_secret**sender_pin)%p)
    print(sender_shared_secret)
    return sender_shared_secret

def receiver_gen_shared_secret(sender_secret,rec_pin,p):
    receiver_shared_secret = (sender_secret**rec_pin)%p
    print(receiver_shared_secret)
    return (receiver_shared_secret)  


    
#s = (A**bob_rec_pin)%prime_num

#https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

#Alice and Bob agree on a large prime number, p, and a number, g, less than p.
#Alice chooses a secret number, a, and calculates A = g^a mod p.

#Bob chooses a secret number, b, and calculates B = g^b mod p.
#Alice and Bob exchange A and B.

#Alice calculates s = B^a mod p.
#Bob calculates s = A^b mod p.
#s is the shared secret.




