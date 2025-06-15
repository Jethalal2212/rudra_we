from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Rudra ke replies
rudra_brain = {
    "hi": ["Yo bhai!", "Kya scene h?", "Aagya tu 😎"],
    "kaise ho": ["Bhai mast! Tu bol 😁", "Bindaas! Tu suna?"],
    "bye": ["Chal milte hain 👋", "Alvida doston 😅"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        user_input = request.form["user_input"].lower()
        reply = random.choice(rudra_brain.get(user_input, ["Tu kya bol raha bhai?"]))
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
