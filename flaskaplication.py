from flask import Flask
import uuid
tasks = []

app = Flask(__name__)


@app.route('/')
def hello_world():
    return str(tasks)


@app.route('/add/<string:task>/<string:status>', methods=['POST'])
def addItem(task, status):
    for i in tasks:
        if task == i.get("task"):
            return "task already exists"
    new_task = {
        "task": task,
        "status": status,
        "id": uuid.uuid4().int
    }
    tasks.append(new_task)
    return "task added"


@app.route('/update/<string:oldtask>/<string:task>/<string:status>', methods=['POST'])
def updateItem(oldtask, task, status):
    for i in tasks:
        if oldtask == i.get("task"):
            i["task"] = task
            i["status"] = status
    return "task updated"


@app.route('/delete/<string:task>', methods=['POST'])
def deleteItem(task):
    for i in tasks:
        if task == i.get("task"):
            i.clear()
    return "task deleted"


if __name__ == '__main__':
    app.run(debug=True)
