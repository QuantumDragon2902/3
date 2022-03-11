from flask import Flask, jsonify
from flask import abort
from flask import request


app = Flask(__name__)

promos = [
    {
        'id': 1,
        'name': u'ICPC',
        'description': u'Some description',
        'prizes': [

        ],
        'participants': [

        ]
    },
    {
        'id': 2,
        'name': u'I Professional',
        'description': u'Another description',
        'prizes': [

        ],
        'participants': [

        ]
    }
]


@app.route('/promo', methods=['GET'])
def get_promo():
    l = []
    for i in promos:
        l.append({'name': i['name'], 'description': i['description']})
    return jsonify({'promos': l})


@app.route('/promo/<int:promo_id>', methods=['GET'])
def get_task(promo_id):
    res = []
    for i in promos:
        if i['id'] == promo_id:
            res.append(i)
    if len(res) == 0:
        abort(404)
    return jsonify({'task': res[0]})


@app.route('/promo/<int:promo_id>', methods=['PUT'])
def update_task(promo_id):
    print('boo')
    res = []
    index = 0
    for i in promos:
        if i['id'] == promo_id:
            res.append(i)
            break
        index += 1
    if len(res) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' not in request.json and type(request.json['name']) != type('fd') and request.json['name'].split(' ') == '':
        abort(400)
    if 'description' not in request.json and type(request.json['description']) != type('fd'):
        abort(400)
    promos[index]['name'] = request.json.get('name', res[0]['name'])
    promos[index]['description'] = request.json.get('description', res[0]['description'])
    res[index]['name'] = request.json.get('name', res[0]['name'])
    res[index]['description'] = request.json.get('description', res[0]['description'])
    return jsonify({'promos': res[0]})


if __name__ == '__main__':
    app.run(debug=True)
