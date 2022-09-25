from flask import Flask, render_template, request,redirect,url_for,session
import cx_Oracle
import random
import os
from datetime import datetime



app=Flask(__name__)
conn=cx_Oracle.connect('rohith/rohith12@//DESKTOP-8ITTR0U:1521/xe') #change username and password of database and your system name#
print(conn.version)
con=conn.cursor()
app.secret_key="hajury&bc*%bnceu"

def tre():
    a = random.randint(0000000000, 9999999999)
    return a
#################################################################################################
@app.route('/',methods=['GET','POST'])
def login():
    lcheck()
    return render_template('login.html')
@app.route('/lcheck',methods=['GET','POST'])
def lcheck():
    msg="not found"
    muser=request.form.get("email")
    mpass=request.form.get("pass")
    con.execute('''select password from users where EMAIL=:muser''',[muser])
    data=con.fetchone()
    print(data)
    if(data==None):
        pass
    else:
        if(mpass==data[0]):
            session["user"]=muser
            return redirect('/home')
        else:
            return render_template('login.html',msg=msg)

@app.route('/ilogin', methods=['GET', 'POST'])
def ilogin():
        ilcheck()
        return render_template('ilogin.html')
@app.route('/ilcheck',methods=['GET','POST'])
def ilcheck():
    msg="not found"
    muser=request.form.get("email")
    mpass=request.form.get("pass")
    con.execute('''select password from instructor where email=:muser''',[muser])
    data=con.fetchone()
    if (data == None):
        pass
    else:
        if (mpass == data[0]):
            session["inst"] = muser
            return redirect('/ihome')
        else:
            return render_template('ilogin.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
        create()
        return render_template('register.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
        id=tre();
        name = request.form.get("name1")
        muser = request.form.get("email")
        mpass = request.form.get("pass1")
        sqlcommand=('''insert into users values (:id,:muser,:name,:mpass)''')
        data=(id,muser,name,mpass)
        con.execute(sqlcommand,data)
        con.execute('''delete from users where name is null''')
        conn.commit()
        return redirect('/')
@app.route('/iregister', methods=['GET', 'POST'])
def iregister():
        icreate()
        return render_template('iregister.html')

@app.route('/icreate', methods=['GET', 'POST'])
def icreate():
        id = tre();
        name = request.form.get("name")
        muser = request.form.get("email")
        mpass = request.form.get("pass")
        sqlcommand=('''insert into instructor values (:id,:muser,:name,:mpass)''')
        data=(id,muser,name,mpass)
        con.execute(sqlcommand,data)
        con.execute('''delete from instructor where name is null''')
        conn.commit()
        return redirect('/ilogin')

#######
@app.route('/ihome',methods=['GET','POST'])
def ihome():
    con.execute('''select * from courses''')
    data = con.fetchall()
    return  render_template('ihome.html',data=data)
@app.route('/home',methods=['GET','POST'])
def home():
    con.execute('''select * from courses''')
    data=con.fetchall()
    return render_template('home.html',data=data)
@app.route('/course',methods=['GET','POST'])
def course():
    id = request.form.get('id')
    con.execute('''select f.links,c.DESCRIP,f.orders,f.file_name from files f,courses c where f.course_id=c.course_id and c.course_id=:id and f.orders=1''',[id])
    data=con.fetchall()
    con.execute('''select f.file_id,f.file_name from files f,courses c where f.course_id=c.course_id and c.course_id=:id order by f.orders ''',[id])
    text=con.fetchall()
    return render_template('inter.html',data=data,text=text)
@app.route('/file',methods=['GET','POST'])
def file():
    id = request.form.get('id')
    con.execute('''select f.links,c.DESCRIP,f.orders,f.file_name from files f,courses c where f.course_id=c.course_id and f.file_id=:id ''',[id])
    data = con.fetchall()
    con.execute('''select f.file_id,f.file_name from files f,courses c where f.course_id=c.course_id and c.course_id=(select course_id from files where file_id=:id) order by f.orders ''',[id])
    text = con.fetchall()
    return render_template('inter.html', data=data, text=text)
@app.route('/insert',methods=['GET','POST'])
def insert():
    return render_template('in1.html')
@app.route('/insertfile',methods=['GET','POST'])
def insertfile():
    if "inst" in session:
        id=tre()
        te=tre()
        name=request.form.get("cname")
        descs = request.form.get("Description")
        duration = request.form.get("duration")
        link1 = request.form.get("link")
        option1 = request.form.get("option")
        i=session["inst"]
        print(id,name,descs,duration,i)
    print(te,id,link1,option1)
    sql=('''insert into courses values(:id,:name,:descs,:duration,:i)''')
    sql2=('''insert into files values(:te,:id,:option1,:link1)''')
    q=(id,name,descs,duration,i)
    q2=(te,id,option1,link1)
    con.execute(sql,q)
    conn.commit()
    con.execute(sql2,q2)
    conn.commit()
    return ('<html><h1>Success</h1></html>')

#######
#################################################################################################
if __name__ =='__main__':
    app.run(debug=True)
