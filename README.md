<div align="center">
	<img alt="Arxiv Sanity Feeds" src="images/logo.png" width="200" height="200" />
	<h1>🦔 Arxiv Sanity RSS Feeds</h1>
	<p>
		<b>Subscribe to the content published on <a href="http://www.arxiv-sanity.com">Arxiv Sanity</a>.</b>
	</p>
	<br>
	<br>
	<br>
</div>

[![Build badge for Arxiv Sanity Feeds](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/spawnfeed.yml/badge.svg)](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/spawnfeed.yml)

All this tool does is scrape [Arxiv Sanity](http://www.arxiv-sanity.com), and produce consumable RSS feeds that can be used in your favorite RSS reader (such as Feedly or Outlook).

Feeds are updated daily.

## Feed Locations

### Home Page [![Subscribe to Home Page feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/home.xml) [![Validate home feed](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_home_feed.yml/badge.svg)](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_home_feed.yml)

```
https://hedgehog.den.dev/feeds/home.xml
```

### Most Recent Papers (Weekly) [![Subscribe to Most Recent Papers (Weekly) feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/toprecent-week.xml) [![Validate most recent papers feed](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_most_recent_feed.yml/badge.svg)](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_most_recent_feed.yml)

```
https://hedgehog.den.dev/feeds/toprecent-week.xml
```

### Random Papers (Last Week) [![Subscribe to Random Papers (Last Week) feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/random-last-week.xml) [![Validate most recent papers feed](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_random_feed.yml/badge.svg)](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_random_feed.yml)

```
https://hedgehog.den.dev/feeds/random-last-week.xml
```

## Building

1. Install [Python 3](https://www.python.org/) on your target operating system.
2. Create a virtual environment with `python3 -m venv .env`.
3. Install required packages with `pip install -r src/feedingress/requirements.txt`.
4. Set up the following environment variables:
	- `AZ_STORAGE_CS` - the Azure Storage account connection string.
5. Run the application: `python -m feedingress`.

Once the application runs, it will upload the generated RSS feeds to the Azure Storage account of choice.
