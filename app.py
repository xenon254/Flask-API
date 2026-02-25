from flask import *
import pymysql

# initialize flask
app=Flask(__name__)
@app.route("/api/signup",methods=['POST'])
def signup():

    # request use input
    username=request.form["username"]
    email=request.form['email']
    password=request.form['password']
    phone=request.form['phone']

    # create connection to database
    connection=pymysql.connect(host="localhost",user='root',password='',database='tembo_sokogarden_sixtus')

    # create cursor
    cursor=connection.cursor()

    # create SQL statement to insert the data
    sql='insert into users(username,email,password,phone)values(%s,%s,%s,%s)'

    # prepare the data
    data=(username,email,password,phone)

    # execute/run
    cursor.execute(sql,data)

    # commit/save
    connection.commit()

    # response
    return jsonify({'Message':'Thank you for joining'})

# signin api
# signin route/endpoint
@app.route('/api/signin',methods=['POST'])
def signin():
    
    # request user input
    email=request.form['email']
    password=request.form['password']
    
    #create a connection
    connection=pymysql.connect(host='localhost',user='root',password='',database='tembo_sokogarden_sixtus')

    # create a cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    #sql statement to check if user exist
    sql='select * from users where email=%s and password=%s'

    #prepare data
    data=(email,password)
    cursor.execute(sql,data)

    # response
    if cursor.rowcount==0:
        return jsonify({'Message':"Login failed"})
    else:
        user=cursor.fetchone()
        user.pop("password",None)
        return jsonify({"message":"Login success","user":user})









































app.run(debug=True)