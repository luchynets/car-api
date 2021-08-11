#import modules
import pymysql

 #create func for add owners
def insert_owner(first_name, last_name, birth_date, gender):
	con = pymysql.connect('localhost', 'root', 'root', 'test_task') #connect for database
	cur = con.cursor() #create cursor
	cur.execute("""INSERT INTO owners VALUES (0, '%s', '%s', '%s', '%s')""" % (first_name, last_name, birth_date, gender)) #insert data
	con.commit() #commit changes
	con.close() #close connection

def insert_car(brand, model, owner, color, fuel_type, new_or_used):
	con = pymysql.connect('localhost', 'root', 'root', 'test_task') #connect for database
	cur = con.cursor() #create cursor
	#check owner created
	query = cur.execute("""SELECT first_name FROM owners WHERE first_name = '%s' AND last_name = '%s'""" % (owner.split()[0], owner.split()[1]))
	is_owner = cur.fetchall()
	if len(is_owner) > 0:
		cur.execute("""INSERT INTO cars VALUES (0, '%s', '%s', '%s', '%s', '%s', '%s')""" % (brand, model, owner, color, fuel_type, new_or_used)) #insert data
		con.commit() #commit changes
		con.close() #close connection
		return True #return succes
	con.close() #close connection
	return False #return not succes 
