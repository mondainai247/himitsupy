# a digital hanko(TM) is an alphanumeric string of variable length, which makes it nearly impossible to duplicate the same two by randomness.
# for example, with 1000 charaters of varying length, the total possiblies of outputs are raised to the 1000th power, overkill.   
# hankotools module: includes the following functions 

# 1) generate_hanko
# 2) generate_hanko_password
# 3) encrypt_hanko
# 4) store_hanko
# 5) read_mojibake_hanko



# If you need hashes for Cosmos Network 
# https://docs.cosmos.network/master/basics/accounts.html
# This function will generate a digital hanko which is an alpha_numeric string of variable length. 
import random
import string
import os


random_length = random.randint(500, 1500)
random_long = random.randint(5000, 10000000000000000)
magic_num = random.randint(1, random_long)

hanko_password = ''

# need to adjus this so it uses the $HOME ~ or finalized application directory. 
hanko_file = os.path.expanduser("~/.himitsutanwa/hanko.txt")

def generate_hanko():
    digital_hanko = ''.join(random.choices(string.ascii_letters + string.digits, k=random_length))
    return digital_hanko
    print('New Hanko has been Generated')


from simplecrypt import encrypt, decrypt
from hashtools import hash256

#from hankotools import generate_hanko, generate_hanko_password, encrypt_hanko, store_hanko, read_mojibake_hanko

# On this one, we might want to add magic_number to prevent a hacker with key_tracker from accessing. they would need the hanko file. 
def generate_hanko_password(user_name, password):
    combined = str(user_name)  + str(password) 
    hanko_password = hash256(combined)
    return hanko_password
    print('Digital Hanko Password successfully Created')

def encrypt_hanko(hanko_password, digital_hanko):
    encrypted_hanko = encrypt(hanko_password, digital_hanko)
    return encrypted_hanko
    print('Digital Hanko Successfully Encrypted')

def store_hanko(encrypted_hanko):
    with open(hanko_file, "wb") as f:
        f.write(encrypted_hanko)
        f.close()

def read_mojibake_hanko(hanko_password, hanko_file):
    with open(hanko_file, "rb") as f:
        mojibake = f.read()
        decoded_hanko = decrypt(hanko_password, mojibake)
        my_hanko = decoded_hanko.decode()
        print("Your Digital Hanko:"  + my_hanko + "----END HANKO")
        return my_hanko



#ciphertext = encrypt('password', plaintext)
#plaintext = decrypt('password', ciphertext)

#def encrypt_string(your_key, some_words:
#    The_encrypted_words = encrypt(your_key, some_words)
#    return The_encrypted_words

#def decrypt_string(your_key, the_encrypted_words):
#    The_decrypted_words = decrypt(your_key, The_encrypted_words)
#    return The_decrypted_words


# Here is a walkthrough of the code that creates a digital hanko, a password for it
# then enrypts it to a file as bytes, then reads decodes and outputs to screen. 
#>>> user_name = 'user@gmail.com'
#>>> password = 'thisismypassword'
#>>> my_hanko = generate_hanko()
#>>> my_hanko_password = generate_hanko_password(user_name, password)
#>>> secret = encrypt_hanko(my_hanko_password, my_hanko)
#>>> store_hanko(secret)
#>>> read_mojibake_hanko(my_password, hanko_file)
#'5UUxxmxnry5L1YENfmLumUiYRmA8JViHnx2WZNDGtbxxOAnpMTD5ukJAqE8co19VDgjkenuvzrqpKe4CTMBSCjmYOldyKY6J518Ve6mWKkTqiD1YqUKgI5QgAlVtt2atQjg2ELi3qSgPaefKXG0bqC2Bb3ykySSSizgUcGNdH77czkqKMKVKim6mrWKGbIOlPTDpI5x0XBBjDbSwwViQ1vRgx79k6Ysu9O3sRXSeQ3O33beJxYrxBXHfA8AdSHkWQqtfwWRsreGnOGhb9dpy4VDbZlp7PwOev2cSMzTGBMAR0Sg1H1IUBvMKUYHFrO8cYXpchNxocT8BYktOQ2Ry4pod3B48xUSSZbgt5cQg74K5qdmpMADp6KAXQuP4j7nIXAnHFpAe9G7s6fV2hALpgKzapCEuUaBQ1rIXu2Xlfv71lu0JCzof1SFGduvGmWfyEa1IPwf145ZojeTtvEH2QpDBlRBLabmdnn9mVFzbSslaN8R2aPFVxuhCMfaY6I2AfKYfNqSVWEOur0IpS3C2704wR29NRa44i4YBkR14kgjBRcvwUTTeFP0z5M85ntUbOEEkzPGxKqivNH6sol0Q6Zs54trz4e4wpHdeiMY8tUSaH4FdBSiYlJ5kAini1ElXubKIQcTy0ZUhNCzgbueOCuFdzh7MZ1woasKM4QCkehzvfDtBos4CLdldFBNeXBTUiaHkZKk9aTxBR5swpKk4nKZtmU2Kk5wlTY6oT0gm355DU40fG5k0jeC1WvcaqP8XIm521Ld2FAt9n18szyESQoaUt'
