import cv2
import numpy as np
import glob
from tempfile import TemporaryFile
from cryptography.fernet import Fernet
import os 

dataset = TemporaryFile()
X_data = []
files = glob.glob ("*.jpg")
i=0
for myFile in files:
    i+=1
    image = cv2.imread (myFile,0)
    X_data.append (image)

npfile =np.array(X_data)

##key=Fernet.generate_key()
##file=open('password.key','wb')
##print(key)
##file.write(key)
##file.close()
##
##file = open('password.key', 'rb')
##key = file.read() 
##file.close()
##
##encoded=npfile.tobytes()
##f1 = Fernet(key)
##encrypted = f1.encrypt(encoded)
##file=open('encrypted_dataset.file','wb')
##file.write(encrypted)
##file.close()

###Password to be noted
##file = open('password.key', 'rb')
##Key = file.read() # The key will be type bytes
##file.close()

file=open('encrypted_segments.file','rb')
data=file.read()
file.close()
Key=b'DkuAr66qG_ZNbKRYLbsWJUhogHWQpodH8kXSZiHJDWY='
f = Fernet(Key)
decrypted = f.decrypt(data)

decoded = np.frombuffer(decrypted,dtype="uint8")#dtype has to be noted before
new_file=decoded.reshape((2, 300, 400,1))#shape has to be noted before

cv2.imshow("img1",new_file[1])


