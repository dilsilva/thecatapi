from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import requests
import json

# a. Para cada uma das raças de gatos disponíveis, armazenar as informações de
# origem, temperamento e descrição em uma base de dados. (se disponível)
# b. Para cada uma das raças acima, salvar o endereço de 3 imagens em uma base de
# dados. (se disponível)
# c. Salvar o endereço de 3 imagens de gatos com chapéu.
# d. Salvar o endereço de 3 imagens de gatos com óculos.

# db_connect = create_engine('sqlite:///TheCat.db')
app = Flask(__name__)



# # DB
# class Breeds(Resource):
#     def get(self):
#         conn = db_connect.connect() # connect to database
#         query = conn.execute("select * from breeds") 
#         return {'breeds': [i[0] for i in query.cursor.fetchall()]} 


# api.add_resource(Breeds, '/breeds') # Route_1

# ROUTES
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/breeds")
def breed_api():
    resp = requests.get('https://api.thecatapi.com/v1/breeds')
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /breeds {}'.format(resp.status_code))
    for todo_item in resp.json():
        return('{} {}'.format(todo_item['id'], todo_item['description']))
    # json_payload = json.loads(resp.text)
    # return(json.dumps(json_payload, indent=2))


@app.route("/breeds/<int:breed_id>")
def breedid_api(breed_id=None):
    if request.method == "GET":
        if breed_id:
            # retorna uma raça especifica
            return jsonify(breed=breed.filter(id=breed_id))
        else:
            # retorna todas as breed
            return jsonify(breed=breed.all())
    elif request.method == "POST":
        if request.is_json:
            # se o request veio com o mimetype "json" usa os dados para
            # inserir novas breed
            breed.bulk_insert(request.json)
            return "Raças inseridas com sucesso", 201
        else:
            # assumimos que os dados vieram via Ajax/POST/Formulário
            breed.create(request.form)
            return "Raça criada com sucesso", 201
    elif request.method == "DELETE" and breed_id:
        # apaga uma noticia especifica
        breed.delete(id=breed_id)
        return "Raça apagada com sucesso!", 204

# @app.route("/temperament")
# @app.route("/origin")

if __name__ == "__main__":
    app.run(port='5002' , debug=True)