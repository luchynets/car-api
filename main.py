#import modules
from flask import Flask, request, jsonify
import insert
import get

#create app
app = Flask(__name__)

#create route "/owner"
@app.route('/owner', methods = ['GET', 'POST'])
def owner():
	#check connection method
	if request.method == 'GET':
		try:
			#get all arguments
			name = request.args['search']
			include_cars = request.args['include_cars']
			limit = request.args.get('limit')
			offset = request.args.get('offset')
			result = get.get_data(name, include_cars, limit, offset) #get data for owner
			#check if owner created
			if result.get('detail') == 'not found':
				return jsonify(result), 404 #return error
			return jsonify(result), 200 #return succes
		#if one of constants do not pass
		except KeyError:
			return jsonify({'detail': 'You do not pass one of this constants (search/include_cars)'}), 400 #return error
	else:
		try:
			#get all arguments
			first_name = request.form['first_name']
			last_name = request.form['last_name']
			birth_date = request.form['birth_date']
			gender = request.form['gender']
			#add new owner
			insert.insert_owner(first_name, last_name, birth_date, gender)
			return jsonify({'detail': 'owner created'}), 201 #return succes
		#if one of constants do not pass
		except KeyError:
			return jsonify({'detail': 'You do not pass one of this constants (first_name/last_name/birth_date/gender)'}), 400 #return error

#create route "/car"
@app.route('/car', methods = ['POST'])
def car():
	try:
		#get all arguments
		brand = request.form['brand']
		model = request.form['model']
		owner = request.form['owner']
		color = request.form['color']
		fuel_type = request.form['fuel_type']
		new_or_used = request.form['new_or_used']
		#check owner created
		if insert.insert_car(brand, model, owner, color, fuel_type, new_or_used):
			return jsonify({'detail': 'car added'}), 201 #return succes
		else:
			return jsonify({'detail': f'that owner ({owner}) was not created'}), 400 #return error
	#if one of constants do not pass
	except KeyError:
		return jsonify({'detail': 'You do not pass one of this constants (brand/model/owner/color/fuel_type/new_or_used)'}), 400 #return error

if __name__ == '__main__':
	app.run(debug = True)
