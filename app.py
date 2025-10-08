from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = list(string.ascii_lowercase)
    if use_upper:
        chars += list(string.ascii_uppercase)
    if use_digits:
        chars += list(string.digits)
    if use_symbols:
        chars += list("!@#$%^&*()-_=+[]{};:,.<>?/|")

    if length < 4:
        return "⚠️ Password length must be at least 4 characters."

    password = "".join(random.choice(chars) for _ in range(length))
    return password

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    error = None
    if request.method == "POST":
        try:
            length = int(request.form.get("length") or 0)
            use_upper = bool(request.form.get("upper"))
            use_digits = bool(request.form.get("digits"))
            use_symbols = bool(request.form.get("symbols"))

            if length <= 0:
                raise ValueError("⚠️ Please enter valid length.")

            password = generate_password(length, use_upper, use_digits, use_symbols)

        except ValueError as ex:
            error = str(ex)
        except Exception:
            error = "⚠️ Invalid input."
    return render_template("index.html", password=password, error=error)

if __name__ == "__main__":
    app.run(debug=True)

