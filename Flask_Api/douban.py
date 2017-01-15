
from flask import Flask, jsonify
import pymongo
from bson import json_util

client = pymongo.MongoClient()
tdb = client["movie"]
doc = tdb["doubanTop250"]

app = Flask(__name__)

@app.route('/')
def sayHello():
	return 'hello douban'

@app.route('/movie')
def doubanMovie():
	result = doc.find().skip(0).limit(10)
	return json_util.dumps(list(result))
	# items = []
	# for item in result:
	# 	print(dict(item))
	# 	items.append({'title':item['title'],'imgsrc':item['imgsrc'], 'quote':item['quote']})
	# print (json_util.dumps(list(result)))
	# return jsonify(items)

if __name__ == '__main__':
	app.run()