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

### Home Page [![Subscribe to Home Page feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/home.xml)

```http
https://hedgehog.den.dev/feeds/home.xml
```
### Top Hyped Papers (Daily) [![Subscribe to Top Hyped Papers (Daily) feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/tophype-day.xml)

```http
https://hedgehog.den.dev/feeds/tophype-day.xml
```

### Discussed Papers [![Subscribe to Discussed Papers feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/discussions.xml)

```http
https://hedgehog.den.dev/feeds/discussions.xml
```

### Most Recent Papers (Weekly) [![Subscribe to Most Recent Papers (Weekly) feed](images/subscribe.svg)](https://hedgehog.den.dev/feeds/toprecent-week.xml)

```http
https://hedgehog.den.dev/feeds/toprecent-week.xml
```

## Building

1. Install [Python 3](https://www.python.org/) on your target operating system.
2. Create a virtual environment with `python3 -m venv .env`.
3. Install required packages with `pip install -r src/feedingress/requirements.txt`.
4. Set up the Azure Storage [connection string](https://docs.microsoft.com/azure/storage/common/storage-account-keys-manage?tabs=azure-portal) environment variable (`AZURE_STORAGE_CONNECTION_STRING`) to the connection string that you obtain from the [Azure Portal](https://portal.azure.com).
5. Run the application: `python -m feedingress`.

Once the application runs, it will upload the generated RSS feeds to the Azure Storage account of choice.
