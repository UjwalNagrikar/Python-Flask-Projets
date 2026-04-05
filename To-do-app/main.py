from flask import Flask, jsonify, request,render_template, redirect

app = Flask(__name__)

# In-memory storage for tasks
tasks = []
# Flask routing
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

@app.route('/view-all')
def view_all():
    return render_template('view_all.html', tasks=tasks, task_count=len(tasks))

if __name__ == '__main__':
    app.run(debug=True)