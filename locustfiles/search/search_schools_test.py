import random
from urllib import parse
import school_keywords

from locust import FastHttpUser, task

keywords = [parse.quote(keyword) for keyword in school_keywords.keywords]


class SearchSchools(FastHttpUser):

    @task
    def get(self):
        self.client.get(url=f"/api/v1/search/schools?keyword={random.choice(keywords)}",
                        name="/api/v1/search/schools")
