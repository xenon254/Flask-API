from flask import *
# initialize the flask app
app=Flask(__name__)

# Define the route
@app.route("/api/home")
def home():
    return jsonify({"Message":"Welcome to Home API"})



# Create a route for products
@app.route("/api/product")
def product():
    return jsonify({"Message":"Welcome to product API"}) 

# Create a route for services
@app.route("/api/services")   
def services():
    return jsonify({"Message":"Welcome to services API"})

# Creating a route to accept user input
@app.route("/api/calc",methods=["POST"])
def calc():
    num1=request.form['num1']
    num2=request.form['num2']

    SUM=int(num1)+int(num2)

    return jsonify({"Answer":SUM})
@app.route("/api/multiply",methods=["POST"])
def multiply():
    num1=request.form['num1']
    num2=request.form['num2']

    product=int(num1)*int(num2)
    return jsonify({"Answer":product})
app.run(debug=True)