import random

from locust import FastHttpUser, task, events


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--is-past", choices=["false", "true"], default="false", help="과거 축제 조회 여부")
    parser.add_argument("--school-id-start", type=int, default=3, help="조회할 처음 범위의 학교 식별자")
    parser.add_argument("--school-id-end", type=int, default=63, help="조회할 마지막 범위의 학교 식별자")


class GetSchoolFestivals(FastHttpUser):

    @task
    def get(self):
        id_start = self.environment.parsed_options.school_id_start
        id_end = self.environment.parsed_options.school_id_end
        is_past = self.environment.parsed_options.is_past
        self.client.get(
            url=f"/api/v1/schools/{random.randint(id_start, id_end)}/festivals?isPast={is_past}",
            name="/api/v1/schools/${id}/festivals")
