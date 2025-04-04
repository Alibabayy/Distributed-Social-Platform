"OpenWeather Class"
# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# yiyang feng
# yiyangf2@uci.edu
# 66462506


from WebAPI import WebAPI


class WrongAPIKeyError(Exception):
    "Test"


class OpenWeather(WebAPI):
    "Openweather class"
    def __init__(self, zipcode, ccode):
        self.zipcode = zipcode
        self.ccode = ccode
        self.apikey = None

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''
        if self.apikey is None:
            print('Please set a correct API key firstly')
            raise WrongAPIKeyError
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
        weather_obj = self._download_url(url)
        if weather_obj is not None:
            self.temperature = round((weather_obj['main']['temp'] - 273.15), 2)
            self.high_temperature = round((weather_obj['main']['temp_max'] - 273.15), 2)
            self.low_temperature = round((weather_obj['main']['temp_min'] - 273.15), 2)
            self.longitude = weather_obj["coord"]['lon']
            self.latitude = weather_obj['coord']['lat']
            self.description = weather_obj['weather'][0]['description']
            self.humidity = weather_obj['main']['humidity']
            self.city = weather_obj['name']
            self.sunset = weather_obj['sys']['sunset']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        if '@temperature' in message:
            message = message.replace('@temperature', str(self.temperature))
        if '@weather' in message:
            message = message.replace('@weather', self.description)
        return message
