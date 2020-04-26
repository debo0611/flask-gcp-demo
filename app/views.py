# write views

from app import app

from flask import render_template, request

@app.route("/")
def index():

    args = None

    if request.args: # if a query string is in the URL

        args = request.args # gives us a nicely parsed dict of key/value

        return render_template("public/index.html", args=args)

    return render_template("public/index.html", args=args)