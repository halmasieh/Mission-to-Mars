# Import dependencies
# Use Flask to render a template.
from flask import Falsk, render_template
# Use PyMongo to interact with our Mongo database. 
from flask_pymongo import flask_pymongo
# Use the scraping code to convert from Jupyter notebook to Python
import scraping

# Set up flask
app = Flask(__name__)

# We also need to tell Python how to connect to Mongo using PyMongo.
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template(index.html, mars=mars) 

@app.route('/scape')
def scape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.upadte({}, mars_data, upsert=True)
    return redirect('/', code=302)
if __name__ == '__main__':
    app.run()
    