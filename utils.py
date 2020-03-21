#!/usr/bin/env python3
import json, requests
class fetchingData():
	def __init__(self, url):
		self.url = url
	def fetchData(self):
		re = requests.get(self.url)
		if re.status_code == requests.codes.ok:
			return re.json()
		else:
			return None
class dataClustering():
	def __init__(self):
		self.metaTemplate = {"identifier": "",
		"timestamp": "",
		"area": "",
		"source": "",
		"category": "",
		"status": "",
		"tags": ""}
		self.contentTemplate = {"identifier": "", "headline": "", "content": ""}
	def fillInMeta(self, identifier, timestamp, source, tags, status=None, category=None, area=None):
		self.metaTemplate["identifier"] = identifier
		self.metaTemplate["timestamp"] = timestamp
		self.metaTemplate["source"] = source
		self.metaTemplate["status"] = status
		self.metaTemplate["category"] = category
		self.metaTemplate["tags"] = tags
		self.metaTemplate["area"] = area
	def fillInContent(self, identifier, headline, content):
		self.contentTemplate["identifier"] = identifier
		self.contentTemplate["headline"] = headline
		self.contentTemplate["content"] = content
	def saveMeta(self, path):
		sfile = open(path, "w")
		sfile.write(json.dumps(self.metaTemplate, ensure_ascii=False))
		sfile.close()
	def saveContent(self, path):
		sfile = open(path, "w")
		sfile.write(json.dumps(self.contentTemplate, ensure_ascii=False))
		sfile.close()
