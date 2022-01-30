from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hi to Flask"

@app.route("/second")
def second():
    return "second page"

@app.route("/third/engin")
def third():
    return "third page"

@app.route("/fourth/<string:id>")
def fourth(id):
    return f"fourth page {id}"



if __name__ == "__main__":
    app.run(debug=True)




