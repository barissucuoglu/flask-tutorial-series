from flask import render_template, request, redirect, url_for
from models import User
from models import Person
from flask_login import login_user, logout_user, current_user, login_required

def register_routes(app, db, bcrypt):

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "GET":
            people = Person.query.all()
            return render_template("index.html", people=people)
        elif request.method == "POST":
            name = request.form.get("name")
            age = int(request.form.get("age"))
            job = request.form.get("job")

            person = Person(name=name, age=age, job=job)
            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            return render_template("index.html", people=people)
    
    @app.route("/delete/<pid>", methods=["DELETE"])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()

        people = Person.query.all()
        return render_template("index.html", people=people)
    
    @app.route("/detail/<pid>")
    def detail(pid):
        person = Person.query.filter(Person.pid == pid).first()
        return render_template("detail.html", person=person)
    
    @app.route("/home", methods=["GET", "POST"])
    def home():
        return render_template("home.html")
    
    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "GET":
            return render_template("signup.html")
        elif request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            hashed_password = bcrypt.generate_password_hash(password)

            user = User(username=username, password=hashed_password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for("home"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            user = User.query.filter(User.username == username).first()

            if bcrypt.check_password_hash(user.password, password):
                login_user(user=user)
                return redirect(url_for("home"))
            else:
                return "Failed"
    
    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("home"))
    
    @app.route("/secret")
    @login_required
    def secret():
        return "My secret message"