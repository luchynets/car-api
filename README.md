# Car-api

Routes:
For create owner -POST: "/owner", Arguments: first_name (Owner name) (Type: String), last_name (Owner surname) (Type: String), birth_date (Owner birth date in format (day.month.year)) (Type: String), gender (Owner gender (male/female)) (Type: String)

For add car for owner -POST: "/car", Arguments: brand (Car brand) (Type: String), model (Car model) (Type: String), owner (Car owner (Name and surname)) (Type: String), color (Car color) (Type: String), fuel_type (Car fuel type (gasoline/gas/diesel/electricity)) (Type: String), new_or_used (If the car is new, set it to True, otherwise if it is used, set it to False) (Type: Boolean)
Note: if such an owner does not exist, an error will be returned

For get owner information -GET: "/owner", Arguments: search (Onwer name or surname) (Type: String), include_cars (Include cars or no(True/False)) (Type: Boolean), limit(Limit of owners count) (Type: Int) (Not necessarily), offset (How many owners to miss) (Type: Int) (Not necessarily)


Examples: 
1. Add new owner:
  -POST: "/owner" (data = {'first_name': 'John', 'last_name': 'Doe', 'birth_date': '19.05.1999', 'gender': 'male})
  Answers:
  If owner created successfully:
    Body - {'detail': 'owner created'}, status_code - 201
  If you missed one of the options:
    Body - {'detail': 'You do not pass one of this constants (first_name/last_name/birth_date/gender)'}, status_code - 400

2. Add new car:
  -POST "/car" (data = {'brand': 'Volkswagen', 'model': 'Golf SportWagen 1.4T SE', 'owner': 'John Doe', 'color': 'Silver', 'fuel_type': 'gas', 'new_or_used': False}
  If car added successfully:
    Body - {'detail': 'car added'}, status_code - 201
  If you missed one of the options:
    Body - {'detail': 'You do not pass one of this constants (brand/model/owner/color/fuel_type/new_or_used)'}, status_code - 400
  If such an owner does not exist:
    Body - {'detail': f'that owner (John Doe) was not created'}, status_code - 400
    
3. Get owner information:
  -GET "/owner?search=Doe&include_cars=True" \n
  If request was successfully:
    Body - {"result": [{
                "age": 22, 
                "cars": [{
                  "brand": "Volkswagen", 
                  "color": "Silver", 
                  "fuel_type": "gas", 
                  "model": "Golf SportWagen 1.4T SE", 
                  "new": "False"
                }
                ], 
                "first_name": "John", 
                "gender": "male", 
                "last_name": "Doe"
            }], 
            "total_count": 1},
    status_code - 200 
    Variables:
      restult - (All owners on request) (Type: List)
        age - (Age of the owner) (Type: Int)
        cars - (All car owners) (Type: List):
          brand - (Car brand) (Type: String)
          color - (Car color) (Type: String)
          fuel_type - (Car fuel type) (Type: String)
          model - (Car model) (Type: String)
          new - (Car condition) (Type: String)
        first_name - (Name of the owner) (Type: String)
        gender - (Gender of the owner) (Type: String)
        last_name - (Surname of the owner) (Type: String)
      total_count - (How many owners were found) (Type: Int)
  If nothing could be found:
    Body - {'detail': 'not found'}, status_code - 404
  If you missed one of the options:
    Body - {'detail': 'You do not pass one of this constants (search/include_cars)'}, status_code - 400
    
  
Enjoy using our api
       
      

