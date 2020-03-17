from hashlib import pbkdf2_hmac

SALT = b'sadasdh380cfqohihrvq'
ITERATIONS = 100

def hash(text):
	return str(pbkdf2_hmac('sha512', str(text).encode(), salt=SALT, iterations=ITERATIONS))[2:-1]