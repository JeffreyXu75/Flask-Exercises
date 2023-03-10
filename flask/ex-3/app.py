from flask import Flask, render_template, request

app = Flask(__name__)

globaldict = {}
valid = ["Org 1", "Org 2", "Org 3", "Org 4", "Org 5"]

@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST" and not (len(request.form["name"])==0 or request.form["group"] not in valid):
      globaldict[request.form["name"]]=(request.form["group"])
    return render_template('home.html')


@app.route('/register.html', methods=["GET", "POST"])
def register():
    return render_template('register.html', result=globaldict)

if __name__ == '__main__':
    app.run(debug=True)