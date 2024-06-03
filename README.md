# Django Weather App

This is a simple Django web application that allows users to view weather data for cities stored within the database. 
Users can also add new cities to the list and see the current weather data for all listed cities. 
User can clear the existing cities by resetting
The weather data is retrieved from the OpenWeatherMap API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.6 or higher)
- Django (3.0 or higher) (`pip install django`)
- Requests library (`pip install requests`)

### Installing

1. Clone the repository to your local machine:

```bash
git clone https://github.com/sumitsharmamanit/weatherapp.git
```


2. Navigate to the project directory:

```bash
cd weather_app
```


3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and set it in the `settings.py` file:

2. 
```python
# weather_app/settings.py
OPEN_WEATHER_API_KEY = 'your-api-key'
```

### Running the Application
1. Apply database migrations:
```python
python manage.py makemigrations
python manage.py migrate
```

2. Start the Django development server:
```python 
python manage.py runserver
```

3. Access the application in your web browser at http://localhost:8000

### Usage
To use the application, follow these steps:

1. Open your web browser.
2. Navigate to the URL where the application is hosted.
3. You will see the homepage with weather data for cities already in the database.
4. To add a new city, enter the city name in the input field and click "Add City".
5. The weather data for the newly added city will be displayed on the homepage.

### Running Tests
To run the automated tests for this system, use the following command:
```python
python manage.py test weather_api.tests
```

### Built With
- Django - The web framework used
- OpenWeatherMap API - Used to retrieve weather data
- Requests - HTTP library for making API requests
