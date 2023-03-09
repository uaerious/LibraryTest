from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirm')
def complete():
    return render_template('complete.html')



app.run(host='0.0.0.0', port=81)
