from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
        return "<i>Welcome To My Web-Site</i>"

@app.route("/home")       
def home():
        return "<i>Welcome To My Home Page<i>"
        
if(__name__=="__main__"):
    app.run()
