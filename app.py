from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def minecraft():
    return render_template("minecraft.html")

@app.route('/RealHero')
def hero():
    return render_template("Player=hero.html")

@app.route('/whaywait')
def wait():
    return render_template("whatwait.html")

@app.route('/secret')
def secret():
    return render_template("secret.html")

@app.route('/mamasdr')
def dr():
    return render_template("mamasdr.html")

if __name__ == '__main__':
    app.run()
