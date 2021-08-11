# Car-api

Routes: <br/>
**For create owner** -POST: "/owner", Arguments: first_name (Owner name) (Type: String), last_name (Owner surname) (Type: String), birth_date (Owner birth date in format (day.month.year)) (Type: String), gender (Owner gender (male/female)) (Type: String)

**For add car for owner** -POST: "/car", Arguments: brand (Car brand) (Type: String), model (Car model) (Type: String), owner (Car owner (Name and surname)) (Type: String), color (Car color) (Type: String), fuel_type (Car fuel type (gasoline/gas/diesel/electricity)) (Type: String), new_or_used (If the car is new, set it to True, otherwise if it is used, set it to False) (Type: Boolean) <br/>
*Note: if such an owner does not exist, an error will be returned*

**For get owner information** -GET: "/owner", Arguments: search (Onwer name or surname) (Type: String), include_cars (Include cars or no(True/False)) (Type: Boolean), limit(Limit of owners count) (Type: Int) (Not necessarily), offset (How many owners to miss) (Type: Int) (Not necessarily)

<hr/>

**Examples:** <br/>
1. **Add new owner:** <br/>
  -POST: "/owner" (data = {'first_name': 'John', 'last_name': 'Doe', 'birth_date': '19.05.1999', 'gender': 'male}) <br/>
  Answers: <br/>
   If owner created successfully: <br/>
   <ul>Body - {'detail': 'owner created'}, status_code - 201</ul> 
   If you missed one of the options: <br/>
   <ul>Body - {'detail': 'You do not pass one of this constants (first_name/last_name/birth_date/gender)'}, status_code - 400</ul> <br/>

2. **Add new car:** <br/>
  -POST "/car" (data = {'brand': 'Volkswagen', 'model': 'Golf SportWagen 1.4T SE', 'owner': 'John Doe', 'color': 'Silver', 'fuel_type': 'gas', 'new_or_used': False} <br/>
  If car added successfully: <br/>
    + Body - {'detail': 'car added'}, status_code - 201 <br/>
  If you missed one of the options: <br/>
    + Body - {'detail': 'You do not pass one of this constants (brand/model/owner/color/fuel_type/new_or_used)'}, status_code - 400 <br/>
  If such an owner does not exist: <br/>
    + Body - {'detail': f'that owner (John Doe) was not created'}, status_code - 400 <br/>
    
3. **Get owner information:** <br/>
  -GET "/owner?search=Doe&include_cars=True" <br/>
  If request was successfully: <br/>
    + Body - {"result": [{ <br/>
                "age": 22, <br/>
                "cars": [{ <br/>
                  "brand": "Volkswagen",  <br/>
                  "color": "Silver", <br/>
                  "fuel_type": "gas", <br/>
                  "model": "Golf SportWagen 1.4T SE", <br/>
                  "new": "False"<br/>
                } <br/>
                ], <br/>
                "first_name": "John", <br/>
                "gender": "male", <br/>
                "last_name": "Doe" <br/>
            }], <br/>
            "total_count": 1}, <br/>
    + status_code - 200 <br/>
    + Variables: <br/>
      + restult - (All owners on request) (Type: List) <br/>
        + age - (Age of the owner) (Type: Int) <br/>
        + cars - (All car owners) (Type: List): <br/>
        + brand - (Car brand) (Type: String) <br/>
        + color - (Car color) (Type: String) <br/>
        + fuel_type - (Car fuel type) (Type: String) <br/>
        + model - (Car model) (Type: String) <br/>
        + new - (Car condition) (Type: String) <br/>
        + first_name - (Name of the owner) (Type: String) <br/>
        + gender - (Gender of the owner) (Type: String) <br/>
        + last_name - (Surname of the owner) (Type: String) <br/>
      + total_count - (How many owners were found) (Type: Int) <br/>
 <br/>
  If nothing could be found: <br/>
  <ul>Body - {'detail': 'not found'}, status_code - 404</ul> <br/>
  If you missed one of the options: <br/>
  <ul>Body - {'detail': 'You do not pass one of this constants (search/include_cars)'}, status_code - 400</ul> <br/>
<br/>
<br/>
Enjoy using our api
       
      

