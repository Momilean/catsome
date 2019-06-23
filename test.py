# -*- coding: UTF-8 -*-

#from werkzeug.security import generate_password_hash
#print(generate_password_hash('123456'))

from werkzeug.security import check_password_hash
pwhash = 'pbkdf2:sha256:50000$fbN3LY8V$6ca9893c346f52564db96856e5c5190216b2fd8031de4031fba047640d0c8f88'
print(check_password_hash(pwhash,'123456'))