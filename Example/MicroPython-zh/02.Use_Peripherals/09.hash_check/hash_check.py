import hashlib
import binascii
# There must be a boot.py file
file_name = "boot.py"
with open(file_name, 'rb') as fp:
    data = fp.read()
    print(data)
    file_hash = hashlib.sha256(data)
    file_hexlify = binascii.hexlify(file_hash.digest())
    print(file_hexlify)
