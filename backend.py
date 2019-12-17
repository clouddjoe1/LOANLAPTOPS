import sqlite3
import datetime
import time

START = time.time()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
    


def connect():
    conn=sqlite3.connect("laptop.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS laptop (id INTEGER PRIMARY KEY, Username text, TSS text, Date integer , Received integer)")
    conn.commit()
    conn.close()

def insert(Username,TSS,Date,Received):
    conn=sqlite3.connect("laptop.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO laptop VALUES (NULL,?,?,?,?)",(Username,TSS,Date,Received))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("laptop.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM laptop")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(Username="",TSS="",Date="",Received=""):
    conn=sqlite3.connect("laptop.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM laptop WHERE Username=? OR TSS=? OR Date=? OR Received=?", (Username,TSS,Date,Received))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("laptop.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM laptop WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,Username,TSS,Date,Received):
    conn=sqlite3.connect("laptop.db")
    cur=conn.cursor()
    cur.execute("UPDATE laptop SET Username=?, TSS=?, Date=?, Received=? WHERE id=?",(Username,TSS,Date,Received,id))
    conn.commit()
    conn.close()

connect()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(TSS="John Smooth"))
print("Loaned since (up %s) " % elapsed())




    

    