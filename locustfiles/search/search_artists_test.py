import random
import artist_keywords
from urllib import parse

from locust import FastHttpUser, task

keywords = [parse.quote(keyword) for keyword in artist_keywords.keywords]


class SearchArtists(FastHttpUser):

    @task
    def get(self):
        self.client.get(url=f"/api/v1/search/artists?keyword={random.choice(keywords)}",
                        name="/api/v1/search/artists")
