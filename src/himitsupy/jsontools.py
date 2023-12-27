#jsontools
import json
import os
from hashtools import hash256
from simplecrypt import encrypt, decrypt
import string
import random
import ipfshttpclient


json_file_path = os.path.expanduser('~/Desktop/App_Beta/data/encrypted_user_json.json')

def write_to_json(userinfo): 
    password = hash256(password)
    json_data = json.dumps(userinfo) 
    encrypted = encrypt(password,json_data) 
    with open(json_file_path,"wb") as file: 
        file.write(encrypted)
    print(f"Json Successfuly Encrypted: Located at {json_file_path}")
    
def save_json_upload_to_ipfs(a, b, c): 
    json_data = json.dump({'Receiver': a, 'Subject': b, 'Message_Body': c}) 
    randfilename = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    file_to_send =  os.path.expanduser('~/Desktop/App_Beta/data/'+ randfilename +'.json')
    print(json_data)
    with open(file_to_send,"w") as file: 
        file.write(json_data)
    client = ipfshttpclient.connect() 
# Connects to: /dns/localhost/tcp/5001/http 
    res = client.add(file_to_send) 
    print(res)
    CID = res['Hash']
    return CID     
    print(f"Json Successfuly saved: Located at {file_to_send}")
    



def read_and_decrypt_json(password): 
    with open(json_file_path, 'rb') as f:
    # Load the json file by reading the bytes from the open file
        data = f.read()
        password = hash256(password)
    # Decrypt the data
        decrypted_data = decrypt(password, data)
    # Load the decrypted data as a json object
        decrypted_data = json.loads(decrypted_data.decode('utf8'))
    # Extract the desired data
        a = decrypted_data['a']
        b = decrypted_data['b']
        c = decrypted_data['c']
        return a, b, c



