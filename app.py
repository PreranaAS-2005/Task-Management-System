from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

USERNAME="admin"
PASSWORD="1234"

tasks = [
    {"id": 1, "name": "Study Python", "completed": False},
    {"id": 2, "name": "Practice Software Testing", "completed": False},
    {"id": 3, "name": "Complete lab record", "completed": True}
]
next_id =4


@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if len(password) < 4:
            message = "Password must contain at least 4 characters."
        elif username == USERNAME and password == PASSWORD:
            return redirect(url_for("dashboard"))
        else:
            message = "Invalid username or password."

    return render_template("login.html", message=message)

@app.route("/dashboard")
def dashboard():
    return render_template("tasks.html",tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    global next_id

    task_name = request.form.get("task", "").strip()

    if task_name:
        tasks.append({
            "id": next_id,
            "name": task_name,
            "completed": False
        })
        next_id += 1

    return redirect(url_for("dashboard"))


@app.route("/complete_task/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break

    return redirect(url_for("dashboard"))

@app.route("/delete_task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break

    return redirect(url_for("dashboard"))


if __name__=="__main__":
    app.run(debug=True) 



