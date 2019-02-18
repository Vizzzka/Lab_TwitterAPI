from flask import Flask, render_template, request
from mark_locations import main

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/map", methods=["POST"])
def register():

    user = request.form.get("user_name")
    if not user:
        return render_template("failure.html")

    main(user)
        
    return render_template("Map_{}.html".format(user))


if __name__ == '__main__':
    app.run(debug=True)