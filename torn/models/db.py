from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    db = DAL('google:datastore+ndb')
    session.connect(request, response, db=db)
    
db.define_table(
    'users',
    Field('username', 'string', notnull=True, requires=[IS_NOT_EMPTY()]),
    Field('email', 'string', notnull=True, requires=[IS_NOT_EMPTY(), IS_MATCH(r'[\w\.\_]+@[\w\_]+\.[\w\_]+')]),
    Field('password', 'string', notnull=True, requires=[IS_NOT_EMPTY()]),
    Field('gender', 'boolean', notnull=True),


    Field('money', 'integer' , notnull=True, default=1000),
    Field('points', 'integer', notnull=True, default=0),
    Field('health', 'integer', notnull=True, default=100),
    Field('nerve', 'integer' , notnull=True, default=15)
)