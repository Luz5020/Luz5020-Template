#  Copyright (c) 2022. luz5020
#  Approved for use in Open Source Projects

from datetime import timedelta

from flask import Flask, url_for, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "Luz"
app.permanent_session_lifetime = timedelta(minutes=5)


# Render-group
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# Run Order
if __name__ == "__main__":
    app.run
