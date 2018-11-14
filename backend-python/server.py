#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import sys
from math import pi

app = Flask(__name__)

BIND = sys.argv[1]
PORT = sys.argv[2]

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('occupation')
parser.add_argument('age')
parser.add_argument('reason')


class People(Resource):
    def get(self, human_id):
        return PEOPLE[human_id]

    def put(self, human_id):
        # Fishy Comment:
        # lol post form data like this but not as api for js frontend please
        # research application/x-www-form-urlencoded!
        PEOPLE[human_id] = request.form['data']
        return {human_id: PEOPLE[human_id]}

    def delete(self, human_id):
        try:
            del PEOPLE[human_id]
            return {"status": "OK"}, 204
        except KeyError as ke:
            return {"status": "No such resource"}, 404


class PeopleList(Resource):
    def get(self):
        return PEOPLE

    def post(self):
        args = parser.parse_args()
        human_id = len(PEOPLE.keys())+1
        PEOPLE[human_id] = {
            "name": args["name"],
            "occupation": args["occupation"],
            "age": args["age"],
            "reason": args["reason"]
        }

        return PEOPLE[human_id], 201


api.add_resource(PeopleList, '/people')
api.add_resource(People, '/people/<int:human_id>')


PEOPLE = {
    0: {"name": "Dennis",
        "occupation": "currently all sorts",
        "age": pi,
        "reason": "since he is awesome"},
}

if __name__ == "__main__":
    app.run(
        host=BIND,
        port=PORT,
        debug=True
    )

