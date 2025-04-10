from flask import Flask, request, jsonify
import random
import uuid
app = Flask(__name__)

# Lista inicial de presentes
import uuid

gift_list = [
    {"id": 1, "name": "Caneca Personalizada", "price": 25.90, "uuid": str(uuid.uuid4())},
    {"id": 2, "name": "Agenda 2025", "price": 40.00, "uuid": str(uuid.uuid4())},
    {"id": 3, "name": "Livro de Receitas", "price": 55.50, "uuid": str(uuid.uuid4())},
    {"id": 4, "name": "Fone de Ouvido Bluetooth", "price": 150.00, "uuid": str(uuid.uuid4())},
    {"id": 5, "name": "Camiseta Estilosa", "price": 60.00, "uuid": str(uuid.uuid4())},
    {"id": 6, "name": "Caixa de Chocolates", "price": 35.00, "uuid": str(uuid.uuid4())},
    {"id": 7, "name": "Kit de Canetas Coloridas", "price": 20.00, "uuid": str(uuid.uuid4())},
    {"id": 8, "name": "Pulseira Artesanal", "price": 45.00, "uuid": str(uuid.uuid4())},
    {"id": 9, "name": "Mini Planta Suculenta", "price": 30.00, "uuid": str(uuid.uuid4())},
    {"id": 10, "name": "Garrafa Térmica", "price": 80.00, "uuid": str(uuid.uuid4())}
]
next_id = 1

# Adicionar um novo registro
@app.route('/', methods=['POST'])
def add_gift():
    data = request.get_json()
    new_gift = {
        'id': len(gift_list) + 1,
        "name": data['name'],
        "price": data['price'],
        'uuid': str(uuid.uuid4())
    }
    gift_list.append(new_gift)
    return jsonify(new_gift), 201

# Alterar um registro existente
@app.route('/update/<gift_id>', methods=['PUT'])
def update_gift(gift_id):
    data = request.get_json()
    for gift in gift_list:
        if gift["uuid"] == gift_id:
            gift["name"] = data.get("name", gift["name"])  
            gift["price"] = data.get("price", gift["price"])  
            return jsonify(gift), 200 
    return jsonify({"error": "Presente não encontrado!"}), 404

# Remover um registro
@app.route('/delete/<gift_id>', methods=['DELETE'])
def delete_gift(gift_id):
    for gift in gift_list:
        if gift["uuid"] == gift_id:
            gift_list.remove(gift)
            return jsonify({"message": "Presente removido com sucesso!"}), 200
    return jsonify({"error": "Presente não encontrado!"}), 404

# Listar todos os registros
@app.route('/gifts')
def list_gifts():
    return jsonify(gift_list), 200

# Buscar um registro por ID
@app.route('/gift/<gift_id>', methods=['GET'])
def get_gift_by_id(gift_id):
    for gift in gift_list:
        if gift_id == gift['uuid']:
            return jsonify(gift)
    return jsonify({"error": "Presente não encontrado!"}), 404

# Presente mais caro
@app.route('/most_expensive', methods=['GET'])
def most_expensive_gift():
    most_expensive = max(gift_list, key=lambda x: x["price"])
    return jsonify(most_expensive), 200

# Presente mais barato
@app.route('/least_expensive', methods=['GET'])
def least_expensive_gift():
    least_expensive = min(gift_list, key=lambda x: x["price"])
    return jsonify(least_expensive), 200

# Item aleatório
@app.route('/random', methods=['GET'])
def random_gift():
    gift = random.choice(gift_list)
    return jsonify(gift), 200

# Listar ordenado por name
@app.route('/sort_by_name', methods=['GET'])
def list_sorted_by_name():
    sorted_list = sorted(gift_list, key=lambda x: x['name'])  
    return jsonify(sorted_list), 200

# Listar ordenado por valor
@app.route('/sort_by_value', methods=['GET'])
def list_sorted_by_value():
    sorted_list = sorted(gift_list, key=lambda x: x['price'])  
    return jsonify(sorted_list), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)