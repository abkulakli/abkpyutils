import json
import requests

class HttpRequester:
    def __init__(self):
        self.url = None

    def set_url(self, url):
        self.url = url

    def post_request(self, payload):
        if self.url is None:
            raise Exception("No app_url configured")

        headers = {"Content-Type": "application/json"}
        response = requests.post(
            url=self.url, data=json.dumps(payload), headers=headers, timeout=5
        )
        print(response)
        response_json = response.json()

        return response_json
