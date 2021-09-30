from re import findall
from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app)



@app.route('/api/v1/', methods=['GET'])
def API():
    if request.method == 'GET':
        uri = 'https://www.brainyquote.com/'
        query = str(request.args['query'])

        if " " in query:
            query = str(query).replace(" ", "+")
        else:
            pass

        search1 = 'search_results?q=' + query
        search = 'search_results?x=0&y=0&q=' + query
        ready_url = uri + search
        content = requests.get(ready_url).content
        soup = BeautifulSoup(content, 'html.parser')
        quotes_links = soup.find_all('a', {'class': 'b-qt'})
        l = []
        for i in quotes_links:
            d = {}
            quote_url = uri + i.get('href')
            quote_content = requests.get(quote_url).content
            quote_soup = BeautifulSoup(quote_content, 'html.parser')
            d['quote'] = quote_soup.find('p', {'class': 'b-qt'}).text
            d['author'] = str(quote_soup.find('p', {'class': 'bq_fq_a'}).text).strip()
            l.append(d)

        return jsonify(l)



if __name__ == '__main__':
    app.run()




""""
@app.route("/api", methods=['GET'])
def hello_world():
    
    d = {}      
    d['Query'] = str(request.args['Query'])
    return jsonify(d)
   
if __name__ == '__main__':
    app.run()


    str(quote_soup.find('p', {'class': 'bg_fq_a'}).text).strip()
"""
