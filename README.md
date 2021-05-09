## To run the project:

1. Create a virtual environment with: `pipenv shell`
    
2. Install packages with: `pipenv install -d`

3. Create the Django migrations: `python manage.py makemigrations`

4. Run the migrations: `python manage.py migrate`

## To run the load data command:

`python manage.py read_data --path ./files/backend_project_data.csv`

## API endpoints:

* To get a property by id:
http://localhost:8000/api/v1/house/\<house_id\>

* To query properties by characteristics, the endpoint has 5 comparision types:

    1. lte for <=
    2. lt for <
    3. gte for >=
    4. gt for >
    5. eq for ==


    these can be used with the any characteristics from the properties:
    http://localhost:8000/api/v1/house/?\<characteristic1\>[comparision]=<value>&<characteristic2>[comparision]=\<value\>...
    

    i.e. to get all the houses with at least 2 bathrooms and 4 bedrooms:
    http://localhost:8000/api/v1/house/?bathrooms[gte]=2&bedrooms=4


