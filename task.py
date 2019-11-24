from flask import Flask ,render_template,request
import sqlite3 as sql
obj=Flask(__name__)

@obj.route('/', methods=['GET'])
def success():
	return 'success'

@obj.route('/newinfo')
def new_person():
	return render_template('person.html')


@obj.route('/record',methods=['POST','GET'])
def record():
	if request.method=='POST':
		try:
			nm=request.form['nm']
			emailaddr=request.form['email']
			phoneno=request.form['phone']
			with sql.connect("database.db") as ch:
				cur=ch.cursor()
				cur.execute("INSERT INTO students (name,emailaddress,phonenumber)Values(?,?,?)",(nm,emailaddr,phoneno))
				ch.commit()
				msg="RECORD SUCCESSFULLY ADDED"
		except:
			ch.rollback()
			msg="ERROR"
		finally:
			return render_template("result.html",msg=msg)
			ch.close()

if __name__ == '__main__':
	obj.run(debug = True, port = 4996)