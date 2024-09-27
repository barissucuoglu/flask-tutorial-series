from flask import Flask, render_template, session

app = Flask(__name__, template_folder="templates")

app.secret_key = "THIS IS SECRET"

@app.route("/")
def index():
    return render_template("index.html", message="Index")

@app.route("/set_data")
def set_data():
    session["name"] = "Naruto"
    session["other"] = "Uzumaki"
    return render_template("index.html", message="Session data set")

@app.route("/get_data")
def get_data():
    if "name" in session.keys() and "other" in session.keys():
        name = session["name"]
        other = session["other"]
        return render_template("index.html", message=f"Name: {name}, Other: {other}")
    else:
        return render_template("index.html", message="No Session Found")
    
@app.route("/clear_session")
def clear_session():
    session.clear()
    #session.pop("name")
    return render_template("index.html", message="Session Cleared")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)