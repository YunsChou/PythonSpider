
from flask import Flask, jsonify
import pymongo
from bson import json_util
#http://api.mongodb.com/python/current/api/bson/json_util.html

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
	print(type(result))
	# 推荐：使用bson将mongo中的数据转为json
	return json_util.dumps(result)
	# 测试：使用jsonify处理mongo中的数据转为json
	# items = []
	# for item in result:
	# 	print(dict(item))
	# 	items.append({'title':item['title'],'imgsrc':item['imgsrc'], 'quote':item['quote']})
	# print (json_util.dumps(list(result)))
	# return jsonify(items)

if __name__ == '__main__':
	app.run()