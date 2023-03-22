from flask import Flask, request, jsonify

app = Flask(__name__)

Items = [
    {"name": "product name", "category:" : "1" , "price:" : "20.5" , "instock:" : "200"},
    
]
def _find_next_id(name):
    data = [x for x in Items if  x['name']==name]
    return data

@app.route('/country', methods=["GET"])
def get_country():
    return jsonify(Items)

@app.route('/country/<name>', methods=["GET"])
def get_country_id(name):
    data = _find_next_id(name)
    return jsonify(data)


@app.route('/' , methods=["POST"])
def post_country():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')
    

    new_data = {
        "name" : name,
        "category" : category,
        "price" : price,
        "instock" : instock
    }

    if (_find_next_id(name)) :
        return {"error" : "Bad Request"}, name
    else : 
        Items.append(new_data)
        return jsonify(Items)

@app.route('/country/<name>', methods = ['DELETE'])
def delete_country(name):

    data = _find_next_id(name)
    if not data:
        return {"error": "country not found"}, 404
    else:
        Items.remove(data[0]) 
        return "country deleted succuessfully" ,200
""""
@app.route('/Itemm/<id>', methods=['PUT'])
def put_Itemm(id):
    global Items
    name = request.form.get('name')
    capital = request.form.get('capital')

    update_data = {
        "name": name,
        "capital": capital
    }

    for Itemm in Items:
        if id == Itemm.get("id"):
            Itemm["name"] = str(name)
            Itemm['capital'] = str(capital)
            return jsonify(Items)
        else:
            return "error", 404
@app.route('/Itemm/<id>', methods=["PATCH"])
def patch_Itemm(id: int):
    Itemm = _find_next_id(id)
    if Itemm is None:
        return jsonify({'error':'Itemm not found!'}),404

    updated_Itemm = jsonify.loads(request.data)
    Itemm.update(updated_Itemm)
    return jsonify(Items)
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)