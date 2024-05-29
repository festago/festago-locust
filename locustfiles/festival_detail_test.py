import random

from locust import FastHttpUser, task, events


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--festival-id-start", type=int, default=454, help="조회할 처음 범위의 축제 식별자")
    parser.add_argument("--festival-id-end", type=int, default=3503, help="조회할 마지막 범위의 축제 식별자")


# 축제 상세 조회 테스트
class FestivalDetail(FastHttpUser):

    @task
    def get(self):
        id_start = self.environment.parsed_options.festival_id_start
        id_end = self.environment.parsed_options.festival_id_end
        self.client.get(url=f"/api/v1/festivals/{random.randint(id_start, id_end)}", name="/api/v1/festivals/${id}")
