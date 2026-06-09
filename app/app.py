from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)


@app.route("/")
def home():
    logging.info("Home page accessed")
    return jsonify({"message": "Todo App Running"})


@app.route("/todo", methods=["POST"])
def add_task():

    data = request.get_json()

    if not data or "task" not in data:
        return jsonify({"error": "task field is required"}), 400

    logging.info(f"Task received: {data}")

    todo = Todo(task=data["task"])

    db.session.add(todo)
    db.session.commit()

    logging.info("Task added successfully")

    return jsonify({"status": "created"}), 201


@app.route("/todo", methods=["GET"])
def get_tasks():

    logging.info("Fetching all tasks")

    tasks = Todo.query.all()

    result = [
        {
            "id": task.id,
            "task": task.task
        }
        for task in tasks
    ]

    return jsonify(result)


@app.route("/health")
def health():

    logging.info("Health endpoint checked")

    return jsonify({"status": "healthy"})


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
