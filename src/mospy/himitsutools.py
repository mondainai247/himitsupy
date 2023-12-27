#himitsutools
import os

from simplecrypt import encrypt, decrypt

file_name = os.path.expanduser('~/Desktop/App_Beta/data/user.bin')



 
#NOT WORKING
def gen_user_doc(user, address):
    user_info = str(user) + str(address)
    encryped_user_info = encrypt(user,user_info)
    print(encryped_user_info)
    with open(file_name, "wb") as f:
        f.write(encryped_user_info)
        print("Encrpted User Info suceesfully stored at: "+ file_name)



def read_user_doc(file_name, user):
    with open(file_name, "rb") as f:
        mojibake_stuff = f.read()
        print(mojibake_stuff)
        decrypted_user_doc = decrypt(user, mojibake_stuff)
        print(decrypted_user_doc.decode())
        return decrypted_user_doc.decode()
