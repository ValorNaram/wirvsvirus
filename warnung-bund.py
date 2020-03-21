#!/usr/bin/env python3
from utils import *
import os

def main():
	outDir = "warnungBund"
	source = "Bundesamt für Bevölkerungsschutz und Katastrophenhilfe"
	outMeta = os.path.join(outDir, "meta")
	outContent = os.path.join(outDir, "content")
	fetcher = fetchingData("https://warnung.bund.de/bbk.mowas/gefahrendurchsagen.json")
	
	data = fetcher.fetchData()
	if data == None:
		print("Error")
		return False
	for message in data:
		cluster = dataClustering()
		message["sent"] = message["sent"].split("+")[0]
		
		status = message["status"]
		if status.lower() == "actual":
			status = "current"
		elif status.lower() == "obsolete":
			status = "obsolete"
		
		cluster.fillInMeta(message["identifier"], message["sent"], source, "", status)
		
		info = message["info"][0]
		description = [info["description"]]
		if "instruction" in info:
			description.append("<b>" + info["instruction"] + "</b>")
		cluster.fillInContent(message["identifier"], info["headline"], "<br/>".join(description))
		
		cluster.saveMeta(os.path.join(outMeta, message["identifier"] + ".json"))
		cluster.saveContent(os.path.join(outMeta, message["identifier"] + ".json"))
if __name__ == "__main__":
	main()
