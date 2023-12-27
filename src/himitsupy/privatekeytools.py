#privatekeytools
import secrets

#def generate_private_key():
#    bits = secrets.randbits(256)
##    bits_hex = hex(bits)
 ##   private_key = bits_hex[:2]
  #  return private_key



def gen_private_key():
    # Generate 32 random bytes
    private_key_bytes = secrets.token_bytes(32)

    # Convert bytes to hexadecimal
    

    return private_key_bytes






#int = 10
# bin(int)
# hex(int)
#bytearray(int)
