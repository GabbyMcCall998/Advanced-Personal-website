from flask import Flask, render_template

app = Flask(__name__)

print(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/')
@app.route('/contact')
def contact():
    return render_template('Contact.html')


if __name__== '__main__':
    app.run(debug=True)