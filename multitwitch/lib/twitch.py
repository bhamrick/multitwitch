import requests


class Twitch(object):
    def __init__(self, clientid):
        self.clientid = clientid
        self.endpoint = 'https://api.twitch.tv/kraken'

    def _build_endpoint(self, target):
        return '/'.join([self.endpoint, target])

    def _basic_headers(self):
        headers = {
            'Client-ID': self.clientid,
            'Accept': 'application/vnd.twitchtv.v5+json'
        }
        return headers

    def _make_request(self, endpoint, payload):
        r = requests.get(
            self._build_endpoint(endpoint),
            params=payload, headers=self._basic_headers()
        )
        return r

    def _make_json_request(self, endpoint, payload):
        r = self._make_request(endpoint, payload)
        return r.json()

    def get_community_info_by_name(self, name):
        payload = {'name': name}
        community_json = self._make_json_request('communities', payload)
        return community_json

    def get_streams_by_community_id(self, id):
        payload = {'community_id': id}
        streams_json = self._make_json_request('streams', payload)
        return streams_json
