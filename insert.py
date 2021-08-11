import pymysql


def insert_owner(first_name, last_name, birth_date, gender):
	con = pymysql.connect('localhost', 'root', 'root', 'test_task')
	cur = con.cursor()
	cur.execute("""INSERT INTO owners VALUES (0, '%s', '%s', '%s', '%s')""" % (first_name, last_name, birth_date, gender))
	con.commit()
	con.close()

def insert_car(brand, model, owner, color, fuel_type, new_or_used):
	con = pymysql.connect('localhost', 'root', 'root', 'test_task')
	cur = con.cursor()
	query = cur.execute("""SELECT first_name FROM owners WHERE first_name = '%s' AND last_name = '%s'""" % (owner.split()[0], owner.split()[1]))
	is_owner = cur.fetchall()
	if len(is_owner) > 0:
		cur.execute("""INSERT INTO cars VALUES (0, '%s', '%s', '%s', '%s', '%s', '%s')""" % (brand, model, owner, color, fuel_type, new_or_used))
		con.commit()
		con.close()
		return True
	con.close()
	return False