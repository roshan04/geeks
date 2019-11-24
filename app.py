from flask import Flask, render_template, request
import sqlite3 as sql
import time
app = Flask(__name__)

@app.route('/')
def home():
   return ('server is running.....')

@app.route('/newinfo')
def new_student():
   return render_template('person.html')

@app.route('/record',methods = ['POST', 'GET'])
def record():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         email = request.form['email']
         phone = request.form['phone']
         now = time.ctime(int(time.time()))
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (name,email,phone,intime) VALUES (?,?,?,?)",(nm,email,phone,now) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True, port = 4998)