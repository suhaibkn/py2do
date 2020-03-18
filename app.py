from dataclasses import dataclass
from datetime import datetime

from flask import Flask, url_for, redirect, jsonify, request
from flask import render_template as view
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Debug')

db = SQLAlchemy(app)


@dataclass
class Todo(db.Model):
    id: int
    todo: str
    done: bool
    archive: bool
    created_at: datetime
    updated_at: datetime

    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(128), nullable=True)
    done = db.Column(db.Boolean, default=False)
    archive = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, _todo=None, _time=None):
        self.todo = _todo

    @staticmethod
    def get_all():
        return Todo.query.filter(Todo.archive == False).all()

    @staticmethod
    def get_by_id(_id):
        return Todo.query.filter(Todo.id == _id).first()

    @staticmethod
    def get_all_active():
        return Todo.query.filter(Todo.done == False).all()

    @staticmethod
    def get_all_archived():
        return Todo.query.filter(Todo.archive == True).first()

    def save(self):
        db.session.add(self)
        return db.session.commit()

    @staticmethod
    def clean():
        Todo.query.delete()
        return db.session.commit()

    @staticmethod
    def remove(self, _id):
        Todo.query.filter(Todo.id == _id).delete()
        return db.session.commit()

    @staticmethod
    def update(_id, _todo):
        Todo.query.filter(Todo.id == _id).update({
            Todo.todo: _todo,
            Todo.updated_at: datetime.now()
        })
        return db.session.commit()

    @staticmethod
    def toggle_done(_id):
        prev = Todo.query.filter(Todo.id == _id).first().done
        Todo.query.filter(Todo.id == _id).update({
            Todo.done: not prev,
            Todo.updated_at: datetime.now()
        })
        return db.session.commit()

    @staticmethod
    def toggle_archive(_id):
        Todo.query.filter(Todo.id == _id).update({
            Todo.delete: True,
            Todo.updated_at: datetime.now()
        })
        return db.session.commit()


@app.route('/')
def index():
    # Todo('Do this dynamically...').save()
    # Todo.clean()
    return redirect(url_for('main'))


@app.route('/main', methods=['GET'])
def main():
    return view('main.htm'), 200


# <><><><><>   REST_API   <><><><><> #
@app.route('/api/get/<string:_type>', methods=['GET'])
def _api_get(_type='all'):
    data = []
    if 'all' == _type:
        data = Todo.get_all()
    elif 'active' == _type:
        data = Todo.get_all_active()
    elif 'archived' == _type:
        data = Todo.get_all_archived()

    return jsonify(data)


@app.route('/api/new', methods=['POST'])
def _api_new():
    data = request.json
    Todo(data['todo']).save()

    return _api_get(), 200


@app.route('/api/clean', methods=['DELETE'])
def _api_clean():
    Todo.clean()
    return _api_get(), 200


@app.route('/api/toggledone/<int:_id>', methods=['GET'])
def _api_done(_id):
    Todo.toggle_done(_id)
    return _api_get(), 200


if __name__ == '__main__':
    app.run()
