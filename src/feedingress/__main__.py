from feedingress.scraper import engine
import os

print('Arxiv Sanity Feed Scraper - Version 0.0.2')
region = os.getenv('DO_SPACES_REGION')
endpoint = os.getenv('DO_SPACES_ENDPOINT')
access_key = os.getenv('DO_SPACES_ACCESS_KEY')
secret_key = os.getenv('DO_SPACES_SECRET_KEY')

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
	engine.Engine.upload_feed(feed, region, endpoint, access_key, secret_key, feed_name="home.xml")

# Get top weekly papers
print('Scraping weekly feed.')
feed = None
data = engine.Engine.scrape("https://arxiv-sanity-lite.com/?q=&rank=time&tags=all&pid=&time_filter=7")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Recent Feed (Week)", feed_description="Top papers based on people's libraries.", feed_link="https://hedgehog.den.dev/feeds/toprecent-week.xml")
else:
	print('No data to process the feed.')

if feed != None:
	engine.Engine.upload_feed(feed, region, endpoint, access_key, secret_key, feed_name="toprecent-week.xml")

# Get top hyped papers for the past day
print('Scraping random (last week) feed.')
feed = None
data = engine.Engine.scrape("https://arxiv-sanity-lite.com/?rank=random&time_filter=7")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Random Papers Feed (Last Week)", feed_description="Top papers mentioned on Twitter over last day.", feed_link="https://hedgehog.den.dev/feeds/tophype-day.xml")
else:
	print('No data to process the feed.')

if feed != None:
	engine.Engine.upload_feed(feed, region, endpoint, access_key, secret_key, feed_name="random-last-week.xml")
