#import flask module
from flask import Flask, request, jsonify
from flask_restful import Api
from resources.routes import initialize_routes
# clefrom database.models import User
from database.db import initialize_db
from flask_cors import CORS, cross_origin
from loguru import logger
import json
# from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'rp_server_one',
    'host': 'localhost',
    'port': 27017
}

initialize_db(app)

# class User(db.Document):
#     name = db.StringField()
#     email = db.StringField()
#     def to_json(self):
#         return {"name": self.name,
#                 "email": self.email}


# @app.route('/add', methods=['POST'])
# def update_record():
#     record = request.get_json()
#     user = User(name=record['name'], email=record['email']).save()
#     # user.save()

#     logger.info("object", user)

#     logger.info("record is inserted")

#     return {"message" : "ok"}


#Test route
@app.route('/')
def hello_world():
    return 'Hello World'

#initialize all the routes
initialize_routes(api)

#Main function
if __name__ == '__main__':
    app.secret_key = "qwertyuiopoiuytrewq"
    app.run()