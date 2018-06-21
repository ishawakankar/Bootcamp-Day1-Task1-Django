
import cgi
import psycopg2

try:
    form = cgi.FieldStorage()
    input_text = form.getfirst("fn")
    input_text1 = form.getfirst("ln")
    input_text2 = form.getfirst("mail")
    input_text3 = form.getfirst("pn")
    input_text4 = form.getfirst("country")
    input_text5 = form.getfirst("city")
    conn = psycopg2.connect("dbname='dbname' user='postgres' host='localhost' password='consultadd'")
    cur = conn.cursor()

except:
    print("Connection error")

try:
    SQL= (""""INSERT into user(mailid, first, last, phone, coun, ci) VALUES(mail,fn,ln,pn,country,city);""")
    cur.execute("SELECT * from user")
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()

    cur.close()

    direct to (view.html)

except:
    print ("Cannot Insert")