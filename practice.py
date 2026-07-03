from flask import Flask,request,redirect,url_for,session,Response

app = Flask(__name__)
app.secret_key = "my-secret"

@app.route("/", methods = ["POST" , "GET"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "user" and password == "123":
            session['user'] = username
            return redirect(url_for("welcome"))
        else :
            return ("invalod candidate")
    return '''
        <h2>LOGIN PAGE </h2>
        <form method = "POST">
        username:<input type="text" name="username"><br>
        password:<input type="password" name="password"><br>
        <input type="submit" value = "login">
        </form?
'''    

@app.route("/welcome")
def welcome():
    if 'user' in session :
        return f'''
        <h2> welcome {session["user"]} </h2>
        <a href ={url_for('logout')}>Logout</a>
'''
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user" , None)
    
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
