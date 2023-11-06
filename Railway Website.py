from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
#MySQL
import random
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1111",database="railway")
mycursor=mydb.cursor()

#FLASK
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/bookit',methods=['GET','POST'])
def bookit():
    pnr=random.randint(100000,999999)
    if request.method == 'POST':
        a = request.form['num']
        l="select Fr_m,T_o,Train from trains where trainnum="+'"'+a+'"'
        mycursor.execute(l)
        data=[]
        for i in mycursor:
            data.append(i)
        Date=request.form['date']
        a = request.form['num']
        name=request.form['name']
        age=request.form['age']
        sex=request.form['sex']
        sex=sex.capitalize()
        contact_number=request.form['contact']
        aadhar_number=request.form['aadhar']
        Fr_om=data[0][0]
        t_o=data[0][1]
        train=data[0][2]
        Seats="1"
        Class="AC-1"
        checkin="PND"
        PNR=str(pnr)
        date=Date.split(sep="-")
        Year=date[0]
        Month=date[1]
        Date=date[2]
        l="insert into passenger (Name, Age, Sex, Contact_number, Aadhar_number, train, Fr_om , t_o , Seats , Class , Date, Month, Year, PNR, checkin ) values ("+ "'"+name+"'"+","+ "'"+age+"'"+","+ "'"+sex+"'"+","+ "'"+contact_number+"'"+","+ "'"+aadhar_number+"'"+","+"'"+train+"'"+","+"'" + Fr_om + "'" + "," + "'" + t_o + "'" + "," + "'" + Seats + "'" + ","+ "'" + Class + "'" +","+ "'" + Date + "'" + "," + "'" + Month + "'" + ","+ "'" + Year + "'" + ","  + "'" + PNR + "'" + "," + "'" + checkin + "'" + ")"
        mycursor.execute(l)
        l="update trains set seat=seat-1 where train like"+"'"+train[0:5]+"%'"+";"
        mycursor.execute(l)
        mydb.commit()
        l="select * from passenger where PNR ="+"'"+PNR+"'"+";"
        mycursor.execute(l)
        a=[]
        for i in mycursor:
            a.append("Name: "+str(i[0]))
            a.append("Age: "+str(i[1]))
            a.append("Sex: "+str(i[2]))
            a.append("Contact Number: "+str(i[3]))
            a.append("Departure: "+str(i[4]))
            a.append("Destination: "+str(i[5]))
            a.append("Seats: "+str(i[6]))
            a.append("Class: "+str(i[7]))
            a.append("Date: "+str(i[8]))
            a.append("Month: "+str(i[9]))
            a.append("PNR: "+str(i[10]))
            a.append("Status: "+str(i[11]))
            a.append("Aadhar Number: "+str(i[12]))
        return render_template('showticket.html',my_array=a)
    return render_template('bookit.html',)    

@app.route('/trains',methods=['GET','POST'])
def trains():
    if request.method == 'POST':
        date=request.form['date']
        a = request.form['button_clicked']
        return render_template('bookit.html',num=a,date=date)
    return render_template('trains.html')
        
@app.route('/booktickets',methods=['GET','POST'])
def booktickets():
    if request.method == 'POST':
        Fr_om=request.form['departure']
        T_o=request.form['destination']
        date=request.form['date']
        l="SELECT * FROM trains WHERE Fr_m like"+"'"+Fr_om+"%'"+" AND T_o like"+"'"+T_o+"%'";
        mycursor.execute(l)
        t=[]
        s=[]
        n=[]
        for i in mycursor:
            t.append(i[2])
            n.append(i[3])
            s.append(i[4])
        return render_template('trains.html',options=t,seats=s,numbers=n,date=date)
    return render_template('book.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        a = request.form['username']
        b = request.form['password']
        l="select password from info where userid ="+"'"+a+"'"+";"
        mycursor.execute(l)
        for i in mycursor:
            c=(i[0])
            if b==c:
                return render_template('book.html')
            else:
                return render_template('login.html')            
    return render_template('login.html')

@app.route('/pnr', methods=['GET', 'POST'])
def pnr():
    if request.method == 'POST':
        a = request.form['pnr']
        b = request.form['aadhar']
        l="select Aadhar_number from passenger where PNR ="+"'"+a+"'"+";"
        mycursor.execute(l)
        for i in mycursor:
            c=(i[0])
            if b==c:
                l="select * from passenger where PNR ="+"'"+a+"'"+";"
                mycursor.execute(l)
                a=[]
                for i in mycursor:
                    a.append("Name: "+str(i[0]))
                    a.append("Age: "+str(i[1]))
                    a.append("Sex: "+str(i[2]))
                    a.append("Contact Number: "+str(i[3]))
                    a.append("Departure: "+str(i[4]))
                    a.append("Destination: "+str(i[5]))
                    a.append("Seats: "+str(i[6]))
                    a.append("Class: "+str(i[7]))
                    a.append("Date: "+str(i[8]))
                    a.append("Month: "+str(i[9]))
                    a.append("PNR: "+str(i[10]))
                    a.append("Status: "+str(i[11]))
                    a.append("Aadhar Number: "+str(i[12]))
                return render_template('accessible.html',my_array=a)
            else:
                return render_template('accessdenied.html')            
    return render_template('pnr.html')

@app.route('/checkindone', methods=['GET', 'POST'])
def checkindone():
    return render_template('checkindone.html')     

@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        p=request.form['pnr']
        a = request.form['button_clicked']
        if a=="confirm":
            l="update passenger set checkin= 'CNF' where PNR="+"'"+p+"'"
            mycursor.execute(l)
            mydb.commit()
        else:
            l="update passenger set checkin= 'CNL' where PNR="+"'"+p+"'"
            mycursor.execute(l)
            mydb.commit()
        return render_template('checkindone.html')     
            
    return render_template('confirmation.html')

@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    if request.method == 'POST':
        a = request.form['pnr']
        b = request.form['contact']
        p=str(a)
        a=str(a)
        l="select Contact_number from passenger where PNR ="+"'"+a+"'"+";"
        mycursor.execute(l)
        for i in mycursor:
            c=(i[0])
            if b==c:
                l="select * from passenger where PNR ="+"'"+a+"'"+";"
                mycursor.execute(l)
                a=[]
                for i in mycursor:
                    a.append("Name: "+str(i[0]))
                    a.append("Age: "+str(i[1]))
                    a.append("Sex: "+str(i[2]))
                    a.append("Contact Number: "+str(i[3]))
                    a.append("Departure: "+str(i[4]))
                    a.append("Destination: "+str(i[5]))
                    a.append("Seats: "+str(i[6]))
                    a.append("Class: "+str(i[7]))
                    a.append("Date: "+str(i[8]))
                    a.append("Month: "+str(i[9]))
                    a.append("PNR: "+str(i[10]))
                    a.append("Status: "+str(i[11]))
                    a.append("Aadhar Number: "+str(i[12]))
                return render_template('confirmation.html',my_array=a,pnr=p)
            else:
                return render_template('accessdenied.html')            
    return render_template('checkin.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        a = request.form['button_clicked']
        if a=="book":
            return render_template('login.html')
        elif a=="pnr":
            return render_template('pnr.html')
        elif a=="checkin":
            return render_template('checkin.html')
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
