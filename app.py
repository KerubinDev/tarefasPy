from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

class Task:
    def __init__(self, title):
        self.title = title

class TaskManager:
    def __init__ (self):
        self.tasks = []
    
    def add_task (self, task_title):
        new_task = Task(task_title)
        self.tasks.append(new_task)

    def get_tasks(self):
        return self.tasks
    
tasks_manager = TaskManager()

@app.route('/')
def index():
    tasks = tasks_manager.get_tasks()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)