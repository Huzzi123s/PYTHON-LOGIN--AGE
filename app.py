from flask import Flask,Response,redirect,url_for,request,session

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/" , methods = ["POST" , "GET"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "user" and password == "123":
            session['user'] = username
            return redirect(url_for("welcome"))
        else:
            return "invalid candiate"
    return '''
         <h2> Login Page </h2>
         <form method = "POST">
         Username: <input type ="text" name = "username"><br>
         password: <input type = "password" name="password"> <br>
         <input type ="submit" value = "login"> 
         '''
        
@app.route("/welcome")        
def welcome():
    if "user" in session:
        return f'''
        <h3>WELCOME {session["user"]} </H3>
        <a href = {url_for('logout')}>logout</a>
'''
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

