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

![Build badge for Arxiv Sanity Feeds](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/spawnfeed.yml/badge.svg) [![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://den.dev/ukraine)

All this tool does is scrape [Arxiv Sanity](http://www.arxiv-sanity.com), and produce consumable RSS feeds that can be used in your favorite RSS reader (such as Feedly or Outlook).

Feeds are updated daily.

## Feed Locations

### Home Page [![Subscribe to Home Page feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/home.xml) [![Validate home feed](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_home_feed.yml/badge.svg)](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_home_feed.yml)

```
https://hedgehog.den.dev/feeds/home.xml
```
### Top Hyped Papers (Daily) [![Subscribe to Top Hyped Papers (Daily) feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/tophype-day.xml) [![Validate top hyped papers feed](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_top_hyped_feed.yml/badge.svg)](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_top_hyped_feed.yml)

```
https://hedgehog.den.dev/feeds/tophype-day.xml
```

### Discussed Papers [![Subscribe to Discussed Papers feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/discussions.xml) [![Validate discussed papers feed](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_discussed_feed.yml/badge.svg)](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_discussed_feed.yml)

```
https://hedgehog.den.dev/feeds/discussions.xml
```

### Most Recent Papers (Weekly) [![Subscribe to Most Recent Papers (Weekly) feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/toprecent-week.xml) [![Validate most recent papers feed](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_most_recent_feed.yml/badge.svg)](https://github.com/dend/arxiv-sanity-feeds/actions/workflows/validate_most_recent_feed.yml)

```
https://hedgehog.den.dev/feeds/toprecent-week.xml
```

## Building

1. Install [Python 3](https://www.python.org/) on your target operating system.
2. Create a virtual environment with `python3 -m venv .env`.
3. Install required packages with `pip install -r src/feedingress/requirements.txt`.
4. Set up the following environment variables:
	- `DO_SPACES_ENDPOINT` - this is your DigitalOcean Spaces endpoint, including the `https://` prefix.
	- `DO_SPACES_REGION` - this is your DigitalOcean Spaces region, such as `sfo3`.
	- `DO_SPACES_ACCESS_KEY` - access key for DigitalOcean Spaces. 
	- `DO_SPACES_SECRET_KEY` - secret key for DigitalOcean Spaces.
5. Run the application: `python -m feedingress`.

Once the application runs, it will upload the generated RSS feeds to the Azure Storage account of choice.
