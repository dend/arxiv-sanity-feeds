from feedingress.scraper import engine

data = engine.Engine.scrape("http://www.arxiv-sanity.com/")
engine.Engine.spawn_feed(data, feed_title="Test", feed_description="Some test", feed_link="https://den.dev")