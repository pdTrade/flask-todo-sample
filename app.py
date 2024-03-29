from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = [{"task": "タスク1", "done": False}]

@app.route("/")
def index():
  return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
  todo = request.form['todo']
  todos.append({"task": todo, "done": False})
  return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
  todo = todos[index]
  if request.method == "POST":
    todo['task'] = request.form["todo"]
    return redirect(url_for("index"))
  else:
    return render_template("edit.html", todo=todo, index=index)

@app.route("/status/<int:index>")
def status(index):
  todos[index]['done'] = not todos[index]['done']
  return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
  del todos[index]
  return redirect(url_for("index"))

if __name__ == '__main__':
  app.run(debug=True)