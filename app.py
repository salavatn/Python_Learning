from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
    # return "Set your NAME and ID in URL: http://176.213.150.93/NAME/ID/"



@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/<string:user_name>/<int:user_id>/')
def user_info(user_name,user_id):
    return "Hello, " + user_name + "! Your ID:" + str(user_id)
