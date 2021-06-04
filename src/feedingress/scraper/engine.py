from bs4 import BeautifulSoup
import requests
import re
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from email import utils

class Engine:
	def scrape(url):
		try:
			re_data = re.compile(r'\[{"abstract":.+;\n')

			raw_html = requests.get(url).text
			parsed_html = BeautifulSoup(raw_html, features="html.parser")

			scripts = parsed_html.find_all("script")
			for script in scripts:
				script_content = script.string
				if (script_content != None):
					matched = re_data.search(script_content)
					if (matched != None):
						# The last character here is a semicolon that needs to be
						# removed for the JSON to be parsed.
						# This seems very hacky, but it gets the job done for now.
						data = str(matched.group(0))[:-2]
						return json.loads(data)
		except Exception as ex:
			print(f"Failed to get Arxiv Sanity content. Error: {ex}")

	def spawn_feed(paper_json, feed_title, feed_description, feed_link):
		rss = ET.Element("rss")
		rss.set("version", "2.0")
		channel = ET.SubElement(rss, "channel")
		title = ET.SubElement(channel, "title")
		title.text = feed_title
		description = ET.SubElement(channel, "description")
		description.text = feed_description
		link = ET.SubElement(channel, "link")
		link.text = feed_link
		atom_link = ET.SubElement(channel, "atom:link")
		atom_link.set("href", feed_link)
		atom_link.set("rel", "self")
		atom_link.set("type", "application/rss+xml")

		for paper in paper_json:
			item = ET.SubElement(rss, "item")
			item_title = ET.SubElement(item, "title")
			item_title.text = paper["title"]
			for paper_author in paper["authors"]:
				item_creator = ET.SubElement(item, "dc:creator")
				item_creator.text = paper_author
			item_description = ET.SubElement(item, "description")
			item_description.text = paper["abstract"]
			item_link = ET.SubElement(item, "link")
			item_link.text = paper["link"]
			item_guid = ET.SubElement(item, "guid")
			item_guid.set("isPermaLink", "true")
			item_guid.text = paper["link"]
			datetime_object = datetime.strptime(paper["published_time"], "%m/%d/%Y")
			item_date_value = utils.format_datetime(datetime_object)
			item_date = ET.SubElement(item, "pubDate")
			item_date.text = item_date_value

		print(ET.tostring(rss))

