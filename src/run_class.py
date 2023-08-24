import requests.exceptions
from requests import Response
from src.compound import Сompound
from abc import ABS


class Run(ABS):
    @abstractmethod
    def get_request(self) -> Response:
        pass

class MyJsonError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class HH(Run):
    def __init__(self, keyword):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"text":keyword, "page":page, "per_page":100, "search_field":name}


    def get_request(self):
        try:
            request = requests.get(self.url, params = self.params)
        except requests.exceptions.RequestException as e:
            raise Exception
        else:
            return request


class Superjob(Run):
    def __init__(self, keyword):
        self.url = "https://api.syperjob.ru/2.3/vacancies/"
        self.params = {"keywords[0][keys]":keyword, "keywords[0][srws]":4, "keywords[0][skws]":"or",
                       "page":page, "count":100 }


    def get_request(self):
        X_Api_App_Id = "4AnW8a8QcKLXKU1UY7neWPYPupYN35XJdRTnSf525nFVQ4oYnF8BSVrGRT1hKzPusP5PS7pJzkDbBZoosSydENe9CUjhCMX"
        headers = {"X_Api_App_Id":os_environ["SUPERJOB_API_KEY"]}