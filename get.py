#import modules
import pymysql
import datetime


#create func for get owner data
def get_data(name, include_cars, limit, offset):
	con = pymysql.connect('localhost', 'root', 'root', 'test_task') #connect database
	cur = con.cursor() #create cursor
	cur.execute("""SELECT * FROM owners WHERE first_name = '%s' OR last_name = '%s'""" % (name, name)) #get all owners with this name or surname
	owners = cur.fetchall() #list with owners
	result = [] #result
	#check if owners were found
	if len(owners) == 0:
		return {'detail': 'not found'} #return error
	#check limit is set
	elif limit == None:
		try:
			#creating result
			for i in range(0, len(owners), int(offset)):
				dat = owners[i][3].split('.') #get birth date owner
				d = datetime.date(int(dat[2]), int(dat[1]), int(dat[0])) #make owner birth date
				now = datetime.datetime.now().date() #get today date
				n = now-d #owner days old 
				result.append({'first_name': owners[i][1], 'last_name': owners[i][2], 'age': n.days // 360, 'gender': owners[i][4],}) #insert data in result
				#check include cars
				if include_cars == 'True':
					cur.execute("""SELECT * FROM cars WHERE owner = '%s'""" % (' '.join([owners[i][1], owners[i][2]]))) #get all qwner cars
					cars = cur.fetchall() #list with cars
					result[i]['cars'] = [{'brand': car[1], 'model': car[2], 'color': car[4], 'fuel_type': car[5], 'new': car[6]} for car in cars] #insert cars
		#if offset doesn't set
		except TypeError:
			#creating result
			for i in range(0, len(owners)):
				dat = owners[i][3].split('.') #get birth date owner
				d = datetime.date(int(dat[2]), int(dat[1]), int(dat[0])) #make owner birth date
				now = datetime.datetime.now().date() #get today date
				n = now-d #owner days old 
				result.append({'first_name': owners[i][1], 'last_name': owners[i][2], 'age': n.days // 360, 'gender': owners[i][4]}) #insert data in result
				#check include cars
				if include_cars == 'True':
					cur.execute("""SELECT * FROM cars WHERE owner = '%s'""" % (' '.join([owners[i][1], owners[i][2]]))) #get all qwner cars
					cars = cur.fetchall() #list with cars
					result[i]['cars'] = [{'brand': car[1], 'model': car[2], 'color': car[4], 'fuel_type': car[5], 'new': car[6]} for car in cars] #insert cars
	#if limit doesn't set
	else:
		try:
			#creating result
			for i in range(0, int(limit), int(offset)):
				dat = owners[i][3].split('.') #get birth date owner
				d = datetime.date(int(dat[2]), int(dat[1]), int(dat[0])) #make owner birth date
				now = datetime.datetime.now().date() #get today date
				n = now-d #owner days old 
				result.append({'first_name': owners[i][1], 'last_name': owners[i][2], 'age': n.days // 360, 'gender': owners[i][4],}) #insert data in result
				#check include cars
				if include_cars == 'True':
					cur.execute("""SELECT * FROM cars WHERE owner = '%s'""" % (' '.join([owners[i][1], owners[i][2]]))) #get all qwner cars
					cars = cur.fetchall() #list with cars
					result[i]['cars'] = [{'brand': car[1], 'model': car[2], 'color': car[4], 'fuel_type': car[5], 'new': car[6]} for car in cars] #insert cars
		#if offset doesn't set
		except TypeError:
			#creating result
			for i in range(0, int(limit)):
				dat = owners[i][3].split('.') #get birth date owner
				d = datetime.date(int(dat[2]), int(dat[1]), int(dat[0])) #make owner birth date
				now = datetime.datetime.now().date() #get today date
				n = now-d #owner days old 
				result.append({'first_name': owners[i][1], 'last_name': owners[i][2], 'age': n.days // 360, 'gender': owners[i][4]}) #insert data in result
				#check include cars
				if include_cars == 'True':
					cur.execute("""SELECT * FROM cars WHERE owner = '%s'""" % (' '.join([owners[i][1], owners[i][2]]))) #get all qwner cars
					cars = cur.fetchall() #list with cars
					result[i]['cars'] = [{'brand': car[1], 'model': car[2], 'color': car[4], 'fuel_type': car[5], 'new': car[6]} for car in cars] #insert cars
	con.close() #close connection
	return {'result': result, 'total_count': len(owners)} #return result
