from flask import Flask, render_template
import datetime
app = Flask(__name__)




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', now = datetime.datetime.now().strftime("%A, %B %d %Y %H:%M:%S"))


if __name__ == '__main__':
    app.run(debug=True)