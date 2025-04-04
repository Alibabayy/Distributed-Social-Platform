"Deal with lastfm API"
# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# yiyang feng
# yiyangf2@uci.edu
# 66462506

# API key: def90821a201304004583d74b9f2b6ac


from WebAPI import WebAPI


class WrongAPIKeyError(Exception):
    "test"


class LastFM(WebAPI):
    "class LastFM"
    def __init___(self):
        "set the apikey to None firstly"
        self.apikey = None

    def load_data(self):
        if self.apikey is None:
            print('Please set a correct API key firstly')
            raise WrongAPIKeyError
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=PinkPantheress&api_key={self.apikey}&format=json"
        url2 = f'http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist=PinkPantheress&api_key={self.apikey}&format=json'
        last_obj = self._download_url(url)
        last_obj2 = self._download_url(url2)
        if last_obj is not None:
            self.name = last_obj['artist']['name']
        if last_obj2 is not None:
            self.album = last_obj2["topalbums"]['album'][0]['name']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        if '@lastfm' in message:
            message = message.replace('@lastfm', self.name)
        if '@album' in message:
            message = message.replace('@album', self.album)
        return message
