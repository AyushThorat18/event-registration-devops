from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        event = request.form.get("event")

        return render_template(
            "success.html",
            name=name,
            email=email,
            event=event
        )

    return render_template("register.html")


if __name__ == "__main__":
    print("CI/CD Auto Trigger Working")
    app.run(host="0.0.0.0", port=5000)
