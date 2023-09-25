from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '80221474'
app.config['MYSQL_DB'] = 'webApplication'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        name = request.form['name']
        cusId = request.form['id']
        gmail = request.form['gmail']
        phone = request.form['phone']

        print(name, cusId)

        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
