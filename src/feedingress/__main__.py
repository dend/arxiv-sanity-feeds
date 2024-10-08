from feedingress.scraper import engine
import os

print('Arxiv Sanity Feed Scraper - Version 0.0.3')
connection_string = os.getenv('AZ_STORAGE_CS')

# There is nothing here just yet.
feed = None

# Get the main feed
print('Scraping main feed.')
data = engine.Engine.scrape("https://arxiv-sanity-lite.com/")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Home Feed", feed_description="Most recent Arxiv papers.", feed_link="https://hedgehog.den.dev/feeds/home.xml")
else:
	print('No data to process the feed.')

if feed != None:
	engine.Engine.upload_feed(feed, connection_string, feed_name="home.xml")

# Get top weekly papers
print('Scraping weekly feed.')
feed = None
data = engine.Engine.scrape("https://arxiv-sanity-lite.com/?q=&rank=time&tags=all&pid=&time_filter=7")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Recent Feed (Week)", feed_description="Top papers based on people's libraries.", feed_link="https://hedgehog.den.dev/feeds/toprecent-week.xml")
else:
	print('No data to process the feed.')

if feed != None:
	engine.Engine.upload_feed(feed, connection_string, feed_name="toprecent-week.xml")

# Get top hyped papers for the past day
print('Scraping random (last week) feed.')
feed = None
data = engine.Engine.scrape("https://arxiv-sanity-lite.com/?rank=random&time_filter=7")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Random Papers Feed (Last Week)", feed_description="Random papers from last week.", feed_link="https://hedgehog.den.dev/feeds/random-last-week.xml")
else:
	print('No data to process the feed.')

if feed != None:
	engine.Engine.upload_feed(feed, connection_string, feed_name="random-last-week.xml")
