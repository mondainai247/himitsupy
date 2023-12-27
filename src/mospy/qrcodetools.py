import qrcode
import json
import os
import glob
import cv2
import pandas as pd
import pathlib
from pyqrcode import QRCode
from PIL import Image 
from randomtools import generate_random_pin
from hashtools import hash256, hash512
from simplecrypt import encrypt, decrypt
from ipfstools import upload_to_ipfs

file_path = ''

some_text = ''
text = 'lots of text'
the_file_path = 'your_himitsu_qrcod.png'



#def gen_qrcode(a,b,c,d):
 #   data = {'address': a, 's': b, 'p': c, 'sender_A_num': d}
  #  img = qrcode.make(json.dumps(data))
   # type(img)  # qrcode.image.pil.PilImage
    #img.save(os.path.expanduser('~/Desktop/my_qr_code.png'))
    


def gen_himitsu_qr_code(a, b, c, d, e):
    data = {'sender_name':a,'qr_code_sender_address': b, 's': c,
            'p': d, 'qr_code_sender_A_num': e}
    img = qrcode.make(json.dumps(data))
    img.save('your_himitsu_qr_code.png')
   


#def read_qrcode(file_path):
#    img = qrcode.QRCode(file_path)
    
#    try:
        
#        return img.data
#    except ValueError:
#        return None


#def read_qr_code(filename):
    """Read an image and read the QR code.
    
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """
    
 #   try:
#        img = cv2.imread(filename)
 #       detect = cv2.QRCodeDetector()
  #    value, points, straight_qrcode = detect.detectAndDecode(img)
  #      print(value)
   #     return value
  #  except:
   #     return  None      


#def read_qr_code(qr_code_image):
    # Decode the QR code
#    d = cv2.QRCodeDetector()
 #   val, points, straight_qrcode = d.detectAndDecode(cv2.imread(qr_code_image))
  #  print(val)
   # return val


def read_qr_code(qr_code_image):
    # Decode the QR code
    d = cv2.QRCodeDetector()
    dir_path = os.path.dirname(os.path.abspath(__file__))
    val, points, straight_qrcode = d.detectAndDecode(cv2.imread(os.path.join(dir_path, qr_code_image)))
    print(val)
    print(type(val))
    return val



#def add_tomodachi_from_qr_code(qr_code_image):
    # Decode the QR code
 #   d = cv2.QRCodeDetector()
  #  dir_path = os.path.dirname(os.path.abspath(__file__))
   # val, points, straight_qrcode = d.detectAndDecode(cv2.imread(os.path.join(dir_path, qr_code_image)))
  #  qr_code_sender_address = json.loads(val)['qr_code_sender_address']
  #  s = json.loads(val)['s']
  #  p = json.loads(val)['p']
  #  qr_code_sender_A_num = json.loads(val)['qr_code_sender_A_num']
  #  return qr_code_sender_address,s,p, qr_code_sender_A_num
def add_tomodachi_from_qr_code(qr_code_image):
    # Decode the QR code
    d = cv2.QRCodeDetector()
    dir_path = os.path.dirname(os.path.abspath(__file__))
    val, points, straight_qrcode = d.detectAndDecode(
        cv2.imread(os.path.join(dir_path, qr_code_image)))
    #load QR Code Values into variables
    tomodachi_name = json.loads(val)['sender_name']    
    qr_code_sender_address = json.loads(val)['qr_code_sender_address']
    s = json.loads(val)['s']
    p = json.loads(val)['p']
    qr_code_sender_A_num = json.loads(val)['qr_code_sender_A_num']
    
    #WE open our himitsu_bango file to extract the user_pin so we can do DiffieH math
    with open ('himitsu_bango.json', 'rb') as f:
            themojibake = f.read()
            from getmac import get_mac_address as gma
            a_gma_string = gma()
            magic_num = '777'
            first_time_password = hash512(a_gma_string+magic_num)
            user_info = decrypt(first_time_password, themojibake)
            user_info = user_info.decode()
            user_info = json.loads(user_info)
            print(user_info)
            f.close()
        
    your_pin =  user_info["sender pin"]

    receiver_secret = ((s**your_pin) % p)
    receiver_shared_secret = (qr_code_sender_A_num**your_pin) % p
    hashed_shared_secret = hash256(str(receiver_shared_secret))
    checksum_shared_secret = hash512(str(receiver_shared_secret))
    
    with open('my_username.json', 'r' ) as f:
        
        my_info = json.load(f)
        user_name = my_info["user_name"]

    the_data = {'receiver_user_name': user_name, 'receiver_secret': receiver_secret, 'receiver_shared_secret':receiver_shared_secret, 'hashed_shared_secret': hashed_shared_secret,
                'checksum_shared_secret': checksum_shared_secret}
    
    
    
    with open('friends.json', 'w') as f:
        friends = {}
        friends[f'{tomodachi_name}'] = [qr_code_sender_address, hashed_shared_secret]
        print(friends)
        json.dump(friends, f)
        f.close() 
           
    jason_data_to_write = json.dumps(the_data)
    with open('tomodachi.json', 'w') as yourjasonfile:
        yourjasonfile.write(jason_data_to_write)
        yourjasonfile.close()

    
    hashed_qr_code_sender_address = hash512(qr_code_sender_address)
    
    the_data_string = json.dumps(the_data)
    print("QR_CODE_Sender address is:  "+qr_code_sender_address)
    the_encrypted_data = encrypt(qr_code_sender_address, the_data_string)

    with open('encrypted_tomodachi.json', 'wb') as yourjasonfile:
        yourjasonfile.write(the_encrypted_data)
        yourjasonfile.close()
    
    encrypted_json_file = 'encrypted_tomodachi.json'
    
    upload_to_ipfs(encrypted_json_file)
    print(qr_code_sender_address, s, p, qr_code_sender_A_num,
          receiver_secret, receiver_shared_secret, hashed_shared_secret)
    print('if any of these values are 0 then there is a problem with the rec_num varaible in qrcodetools at the top')      
    print(hashed_qr_code_sender_address)
    return qr_code_sender_address, s, p, qr_code_sender_A_num, receiver_secret, receiver_shared_secret, hashed_shared_secret
#def upload_qrcode()

#window = Window('QR code reader').Layout(layout)

#button, values = window.Read()

#qrcode = values[0]

#data = qrcode.decode()

#print(data)    