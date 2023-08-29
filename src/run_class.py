import requests.exceptions
from requests import Response
from src.compound import Compound
from abc import ABC, abstractmethod
import os
import requests

"""    Работа c Api """

class Run(ABC):
    @abstractmethod
    def get_request(self) -> Response:
        pass


class HH(Run):#Run
    def __init__(self, keyword, page = 1):
        self.url = "https://api.hh.ru/vacancies/"
        self.params = {"text":keyword, "page": page, "per_page":50,"search_field": 'name'}


    def get_request(self):
        request = requests.get(self.url, params = self.params)
        return request


class Superjob(Run):
    def __init__(self, keyword, page = 0):
        self.url = "https://api.syperjob.ru/2.0/vacancies/"
        self.params = {"keywords[0][keys]": keyword, "page": page, "count":50}


    def get_request(self):
        headers = {"X-Api-App-Id": os.environ.get("SUPERJOB_API_KEY")}
        return requests.get(self.url, headers = headers, params = self.params)