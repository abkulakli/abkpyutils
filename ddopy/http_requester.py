import json
import requests


class HttpRequester:
    def __init__(self):
        self._endpoint_url = None

    def set_endpoint_url(self, url):
        self._endpoint_url = url

    def post_request(self, payload):
        if self._endpoint_url is None:
            raise Exception("Endpoint URL is not set. Call set_endpoint_url() method first.")

        headers = {"Content-Type": "application/json"}
        response = requests.post(url=self._endpoint_url, data=json.dumps(payload), headers=headers, timeout=5)
        response_json = response.json()

        return response_json
