# testing endpoints with python http requests
import requests

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()  # gets json data and converts into python list
    print(type(data))
    for obj in data:
        print(obj['id'])
    return r.json()


get_list()
