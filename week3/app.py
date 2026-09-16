from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    username = request.form['username']
    email = request.form['email']
    return render_template('success.html', username=username, email=email)


if __name__ == '__main__':
    app.run(debug=True)
