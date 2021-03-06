import future,bs4,pymongo, xmltodict, json, os
import urllib2 as request

from bson.json_util import dumps



from flask import Flask

#Establish mongodb connection here

try:
    connection = pymongo.MongoClient("mongodb://mongo")
except pymongo.errors.ConnectionFailure as e:
    print(e)

db=connection.book
record1 = db.book_collection1

url="http://thecatapi.com/api/images/get?format=xml&results_per_page=1&api_key=os.environ['API_KEY']"


app = Flask(__name__)

@app.route('/cat')
def cat():

    cat_response = request.urlopen(url) #get the url
    xml_doc = bs4.BeautifulSoup(cat_response.read(), "xml") #parse xml
    # Form the JSON from XML
    string={'url': xml_doc.find('url').get_text(), 'id': xml_doc.find('id').get_text(), 'source_url': xml_doc.find('source_url').get_text()}
    my_json_string = json.dumps({"image": string})
    #Insert the JSON into MongoDb
    record1.insert(string)
    return my_json_string + '\n'


@app.route('/history')
def index1():

    cursor = record1.find({},{"_id":False}) #get the whole json except for the objectID
    history= dumps({"images" : list(cursor)}) #serialize the string
    return history + '\n'

@app.errorhandler(404)
def page_not_found(e):
    return "Your endpoints have to be either /cat or /history\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
