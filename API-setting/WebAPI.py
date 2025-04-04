"The parent class"
# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Yiyang feng
# yiyangf2@uci.edu
# 66462506

from abc import ABC, abstractmethod
import urllib
import json
import urllib.request


class InvalidDataFormatError(Exception):
    "test"


class LossConnectionError(Exception):
    "test"


class WrongAPIError(Exception):
    "test"


class WebAPI(ABC):
    "class WebAPI inherit from ABC"
    def _download_url(self, url_to_download: str) -> dict:
        response = None
        r_obj = None
        try:
            request = urllib.request.Request(url_to_download)
            response = urllib.request.urlopen(request)
            json_result = response.read()
            r_obj = json.loads(json_result)
        except urllib.error.URLError:
            print('Loss of connection to the Internet.')
            raise LossConnectionError
        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
            raise WrongAPIError
        except ValueError as exc:
            print("The data received from remote API is not a json message.")
            raise InvalidDataFormatError
        finally:
            if response is not None:
                response.close()
        return r_obj

    def set_apikey(self, apikey: str) -> None:
        "set apikey"
        self.apikey = apikey

    @abstractmethod
    def load_data(self):
        "load data parent function"

    @abstractmethod
    def transclude(self, message: str) -> str:
        "transclude parent function"
