from flask import Flask, render_template, request
import re

app = Flask(__name__)

common_passwords = [
    "123456",
    "password",
    "qwerty",
    "admin",
    "welcome",
    "password123"
]

def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 20
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        suggestions.append("Add special characters")

    common = False
    if password.lower() in common_passwords:
        common = True
        suggestions.append("This is a commonly used password")

    if score < 40:
        strength = "Weak"
        color = "danger"
    elif score < 80:
        strength = "Medium"
        color = "warning"
    else:
        strength = "Strong"
        color = "success"

    return score, strength, color, suggestions, common

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        password = request.form["password"]

        score, strength, color, suggestions, common = analyze_password(password)

        result = {
            "score": score,
            "strength": strength,
            "color": color,
            "suggestions": suggestions,
            "common": common,
            "length": len(password)
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)