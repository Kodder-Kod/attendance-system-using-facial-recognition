import mysql.connector as sa



def con():
    conn = sa.connect(host='localhost', user='root', password='', database='recon')
    cur = conn.cursor()  # assign cursor
    lol = "select email from Admin where email =%s and Password=%s"
    cur.execute(lol, [(name), (pas)])
    result = cur.fetchall()

    conn.close()

    return result
