from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User_page: " + name + '-' + str(id)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/home_work')
def home_work():
    return render_template("home_work.html")

if __name__ == '__main__':
    app.run(debug=True)
