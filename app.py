from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rishi@123",
    database="demo"
)
cursor = db.cursor()

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("Untitled-1.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password)
            )
            db.commit()
            return redirect("/login")

        except mysql.connector.errors.IntegrityError:
            return "⚠ Email already exists! Try another."

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )
        user = cursor.fetchone()

        if user:
            return redirect("/dashboard")
        else:
            return "❌ Invalid Email or Password!"

    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
# ---------- CALUCLATOR ----------
@app.route("/caluclator.html")
def caluclator():
    return render_template("caluclator.html")

# -------- MEAL PLAN----------
@app.route("/mealplan.html", methods=["GET", "POST"])
def mealplan():
    return render_template("mealplan.html")

# ---------- SCANNER ----------
@app.route("/scanner.html")
def scanner():
    return render_template("scanner.html")

# ---------- ABOUT----------
@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
