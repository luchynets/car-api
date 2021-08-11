import pymysql
import datetime


def get_data(name, include_cars, limit, offset):
	con = pymysql.connect('localhost', 'root', 'root', 'test_task')
	cur = con.cursor()
	cur.execute("""SELECT * FROM owners WHERE first_name = '%s' OR last_name = '%s'""" % (name, name))
	owners = cur.fetchall()
	result = []
	if len(owners) == 0:
		return {'detail': 'not found'}
	elif limit == None:
		try:
			for i in range(0, len(owners), int(offset)):
				dat = owners[i][3].split('.')
				d = datetime.date(int(dat[2]), int(dat[1]), int(dat[0]))
				now = datetime.datetime.now().date()
				n = now-d
				result.append({'first_name': owners[i][1], 'last_name': owners[i][2], 'age': n.days // 360, 'gender': owners[i][4],})
				if include_cars == 'True':
					cur.execute("""SELECT * FROM cars WHERE owner = '%s'""" % (' '.join([owners[i][1], owners[i][2]])))
					cars = cur.fetchall()
					result[i]['cars'] = [{'brand': car[1], 'model': car[2], 'color': car[4], 'fuel_type': car[5], 'new': car[6]} for car in cars]
		except TypeError:
			for i in range(0, len(owners)):
				dat = owners[i][3].split('.')
				d = datetime.date(int(dat[2]), int(dat[1]), int(dat[0]))
				now = datetime.datetime.now().date()
				n = now-d
				result.append({'first_name': owners[i][1], 'last_name': owners[i][2], 'age': n.days // 360, 'gender': owners[i][4]})
				if include_cars == 'True':
					cur.execute("""SELECT * FROM cars WHERE owner = '%s'""" % (' '.join([owners[i][1], owners[i][2]])))
					cars = cur.fetchall()
					result[i]['cars'] = [{'brand': car[1], 'model': car[2], 'color': car[4], 'fuel_type': car[5], 'new': car[6]} for car in cars]
	else:
		try:
			for i in range(0, int(limit), int(offset)):
				dat = owners[i][3].split('.')
				d = datetime.date(int(dat[2]), int(dat[1]), int(dat[0]))
				now = datetime.datetime.now().date()
				n = now-d
				result.append({'first_name': owners[i][1], 'last_name': owners[i][2], 'age': n.days // 360, 'gender': owners[i][4],})
				if include_cars == 'True':
					cur.execute("""SELECT * FROM cars WHERE owner = '%s'""" % (' '.join([owners[i][1], owners[i][2]])))
					cars = cur.fetchall()
					result[i]['cars'] = [{'brand': car[1], 'model': car[2], 'color': car[4], 'fuel_type': car[5], 'new': car[6]} for car in cars]
		except TypeError:
			for i in range(0, int(limit)):
				dat = owners[i][3].split('.')
				d = datetime.date(int(dat[2]), int(dat[1]), int(dat[0]))
				now = datetime.datetime.now().date()
				n = now-d
				result.append({'first_name': owners[i][1], 'last_name': owners[i][2], 'age': n.days // 360, 'gender': owners[i][4]})
				if include_cars == 'True':
					cur.execute("""SELECT * FROM cars WHERE owner = '%s'""" % (' '.join([owners[i][1], owners[i][2]])))
					cars = cur.fetchall()
					result[i]['cars'] = [{'brand': car[1], 'model': car[2], 'color': car[4], 'fuel_type': car[5], 'new': car[6]} for car in cars]
	con.close()
	return {'result': result, 'total_count': len(owners)}