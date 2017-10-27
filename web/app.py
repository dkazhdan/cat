import future,bs4,pymongo, xmltodict, json
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

url="http://thecatapi.com/api/images/get?format=xml&results_per_page=1"


app = Flask(__name__)

@app.route('/cat')
def cat():

    cat_response = request.urlopen(url) #get the url
    xml_doc = bs4.BeautifulSoup(cat_response.read(), "xml") #parse xml
    string={'url': xml_doc.find('url').get_text(), 'id': xml_doc.find('id').get_text(), 'source_url': xml_doc.find('source_url').get_text()}
    my_json_string = json.dumps({"image": string})
    #record1.drop()
    record1.insert(string)
    return my_json_string + '\n'


@app.route('/history')
def index1():

    cursor = record1.find({},{"_id":False}) #get the whole json except for the objectID
    history= dumps({"images" : list(cursor)}) #serialize the string
    return history + '\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
