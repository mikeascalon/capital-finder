from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # s = self.path
        # print(s)
        # url_components = parse.urlsplit(s)
        # query_string_list = parse.parse_qsl(url_components.query)
        # dic = dict(query_string_list)

        # country_name = dic.get("country_name")
        # capital = dic.get("capital")
        # if country_name in dic:  # Corrected the key to "country_name"
        #     url = "https://restcountries.com/v3.1/name/"
        #     # country_name = dic[country_name]

        #     r = requests.get(url + country_name)
        
        #     data = r.json()
        #     # informations = []

        #     # for countries in data:
        #     #     if "capital" in countries:  # Check if "capital" key exists
        #     #         capital = countries["capital"]
        #     #         informations.append(capital)
        #     # message = str(informations)
        #     message = "country found"

        # else:
        #     message = "Give me a country to find the capital please"
        message = "country found"
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return 
