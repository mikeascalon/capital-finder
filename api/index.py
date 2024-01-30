# from http.server import BaseHTTPRequestHandler
# from urllib import parse
# import requests

# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         s = self.path
#         print(s)
#         url_components = parse.urlsplit(s)
#         query_string_list = parse.parse_qsl(url_components.query)
#         dic = dict(query_string_list)

#         country_name = dic.get("country_name")
#         if country_name:  # Check if country_name is not None
#             url = "https://restcountries.com/v3.1/name/"

#             r = requests.get(url + country_name)
        
#             if r.status_code == 200:
#                 data = r.json()
#                 if isinstance(data, list) and len(data) > 0:
#                     capital = data[0].get("capital")
#                     if capital:
#                         message = f"The capital of {country_name} is {capital}"
#                     else:
#                         message = f"No capital information found for {country_name}"
#                 else:
#                     message = f"Country {country_name} not found"
#             else:
#                 message = "Error fetching data from the API"
#         else:
#             message = "Give me a country_name to find the capital please"

#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()

#         self.wfile.write(message.encode())

#         return

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = "Howdy"
        self.wfile.write(message.encode())
        return
