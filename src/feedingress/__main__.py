from feedingress.scraper import engine
import os

azure_storage_connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Get the main feed
print('Scraping main feed.')
data = engine.Engine.scrape("http://www.arxiv-sanity.com/")
feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Home Feed", feed_description="Most recent Arxiv papers.", feed_link="https://hedgehog.den.dev/feeds/home.xml")

if feed != None:
	engine.Engine.upload_feed(feed, azure_storage_connection_string, feed_name="home.xml")

# Get top weekly papers
print('Scraping weekly feed.')
data = engine.Engine.scrape("http://www.arxiv-sanity.com/top?timefilter=week&vfilter=all")
feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Top Recent Feed (Week)", feed_description="Top papers based on people's libraries.", feed_link="https://hedgehog.den.dev/feeds/toprecent-week.xml")

if feed != None:
	engine.Engine.upload_feed(feed, azure_storage_connection_string, feed_name="toprecent-week.xml")

# Get top hyped papers for the past day
print('Scraping top hyped feed.')
data = engine.Engine.scrape("http://www.arxiv-sanity.com/toptwtr?timefilter=day")
feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Top Hyped Feed (Day)", feed_description="Top papers mentioned on Twitter over last day.", feed_link="https://hedgehog.den.dev/feeds/tophype-day.xml")

if feed != None:
	engine.Engine.upload_feed(feed, azure_storage_connection_string, feed_name="tophype-day.xml")

# Get discussed feeds
print('Scraping discussed feed.')
data = engine.Engine.scrape("http://www.arxiv-sanity.com/discussions")
feed = engine.Engine.spawn_feed(data, feed_title="Arxiv Sanity Discussion Feed", feed_description="Papers with associated discussions.", feed_link="https://hedgehog.den.dev/feeds/discussions.xml")

if feed != None:
	engine.Engine.upload_feed(feed, azure_storage_connection_string, feed_name="discussions.xml")
