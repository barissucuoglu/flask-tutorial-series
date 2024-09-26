from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    my_value = "Study"
    my_result = 10 + 20
    my_list = [10, 17, 30, 37]
    return render_template("index.html", my_value=my_value, my_result=my_result, my_list=my_list)

@app.route("/other")
def other():
    text = "Base of filtering Jinja2 Filters"
    return render_template("other.html", text=text)

@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(url_for("other"))

@app.template_filter("reverse_string")
def reverse_string(text):
    return text[::-1]

@app.template_filter("repeat")
def repeat(text, times=2):
    return text * times

@app.template_filter("alternate_case")
def alternate_case(text):
    return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text) ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
