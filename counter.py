#This program is used for counting the number of hits on a web site #I have used python as a Programming language with flask and sqlAlchemy.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def count():
    return render_template("index.html")


@app.route("/success")
def sucess():
    return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
