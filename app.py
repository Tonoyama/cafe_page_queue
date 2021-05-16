# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def view():
    count = 50
    count2 = 60
    count3 = 40
    count_plus = int(count)+int(count2)
    return render_template('index.html', count1=count_plus, count2=count3)


if __name__ == "__main__":
    app.run()