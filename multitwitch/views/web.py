import requests
import json

from multitwitch.lib.session import web, ajax
from pyramid.response import FileResponse

import multitwitch.lib.twitch as T
import multitwitch.lib.streamlister as sl

class WebView:

    @web(template="web/home.tmpl")
    def home(request):
        streamlister = sl.StreamLister()
        stream_list = streamlister.get_community_streams_by_name('x3lgaming')
        return {'project' : 'poo',
                'streams' : [],
                'community_streams': stream_list,
                'base_url' : 'http://rtmp.roaet.com:5000',
                'unique_streams' : [],
                'nstreams' : len([])}

    @web(template="web/streams.tmpl")
    def streams(request):
        path = request.path
        if path.startswith('/'):
            path = path[1:]
        if path.endswith('/'):
            path = path[:-1]
        path_parts = path.split("/")
        if len(path_parts) <= 1:
            return "REDIRECT:root:"
        if 'layout' not in path_parts[-1]:
            path = '/'.join(path_parts)
            path = '%s/layout0' % path
            return "REDIRECT:multitwitch:%s" % path
        stream_list = path_parts[:-1]
        edit_string = '/'.join(stream_list)
        return {'project' : 'poo',
                'streams' : stream_list,
                'base_url' : 'http://rtmp.roaet.com:5000',
                'unique_streams' : [],
                'edit_string': edit_string,
                'nstreams' : len(stream_list)}

    @web(template="web/home.tmpl")
    def edit(request):
        print("in edit")
        path = request.path
        if path.startswith('/'):
            path = path[1:]
        if path.endswith('/'):
            path = path[:-1]
        path_parts = path.split("/")
        if len(path_parts) <= 1:
            return "REDIRECT:root:"
        if 'layout' not in path_parts[-1]:
            path = '/'.join(path_parts)
            path = '%s/layout0' % path
            return "REDIRECT:multitwitch:%s" % path
        stream_list = path_parts[:-1]
        stream_list.pop(0)
        edit_string = '/'.join(stream_list)
        streamlister = sl.StreamLister()
        stream_list = streamlister.get_community_streams_by_name('x3lgaming')
        return {'project' : 'poo',
                'streams' : [],
                'community_streams': stream_list,
                'base_url' : 'http://rtmp.roaet.com:5000',
                'unique_streams' : [],
                'edit_string': edit_string,
                'nstreams' : len(stream_list)}

    @web()
    def twitch_api_test(request):
        streamlister = sl.StreamLister()
        stream_list = streamlister.get_community_streams_by_name('x3lgaming')
        return str(stream_list)

    @web()
    def view(request):
        stream_list = []
        layout = 'layout0'
        if len(request.GET) == 0:
            return "REDIRECT:root:"
        for idx in xrange(7):
            key = 's%d' % idx
            if len(request.GET[key]) > 0:
                stream_list.append(request.GET[key])
        if len(request.GET['layout']) > 0:
            layout = "layout%s" % request.GET['layout']
        stream_list.append(layout)
        path = '/'.join(stream_list)
        return "REDIRECT:multitwitch:%s" % path

    @staticmethod
    def favicon(request):
        return FileResponse("multitwitch/static/favicon.ico", content_type="image/x-icon")
