# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/hello")
def hello():
    response = make_response("Hello World\n")
    response.status_code = 202
    response.headers["content-type"] = "text/plain"
    return response


@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"


@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


# http://127.0.0.1:5555/handle_url_params?name=Mike&greeting=Hello
@app.route("/handle_url_params")
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args.get("greeting")
        name = request.args["name"]
        return f"{greeting}, {name}"
    else:
        return "Some parameters are missing"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)

