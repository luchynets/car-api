from flask import Flask, request, jsonify
import insert
import get


app = Flask(__name__)

@app.route('/owner', methods = ['GET', 'POST'])
def owner():
	if request.method == 'GET':
		try:
			name = request.args['search']
			include_cars = request.args['include_cars']
			limit = request.args.get('limit')
			offset = request.args.get('offset')
			result = get.get_data(name, include_cars, limit, offset)
			if result.get('detail') == 'not found':
				return jsonify(result), 404
			return jsonify(result), 200
		except KeyError:
			return jsonify({'detail': 'You do not pass one of this constants (search/include_cars)'}), 400
	else:
		try:
			first_name = request.form['first_name']
			last_name = request.form['last_name']
			birth_date = request.form['birth_date']
			gender = request.form['gender']
			insert.insert_owner(first_name, last_name, birth_date, gender)
			return jsonify({'detail': 'owner created'}), 201
		except KeyError:
			return jsonify({'detail': 'You do not pass one of this constants (first_name/last_name/birth_date/gender)'}), 400

@app.route('/car', methods = ['POST'])
def car():
	try:
		brand = request.form['brand']
		model = request.form['model']
		owner = request.form['owner']
		color = request.form['color']
		fuel_type = request.form['fuel_type']
		new_or_used = request.form['new_or_used']
		if insert.insert_car(brand, model, owner, color, fuel_type, new_or_used):
			return jsonify({'detail': 'car added'}), 201
		else:
			return jsonify({'detail': f'that owner ({owner}) was not created'}), 400
	except KeyError:
		return jsonify({'detail': 'You do not pass one of this constants (brand/model/owner/color/fuel_type/new_or_used)'}), 400

if __name__ == '__main__':
	app.run(debug = True)