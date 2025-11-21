from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" - will reset when server restarts
tasks = []

@app.route('/')
def hello_world():
    return 'Welcome to Task Manager API'

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({
        'tasks': tasks,
        'total': len(tasks)
    })

# POST /tasks - Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    # Get JSON data from request
    data = request.get_json()

    # Basic validation
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data.get('description', ""),
        'completed': False
    }

    tasks.append(new_task)
    return jsonify(new_task), 201  # 201 = Created

if __name__ == '__main__':
    app.run(debug=True)
    



