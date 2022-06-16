passes = ["204d47e88780cbd6690327b367264903",
    "2389ec754b3ccf9dbfd9766ce4d764b7", 
    "89ef9f02ea3d2a35f0f3665e9904a258", 
    "a4a7e568c8bd7e4c85cfd6df60267bc4", 
    "fc4180d298c4caa3f3860d9cb94c2fcf"]
import hashlib
import itertools

alphabet = '0123456789'

for c in itertools.product(alphabet, repeat=4):
    password= "FLAG-HQNT-" + ''.join(c)
    hashy = hashlib.md5(password.encode('utf-8')).hexdigest()
    if hashy in passes:
        print (password + " : " + hashy)

