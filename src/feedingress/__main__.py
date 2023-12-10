from feedingress.scraper import engine
from feedingress.scraper.storage import local
import os

print('Arxiv Sanity Feed Scraper - Version 0.0.3')
feedHost = os.getenv('FEED_HOST', 'https://hedgehog.den.dev/feeds')

storages= list()

# if os.getenv('DO_SPACES_ACCESS_KEY'):
# 	from feedingress.scraper.storage import DigitalOcean
 
# 	Region = os.getenv('DO_SPACES_REGION')
# 	endpoint = os.getenv('DO_SPACES_ENDPOINT')
# 	DO_access_key = os.getenv('DO_SPACES_ACCESS_KEY')
# 	DO_secret_key = os.getenv('DO_SPACES_SECRET_KEY')

# 	storages.append(DigitalOcean(region, endpoint, DO_access_key, DO_secret_key))

storages.append(local('./feeds'))

# There is nothing here just yet.
feed = None

# Get the main feed
print('Scraping main feed.')
data = engine.Engine.scrape("https://arxiv-sanity-lite.com/")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Home Feed", feed_description="Most recent Arxiv papers.", feed_link=f"{feedHost}/feeds/home.xml")
else:
	print('No data to process the feed.')

if feed != None:
	for storage in storages:
		storage.upload_feed(feed, "home.xml")

# Get top weekly papers
print('Scraping weekly feed.')
feed = None
data = engine.Engine.scrape("https://arxiv-sanity-lite.com/?q=&rank=time&tags=all&pid=&time_filter=7")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Recent Feed (Week)", feed_description="Top papers based on people's libraries.", feed_link=f"{feedHost}/feeds/toprecent-week.xml")
else:
	print('No data to process the feed.')

if feed != None:
	for storage in storages:
		storage.upload_feed(feed, "toprecent-week.xml")

# Get top hyped papers for the past day
print('Scraping random (last week) feed.')
feed = None
data = engine.Engine.scrape("https://arxiv-sanity-lite.com/?rank=random&time_filter=7")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Random Papers Feed (Last Week)", feed_description="Random papers from last week.", feed_link=f"{feedHost}/feeds/random-last-week.xml")
else:
	print('No data to process the feed.')

if feed != None:
	for storage in storages:
		storage.upload_feed(feed, "random-last-week.xml")
