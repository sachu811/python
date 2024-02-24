from flask import Flask
 
app=Flask(__name__)

@app.route("/",methods=["GET"]) #decorator
def welcome():
    return "Welcome My page"

@app.route("/index",methods=["GET"]) 
def index():
    return "<h1>This is Index Page</h1>"

@app.route("/contact/<int:phone>",methods=["GET"])
def contact(phone):
    return str(phone)

if __name__=='__main__':
    app.run(debug=True)