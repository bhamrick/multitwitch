from multitwitch.lib.session import web, ajax
from pyramid.response import FileResponse

class WebView:
    @web(template="web/home.tmpl")
    def home(request):
        streams = request.matchdict['streams']
        uniq_streams = []
        for s in streams:
            if s not in uniq_streams:
                uniq_streams.append(s)
        return {'project' : 'multitwitch',
                'streams' : streams,
                'unique_streams' : uniq_streams,
                'nstreams' : len(streams)}

    @staticmethod
    def favicon(request):
        return FileResponse("multitwitch/static/favicon.ico", content_type="image/x-icon")
