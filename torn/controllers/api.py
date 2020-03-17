from json import loads as load_json, dumps as to_json
from gluon.custom_import import track_changes
track_changes(True)

from hasher import hash as pwd_hash

def login():
	response = {'success': False, 'items': [], 'message': 'Something wrong!'}
	if request.method != 'POST': raise HTTP(503) # Forbidden access
	if request.vars and 'submit' in request.vars:
		try:
			usr, pwd = [request.vars[k] for k in ['usr', 'pwd']]
			hsh_pwd = pwd_hash(pwd)
			rows = db(
				((db.users.username == usr) | (db.users.email == usr)) &
				(db.users.password == hsh_pwd)
			).select()
			if len(rows) == 1:
				session.user_id = rows[0].id
				response['success'] = True
				response['message'] = 'Login success!'
			else:
				response['message'] = 'Login failed!' 
		except Exception as e:
			response['message'] = str(e)
	return to_json(response)