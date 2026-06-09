from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=(
f"mysql+pymysql://{os.getenv('DB_USER')}:"
f"{os.getenv('DB_PASSWORD')}@"
f"{os.getenv('DB_HOST')}/"
f"{os.getenv('DB_NAME')}"
)

db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    task=db.Column(db.String(200))

@app.route("/")
def home():
    return jsonify({"message":"Todo App Running"})

@app.route("/todo",methods=["POST"])
def add_task():
    data=request.json
    todo=Todo(task=data['task'])
    db.session.add(todo)
    db.session.commit()
    return jsonify({"status":"created"})

@app.route("/todo")
def get_tasks():
    tasks=Todo.query.all()

    result=[
        {
            "id":t.id,
            "task":t.task
        }
        for t in tasks
    ]

    return jsonify(result)

@app.route("/health")
def health():
    return jsonify({"status":"healthy"})

if __name__=="__main__":
    app.run(host="0.0.0.0")
