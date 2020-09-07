from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from flask_apscheduler import APScheduler
import requests
import json

app = Flask(__name__)
scheduler = APScheduler()
@app.route('/')
def index():
    return "<br><br><h1 align='center'>Hi from Kisan-Backend.</h1><p align='center'>Empowering farmers.</p>"

@app.route('/sancharkendra')
def sancharkendra():

    res = requests.get('https://sancharkendra.com/archives/category/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('div',{'class':'flxi skcatpg'})

    collections = []
    article_id = 0

    for article in articles:
        d = {}
        append_flag = True
        article_id += 1
        d['id'] = article_id
        try:
            d['image_url'] = article.find('img').get('src')
        except:
            append_flag = False
        d['article_url'] = article.find('a').get('href')
        d['headline'] = article.find('h4').text.strip()

        if append_flag == True:
            collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')


@app.route('/ekantipur')
def ekantipur():

    res = requests.get('https://ekantipur.com/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('article',{'class':'normal'})

    collections = []
    article_id = 0

    for article in articles:
        d = {}
        append_flag = True
        article_id += 1
        d['id'] = article_id
        try:
             d['image_url'] = article.find('img').get('data-src')
        except:
             append_flag = False
        d['article_url'] = 'https://ekantipur.com/' + article.find('a').get('href')
        d['headline'] = article.find('h2').text.strip()
        d['description'] = (article.find('p')).text.strip()

        if append_flag == True:
            collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')

@app.route('/gorkhapatra')
def gorkhapatra():

    res = requests.get('https://gorkhapatraonline.com/mainnews')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('div',{'class':'business'})

    collections = []
    article_id = 0

    for article in articles:
        d = {}
        append_flag = True
        article_id += 1
        d['id'] = article_id
        d['date'] = article.find('span').text.strip()
        try:
             d['image_url'] = article.find('img').get('src')
        except:
             append_flag = False
        d['article_url'] = article.find('a').get('href')
        d['headline'] = article.find('p',{'class':'trand middle-font'}).text.strip()
        d['description'] = article.find('p',{'class':'description'}).text.strip()

        if append_flag == True:
            collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')

@app.route('/onlinekhabar')
def onlinekhabar():

    res = requests.get('http://onlinekhabar.com/content/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('div',{'class':'relative'})

    collections = []
    article_id = 0

    for article in articles:
        d = {}
        append_flag = True
        article_id += 1
        d['id'] = article_id
        try:
            d['image_url'] = article.find('img').get('src')
        except:
            append_flag = False
        d['article_url'] = article.find('a').get('href')
        d['headline'] = article.find('a',{'class':'title__regular'}).text.strip()

        if append_flag == True:
            collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')

@app.route('/ratopati')
def ratopati():

    res = requests.get('https://ratopati.com/category/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('div',{'class':'item'})

    collections = []
    article_id = 0

    for article in articles:
        d = {}
        append_flag = True
        article_id += 1
        d['id'] = article_id
        d['date'] = (article.find('span',{'class':'item-meta'})).text[11:]
        try:
            d['image_url'] = article.find('img').get('src')
        except:
            append_flag = False
        d['headline'] = article.select('a')[1].text.strip()
        d['article_url'] = 'https://ratopati.com/category/news' + article.find('a').get('href')
        d['description'] = article.find('p').text.strip()

        if append_flag == True:
            collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')

@app.route('/etajakhabar')
def etajakhabar():

    res = requests.get('https://www.etajakhabar.com/category/%e0%a4%b8%e0%a4%ae%e0%a4%be%e0%a4%9a%e0%a4%be%e0%a4%b0/')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('a',{'class':'post-list d-flex'})

    collections = []
    article_id = 0

    for article in articles:
        d = {}
        append_flag = True
        article_id += 1
        d['id'] = article_id
        try:
            d['image_url'] = article.find('img').get('src')
        except:
            append_flag = False
        d['article_url'] = article.get('href')
        d['headline'] = article.find('h5').text.strip()
        d['description'] = article.find('p').text.strip()

        if append_flag == True:
            collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')


@app.route('/news24nepal')
def news24nepal():

    res = requests.get('https://www.news24nepal.tv/')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('div',{'class':'col-md-6 mb-3 news-item'})

    collections = []
    article_id = 0

    for article in articles:
        d = {}
        append_flag = True
        article_id += 1
        d['id'] = article_id
        try:
            d['image_url'] = article.find('img').get('src')
        except:
            append_flag = False
        d['article_url'] = article.find('a').get('href')
        d['date'] = article.find('a').get('href')[27:37]
        d['headline'] = article.find('h6').text.strip()

        if append_flag == True:
            collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')

@app.route('/setopati')
def setopati():

    res = requests.get('https://www.setopati.com/special/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('div',{'class':'items'})

    collections = []
    article_id = 0

    for article in articles:
        d = {}
        append_flag = True
        article_id += 1
        d['id'] = article_id
        try:
             d['image_url'] = article.find('img').get('src')
        except:
             append_flag = False
        try:
             d['article_url'] = article.find('a').get('href')
        except:
             append_flag = False
        try:
             d['date'] = article.find('span',{'class':'time-stamp'}).text.strip()
        except:
             append_flag = False
        try:
             d['headline'] = article.find('span',{'class':'main-title'}).text.strip()
        except:
             append_flag = False

        if append_flag == True:
            collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')

@app.route('/krishidaily')
def krishidaily():

    res = requests.get('https://krishidaily.com/category/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('article', {'class':'listing-item-blog'})

    collections = []
    article_id = 0
    for article in articles:
        d = {}
        append_flag = True
        article_id += 1

        d['id'] = article_id
        d['date'] = article.find('span', {'class': 'time'}).text.strip()
        try:
            d['image_url'] = article.find('a', {'class': 'img-holder'}).get('data-src')
        except:
            append_flag = False
        try:
            d['headline'] = article.find('a', {'class': 'post-title'}).text.strip()
        except:
            append_flag = False
        d['description'] = article.find('div', {'class':'post-summary'}).text.strip()
        d['article_url'] = article.find('a', {'class': 'post-title'}).get('href')

        if append_flag == True:
            collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')

@app.route('/covid19')
def covid19():
    res = requests.get('https://covid19.ekantipur.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    information = soup.find_all('tr',{'class':'district-row'})

    collections = []
    info_id = 0
    for info in information:
        d = {}
        info_id += 1
        d['id'] = info_id
        d['district'] = info.find('span',{'class':'district-name'}).text
        d['infected'] = info.find('td',{'class':'sorting_1'}).text
        d['recovered'] = info.find('span',{'class':'recovered'}).text
        d['deaths'] = info.find('span',{'class':'deaths'}).text
        collections.append(d)

    d = {}
    d['id'] = 78
    d['district'] = None
    d['infected'] = soup.find('span',{'class':'nepal-total'}).text[15:20]
    d['active'] = soup.find('span',{'class':'nepal-total'}).text[28:33]
    d['recovered'] = soup.find('span',{'class':'nepal-total'}).text[50:57]
    d['deaths'] = soup.find('span',{'class':'nepal-total'}).text[41:44]
    collections.append(d)

    return json.dumps(collections, ensure_ascii=False).encode('utf8')

if __name__ == '__main__':
    scheduler.add_job(id = 'schedule_scrap', func =sancharkendra , trigger = 'interval', seconds = 300)
    scheduler.add_job(id = 'schedule_scrap', func =ekantipur , trigger = 'interval', seconds = 300)
    scheduler.add_job(id = 'schedule_scrap', func =gorkhapatra , trigger = 'interval', seconds = 300)
    scheduler.add_job(id = 'schedule_scrap', func =onlinekhabar , trigger = 'interval', seconds = 300)
    scheduler.add_job(id = 'schedule_scrap', func =ratopati , trigger = 'interval', seconds = 300)
    scheduler.add_job(id = 'schedule_scrap', func =etajakhabar , trigger = 'interval', seconds = 300)
    scheduler.add_job(id = 'schedule_scrap', func =news24nepal , trigger = 'interval', seconds = 300)
    scheduler.add_job(id = 'schedule_scrap', func =setopati , trigger = 'interval', seconds = 300)
    scheduler.add_job(id = 'schedule_scrap', func =krishidaily , trigger = 'interval', seconds = 300)
    scheduler.add_job(id = 'schedule_scrap', func =covid19 , trigger = 'interval', seconds = 300)
    scheduler.start()
    app.run()
