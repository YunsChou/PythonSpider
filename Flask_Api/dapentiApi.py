
from flask import Flask
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient()
tdb = client["dapenti"]
caijingDoc = tdb["caijing"]
tuguaDoc = tdb['tugua']
yituDoc = tdb['yitu']

app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello dapenti'

@app.route('/caijing')
def caijing():
	result = caijingDoc.find().skip(0).limit(10)
	return dumps(result)

@app.route('/tugua')
def tugua():
	result = tuguaDoc.find().skip(0).limit(10)
	return dumps(result)

@app.route('/yitu')
def yitu():
	result = yituDoc.find().skip(0).limit(10)
	return dumps(result)

if __name__ == '__main__':
	app.run()
