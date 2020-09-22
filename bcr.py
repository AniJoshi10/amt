"""
  Source - https://auth0.com/blog/hashing-in-action-understanding-bcrypt/
  $ pip3 install bcrypt

"""

import bcrypt

# Password in str
inp = input("Passwd")
# Password in Bytes
passwd = inp.encode()
# Random initial salt to be added to passwd rounds=15
salt = bcrypt.gensalt(15)

# Hashed value to be stored in Database
hashed = bcrypt.hashpw(passwd, salt)

# Check password with hashed value stored in Database
inp = input("Confirm")
inppasswd = inp.encode()

booleanval = bcrypt.checkpw(inppasswd, hashed)
print(booleanval)
