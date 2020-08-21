from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/api')
def api():
    url = 'https://techverse.info/askmattrab-new-milestone-achieved-for-online-learning-in-nepal'
    d = {}
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    d['title'] = soup.find('h1', {'class': 'single-title'}).text
    return d
