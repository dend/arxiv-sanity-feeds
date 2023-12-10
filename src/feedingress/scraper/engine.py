from bs4 import BeautifulSoup
import requests
import re
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from email import utils

class Engine:
	# Default timeout, in seconds, for all requests.
	TIMEOUT = 30

	@classmethod
	def scrape(cls, url):
		try:
			re_data = re.compile(r'\[{"authors":.+;\n')

			raw_html = requests.get(url, timeout=cls.TIMEOUT).text
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

	@staticmethod
	def spawn_feed(paper_json, feed_title, feed_description, feed_link):
		rss = ET.Element("rss")
		rss.set("version", "2.0")
		rss.set("xmlns:atom", "http://www.w3.org/2005/Atom")
		rss.set("xmlns:dc", "http://purl.org/dc/elements/1.1/")
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

		if paper_json != None:
			for paper in paper_json:
				item = ET.SubElement(channel, "item")
				item_title = ET.SubElement(item, "title")
				item_title.text = paper["title"]
				for paper_author in [x.strip() for x in paper["authors"].split(',')]:
					item_creator = ET.SubElement(item, "dc:creator")
					item_creator.text = paper_author
				item_description = ET.SubElement(item, "description")
				item_description.text = paper["summary"]
				item_link = ET.SubElement(item, "link")
				item_link.text = f'https://arxiv.org/abs/{paper["id"]}'
				item_guid = ET.SubElement(item, "guid")
				item_guid.set("isPermaLink", "true")
				item_guid.text = f'https://arxiv.org/abs/{paper["id"]}'
				datetime_object = datetime.strptime(paper["time"], "%b %d %Y")
				item_date_value = utils.format_datetime(datetime_object)
				item_date = ET.SubElement(item, "pubDate")
				item_date.text = item_date_value

			return ET.tostring(rss, encoding='utf-8', method='xml', xml_declaration=True).decode()
		return None



