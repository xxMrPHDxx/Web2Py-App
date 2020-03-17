from hasher import hash as pwd_hash

def index():
    return locals()

def register():
    if request.vars:
        request.vars.password = pwd_hash(request.vars.password) 

    if request.vars and request.method != 'POST':
        raise HTTP(403, "Forbidden")
    elif request.vars:
        # Manual insertion into database
        columns = {key: request.vars[key] for key in request.vars}
        db.users.insert(**columns)
    else: columns = None
    return locals()

def login():

    return locals()