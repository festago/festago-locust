import random
from urllib import parse
import artist_keywords

from locust import FastHttpUser, task

keywords = [parse.quote(keyword) for keyword in artist_keywords.keywords]


class SearchFestivalsArtist(FastHttpUser):

    @task
    def get(self):
        self.client.get(url=f"/api/v1/search/festivals?keyword={random.choice(keywords)}",
                        name="/api/v1/search/festivals")
