## Flask, Task - 1
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# @app.route('/index')
# @app.route('/index/')
# def index():
#     return "Hello World! Again!"
#
#
# if __name__ == '__main.py__':
#     app.run(host='192.168.100.171', port=9443)


# # Flask, Task - 2
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def render_index():
#     return "Hello, World!"
#
# @app.route("/another-page/")
# def render_another_page():
#     return "Еще одна страница"



# # Flask, Task - 3
# from flask import Flask
#
# app = Flask(__name__)
# @app.route('/')
# @app.route('/index/')
# def index():
#     return "index"
#
# @app.route('/contact/')
# def contact():
#     return "Contact information"
#
#
# @app.route('/calculate/7/9/')
# def calculate():
#     return str(7 ** 9)



# # Flask, Task - 4
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/<int:mypage>/")
# def dynam_pages(mypage):
#     return '{}'.format(mypage + 1)



# Flask, Task - 5
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/<string:user_name>/<int:user_id>')
def user_info(user_name,user_id):
    return "Hello, " + user_name + "! Your ID is: " + str(user_id)

