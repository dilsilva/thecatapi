from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


db_connect = create_engine('sqlite:///TheCat.db')
app = Flask(__name__)
api = Api(app)


# DB
class Breeds(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from breeds") 
        return {'breeds': [i[0] for i in query.cursor.fetchall()]} 


api.add_resource(Breeds, '/breeds') # Route_1

# ROUTES
@app.route("/breeds")
@app.route("/breeds/$RACE")
@app.route("/temperament")
@app.route("/origin")

if __name__ == '__main__':
     app.run(port='5002')