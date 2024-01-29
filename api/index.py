from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "capital" in dic:
            url = "https://restcountries.com/v3.1/name/"
            country_name = dic["capital"]

            r = requests.get(url + dic["country_name"])
        
            data = r.json()
            informations = []

            for word_data in data:
                if "capital" in word_data:  # Check if "capital" key exists
                    capital = word_data["capital"][0]  # Corrected "captital" to "capital"
                    informations.append(capital)
            message = str(informations)

        else:
            message = "Give me a country to find the capital please"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return