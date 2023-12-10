from abc import abstractmethod
import os
import boto3
from io import StringIO


# NOTICE that the Feed Host will be different for each souce
# and it has to be passed to feed
# hence each backend will have to have its own workflow
# here, only the local storage backend is used

class storage():
    """
    abstract storage backend for hosting scraped data
    call upload_feed() to upload a feed to the backend
    """
    def __init__(self):
        self._name = "storage"
        self.upload_feed = self._upload_feed
        
    @abstractmethod
    def _upload_feed(self, feed, feed_name):
        raise NotImplementedError("upload_feed() not implemented")
    
class local(storage):
    """
    local storage backend
    """
    def __init__(self, path):
        super().__init__()
        self._name = "local"
        self._path = path
        if not os.path.exists(path):
            os.makedirs(path)
    def _upload_feed(self, feed, feed_name):
        print(f"Uploading feed: {feed_name}")
        with open(f"{self._path}/{feed_name}", "w") as f:
            f.write(feed)
    
class DigitalOcean(storage):
    """
    DigitalOcean Spaces storage backend
    """
    def __init__(self, region, endpoint, access_key, secret_key):
        super().__init__()
        self._name = "DigitalOcean Spaces"
        self._region = region
        self._endpoint = endpoint
        self._access_key = access_key
        self._secret_key = secret_key
    def _upload_feed(self, feed, feed_name):
        print(f"Uploading feed: {feed_name}")
        session = boto3.session.Session()
        client = session.client('s3',
                                region_name=self._region,
                                endpoint_url=self._endpoint,
                                aws_access_key_id=self._access_key,
                                aws_secret_access_key=self._secret_key)
        client.put_object(Body=feed.encode('utf-8'), Bucket='hedgehog', Key=f'feeds/{feed_name}', ContentType='application/xml', ACL='public-read')
        
	# @staticmethod
	# def upload_feed(feed, region, endpoint, access_key, secret_key, feed_name):
	# 	print(f"Uploading feed: {feed_name}")

	# 	session = boto3.session.Session()

	# 	client = session.client('s3',
    #                     region_name=region,
    #                     endpoint_url=endpoint,
    #                     aws_access_key_id=access_key,
    #                     aws_secret_access_key=secret_key)

	# 	client.put_object(Body=feed.encode('utf-8'), Bucket='hedgehog', Key=f'feeds/{feed_name}', ContentType='application/xml', ACL='public-read')