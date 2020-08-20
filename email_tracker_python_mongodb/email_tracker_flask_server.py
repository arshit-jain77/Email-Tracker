from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://localhost:27017')
db = client['talenq']
mails = db.mails
class EmailTracker(Resource):
    def get(self):
        code = request.args["code"]
        myquery = {"unique_code": code}
        updated_status = {"$set": {"track_status": 'yes'}}
        mails.update_one(myquery, updated_status)

api.add_resource(EmailTracker, '/email-track')

if __name__ == '__main__':
    app.run(debug=True)