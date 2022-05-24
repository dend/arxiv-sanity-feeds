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
data = engine.Engine.scrape("http://www.arxiv-sanity.com/")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Home Feed", feed_description="Most recent Arxiv papers.", feed_link="https://hedgehog.den.dev/feeds/home.xml")
else:
	print('No data to process the feed.')

if feed != None:
	engine.Engine.upload_feed(feed, region, endpoint, access_key, secret_key, feed_name="home.xml")

# Get top weekly papers
print('Scraping weekly feed.')
feed = None
data = engine.Engine.scrape("http://www.arxiv-sanity.com/top?timefilter=week&vfilter=all")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Top Recent Feed (Week)", feed_description="Top papers based on people's libraries.", feed_link="https://hedgehog.den.dev/feeds/toprecent-week.xml")
else:
	print('No data to process the feed.')

if feed != None:
	engine.Engine.upload_feed(feed, region, endpoint, access_key, secret_key, feed_name="toprecent-week.xml")

# Get top hyped papers for the past day
print('Scraping top hyped feed.')
feed = None
data = engine.Engine.scrape("http://www.arxiv-sanity.com/toptwtr?timefilter=day")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Top Hyped Feed (Day)", feed_description="Top papers mentioned on Twitter over last day.", feed_link="https://hedgehog.den.dev/feeds/tophype-day.xml")
else:
	print('No data to process the feed.')

if feed != None:
	engine.Engine.upload_feed(feed, region, endpoint, access_key, secret_key, feed_name="tophype-day.xml")

# Get discussed feeds
print('Scraping discussed feed.')
feed = None
data = engine.Engine.scrape("http://www.arxiv-sanity.com/discussions")

if data != None:
	feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Discussion Feed", feed_description="Papers with associated discussions.", feed_link="https://hedgehog.den.dev/feeds/discussions.xml")
else:
	print('No data to process the feed.')

if feed != None:
	engine.Engine.upload_feed(feed, region, endpoint, access_key, secret_key, feed_name="discussions.xml")
