from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
       
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        country_name = dic.get("country")
        capital = dic.get("capital")
       
        if country_name:
            url = f"https://restcountries.com/v3.1/name/{country_name}"

            r = requests.get(url)
            data = r.json()
            if data and isinstance(data, list) and "capital" in data[0]:
                capital_info = data[0]["capital"]
                join_capitals = " and ".join(capital_info)
                message = f"The capital of {country_name} is {join_capitals}"
            else:
                message = f"Capital information not found for {country_name}."

        elif capital:
            url = f"https://restcountries.com/v3.1/capital/{capital}"
  
            r = requests.get(url)
            data = r.json()
            if data and isinstance(data, list) and "name" in data[0]:
                country_name = data[0]["name"]["common"]
                message = f"The country with capital {capital} is {country_name}."
            else:
                message = f"No country found with capital {capital}."
        else:
            message = "Please provide a valid 'country' or 'capital' query parameter."
    

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return 
