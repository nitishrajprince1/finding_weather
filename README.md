# Get Any City Weather Data in Json or XML format

1. Create a virtual environment
2. Install all the required packages from requirments
pip install -r requirements.txt
3. you can put API key in constant or in .env
4. open ipython

## Code:


now you can use 'get_weather' function to get data in your desired format
example
we have to get weather of 'London' in 'XML' format


from app import *
get_weather('London','xml')
