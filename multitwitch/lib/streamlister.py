import json

import multitwitch.lib.twitch as T


class StreamLister(object):
    def __init__(self):
        self.twitch_api = T.Twitch('eiy6ed1wqrgawtj9g63q9ghks1wkb7')

    def _get_list_info_dict(self, json_object):
        stream_info = {}
        stream_info['name'] = json_object['channel']['name']
        stream_info['url'] = json_object['channel']['url']
        stream_info['description'] = json_object['channel']['description']
        stream_info['game'] = json_object['channel']['game']
        stream_info['id'] = json_object['_id']
        stream_info['preview'] = json_object['preview']['medium']
        return stream_info

    def get_community_streams_by_name(self, name):
        community_json = self.twitch_api.get_community_info_by_name(name)
        community_id = community_json['_id']
        streams_json = self.twitch_api.get_streams_by_community_id(
            community_id)
        list_info = [] 
        for stream in streams_json['streams']:
            list_info.append(self._get_list_info_dict(stream))
        return list_info
