import web

db_host = 'localhost'
db_name = 'kuorra_login'
db_user = 'root'
db_pw = '7757424081'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )