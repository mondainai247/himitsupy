#ipfstools

import ipfshttpclient 
from simplecrypt import decrypt


def upload_to_ipfs(file_to_upload): 
    client = ipfshttpclient.connect() 
# Connects to: /dns/localhost/tcp/5001/http 
    res = client.add(file_to_upload) 
    print(res)
    CID = res['Hash']
    print(CID)
    return CID 

# {‘Hash’: ‘QmN…’, ‘Name’: ‘my-file.txt’}


import ipfshttpclient 




def download_from_ipfs(file_to_download): 
    client = ipfshttpclient.connect() 

# Connects to: /dns/localhost/tcp/5001/http 

    new_file = client.get(file_to_download)
    return new_file

def download_and_decrypt_message(your_ipfs_cid, shared_key):
    # Download the message from IPFS using the CID
    client = ipfshttpclient.connect()       
    your_new_file = client.cat(str(your_ipfs_cid))

    
        #decrypt the tomodachi data from IPFS
    your_decrypted_message = decrypt(shared_key, your_new_file)
    # Decrypt the message using the shared key
    # ...

    # Return the decrypted message
    return your_decrypted_message
