from flask import Flask, redirect, render_template
from flask_pymongo import PyMongo
from mars_scrape import scrape

app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_db')
mars = mongo.db.mars

@app.route('/')
def index():
    mars.find_one()
    return render_template('index.html', mars = mars)

@app.route('/scrape')
def scrape_mars():
    data = scrape()
    mars.update({},data,upsert=True)
    return redirect('/')
    
if __name__=='__main__':
    app.run(debug=True)