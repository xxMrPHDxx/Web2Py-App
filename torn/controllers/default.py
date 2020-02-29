from hashlib import pbkdf2_hmac

def index():
    return locals()

def register():
    if request.vars:
        request.vars.password = pbkdf2_hmac('sha512', request.vars.password, 'salt', 16) 

    if request.vars and request.method != 'POST':
        raise HTTP(403, "Forbidden")
    elif request.vars:
        # Manual insertion into database
        columns = {key: request.vars[key] for key in request.vars}
        db.users.insert(**columns)
    else: columns = None
    return locals()