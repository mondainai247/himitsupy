# hash256
# generate_private_key


import hashlib
from hashlib import sha256, sha512
from weakref import WeakValueDictionary


#from Crypto.Hash import keccak

#def kash256(word):
#    k = keccak.new(digest_bits=256)
#    k.update(b'f' + f'{word}'.encode('utf-8'))
##    kash_me = k.hexdigest()
#   return kash_me


import base58

#def cash58(word):
 #   encoded_word = word.encode()
  #  priv = hashlib.sha256(encoded_word).digest()
   # cos_key = (base58.b58encode(priv))
    #cosmos_key = cos_key.decode()
    #cut_key = cos_key[6:]
    #himitsu_address = "himitsu" + cut_key
    #return himitsu_address



def hash256(word):
    a = word.encode()
    b = hashlib.sha256(a)
    c = b.hexdigest() 
    return c

def hash512(word):
    a = word.encode()
    b = hashlib.sha512(a)
    c = b.hexdigest() 
    return c


    

#Now Lets make a public key


import hashlib

import ecdsa
import hdwallets
import bech32
from mnemonic import Mnemonic
from sha3 import keccak_256
import binascii


def seed_to_private_key(seed, derivation_path, passphrase: str = ""):
    seed_bytes = Mnemonic.to_seed(seed, passphrase=passphrase)
    hd_wallet = hdwallets.BIP32.from_seed(seed_bytes)
    # This can raise a `hdwallets.BIP32DerivationError` (which we alias so
    # that the same exception type is also in the `cosmospy` namespace).
    derived_privkey = hd_wallet.get_privkey_from_path(derivation_path)

    return derived_privkey


def privkey_to_pubkey(privkey: bytes, raw: bool = False) -> bytes:
    privkey_obj = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    pubkey_obj = privkey_obj.get_verifying_key()
    return pubkey_obj.to_string("raw") if raw else pubkey_obj.to_string("compressed")




from Crypto.Hash import RIPEMD
import hashlib



def pubkey_to_address(pubkey: bytes, *, hrp: str) -> str:
    s = hashlib.sha256(pubkey).digest()
    r = RIPEMD.new(s).digest()
    five_bit_r = bech32.convertbits(r, 8, 5)
    assert five_bit_r is not None, "Unsuccessful bech32.convertbits call"
    return bech32.bech32_encode(hrp, five_bit_r)



def privkey_to_address(privkey: bytes, *, hrp: str) -> str:
    pubkey = privkey_to_pubkey(privkey)
    return pubkey_to_address(pubkey, hrp='himitsu')
