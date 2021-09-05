#!C:\Users\Admin\AppData\Local\Programs\Python\Python38\python.exe
import pymysql
import cgi
print("Content-type:text/html\n\r\n\r")
print("<body bgcolor='pink'>")
form = cgi.FieldStorage()
nm = form.getvalue('nm')
em = form.getvalue('em')
pas = form.getvalue('pas')
ph = form.getvalue('ph')
state = form.getvalue('state')
prog = form.getvalue('prog')
con = pymysql.connect(user='root', password='',
                      host='localhost', database='school')
cur = con.cursor()
cur.execute('insert into student values("%s","%s","%s","%s","%s","%s")' % (
    nm, em, pas, ph, state, prog))
con.commit()
con.close()
print("<h2> Successfully inserted </h2>")
